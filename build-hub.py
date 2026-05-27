#!/usr/bin/env python3
"""
build-hub.py — Scans the OL Prototypes project and generates index.html
Run:  python3 build-hub.py
"""

import os, re, glob, html
from datetime import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
SKILLS_DIR = os.path.join(ROOT, '.claude', 'skills')

def esc(s):
    return html.escape(str(s))

# ═══ SCAN ═══
def scan_games():
    files = sorted(
        glob.glob(os.path.join(ROOT, '*.html')) +
        glob.glob(os.path.join(ROOT, 'minigame prototypes', '*.html'))
    )
    seen, filtered = set(), []
    for f in files:
        name = os.path.basename(f)
        if name in seen or name == 'index.html': continue
        seen.add(name)
        if any(kw in name for kw in ['game-','quest','spell','enchanted','lesson','harp','locked','door']):
            filtered.append(f)
    games = []
    for f in filtered:
        name = os.path.basename(f)
        content = open(f, encoding='utf-8').read()
        m = re.search(r'<title>(.*?)</title>', content)
        title = re.sub(r'\s*[—–-]\s*.+$', '', m.group(1)).strip() if m else name
        m2 = re.search(r'class="skill-tag"[^>]*>(.*?)</', content)
        skill = m2.group(1).strip() if m2 else ''
        m3 = re.search(r'class="eyebrow"[^>]*>(.*?)</', content)
        domain = m3.group(1).strip() if m3 else ''
        num = re.search(r'game-(\d+)', name)
        num = num.group(1) if num else '—'
        games.append(dict(file=name, num=num, title=title, domain=domain, skill=skill))
    return games

def scan_skills():
    if not os.path.isdir(SKILLS_DIR): return []
    skills = []
    for d in sorted(os.listdir(SKILLS_DIR)):
        sf = os.path.join(SKILLS_DIR, d, 'SKILL.md')
        if not os.path.isfile(sf): continue
        content = open(sf, encoding='utf-8').read()
        fm = re.search(r'^---\s*\n(.*?)\n---', content, re.S)
        name, desc = d, ''
        if fm:
            nm = re.search(r'name:\s*(.+)', fm.group(1))
            dm = re.search(r'description:\s*(.+)', fm.group(1))
            if nm: name = nm.group(1).strip()
            if dm: desc = dm.group(1).strip()
        skills.append(dict(dir=d, name=name, description=desc))
    return skills

def scan_decisions():
    df = os.path.join(ROOT, 'decisions.md')
    if not os.path.isfile(df): return []
    content = open(df, encoding='utf-8').read()
    blocks = re.split(r'\n## DEC-', content)[1:]
    decs = []
    for block in blocks:
        lines = block.strip().split('\n')
        im = re.match(r'^(\d+):\s*(.+)', lines[0] if lines else '')
        did = f'DEC-{im.group(1)}' if im else '?'
        title = im.group(2).strip() if im else ''
        def grab(key):
            m = re.search(rf'\*\*{key}:\*\*\s*(.+)', block)
            return m.group(1).strip() if m else ''
        decs.append(dict(id=did, title=title, date=grab('Date'), domain=grab('Domain'), status=grab('Status')))
    return decs

def scan_resources():
    rf = os.path.join(SKILLS_DIR, 'resources', 'SKILL.md')
    if not os.path.isfile(rf): return []
    content = open(rf, encoding='utf-8').read()
    blocks = re.split(r'\n### R-', content)[1:]
    res = []
    for block in blocks:
        im = re.match(r'^(\d+):\s*(.+)', block.strip().split('\n')[0])
        rid = f'R-{im.group(1)}' if im else '?'
        title = im.group(2).strip() if im else ''
        def grab(key):
            m = re.search(rf'\*\*{key}\*\*\s*\|\s*(.+)', block)
            return m.group(1).strip() if m else ''
        res.append(dict(id=rid, title=title, authors=grab('Authors'), type=grab('Type'),
                        topics=grab('Topics'), skill=grab('Skill derived').replace('`','')))
    return res

def scan_docs():
    docs = []
    if os.path.isfile(os.path.join(ROOT, 'game vision.md')):
        docs.append(dict(title='Product Vision', desc='Core concept, three-phase roadmap, design principles.'))
    decs = scan_decisions()
    if os.path.isfile(os.path.join(ROOT, 'decisions.md')):
        docs.append(dict(title='Decision Log', desc=f'{len(decs)} design decisions with rationale and evidence.'))
    if os.path.isfile(os.path.join(ROOT, 'Reading Exercise to Game Mechanic.csv')):
        docs.append(dict(title='Curriculum Map', desc='~50 Orton-Gillingham activities with modalities and sample items.'))
    return docs

# ═══ GENERATE ═══
def generate():
    games = scan_games()
    skills = scan_skills()
    docs = scan_docs()
    decisions = scan_decisions()
    resources = scan_resources()
    now = datetime.now().strftime('%B %d, %Y')

    # Abby's game rows (no links by default)
    abby_game_rows = '\n          '.join(
        f'<tr><td>{esc(g["num"])}</td><td>{esc(g["title"])}</td>'
        f'<td>{esc(g["domain"])}</td><td>{esc(g["skill"])}</td>'
        f'<td><span class="status status-wip">In Progress</span></td></tr>'
        for g in games
    )

    doc_cards = '\n    '.join(
        f'<div class="card"><div class="card-title">{esc(d["title"])}</div>'
        f'<div class="card-desc">{esc(d["desc"])}</div></div>' for d in docs
    )

    skill_cards = '\n    '.join(
        f'<div class="card"><div class="card-title">{esc(s["name"])}</div>'
        f'<div class="card-desc">{esc(s["description"][:130])}{"..." if len(s["description"])>130 else ""}</div>'
        f'<div class="card-meta"><span class="tag tag-teal">/{esc(s["name"])}</span></div></div>'
        for s in skills
    )

    resource_rows = '\n      '.join(
        f'<tr><td>{esc(r["id"])}</td><td>{esc(r["title"])}</td><td>{esc(r["authors"])}</td>'
        f'<td><span class="tag">{esc(r["type"])}</span></td>'
        f'<td>{esc(r["topics"][:50])}{"..." if len(r["topics"])>50 else ""}</td></tr>'
        for r in resources
    )

    decision_rows = '\n      '.join(
        f'<tr><td>{esc(d["id"])}</td><td>{esc(d["title"])}</td>'
        f'<td>{esc(d["domain"])}</td><td>{esc(d["date"])}</td>'
        f'<td><span class="status status-done">{esc(d["status"])}</span></td></tr>'
        for d in decisions
    )

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>OL Project HQ</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap');
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#faf9f5;font-family:'Inter',sans-serif;color:#2a2a2a;min-height:100vh}}

header{{background:#ed6a5a;padding:44px 24px 36px;text-align:center}}
header h1{{font-family:'Lora',serif;font-size:clamp(26px,5vw,40px);color:#fff;font-weight:700;margin-bottom:8px}}
header p{{font-size:14px;color:rgba(255,255,255,0.88);max-width:520px;margin:0 auto;line-height:1.65;font-family:'Lora',serif}}
header .meta{{font-size:11px;color:rgba(255,255,255,0.55);margin-top:10px}}

main{{max-width:920px;margin:0 auto;padding:28px 20px}}
.section{{margin-bottom:40px}}
.section-title{{font-family:'Lora',serif;font-size:20px;font-weight:700;color:#3a3a3a;
  margin-bottom:16px;padding-bottom:10px;border-bottom:3px solid #ed6a5a}}

/* Storyboard link */
.sb-link{{display:block;background:#f4f1bb;border:2px solid #e0dda0;border-radius:14px;
  padding:24px;text-decoration:none;color:#2a2a2a;transition:all .15s;margin-bottom:32px}}
.sb-link:hover{{border-color:#ed6a5a;box-shadow:0 4px 16px rgba(237,106,90,0.12)}}
.sb-head{{display:flex;align-items:center;gap:14px;margin-bottom:10px}}
.sb-icon{{font-size:28px}}
.sb-title{{font-family:'Lora',serif;font-size:18px;font-weight:700;color:#3a3a3a}}
.sb-desc{{font-size:13px;color:#5a5a5a;line-height:1.55}}
.sb-pills{{display:flex;gap:8px;margin-top:12px;flex-wrap:wrap}}
.sb-pill{{font-size:10px;font-weight:600;padding:3px 10px;border-radius:10px;
  background:rgba(155,193,188,0.3);color:#4a6a66}}

/* Team profiles — stacked vertically */
.profiles{{display:flex;flex-direction:column;gap:12px;margin-bottom:32px}}
.profile{{background:#fff;border:2px solid #eae8e2;border-radius:14px;overflow:hidden}}
.profile-header{{padding:16px 18px;cursor:pointer;display:flex;align-items:center;justify-content:space-between;
  -webkit-tap-highlight-color:transparent}}
.profile-header:hover{{background:#faf8f2}}
.profile-info{{display:flex;align-items:center;gap:12px}}
.profile-avatar{{width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;
  font-size:16px;font-weight:700;color:#fff}}
.profile-name{{font-family:'Lora',serif;font-size:15px;font-weight:700;color:#3a3a3a}}
.profile-role{{font-size:10px;color:#999}}
.profile-arrow{{font-size:14px;color:#ccc;transition:transform .2s}}
.profile.open .profile-arrow{{transform:rotate(180deg)}}
.profile-body{{display:none}}
.profile.open .profile-body{{display:block}}
.profile-content{{padding:12px 18px 18px;border-top:1px solid #f0ede8}}
.profile-empty{{font-size:12px;color:#bbb;padding:20px 0;text-align:center;font-style:italic}}
.profile-table{{width:100%;border-collapse:collapse;font-size:11px;margin-top:12px}}
.profile-table th{{text-align:left;padding:8px 10px;background:#ed6a5a;color:#fff;font-weight:600;
  font-size:9px;text-transform:uppercase;letter-spacing:1px;font-family:'Lora',serif}}
.profile-table td{{padding:8px 10px;border-bottom:1px solid #f0ede8;color:#3a3a3a}}
.profile-count{{font-size:10px;color:#999;font-weight:600}}

/* Cards */
.cards{{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:14px}}
.card{{background:#fff;border-radius:12px;padding:18px;border:2px solid #eae8e2;transition:border-color .15s,box-shadow .15s}}
.card:hover{{border-color:#9bc1bc;box-shadow:0 3px 12px rgba(155,193,188,0.15)}}
.card-title{{font-family:'Lora',serif;font-weight:700;font-size:15px;color:#3a3a3a;margin-bottom:5px}}
.card-desc{{font-size:12px;color:#6a6a6a;line-height:1.55}}
.card-meta{{font-size:10px;color:#999;margin-top:8px;display:flex;gap:10px;flex-wrap:wrap}}

.tag{{background:#f4f1bb;padding:2px 8px;border-radius:8px;font-size:10px;font-weight:600;color:#7a7040}}
.tag-teal{{background:rgba(155,193,188,0.25);color:#4a6a66}}

/* Tables */
.table-wrap{{overflow-x:auto}}
table{{width:100%;border-collapse:collapse;font-size:12px}}
th{{text-align:left;padding:10px 12px;background:#ed6a5a;color:#fff;font-weight:600;
  font-size:10px;text-transform:uppercase;letter-spacing:1px;font-family:'Lora',serif}}
td{{padding:10px 12px;border-bottom:1px solid #eae8e2;color:#3a3a3a}}
tr:hover td{{background:#faf8f2}}

.status{{display:inline-block;padding:3px 10px;border-radius:8px;font-size:9px;
  font-weight:700;text-transform:uppercase;letter-spacing:1px}}
.status-done{{background:rgba(155,193,188,0.25);color:#4a6a66}}
.status-wip{{background:rgba(237,106,90,0.12);color:#c04a3a}}

/* Roadmap */
.roadmap{{position:relative;padding-left:36px}}
.roadmap::before{{content:'';position:absolute;left:14px;top:0;bottom:0;width:3px;background:#eae8e2}}
.rm-stage{{position:relative;margin-bottom:24px}}
.rm-dot{{position:absolute;left:-30px;top:6px;width:18px;height:18px;border-radius:50%;border:3px solid #eae8e2;background:#faf9f5;z-index:2}}
.rm-stage.done .rm-dot{{background:#9bc1bc;border-color:#9bc1bc}}
.rm-stage.active .rm-dot{{background:#ed6a5a;border-color:#ed6a5a;box-shadow:0 0 0 4px rgba(237,106,90,0.2)}}
.rm-stage.future .rm-dot{{background:#faf9f5;border-color:#ddd}}
.rm-header{{display:flex;align-items:center;gap:10px;cursor:pointer;padding:6px 0;-webkit-tap-highlight-color:transparent}}
.rm-header:hover .rm-title{{color:#ed6a5a}}
.rm-badge{{font-size:9px;font-weight:700;padding:3px 8px;border-radius:10px;text-transform:uppercase;letter-spacing:1px}}
.rm-badge-done{{background:rgba(155,193,188,0.25);color:#4a6a66}}
.rm-badge-active{{background:rgba(237,106,90,0.12);color:#c04a3a}}
.rm-badge-future{{background:#eae8e2;color:#999}}
.rm-title{{font-family:'Lora',serif;font-size:15px;font-weight:700;color:#3a3a3a;transition:color .15s}}
.rm-body{{display:none}}
.rm-stage.open .rm-body{{display:block}}
.rm-content{{padding:10px 0 4px;margin-left:8px;padding-left:16px;border-left:2px solid #eae8e2}}
.rm-items{{list-style:none;padding:0}}
.rm-items li{{font-size:12px;color:#5a5a5a;line-height:1.7;padding:2px 0;display:flex;align-items:flex-start;gap:8px}}
.rm-items li::before{{content:'';display:inline-block;width:14px;height:14px;border-radius:3px;border:2px solid #ddd;flex-shrink:0;margin-top:2px}}
.rm-items li.done::before{{background:#9bc1bc;border-color:#9bc1bc;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 14 14' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M3 7l3 3 5-5' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E")}}
.rm-items li.done{{color:#999;text-decoration:line-through;text-decoration-color:#ccc}}

footer{{text-align:center;padding:28px;font-size:11px;color:#bbb;font-family:'Lora',serif}}
</style>
</head>
<body>
<header>
  <h1>OL Project HQ</h1>
  <p>An RPG that adapts evidence-based dyslexia tutoring into playful game mechanics.</p>
  <div class="meta">Last updated: {esc(now)} · {len(games)} prototypes · {len(skills)} skills · {len(decisions)} decisions</div>
</header>
<main>

<!-- Storyboard -->
<a class="sb-link" href="storyboard.html">
  <div class="sb-head">
    <span class="sb-icon">🗺️</span>
    <span class="sb-title">Game Storyboard</span>
  </div>
  <div class="sb-desc">Interactive zoomable board showing the full curriculum flow. Click domains to expand lessons, click games to see beat-by-beat storyboards with editable notes.</div>
  <div class="sb-pills">
    <span class="sb-pill">Print Concepts</span>
    <span class="sb-pill">Letter Knowledge</span>
    <span class="sb-pill">Phonological Awareness</span>
    <span class="sb-pill">Alphabetic Principle</span>
    <span class="sb-pill">Decoding</span>
    <span class="sb-pill">Encoding</span>
    <span class="sb-pill">Comprehension</span>
  </div>
</a>

<!-- Team Profiles -->
<div class="section">
  <div class="section-title">Team</div>
  <div class="profiles">

    <!-- Abby -->
    <div class="profile" id="profile-abby">
      <div class="profile-header" onclick="toggleProfile('profile-abby')">
        <div class="profile-info">
          <div class="profile-avatar" style="background:#ed6a5a">A</div>
          <div>
            <div class="profile-name">Abby</div>
            <div class="profile-role">Game Design · Prototyping</div>
          </div>
        </div>
        <div style="display:flex;align-items:center;gap:10px">
          <span class="profile-count">{len(games)} prototypes</span>
          <span class="profile-arrow">▾</span>
        </div>
      </div>
      <div class="profile-body">
        <div class="profile-content">
          <table class="profile-table">
            <tr><th>#</th><th>Prototype</th><th>Domain</th><th>Skill</th><th>Status</th></tr>
            {abby_game_rows}
          </table>
        </div>
      </div>
    </div>

    <!-- Bob -->
    <div class="profile" id="profile-bob">
      <div class="profile-header" onclick="toggleProfile('profile-bob')">
        <div class="profile-info">
          <div class="profile-avatar" style="background:#9bc1bc">B</div>
          <div>
            <div class="profile-name">Bob</div>
            <div class="profile-role">—</div>
          </div>
        </div>
        <span class="profile-arrow">▾</span>
      </div>
      <div class="profile-body">
        <div class="profile-content">
          <div class="profile-empty">No prototypes yet</div>
        </div>
      </div>
    </div>

    <!-- Tyler -->
    <div class="profile" id="profile-tyler">
      <div class="profile-header" onclick="toggleProfile('profile-tyler')">
        <div class="profile-info">
          <div class="profile-avatar" style="background:#f4c952">T</div>
          <div>
            <div class="profile-name">Tyler</div>
            <div class="profile-role">Curriculum · Instruction</div>
          </div>
        </div>
        <span class="profile-arrow">▾</span>
      </div>
      <div class="profile-body">
        <div class="profile-content">
          <div class="profile-empty">No prototypes yet</div>
        </div>
      </div>
    </div>

  </div>
</div>

<!-- Prototype Categories -->
<div class="section">
  <div class="section-title">Prototype Categories</div>

  <div style="display:flex;gap:12px;margin-bottom:20px;flex-wrap:wrap">
    <div style="flex:1;min-width:260px;background:#fff;border:2px solid #eae8e2;border-radius:12px;padding:18px">
      <div style="font-family:'Lora',serif;font-size:15px;font-weight:700;color:#3a3a3a;margin-bottom:6px">Sprint Mini-Games</div>
      <div style="font-size:12px;color:#6a6a6a;line-height:1.55;margin-bottom:10px">Short-form challenges (~20-60 seconds) that test a specific skill. These would appear during a longer play session as gates — the player must pass them to unlock a new feature or move forward in the game.</div>
      <div style="font-size:11px;color:#999">Enchanted Gems · Spell Caster · Whispering Stones · Block Breaker · Seed Script · Syllable Sprout</div>
    </div>
    <div style="flex:1;min-width:260px;background:#fff;border:2px solid #eae8e2;border-radius:12px;padding:18px">
      <div style="font-family:'Lora',serif;font-size:15px;font-weight:700;color:#3a3a3a;margin-bottom:6px">Narrative Explorations</div>
      <div style="font-size:12px;color:#6a6a6a;line-height:1.55;margin-bottom:10px">Longer-form experiments that explore how to embed evidence-based dyslexia tutoring inside a story the player cares about. These test different narrative frames for the explicit instruction model.</div>
      <div style="font-size:11px;color:#999">The Locked Door · Quest Catcher · Lesson: Letter Sounds</div>
    </div>
  </div>

  <!-- Narrative Briefs -->
  <div style="font-family:'Lora',serif;font-size:16px;font-weight:700;color:#3a3a3a;margin:24px 0 12px;padding-bottom:8px;border-bottom:2px solid #eae8e2">Narrative Exploration Briefs</div>

  <div style="background:#fff;border:2px solid #eae8e2;border-radius:12px;padding:18px;margin-bottom:14px">
    <div style="font-family:'Lora',serif;font-size:14px;font-weight:700;color:#ed6a5a;margin-bottom:4px">The Locked Door</div>
    <div style="font-size:10px;color:#999;margin-bottom:8px">Skill: Letter Sounds (S, T, M, N) · Full lesson with explicit instruction</div>
    <div style="font-size:12px;color:#4a4a4a;line-height:1.65;margin-bottom:10px">
      <strong>Direction:</strong> An NPC guide discovers a locked magical door with 4 gem-shaped rune slots. Each letter-sound the player learns fills one slot. The narrative creates a reason to learn — you need these sounds to open the door and see what's behind it.
    </div>
    <div style="font-size:12px;color:#4a4a4a;line-height:1.65;margin-bottom:10px">
      <strong>How mini-games fit in:</strong> The guided practice phase (picking the right gem after being taught each sound) is essentially a mini version of the Enchanted Gems sprint. The final sprint before the door opens IS the Enchanted Gems mechanic — floating gems, timed, same interaction. The narrative wraps around the sprint to give it purpose.
    </div>
    <div style="font-size:12px;color:#4a4a4a;line-height:1.65">
      <strong>What we learned:</strong> The 80/20 explicit instruction ratio works well in narrative form. Teaching through an NPC character (The Guide) feels natural — the player receives instruction without feeling lectured. The door-opening payoff gives the sprint real stakes. The visual feedback of gems filling into the door creates a tangible sense of progress.
    </div>
  </div>

  <div style="background:#fff;border:2px solid #eae8e2;border-radius:12px;padding:18px;margin-bottom:14px">
    <div style="font-family:'Lora',serif;font-size:14px;font-weight:700;color:#ed6a5a;margin-bottom:4px">Quest Catcher — The Lost Treasure of Stonehollow</div>
    <div style="font-size:10px;color:#999;margin-bottom:8px">Skill: Vocabulary in Context · 4-chapter continuous quest</div>
    <div style="font-size:12px;color:#4a4a4a;line-height:1.65;margin-bottom:10px">
      <strong>Direction:</strong> A single continuous quest with Scout Mira exploring a mountain. Each vocabulary word (crevice, navigate, dilapidated) is a prerequisite to the next step — you must understand the word to progress through the story. The vocabulary is not the goal; the adventure is. The words are keys that unlock the next chapter.
    </div>
    <div style="font-size:12px;color:#4a4a4a;line-height:1.65;margin-bottom:10px">
      <strong>How mini-games fit in:</strong> Each vocabulary question is a brief challenge embedded in the narrative — similar to how a sprint mini-game would pause the story for a skill check. The 4-option multiple choice mechanic could be swapped for any identification-style sprint. The key insight is that the challenge serves the quest, not the other way around.
    </div>
    <div style="font-size:12px;color:#4a4a4a;line-height:1.65">
      <strong>What we learned:</strong> Framing vocabulary as a prerequisite to adventure (not the point of the game) dramatically changes how it feels. The visual scene progression (outside mountain → dark cave → crumbling chamber → treasure room) gives each word a concrete context. The celebration at the end — Mira recapping the journey using all the vocabulary words — reinforces learning through narrative payoff rather than a score screen. For 8-12 year olds, the heroic framing ("Quest Catcher") makes the educational content feel age-appropriate rather than babyish.
    </div>
  </div>

  <div style="background:#fff;border:2px solid #eae8e2;border-radius:12px;padding:18px;margin-bottom:14px">
    <div style="font-family:'Lora',serif;font-size:14px;font-weight:700;color:#ed6a5a;margin-bottom:4px">Lesson: Letter Sounds (Basic)</div>
    <div style="font-size:10px;color:#999;margin-bottom:8px">Skill: Letter Sounds (S, T, M, N) · Structured lesson without strong narrative</div>
    <div style="font-size:12px;color:#4a4a4a;line-height:1.65;margin-bottom:10px">
      <strong>Direction:</strong> A straightforward implementation of the WRS lesson plan structure — teach each sound explicitly, guided practice with gem selection, transition screen, then an independent sprint. This was the baseline before adding narrative. It follows the 80/20 ratio and 3-stage structure (Tutorial → Guided → Sprint) directly.
    </div>
    <div style="font-size:12px;color:#4a4a4a;line-height:1.65;margin-bottom:10px">
      <strong>How mini-games fit in:</strong> The sprint phase at the end IS the Enchanted Gems mini-game, preceded by the full teach and guided phases. This shows the basic skeleton that any lesson would follow — the mini-game is the final 20% after 80% of explicit instruction.
    </div>
    <div style="font-size:12px;color:#4a4a4a;line-height:1.65">
      <strong>What we learned:</strong> The structure is pedagogically sound but emotionally flat without narrative. Students go through the motions but don't have a reason to care beyond "learn this." This prototype confirmed that the explicit instruction model works mechanically, but needs a narrative frame (like The Locked Door) to create engagement. It served as the control group — proving that the teaching works, while the narrative explorations prove that the teaching can also be fun.
    </div>
  </div>
</div>

<!-- Documents -->
<div class="section">
  <div class="section-title">Project Documents ({len(docs)})</div>
  <div class="cards">{doc_cards}</div>
</div>

<!-- Skills -->
<div class="section">
  <div class="section-title">Design Frameworks ({len(skills)})</div>
  <div class="cards">{skill_cards}</div>
</div>

<!-- Resources -->
{"" if not resources else '<div class="section"><div class="section-title">Research Sources ('+str(len(resources))+')</div><div class="table-wrap"><table><tr><th>ID</th><th>Title</th><th>Authors</th><th>Type</th><th>Topics</th></tr>'+resource_rows+'</table></div></div>'}

<!-- Decisions -->
{"" if not decisions else '<div class="section"><div class="section-title">Decision Log ('+str(len(decisions))+')</div><div class="table-wrap"><table><tr><th>ID</th><th>Decision</th><th>Domain</th><th>Date</th><th>Status</th></tr>'+decision_rows+'</table></div></div>'}

<!-- Roadmap -->
<div class="section">
  <div class="section-title">Project Roadmap</div>
  <div style="font-size:12px;color:#888;margin-bottom:14px;display:flex;gap:12px;flex-wrap:wrap">
    <span style="display:flex;align-items:center;gap:4px"><span style="width:10px;height:10px;border-radius:50%;background:#9bc1bc;display:inline-block"></span> Complete</span>
    <span style="display:flex;align-items:center;gap:4px"><span style="width:10px;height:10px;border-radius:50%;background:#ed6a5a;display:inline-block"></span> In Progress</span>
    <span style="display:flex;align-items:center;gap:4px"><span style="width:10px;height:10px;border-radius:50%;background:#e4e0da;display:inline-block"></span> Upcoming</span>
    <span style="font-size:10px;color:#aaa">Click to expand</span>
  </div>
  <div class="roadmap">

    <div class="rm-stage done" onclick="this.classList.toggle('open')">
      <div class="rm-dot"></div>
      <div class="rm-header"><span class="rm-badge rm-badge-done">Complete</span><span class="rm-title">Stage 0 — Vision &amp; Strategy</span></div>
      <div class="rm-body"><div class="rm-content">
        <ul class="rm-items">
          <li class="done">Product vision document</li>
          <li class="done">Target audience defined</li>
          <li class="done">Curriculum backbone mapped (CSV)</li>
          <li class="done">Platform: browser-first, mobile touch</li>
          <li class="done">Design principles established</li>
        </ul>
      </div></div>
    </div>

    <div class="rm-stage done" onclick="this.classList.toggle('open')">
      <div class="rm-dot"></div>
      <div class="rm-header"><span class="rm-badge rm-badge-done">Complete</span><span class="rm-title">Stage 1 — Discover (Research)</span></div>
      <div class="rm-body"><div class="rm-content">
        <ul class="rm-items">
          <li class="done">Handbook of Game-Based Learning (R-001)</li>
          <li class="done">Actionable Gamification / Octalysis (R-002)</li>
          <li class="done">MDA Framework (R-003)</li>
          <li class="done">Meeting: Explicit &amp; Systematic Instruction (R-004)</li>
          <li class="done">WRS Lesson Plan Structure (R-005)</li>
          <li>Interview OG tutors</li>
          <li>Interview parents/caregivers</li>
          <li>Observe live tutoring sessions</li>
        </ul>
      </div></div>
    </div>

    <div class="rm-stage done" onclick="this.classList.toggle('open')">
      <div class="rm-dot"></div>
      <div class="rm-header"><span class="rm-badge rm-badge-done">Complete</span><span class="rm-title">Stage 2 — Define (Frameworks)</span></div>
      <div class="rm-body"><div class="rm-content">
        <ul class="rm-items">
          <li class="done">{len(skills)} design skills created</li>
          <li class="done">{len(decisions)} key decisions logged</li>
          <li class="done">80/20 instruction ratio established</li>
          <li class="done">3-stage lesson structure (Tutorial → Guided → Sprint)</li>
          <li class="done">Hint escalation replacing lives</li>
          <li>User personas (Learner, Tutor, Parent)</li>
        </ul>
      </div></div>
    </div>

    <div class="rm-stage active open" onclick="this.classList.toggle('open')">
      <div class="rm-dot"></div>
      <div class="rm-header"><span class="rm-badge rm-badge-active">In Progress</span><span class="rm-title">Stage 3 — Develop (Build &amp; Test)</span></div>
      <div class="rm-body"><div class="rm-content">
        <ul class="rm-items">
          <li class="done">{len(games)} mini-game prototypes built</li>
          <li class="done">Full lesson prototype (Locked Door)</li>
          <li class="done">Interactive storyboard created</li>
          <li class="done">Audio assets (ElevenLabs phonemes + words)</li>
          <li>Print Concepts game</li>
          <li>Encoding game</li>
          <li>Phoneme blending game</li>
          <li>Playtest with target users</li>
          <li>Font readability audit</li>
        </ul>
      </div></div>
    </div>

    <div class="rm-stage future" onclick="this.classList.toggle('open')">
      <div class="rm-dot"></div>
      <div class="rm-header"><span class="rm-badge rm-badge-future">Upcoming</span><span class="rm-title">Stage 4 — Deliver (Polish &amp; Ship)</span></div>
      <div class="rm-body"><div class="rm-content">
        <ul class="rm-items">
          <li>Full session playtest (3+ games in sequence)</li>
          <li>Curriculum alignment sign-off</li>
          <li>Accessibility audit</li>
          <li>Device testing</li>
          <li>Analytics instrumentation</li>
        </ul>
      </div></div>
    </div>

  </div>
</div>

</main>
<footer>OL Project HQ · Auto-generated</footer>

<script>
function toggleProfile(id){{
  const el=document.getElementById(id);
  const isOpen=el.classList.contains('open');
  // Close all profiles first
  document.querySelectorAll('.profile').forEach(p=>p.classList.remove('open'));
  // Open this one if it wasn't already open
  if(!isOpen) el.classList.add('open');
}}
</script>
</body>
</html>'''

if __name__ == '__main__':
    output = generate()
    with open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(output)
    games = scan_games()
    skills = scan_skills()
    decisions = scan_decisions()
    resources = scan_resources()
    print(f'✓ index.html generated')
    print(f'  {len(games)} games, {len(skills)} skills, {len(decisions)} decisions, {len(resources)} resources')
