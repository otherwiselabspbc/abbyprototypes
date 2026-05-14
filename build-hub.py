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
        skills.append(dict(dir=d, name=name, description=desc, path=f'.claude/skills/{d}/SKILL.md'))
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
        lines = block.strip().split('\n')
        im = re.match(r'^(\d+):\s*(.+)', lines[0] if lines else '')
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
        docs.append(dict(file='game vision.md', title='Product Vision', desc='Core concept, three-phase roadmap, design principles.'))
    decs = scan_decisions()
    if os.path.isfile(os.path.join(ROOT, 'decisions.md')):
        docs.append(dict(file='decisions.md', title='Decision Log', desc=f'{len(decs)} design decisions with rationale and evidence.'))
    if os.path.isfile(os.path.join(ROOT, 'Reading Exercise to Game Mechanic.csv')):
        docs.append(dict(file='Reading Exercise to Game Mechanic.csv', title='Curriculum Map', desc='~50 Orton-Gillingham activities with modalities and sample items.'))
    return docs

# ═══ GENERATE ═══
def generate():
    games = scan_games()
    skills = scan_skills()
    docs = scan_docs()
    decisions = scan_decisions()
    resources = scan_resources()
    now = datetime.now().strftime('%B %d, %Y')

    # Game rows — no clickable links, "In Progress" default status
    game_rows = '\n    '.join(
        f'<tr><td>{esc(g["num"])}</td>'
        f'<td>{esc(g["title"])}</td>'
        f'<td>{esc(g["domain"])}</td><td>{esc(g["skill"])}</td>'
        f'<td><span class="status status-wip">In Progress</span></td></tr>'
        for g in games
    )

    doc_cards = '\n    '.join(
        f'''<div class="card">
      <div class="card-title">{esc(d["title"])}</div>
      <div class="card-desc">{esc(d["desc"])}</div>
    </div>''' for d in docs
    )

    skill_cards = '\n    '.join(
        f'''<div class="card">
      <div class="card-title">{esc(s["name"])}</div>
      <div class="card-desc">{esc(s["description"][:140])}{"..." if len(s["description"])>140 else ""}</div>
      <div class="card-meta"><span class="tag tag-teal">/{esc(s["name"])}</span></div>
    </div>''' for s in skills
    )

    resource_rows = '\n    '.join(
        f'<tr><td>{esc(r["id"])}</td><td>{esc(r["title"])}</td><td>{esc(r["authors"])}</td>'
        f'<td><span class="tag">{esc(r["type"])}</span></td>'
        f'<td>{esc(r["topics"][:50])}{"..." if len(r["topics"])>50 else ""}</td>'
        f'<td><span class="tag tag-teal">{esc(r["skill"])}</span></td></tr>'
        for r in resources
    )

    decision_rows = '\n    '.join(
        f'<tr><td>{esc(d["id"])}</td>'
        f'<td>{esc(d["title"])}</td>'
        f'<td>{esc(d["domain"])}</td><td>{esc(d["date"])}</td>'
        f'<td><span class="status status-done">{esc(d["status"])}</span></td></tr>'
        for d in decisions
    )

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>OL Prototypes — Project Hub</title>
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

/* Storyboard preview */
.storyboard-link{{display:block;background:#f4f1bb;border:2px solid #e0dda0;border-radius:14px;
  padding:24px;text-decoration:none;color:#2a2a2a;transition:all .15s;margin-bottom:32px}}
.storyboard-link:hover{{border-color:#ed6a5a;box-shadow:0 4px 16px rgba(237,106,90,0.12)}}
.sb-head{{display:flex;align-items:center;gap:14px;margin-bottom:10px}}
.sb-icon{{font-size:28px}}
.sb-title{{font-family:'Lora',serif;font-size:18px;font-weight:700;color:#3a3a3a}}
.sb-desc{{font-size:13px;color:#5a5a5a;line-height:1.55}}
.sb-domains{{display:flex;gap:8px;margin-top:12px;flex-wrap:wrap}}
.sb-domain{{font-size:10px;font-weight:600;padding:3px 10px;border-radius:10px;
  background:rgba(155,193,188,0.3);color:#4a6a66}}

/* Cards */
.cards{{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:14px}}
.card{{background:#fff;border-radius:12px;padding:18px;border:2px solid #eae8e2;
  transition:border-color .15s,box-shadow .15s}}
.card:hover{{border-color:#9bc1bc;box-shadow:0 3px 12px rgba(155,193,188,0.15)}}
.card-title{{font-family:'Lora',serif;font-weight:700;font-size:15px;color:#3a3a3a;margin-bottom:5px}}
.card-desc{{font-size:12px;color:#6a6a6a;line-height:1.55}}
.card-meta{{font-size:10px;color:#999;margin-top:8px;display:flex;gap:10px;flex-wrap:wrap}}

.tag{{background:#f4f1bb;padding:2px 8px;border-radius:8px;font-size:10px;font-weight:600;color:#7a7040}}
.tag-teal{{background:rgba(155,193,188,0.25);color:#4a6a66}}
.tag-red{{background:rgba(237,106,90,0.12);color:#c04a3a}}

/* Tables */
.table-wrap{{overflow-x:auto}}
table{{width:100%;border-collapse:collapse;font-size:12px}}
th{{text-align:left;padding:10px 12px;background:#ed6a5a;color:#fff;font-weight:600;
  font-size:10px;text-transform:uppercase;letter-spacing:1px;font-family:'Lora',serif}}
td{{padding:10px 12px;border-bottom:1px solid #eae8e2;color:#3a3a3a}}
tr:hover td{{background:#faf8f2}}

/* Status badges */
.status{{display:inline-block;padding:3px 10px;border-radius:8px;font-size:9px;
  font-weight:700;text-transform:uppercase;letter-spacing:1px}}
.status-done{{background:rgba(155,193,188,0.25);color:#4a6a66}}
.status-wip{{background:rgba(237,106,90,0.12);color:#c04a3a}}

footer{{text-align:center;padding:28px;font-size:11px;color:#bbb;font-family:'Lora',serif}}
</style>
</head>
<body>
<header>
  <h1>OL Prototypes</h1>
  <p>An RPG that adapts evidence-based dyslexia tutoring into playful game mechanics. Mini-games, world-building, and a curriculum backbone that makes learning feel like an adventure.</p>
  <div class="meta">Last built: {esc(now)} · {len(games)} games · {len(skills)} skills · {len(decisions)} decisions · {len(resources)} resources</div>
</header>
<main>

<!-- Storyboard Link -->
<a class="storyboard-link" href="storyboard.html">
  <div class="sb-head">
    <span class="sb-icon">🗺️</span>
    <span class="sb-title">Game Storyboard</span>
  </div>
  <div class="sb-desc">Interactive zoomable board showing the full curriculum flow. Click to expand domains, lessons, and phases. Click any game to see its beat-by-beat storyboard with editable notes.</div>
  <div class="sb-domains">
    <span class="sb-domain">Print Concepts</span>
    <span class="sb-domain">Letter Knowledge</span>
    <span class="sb-domain">Phonological Awareness</span>
    <span class="sb-domain">Alphabetic Principle</span>
    <span class="sb-domain">Decoding</span>
    <span class="sb-domain">Encoding</span>
    <span class="sb-domain">Comprehension</span>
  </div>
</a>

<!-- Mini-Games -->
<div class="section">
  <div class="section-title">Mini-Games ({len(games)})</div>
  <div class="table-wrap"><table>
    <tr><th>#</th><th>Game</th><th>Domain</th><th>Skill</th><th>Status</th></tr>
    {game_rows}
  </table></div>
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

{"" if not resources else "<div class='section'><div class='section-title'>Research Sources ("+str(len(resources))+")</div><div class='table-wrap'><table><tr><th>ID</th><th>Title</th><th>Authors</th><th>Type</th><th>Topics</th><th>Skill</th></tr>"+resource_rows+"</table></div></div>"}

{"" if not decisions else "<div class='section'><div class='section-title'>Decision Log ("+str(len(decisions))+")</div><div class='table-wrap'><table><tr><th>ID</th><th>Decision</th><th>Domain</th><th>Date</th><th>Status</th></tr>"+decision_rows+"</table></div></div>"}

</main>
<footer>OL Prototypes · Auto-generated by build-hub.py</footer>
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
