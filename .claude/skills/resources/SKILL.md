---
name: resources
description: Central library of all research sources, readings, and references used in the OL Prototypes design process. Search by topic, type, or skill. Get summaries, key takeaways, and see how each resource shaped the product.
---

When this skill is invoked, use it to $ARGUMENTS. Examples:
- `/resources` — show the full library
- `/resources add [title]` — log a new resource
- `/resources topic feedback` — filter by topic
- `/resources summarize [title]` — show key learnings from a specific resource

When adding a new resource, always fill in ALL fields in the entry template below.

---

## Resource Library

### R-001: Handbook of Game-Based Learning

| Field | Value |
|---|---|
| **Title** | Handbook of Game-Based Learning |
| **Authors** | Jan L. Plass, Richard E. Mayer, Bruce D. Homer |
| **Year** | 2019 |
| **Publisher** | MIT Press |
| **Type** | Academic textbook |
| **Pages** | 601 |
| **File** | `~/Downloads/vdoc.pub_handbook-of-game-based-learning.pdf` |
| **Topics** | Cognitive load, feedback design, motivation (SDT), emotional design, narrative, adaptivity, multimedia principles, collaboration vs competition |
| **Skill derived** | `/game-based-learning` |
| **Date added** | 2026-04-15 |

**Key takeaways:**
1. **Cognitive load is the balancing act.** Three types: extraneous (minimize), essential (manage), generative (maximize). Every game element must serve the learning goal or it's a distractor.
2. **Modality principle (d=1.4).** Spoken narration > on-screen text for instructions. Frees the visual channel for gameplay.
3. **Pretraining principle (d=0.8).** Introduce key concepts before gameplay begins — this became our Learn phase.
4. **Process feedback (d=1.31).** Explaining WHY an answer is wrong beats outcome-only ("correct/incorrect"). This became our 3-tier hint escalation.
5. **Self-Determination Theory.** Three needs: competence, autonomy, relatedness. External rewards (points, badges) frequently UNDERMINE intrinsic motivation.
6. **Emotional design.** Warm/bright colors, round shapes, and face-like characters enhance learning outcomes. Dark/muted palettes suppress engagement.
7. **"Chocolate-covered broccoli" warning.** Gamifying a bad task doesn't make it fun — the gameplay must BE the learning.
8. **Confusion can be productive** — but only when the learner can resolve it AND the game provides scaffolds.

**How it shaped our product:**
- Learn & Practice two-phase structure (pretraining principle)
- All instructions spoken aloud (modality principle)
- 3-tier hint escalation with process feedback (feedback research)
- Warm, bright color palette (emotional design)
- No external leaderboards or competitive pressure (SDT warnings)
- Every wrong answer explains WHY (process > outcome feedback)

---

### R-002: Actionable Gamification — Beyond Points, Badges, and Leaderboards

| Field | Value |
|---|---|
| **Title** | Actionable Gamification: Beyond Points, Badges, and Leaderboards |
| **Authors** | Yu-kai Chou |
| **Year** | 2016 |
| **Publisher** | Self-published (Octalysis Media) |
| **Type** | Practitioner book |
| **Pages** | 501 |
| **File** | `~/Downloads/Actionable-Gamification-Full-Book.pdf` |
| **Topics** | 8 Core Drives of motivation, White Hat vs Black Hat gamification, extrinsic vs intrinsic motivation, game technique taxonomy |
| **Skill derived** | `/octalysis` |
| **Date added** | 2026-04-15 |

**Key takeaways:**
1. **8 Core Drives.** All human motivation traces to: Epic Meaning, Accomplishment, Creativity, Ownership, Social Influence, Scarcity, Unpredictability, Loss & Avoidance.
2. **White Hat (top) = empowering, fulfilling.** Black Hat (bottom) = urgent, obsessive. White Hat sustains long-term. Black Hat creates short-term action but burnout.
3. **CD3 (Creativity & Feedback) is the "golden corner."** Both White Hat AND intrinsic. Games that last centuries (Chess, Poker) live here. This is the antidote to gamification fatigue.
4. **The "Toll" problem.** If learning feels like a tax before the fun, the design has failed. Learning must be the player's ALLY in the satisfaction loop.
5. **External rewards undermine intrinsic motivation (Overjustification Effect).** Paying people for creative tasks reduces creative quality.
6. **CD8 (Loss & Avoidance) is the most dangerous drive.** Extraordinarily powerful but demoralizing long-term. Should only be used at critical bumps.
7. **Players are brutally efficient.** They skip anything not in the satisfaction loop.

**How it shaped our product:**
- Garden overworld activates CD1 (meaning), CD4 (ownership), CD3 (creativity via shop/customization)
- Plants never die (CD8 capped at 2/10 for our vulnerable audience)
- Shop currency earned through learning, not purchased (CD4 without pay-to-win)
- Mystery seeds and ambient surprises for CD7 (unpredictability)
- Ideal OL profile: heavily White Hat, moderately Right Brain, minimal Black Hat

---

### R-003: MDA — A Formal Approach to Game Design and Game Research

| Field | Value |
|---|---|
| **Title** | MDA: A Formal Approach to Game Design and Game Research |
| **Authors** | Robin Hunicke, Marc LeBlanc, Robert Zubek |
| **Year** | 2004 |
| **Publisher** | GDC (Game Developers Conference) |
| **Type** | Academic paper |
| **Pages** | 5 |
| **File** | `~/Downloads/MDA.pdf` |
| **Topics** | Game design decomposition, mechanics vs dynamics vs aesthetics, 8 aesthetic categories, experience-driven design |
| **Skill derived** | `/mda` |
| **Date added** | 2026-04-15 |

**Key takeaways:**
1. **Three causally linked layers.** Designers build Mechanics → which produce Dynamics → which create Aesthetics (player feelings). Players experience it in reverse.
2. **8 aesthetics replace "fun."** Sensation, Fantasy, Narrative, Challenge, Fellowship, Discovery, Expression, Submission. Name your targets before building.
3. **Small mechanic changes cascade.** Adjusting one rule can completely alter how the game feels. Always trace changes through all three layers.
4. **Experience-driven > feature-driven.** Ask "What will the player FEEL?" not "What feature should we add?"
5. **No mechanic has value in isolation.** "Is this a good tracing algorithm?" is the wrong question. "Does this tracing algorithm create challenge + satisfaction?" is the right one.

**How it shaped our product:**
- Every new game starts by naming target aesthetics (Challenge, Fantasy, Discovery, Expression)
- MDA audit runs before shipping — does the mechanic actually produce the intended feeling?
- Used to diagnose why games feel "off" — trace backward from the unintended aesthetic to find the broken mechanic

---

### R-004: Otherwise Labs Check-in — Explicit & Systematic Instruction

| Field | Value |
|---|---|
| **Title** | Abby <> Bob Otherwise Labs check-in — Meeting Notes |
| **Authors** | Tyler Ogata, Abigail Garewal, Robert Borges |
| **Year** | 2026 |
| **Publisher** | Internal meeting (Gemini notes) |
| **Type** | Meeting notes |
| **Pages** | 5 |
| **File** | `~/Downloads/Abby __ Bob Otherwise Labs check-in - 2026_05_07 15_00 PDT - Notes by Gemini.pdf` |
| **Topics** | Explicit instruction, systematic teaching, 80/20 ratio, 3-stage learning structure, concealing failure, lesson plan structure, contextualized learning |
| **Skill derived** | `/explicit-instruction` |
| **Date added** | 2026-05-14 |

**Key takeaways:**
1. **80/20 ratio.** Lessons are 80% explicit instruction and 20% practice. Mini-games are the 20% — the game must also contain the 80%.
2. **Explicit means directly telling.** The game states the rule/concept clearly before practice begins. Students don't infer or discover it on their own.
3. **3-stage structure.** Tutorial (teach concept + mechanic) → Supervised Learning (must demonstrate understanding to proceed) → Independent Practice (the sprint).
4. **Systematic linking.** Concepts must be taught in order. Can't teach "I says its name before LD" without first teaching what a long vowel is.
5. **Contextualize learning.** "You need to decode this word to unlock the passage" is better than "practice reading this word."
6. **Conceal failure.** Errors should feel like part of the learning process, not setbacks. No red X marks. Wrong answers trigger re-teaching.
7. **Students should know they're learning.** Awareness of growth is motivating. Pride comes from feeling the skill develop — don't hide that this is educational.
8. **One lesson plan = multiple mini-games.** Each lesson covers different activities; each could be a separate game within a session.

**How it shaped our product:**
- The `/explicit-instruction` skill was created to codify these principles
- Every game must now include explicit concept teaching, not just game-mechanic practice
- The 3-stage structure (Tutorial → Supervised → Independent) replaces our previous simpler Learn/Practice split
- Error feedback must re-teach the concept, not just indicate wrongness

---

### R-005: WRS Lesson Plan Poster

| Field | Value |
|---|---|
| **Title** | WRS Lesson Plan Outline |
| **Authors** | Wilson Reading System |
| **Year** | — |
| **Publisher** | Wilson Language Training |
| **Type** | Reference poster / infographic |
| **Pages** | 1 |
| **File** | `~/Downloads/WRS Lesson Plan Poster.avif` |
| **Topics** | Lesson plan structure, 10-step lesson sequence, reading and spelling instruction flow, session rhythm |
| **Skill derived** | Added to `/explicit-instruction` |
| **Date added** | 2026-05-14 |

**Key takeaways:**
1. **10-step lesson structure.** Sounds drill → Teach concepts → Word cards → Wordlist reading → Sentence reading → Reverse drill → Teach spelling → Written dictation → Passage reading → Fluency & comprehension.
2. **Smallest to largest.** The lesson flows: Sound → Letter → Word → Sentence → Passage → Story. Then reverses for encoding.
3. **Each step has a clear purpose.** Steps 1-5 are reading direction. Steps 6-8 are spelling direction. Steps 9-10 are extended application.
4. **Quick drills bookend the teaching.** Fast sound recognition at the start (Step 1) and fast sound-to-letter at the midpoint (Step 6) act as warm-ups.
5. **Teaching always precedes practice.** Steps 2 and 7 are explicit instruction. Steps 4, 5, 8 are independent practice. The pattern is always: teach → practice → teach → practice.

**How it shaped our product:**
- Maps each mini-game type to a WRS step (Enchanted Gems = Step 1, Spell Caster = Step 4, Quest Catcher = Step 5)
- Shows how mini-games should be sequenced in a session: drill → teach → practice → teach → practice
- Confirms that our games span multiple WRS steps, not just one

---

## Topic Index

Quick lookup — which resource covers which topic:

| Topic | Resources |
|---|---|
| Cognitive load | R-001 (Ch 4, 12) |
| Feedback design | R-001 (Ch 8) |
| Motivation theory | R-001 (Ch 6), R-002 (full book) |
| Emotional design | R-001 (Ch 5, 14) |
| Narrative in games | R-001 (Ch 11), R-003 |
| Adaptivity / scaffolding | R-001 (Ch 10) |
| Player motivation drives | R-002 (8 Core Drives) |
| White Hat vs Black Hat | R-002 (Ch 14) |
| Extrinsic vs intrinsic | R-001 (Ch 6), R-002 (Ch 13) |
| Game feel / aesthetics | R-003 |
| Mechanics → Dynamics → Aesthetics | R-003 |
| Collaboration vs competition | R-001 (Ch 13), R-002 (CD5) |
| Dyslexia / OG methodology | (curriculum CSV), R-004 |
| Multimedia principles | R-001 (Ch 12) |
| Scarcity / retention | R-002 (Ch 10) |
| Loss aversion | R-002 (Ch 12) |
| Explicit instruction | R-004 |
| Systematic teaching / concept sequencing | R-004 |
| Lesson plan structure | R-004 |
| Concealing failure | R-004, R-001 (Ch 5) |
| 80/20 instruction ratio | R-004 |
| 3-stage learning (tutorial/supervised/practice) | R-004 |

---

## Resource Entry Template

When adding a new resource, copy this block:

```
### R-[NNN]: [Title]

| Field | Value |
|---|---|
| **Title** | |
| **Authors** | |
| **Year** | |
| **Publisher** | |
| **Type** | [Academic paper / Textbook / Practitioner book / Article / Video / Talk] |
| **Pages** | |
| **File** | [Path to local file, or URL] |
| **Topics** | [Comma-separated keywords] |
| **Skill derived** | [Which /skill was created from it, if any] |
| **Date added** | |

**Key takeaways:**
1. ...
2. ...
3. ...

**How it shaped our product:**
- ...
```

---

## How to Use This Skill

- **"What does the research say about X?"** → Check the Topic Index, then read the relevant resource's key takeaways.
- **"I just read a new paper."** → `/resources add` and fill in the template. Extract 3-7 key takeaways and document how they apply to OL Prototypes.
- **"Which resource covers feedback?"** → Check the Topic Index row for "Feedback design."
- **"Give me the full summary of R-002."** → Read the entry above or load the original PDF for deeper detail.
- **"How did [resource] shape the product?"** → Each entry has a "How it shaped our product" section linking theory to concrete decisions.
