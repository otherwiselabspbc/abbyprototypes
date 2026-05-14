#!/usr/bin/env python3
"""
build-hub.py — Scans the OL Prototypes project and generates index.html

Run:  python3 build-hub.py
Then open index.html in your browser.
"""

import os, re, glob, html
from datetime import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
SKILLS_DIR = os.path.join(ROOT, '.claude', 'skills')

def esc(s):
    return html.escape(str(s))

# ══════════════════════════════════════
# SCAN GAMES
# ══════════════════════════════════════
def scan_games():
    # Scan both root and minigame prototypes subfolder
    files = sorted(
        glob.glob(os.path.join(ROOT, 'game-*.html')) +
        glob.glob(os.path.join(ROOT, '*.html')) +
        glob.glob(os.path.join(ROOT, 'minigame prototypes', '*.html'))
    )
    # Deduplicate and filter to game/lesson/quest/spell/enchanted files
    seen = set()
    filtered = []
    for f in files:
        name = os.path.basename(f)
        if name in seen or name == 'index.html':
            continue
        seen.add(name)
        if any(kw in name for kw in ['game-','quest','spell','enchanted','lesson','harp']):
            filtered.append(f)
    files = filtered
    games = []
    for f in files:
        name = os.path.basename(f)
        content = open(f, encoding='utf-8').read()
        m = re.search(r'<title>(.*?)</title>', content)
        title = re.sub(r'\s*[—–-]\s*.+$', '', m.group(1)).strip() if m else name
        m2 = re.search(r'class="skill-tag"[^>]*>(.*?)</', content)
        skill = m2.group(1).strip() if m2 else ''
        m3 = re.search(r'class="eyebrow"[^>]*>(.*?)</', content)
        domain = m3.group(1).strip() if m3 else ''
        num = re.search(r'game-(\d+)', name)
        num = num.group(1) if num else '?'
        games.append(dict(file=name, num=num, title=title, domain=domain, skill=skill))
    return games

# ══════════════════════════════════════
# SCAN SKILLS
# ══════════════════════════════════════
def scan_skills():
    if not os.path.isdir(SKILLS_DIR):
        return []
    skills = []
    for d in sorted(os.listdir(SKILLS_DIR)):
        sf = os.path.join(SKILLS_DIR, d, 'SKILL.md')
        if not os.path.isfile(sf):
            continue
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

# ══════════════════════════════════════
# SCAN DECISIONS
# ══════════════════════════════════════
def scan_decisions():
    df = os.path.join(ROOT, 'decisions.md')
    if not os.path.isfile(df):
        return []
    content = open(df, encoding='utf-8').read()
    blocks = re.split(r'\n## DEC-', content)[1:]
    decs = []
    for block in blocks:
        lines = block.strip().split('\n')
        im = re.match(r'^(\d+):\s*(.+)', lines[0] if lines else '')
        did = f'DEC-{im.group(1)}' if im else '?'
        title = im.group(2).strip() if im else lines[0].strip() if lines else ''
        date = (re.search(r'\*\*Date:\*\*\s*(.+)', block) or type('',(),{'group':lambda s,x:''})()).group(1).strip() if re.search(r'\*\*Date:\*\*', block) else ''
        domain = (re.search(r'\*\*Domain:\*\*\s*(.+)', block) or type('',(),{'group':lambda s,x:''})()).group(1).strip() if re.search(r'\*\*Domain:\*\*', block) else ''
        status = (re.search(r'\*\*Status:\*\*\s*(.+)', block) or type('',(),{'group':lambda s,x:''})()).group(1).strip() if re.search(r'\*\*Status:\*\*', block) else ''
        decs.append(dict(id=did, title=title, date=date, domain=domain, status=status))
    return decs

# ══════════════════════════════════════
# SCAN RESOURCES
# ══════════════════════════════════════
def scan_resources():
    rf = os.path.join(SKILLS_DIR, 'resources', 'SKILL.md')
    if not os.path.isfile(rf):
        return []
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

# ══════════════════════════════════════
# SCAN DOCS
# ══════════════════════════════════════
def scan_docs():
    docs = []
    if os.path.isfile(os.path.join(ROOT, 'game vision.md')):
        docs.append(dict(file='game vision.md', title='Product Vision',
                         desc='Garden overworld concept, skill-to-plant mapping, three-phase roadmap, design principles.'))
    decs = scan_decisions()
    if os.path.isfile(os.path.join(ROOT, 'decisions.md')):
        docs.append(dict(file='decisions.md', title='Decision Log',
                         desc=f'{len(decs)} design decisions with rationale, evidence, and status.'))
    if os.path.isfile(os.path.join(ROOT, 'Reading Exercise to Game Mechanic.csv')):
        docs.append(dict(file='Reading Exercise to Game Mechanic.csv', title='Curriculum Map (CSV)',
                         desc='~50 Orton-Gillingham activities with modalities, sample items, and game mechanic ideas.'))
    return docs

# ══════════════════════════════════════
# SVG ICONS
# ══════════════════════════════════════
ICONS = {
    'games': '<svg viewBox="0 0 24 24" fill="none" stroke="#20a39e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="6" width="20" height="12" rx="3"/><line x1="6" y1="10" x2="6" y2="14"/><line x1="4" y1="12" x2="8" y2="12"/><circle cx="16" cy="10" r="1" fill="#20a39e"/><circle cx="18" cy="13" r="1" fill="#20a39e"/></svg>',
    'docs': '<svg viewBox="0 0 24 24" fill="none" stroke="#20a39e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="8" y1="13" x2="16" y2="13"/><line x1="8" y1="17" x2="13" y2="17"/></svg>',
    'frameworks': '<svg viewBox="0 0 24 24" fill="none" stroke="#20a39e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a7 7 0 0 1 0 14 7 7 0 0 1 0-14"/><path d="M12 8v4l3 3"/></svg>',
    'resources': '<svg viewBox="0 0 24 24" fill="none" stroke="#20a39e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>',
    'decisions': '<svg viewBox="0 0 24 24" fill="none" stroke="#20a39e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>',
    'status': '<svg viewBox="0 0 24 24" fill="none" stroke="#20a39e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>',
    'vision': '<svg viewBox="0 0 24 24" fill="none" stroke="#20a39e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22c4-4 8-7.5 8-12a8 8 0 1 0-16 0c0 4.5 4 8 8 12z"/><path d="M12 10v4"/><path d="M10 12h4"/></svg>',
    'grid': '<svg viewBox="0 0 24 24" fill="none" stroke="#20a39e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>',
    'star': '<svg viewBox="0 0 24 24" fill="none" stroke="#20a39e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>',
    'wrench': '<svg viewBox="0 0 24 24" fill="none" stroke="#20a39e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>',
}

SKILL_ICONS = {
    'curriculum-mapping': '<svg viewBox="0 0 24 24" fill="none" stroke="#20a39e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/><line x1="9" y1="7" x2="16" y2="7"/><line x1="9" y1="11" x2="14" y2="11"/></svg>',
    'game-based-learning': '<svg viewBox="0 0 24 24" fill="none" stroke="#20a39e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c0 2 3 3 6 3s6-1 6-3v-5"/></svg>',
    'game-storyboard': '<svg viewBox="0 0 24 24" fill="none" stroke="#20a39e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="9" x2="9" y2="21"/></svg>',
    'game-vision': ICONS['star'],
    'mda': '<svg viewBox="0 0 24 24" fill="none" stroke="#20a39e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>',
    'octalysis': '<svg viewBox="0 0 24 24" fill="none" stroke="#20a39e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>',
    'product-management': '<svg viewBox="0 0 24 24" fill="none" stroke="#20a39e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h20v18H2z"/><path d="M2 9h20"/><path d="M9 3v18"/></svg>',
    'resources': ICONS['resources'],
    'ui-ux': '<svg viewBox="0 0 24 24" fill="none" stroke="#20a39e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>',
}

# ══════════════════════════════════════
# GENERATE
# ══════════════════════════════════════
def generate():
    games = scan_games()
    skills = scan_skills()
    docs = scan_docs()
    decisions = scan_decisions()
    resources = scan_resources()
    now = datetime.now().strftime('%B %d, %Y')

    playable = [g for g in games if g['num'].isdigit() and int(g['num']) >= 3 or not g['num'].isdigit()]

    quick_links = '\n  '.join(
        f'<a class="quick-link" href="{esc(g["file"])}" onclick="sessionStorage.setItem(\'fromGarden\',\'1\')">{esc(g["title"])}</a>'
        for g in playable
    )

    game_rows = '\n    '.join(
        f'<tr><td>{esc(g["num"])}</td>'
        f'<td><a href="{esc(g["file"])}" onclick="sessionStorage.setItem(\'fromGarden\',\'1\')">{esc(g["title"])}</a></td>'
        f'<td>{esc(g["domain"])}</td><td>{esc(g["skill"])}</td>'
        f'<td><span class="status status-done">Done</span></td></tr>'
        for g in games
    )

    doc_cards = '\n    '.join(
        f'''<a class="card" href="{esc(d["file"])}">
      <span class="card-icon">{[ICONS["vision"], ICONS["decisions"], ICONS["grid"]][i] if i<3 else ICONS["docs"]}</span>
      <div class="card-title">{esc(d["title"])}</div>
      <div class="card-desc">{esc(d["desc"])}</div>
    </a>''' for i, d in enumerate(docs)
    )

    skill_cards = '\n    '.join(
        f'''<a class="card" href="{esc(s["path"])}">
      <span class="card-icon">{SKILL_ICONS.get(s["dir"], ICONS["star"])}</span>
      <div class="card-title">{esc(s["name"])}</div>
      <div class="card-desc">{esc(s["description"][:150])}{"..." if len(s["description"])>150 else ""}</div>
      <div class="card-meta"><span class="tag tag-blue">/{esc(s["name"])}</span></div>
    </a>''' for s in skills
    )

    resource_rows = '\n    '.join(
        f'<tr><td>{esc(r["id"])}</td><td>{esc(r["title"])}</td><td>{esc(r["authors"])}</td>'
        f'<td><span class="tag">{esc(r["type"])}</span></td>'
        f'<td>{esc(r["topics"][:60])}{"..." if len(r["topics"])>60 else ""}</td>'
        f'<td><span class="tag tag-blue">{esc(r["skill"])}</span></td></tr>'
        for r in resources
    )

    decision_rows = '\n    '.join(
        f'<tr><td>{esc(d["id"])}</td>'
        f'<td><a href="decisions.md">{esc(d["title"])}</a></td>'
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
<link href="https://fonts.googleapis.com/css2?family=Abel&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#f5f0e8;font-family:'Inter',sans-serif;color:#2d1b0e;min-height:100vh}}
header{{background:linear-gradient(135deg,#20a39e 0%,#178a86 100%);padding:40px 24px 32px;text-align:center}}
header h1{{font-family:'Abel',sans-serif;font-size:clamp(24px,5vw,38px);color:#fff;font-weight:800;margin-bottom:8px;letter-spacing:-0.02em}}
header p{{font-size:14px;color:rgba(255,255,255,0.85);max-width:500px;margin:0 auto;line-height:1.6}}
header .meta{{font-size:11px;color:rgba(255,255,255,0.5);margin-top:8px}}
main{{max-width:960px;margin:0 auto;padding:24px}}
.section{{margin-bottom:36px}}
.section-title{{font-family:'Abel',sans-serif;font-size:18px;font-weight:700;color:#20a39e;margin-bottom:16px;padding-bottom:8px;border-bottom:3px solid #ffba49;display:flex;align-items:center;gap:10px}}
.section-title svg{{width:22px;height:22px;vertical-align:middle;flex-shrink:0}}
.cards{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px}}
.card{{background:#fff;border-radius:12px;padding:20px;border:2px solid #e4e0da;transition:border-color .15s,box-shadow .15s;text-decoration:none;color:inherit;display:block}}
.card:hover{{border-color:#ef5b5b;box-shadow:0 4px 12px rgba(239,71,111,0.12)}}
.card-icon{{margin-bottom:10px;display:block;width:32px;height:32px}}
.card-icon svg{{width:32px;height:32px}}
.card-title{{font-family:'Abel',sans-serif;font-weight:700;font-size:16px;color:#20a39e;margin-bottom:6px}}
.card-desc{{font-size:13px;color:#555;line-height:1.55}}
.card-meta{{font-size:11px;color:#a09080;margin-top:10px;display:flex;gap:12px;flex-wrap:wrap}}
.tag{{background:#fff4d6;padding:2px 8px;border-radius:10px;font-size:10px;font-weight:600;color:#a07800}}
.tag-green{{background:#e8f5e0;color:#2d6a1e}}
.tag-blue{{background:#d8f5f3;color:#20a39e}}
.tag-red{{background:#fde0e0;color:#ef5b5b}}
.status{{display:inline-block;padding:3px 10px;border-radius:10px;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:1px}}
.status-done{{background:#e8f5e0;color:#2d6a1e}}
.status-backlog{{background:#e8e4de;color:#888}}
.table-wrap{{overflow-x:auto}}
table{{width:100%;border-collapse:collapse;font-size:13px}}
th{{text-align:left;padding:10px 12px;background:#20a39e;color:#fff;font-weight:600;font-size:11px;text-transform:uppercase;letter-spacing:1px}}
td{{padding:10px 12px;border-bottom:1px solid #e8dcc8}}
tr:hover td{{background:#faf6f0}}
td a{{color:#ef5b5b;text-decoration:none;font-weight:500}}
td a:hover{{text-decoration:underline}}
.quick-bar{{background:#fff;border:2px solid #e4e0da;border-radius:12px;padding:16px 20px;margin-bottom:24px;display:flex;gap:16px;flex-wrap:wrap;align-items:center}}
.quick-bar-label{{font-size:11px;font-weight:700;color:#20a39e;text-transform:uppercase;letter-spacing:1px}}
.quick-link{{font-size:13px;color:#20a39e;text-decoration:none;font-weight:600;padding:4px 12px;border-radius:8px;background:#d8f5f3;transition:background .15s}}
.quick-link:hover{{background:#ef5b5b;color:#fff}}
footer{{text-align:center;padding:24px;font-size:11px;color:#a09080}}

/* ══ ROADMAP ══ */
.roadmap{{position:relative;padding-left:36px}}
.roadmap::before{{content:'';position:absolute;left:14px;top:0;bottom:0;width:3px;background:#e4e0da}}
.rm-stage{{position:relative;margin-bottom:28px}}
.rm-dot{{position:absolute;left:-30px;top:6px;width:18px;height:18px;border-radius:50%;border:3px solid #e4e0da;background:#f5f0e8;z-index:2;transition:all .2s}}
.rm-stage.done .rm-dot{{background:#20a39e;border-color:#20a39e}}
.rm-stage.active .rm-dot{{background:#ffba49;border-color:#ffba49;box-shadow:0 0 0 4px rgba(255,186,73,0.25)}}
.rm-stage.future .rm-dot{{background:#f5f0e8;border-color:#d4d0ca}}
.rm-header{{display:flex;align-items:center;gap:10px;cursor:pointer;padding:8px 0;-webkit-tap-highlight-color:transparent}}
.rm-header:hover .rm-title{{color:#ef5b5b}}
.rm-badge{{font-size:9px;font-weight:700;padding:3px 8px;border-radius:10px;text-transform:uppercase;letter-spacing:1px}}
.rm-badge-done{{background:#d8f5f3;color:#178a86}}
.rm-badge-active{{background:#fff4d6;color:#a07800}}
.rm-badge-future{{background:#e8e4de;color:#999}}
.rm-type{{font-size:9px;color:#999;font-style:italic}}
.rm-title{{font-family:'Abel',sans-serif;font-size:16px;font-weight:700;color:#2d1b0e;transition:color .15s}}
.rm-body{{max-height:0;overflow:hidden;transition:max-height .35s ease-out}}
.rm-stage.open .rm-body{{max-height:2000px;transition:max-height .5s ease-in}}
.rm-content{{padding:12px 0 8px;border-left:2px solid #e4e0da;margin-left:8px;padding-left:16px}}
.rm-milestone{{margin-bottom:16px}}
.rm-milestone-title{{font-family:'Abel',sans-serif;font-size:14px;font-weight:600;color:#20a39e;margin-bottom:6px}}
.rm-items{{list-style:none;padding:0}}
.rm-items li{{font-size:12px;color:#555;line-height:1.7;padding:2px 0;display:flex;align-items:flex-start;gap:8px}}
.rm-items li::before{{content:'';display:inline-block;width:14px;height:14px;border-radius:3px;border:2px solid #d4d0ca;flex-shrink:0;margin-top:2px}}
.rm-items li.done::before{{background:#20a39e;border-color:#20a39e;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 14 14' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M3 7l3 3 5-5' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E")}}
.rm-items li.done{{color:#999;text-decoration:line-through;text-decoration-color:#ccc}}
.rm-req{{margin-top:8px;font-size:11px;color:#888;background:#faf6f0;padding:8px 12px;border-radius:6px;border-left:3px solid #ffba49}}
.rm-req strong{{color:#a07800}}
.rm-diamond{{display:flex;align-items:center;gap:6px;margin:4px 0 8px}}
.rm-diamond-shape{{width:28px;height:14px;position:relative}}
.rm-diamond-shape::before,.rm-diamond-shape::after{{content:'';position:absolute;top:0;width:0;height:0;border-style:solid}}
.rm-diamond-shape::before{{left:0;border-width:7px 0 7px 14px;border-color:transparent transparent transparent #20a39e}}
.rm-diamond-shape::after{{right:0;border-width:7px 14px 7px 0;border-color:transparent #178a86 transparent transparent}}
.rm-diamond-label{{font-size:9px;color:#999;text-transform:uppercase;letter-spacing:1px}}
</style>
</head>
<body>
<header>
  <h1>OL Prototypes</h1>
  <p>An RPG that adapts evidence-based dyslexia tutoring into playful game mechanics. Mini-games, world-building, and a curriculum backbone that makes learning feel like an adventure.</p>
  <div class="meta">Last built: {esc(now)} &middot; {len(games)} games &middot; {len(skills)} skills &middot; {len(decisions)} decisions &middot; {len(resources)} resources</div>
</header>
<main>

<div class="quick-bar">
  <span class="quick-bar-label">Quick Launch</span>
  <a class="quick-link" href="garden-overworld.html">Garden Overworld</a>
  {quick_links}
</div>

<div class="section">
  <div class="section-title">{ICONS['games']} Mini-Games ({len(games)})</div>
  <div class="table-wrap"><table>
    <tr><th>#</th><th>Game</th><th>Domain</th><th>Skill</th><th>Status</th></tr>
    {game_rows}
  </table></div>
</div>

<div class="section">
  <div class="section-title">{ICONS['docs']} Project Documents ({len(docs)})</div>
  <div class="cards">
    {doc_cards}
  </div>
</div>

<div class="section">
  <div class="section-title">{ICONS['frameworks']} Design Frameworks ({len(skills)})</div>
  <div class="cards">
    {skill_cards}
  </div>
</div>

{"" if not resources else f"""<div class="section">
  <div class="section-title">{ICONS['resources']} Research Sources ({len(resources)})</div>
  <div class="table-wrap"><table>
    <tr><th>ID</th><th>Title</th><th>Authors</th><th>Type</th><th>Topics</th><th>Skill</th></tr>
    {resource_rows}
  </table></div>
</div>"""}

{"" if not decisions else f"""<div class="section">
  <div class="section-title">{ICONS['decisions']} Decision Log ({len(decisions)})</div>
  <div class="table-wrap"><table>
    <tr><th>ID</th><th>Decision</th><th>Domain</th><th>Date</th><th>Status</th></tr>
    {decision_rows}
  </table></div>
</div>"""}

<!-- ROADMAP -->
<div class="section">
  <div class="section-title">{ICONS['status']} Project Roadmap</div>

  <div style="font-size:12px;color:#888;margin-bottom:16px;display:flex;align-items:center;gap:12px;flex-wrap:wrap">
    <span style="display:flex;align-items:center;gap:4px"><span style="width:10px;height:10px;border-radius:50%;background:#20a39e;display:inline-block"></span> Complete</span>
    <span style="display:flex;align-items:center;gap:4px"><span style="width:10px;height:10px;border-radius:50%;background:#ffba49;display:inline-block"></span> In Progress</span>
    <span style="display:flex;align-items:center;gap:4px"><span style="width:10px;height:10px;border-radius:50%;background:#e4e0da;display:inline-block"></span> Upcoming</span>
    <span style="font-size:11px;color:#aaa;margin-left:8px">Click any stage to expand</span>
  </div>

  <div class="roadmap">

    <!-- STAGE 0 -->
    <div class="rm-stage done" onclick="this.classList.toggle('open')">
      <div class="rm-dot"></div>
      <div class="rm-header">
        <span class="rm-badge rm-badge-done">Complete</span>
        <span class="rm-title">Stage 0 — Vision &amp; Strategy</span>
      </div>
      <div class="rm-body"><div class="rm-content">
        <div class="rm-diamond"><div class="rm-diamond-shape"></div><span class="rm-diamond-label">Foundation</span></div>
        <div class="rm-milestone">
          <div class="rm-milestone-title">Define the product</div>
          <ul class="rm-items">
            <li class="done">Write product vision document</li>
            <li class="done">Define target audience (tweens with dyslexia, tutors, families)</li>
            <li class="done">Map curriculum backbone from OG activities (CSV)</li>
            <li class="done">Choose platform (browser-first, mobile touch)</li>
            <li class="done">Establish design principles (6 principles)</li>
          </ul>
        </div>
        <div class="rm-milestone">
          <div class="rm-milestone-title">Set creative direction</div>
          <ul class="rm-items">
            <li class="done">Explore aesthetic directions (dark fantasy → pixel RPG → cozy illustrated)</li>
            <li class="done">Settle on garden overworld concept</li>
            <li class="done">Define skill-to-plant mapping (6 domains → 6 plant types)</li>
            <li class="done">Design currency system (Seeds + Sunshine)</li>
          </ul>
        </div>
        <div class="rm-req"><strong>Requires:</strong> Product vision doc, curriculum CSV, design principles</div>
      </div></div>
    </div>

    <!-- STAGE 1 -->
    <div class="rm-stage done" onclick="this.classList.toggle('open')">
      <div class="rm-dot"></div>
      <div class="rm-header">
        <span class="rm-badge rm-badge-done">Complete</span>
        <span class="rm-type">Diverge ◇</span>
        <span class="rm-title">Stage 1 — Discover</span>
      </div>
      <div class="rm-body"><div class="rm-content">
        <div class="rm-diamond"><div class="rm-diamond-shape"></div><span class="rm-diamond-label">Diverge — explore the problem space</span></div>
        <div class="rm-milestone">
          <div class="rm-milestone-title">Research foundations</div>
          <ul class="rm-items">
            <li class="done">Read &amp; distill Handbook of Game-Based Learning (R-001)</li>
            <li class="done">Read &amp; distill Actionable Gamification / Octalysis (R-002)</li>
            <li class="done">Read &amp; distill MDA Framework (R-003)</li>
            <li class="done">Review OG / Lindamood-Bell methodology for curriculum mapping</li>
          </ul>
        </div>
        <div class="rm-milestone">
          <div class="rm-milestone-title">User research (to do)</div>
          <ul class="rm-items">
            <li>Interview 3-5 OG tutors about current teaching methods</li>
            <li>Interview 3-5 parents/caregivers about home reading practice</li>
            <li>Observe 2-3 live tutoring sessions (contextual inquiry)</li>
            <li>Audit comparable products (Nessy, Reading Eggs, Teach Your Monster)</li>
          </ul>
        </div>
        <div class="rm-req"><strong>Requires:</strong> Access to OG tutors, IRB/consent for kid observation, competitor accounts</div>
      </div></div>
    </div>

    <!-- STAGE 2 -->
    <div class="rm-stage done" onclick="this.classList.toggle('open')">
      <div class="rm-dot"></div>
      <div class="rm-header">
        <span class="rm-badge rm-badge-done">Complete</span>
        <span class="rm-type">Converge ◇</span>
        <span class="rm-title">Stage 2 — Define</span>
      </div>
      <div class="rm-body"><div class="rm-content">
        <div class="rm-diamond"><div class="rm-diamond-shape"></div><span class="rm-diamond-label">Converge — synthesize into clear direction</span></div>
        <div class="rm-milestone">
          <div class="rm-milestone-title">Establish frameworks</div>
          <ul class="rm-items">
            <li class="done">Create /curriculum-mapping skill</li>
            <li class="done">Create /game-based-learning skill</li>
            <li class="done">Create /octalysis skill</li>
            <li class="done">Create /mda skill</li>
            <li class="done">Create /ui-ux skill</li>
            <li class="done">Create /game-storyboard skill (5-screen structure)</li>
            <li class="done">Create /product-management skill</li>
            <li class="done">Create /resources skill</li>
          </ul>
        </div>
        <div class="rm-milestone">
          <div class="rm-milestone-title">Lock key decisions</div>
          <ul class="rm-items">
            <li class="done">Learn &amp; Practice two-phase game structure (DEC-003)</li>
            <li class="done">3-tier hint escalation replacing lives (DEC-004)</li>
            <li class="done">Process feedback on every answer (DEC-004)</li>
            <li class="done">Plants pause but never die (DEC-002)</li>
            <li class="done">One skill per game (DEC-007)</li>
            <li class="done">Dual currency: Seeds + Sunshine (DEC-006)</li>
            <li class="done">Cozy illustrated aesthetic (DEC-005)</li>
          </ul>
        </div>
        <div class="rm-milestone">
          <div class="rm-milestone-title">Define personas (to do)</div>
          <ul class="rm-items">
            <li>Create 3 user personas (Learner, Tutor, Parent)</li>
            <li>Create empathy maps for each</li>
            <li>Map current-state journey (tutoring session, homework)</li>
          </ul>
        </div>
        <div class="rm-req"><strong>Requires:</strong> User research insights, design principles, framework skills</div>
      </div></div>
    </div>

    <!-- STAGE 3 — CURRENT -->
    <div class="rm-stage active open" onclick="this.classList.toggle('open')">
      <div class="rm-dot"></div>
      <div class="rm-header">
        <span class="rm-badge rm-badge-active">In Progress</span>
        <span class="rm-type">Diverge ◇</span>
        <span class="rm-title">Stage 3 — Develop (current)</span>
      </div>
      <div class="rm-body"><div class="rm-content">
        <div class="rm-diamond"><div class="rm-diamond-shape"></div><span class="rm-diamond-label">Diverge — build and test many prototypes</span></div>

        <div class="rm-milestone">
          <div class="rm-milestone-title">Milestone 3A: Core prototypes ({len(games)} of 7 target)</div>
          <ul class="rm-items">
            <li class="done">Game 01: Rune Stones (PA — Phoneme Sequence)</li>
            <li class="done">Game 02: Enchanted Harp (PA — Phoneme Sequence alt)</li>
            <li class="done">Game 03: Whispering Stones (PA — Rhyme Detection)</li>
            <li class="done">Game 04: Block Breaker (Letter Knowledge — Tap)</li>
            <li class="done">Game 05: Seed Script (Letter Knowledge — Trace)</li>
            <li class="done">Game 06: Syllable Sprout (PA — Syllable Counting)</li>
            <li>Game 07: Print Concepts game (TBD)</li>
          </ul>
          <div class="rm-req"><strong>Requires:</strong> /curriculum-mapping for skill selection, /game-storyboard for structure, /mda audit per game</div>
        </div>

        <div class="rm-milestone">
          <div class="rm-milestone-title">Milestone 3B: Garden overworld</div>
          <ul class="rm-items">
            <li class="done">Build garden overworld with illustrated environment</li>
            <li class="done">Connect games to garden plots (3 linked, others "coming soon")</li>
            <li class="done">Add winding path with curriculum-ordered plots</li>
            <li class="done">Add shop with currency system</li>
            <li>Add daily return mechanic (plant wilting/perking)</li>
            <li>Add shop items that visually change the garden</li>
            <li>Add plant growth animations triggered by game completion</li>
          </ul>
          <div class="rm-req"><strong>Requires:</strong> Garden prototype, game-to-overworld navigation, sessionStorage state</div>
        </div>

        <div class="rm-milestone">
          <div class="rm-milestone-title">Milestone 3C: Remaining game domains</div>
          <ul class="rm-items">
            <li>Alphabetic Principle game (CSV rows 29-31)</li>
            <li>Decoding game (CSV rows 38-42)</li>
            <li>Encoding game (CSV rows 47-50)</li>
            <li>PA — Phoneme Counting (CSV row 21)</li>
            <li>PA — Syllable Blending (CSV row 22)</li>
            <li>PA — Phoneme Blending (CSV row 23)</li>
          </ul>
          <div class="rm-req"><strong>Requires:</strong> Core prototype patterns established from 3A, reusable game templates</div>
        </div>

        <div class="rm-milestone">
          <div class="rm-milestone-title">Milestone 3D: Playtesting</div>
          <ul class="rm-items">
            <li>Paper prototype test with 1-2 kids (per new mechanic)</li>
            <li>Lo-fi playtest with 3-5 kids (moderated, 15min sessions)</li>
            <li>Hi-fi playtest with 3-5 kids (unmoderated, pre/post skill check)</li>
            <li>Tutor feedback session on curriculum alignment</li>
            <li>Write playtest reports using /product-management template</li>
          </ul>
          <div class="rm-req"><strong>Requires:</strong> Access to target users, playtest consent, recording setup, smiley-face rating scales</div>
        </div>

        <div class="rm-milestone">
          <div class="rm-milestone-title">Milestone 3E: Branding &amp; polish</div>
          <ul class="rm-items">
            <li>Audit font readability for dyslexic users</li>
            <li>Design mascot / NPC shop keeper character</li>
            <li>Create ambient garden soundtrack</li>
            <li>Design plant growth sound effects</li>
            <li>Build UI component library (buttons, cards, modals)</li>
          </ul>
          <div class="rm-req"><strong>Requires:</strong> Settled art direction, sound design brief, /ui-ux audit</div>
        </div>
      </div></div>
    </div>

    <!-- STAGE 4 -->
    <div class="rm-stage future" onclick="this.classList.toggle('open')">
      <div class="rm-dot"></div>
      <div class="rm-header">
        <span class="rm-badge rm-badge-future">Upcoming</span>
        <span class="rm-type">Converge ◇</span>
        <span class="rm-title">Stage 4 — Deliver</span>
      </div>
      <div class="rm-body"><div class="rm-content">
        <div class="rm-diamond"><div class="rm-diamond-shape"></div><span class="rm-diamond-label">Converge — polish and ship</span></div>

        <div class="rm-milestone">
          <div class="rm-milestone-title">Milestone 4A: Validation</div>
          <ul class="rm-items">
            <li>Full session playtest (overworld → 3+ games in sequence → return)</li>
            <li>Curriculum alignment sign-off from OG tutor</li>
            <li>Accessibility audit (contrast, touch targets, dyslexia-friendly fonts)</li>
            <li>Device testing (mobile Safari, Chrome, iPad, Android tablet)</li>
          </ul>
          <div class="rm-req"><strong>Requires:</strong> All target games complete, tutor reviewer, WCAG checklist</div>
        </div>

        <div class="rm-milestone">
          <div class="rm-milestone-title">Milestone 4B: Launch prep</div>
          <ul class="rm-items">
            <li>Design first-time onboarding flow (kid + tutor)</li>
            <li>Instrument analytics (completion rate, error patterns, time on task)</li>
            <li>Create parent/tutor dashboard (progress visibility)</li>
            <li>Deploy to GitHub Pages or hosting platform</li>
            <li>Write launch communications for tutors and families</li>
          </ul>
          <div class="rm-req"><strong>Requires:</strong> Validated prototype, analytics infrastructure, hosting setup</div>
        </div>

        <div class="rm-milestone">
          <div class="rm-milestone-title">Milestone 4C: Retrospective</div>
          <ul class="rm-items">
            <li>Document what mechanics worked best</li>
            <li>Identify games to carry into Phase 2 (Escape Rooms)</li>
            <li>Write Phase 1 retrospective</li>
            <li>Plan Phase 2 scope</li>
          </ul>
        </div>
      </div></div>
    </div>

    <!-- PHASE 2 -->
    <div class="rm-stage future" onclick="this.classList.toggle('open')">
      <div class="rm-dot"></div>
      <div class="rm-header">
        <span class="rm-badge rm-badge-future">Future</span>
        <span class="rm-title">Phase 2 — Escape Rooms</span>
      </div>
      <div class="rm-body"><div class="rm-content">
        <div class="rm-milestone">
          <div class="rm-milestone-title">Sequence best mechanics into structured progression</div>
          <ul class="rm-items">
            <li>Each room: Learn a skill → Practice → Demonstrate mastery → Unlock next room</li>
            <li>Full garden as explorable space with walking, tending, shopping</li>
            <li>Live currency economy</li>
            <li>Polished daily check-in loop</li>
          </ul>
        </div>
      </div></div>
    </div>

    <!-- PHASE 3 -->
    <div class="rm-stage future" onclick="this.classList.toggle('open')">
      <div class="rm-dot"></div>
      <div class="rm-header">
        <span class="rm-badge rm-badge-future">Future</span>
        <span class="rm-title">Phase 3 — The Living World</span>
      </div>
      <div class="rm-body"><div class="rm-content">
        <div class="rm-milestone">
          <div class="rm-milestone-title">Expand into a full world</div>
          <ul class="rm-items">
            <li>Neighboring gardens, seasonal events, rare plants</li>
            <li>Social features (visit a friend's garden)</li>
            <li>Full curriculum embedded in world mechanics</li>
            <li>Greenhouse for advanced skills</li>
          </ul>
        </div>
      </div></div>
    </div>

  </div>
</div>

</main>
<footer>OL Prototypes — Phase 1 Mini-Games &middot; Auto-generated by build-hub.py</footer>
</body>
</html>'''

# ══════════════════════════════════════
# WRITE
# ══════════════════════════════════════
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
