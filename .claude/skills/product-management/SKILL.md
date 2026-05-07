---
name: product-management
description: Manage the end-to-end design process for OL Prototypes. Covers design stages (Double Diamond), decision logging, user research, prototyping, branding, backlog management, and playtesting methodology. Use when planning work, making design decisions, or organizing the project.
---

When this skill is invoked, use it to $ARGUMENTS. If no argument is given, show the current project status — which stage we're in, what's next, and any open decisions.

---

## The Design Process (Double Diamond + Build)

```
STAGE 0          STAGE 1        STAGE 2        STAGE 3         STAGE 4
Vision &     →   Discover   →   Define     →   Develop     →   Deliver
Strategy         (diverge)      (converge)     (diverge)       (converge)
                  ◇                ◇              ◇               ◇
              What's the      What's the     Build & test     Polish &
              problem?        solution?      many options     ship
```

**Current phase:** Stage 3 (Develop) — building and testing mini-game prototypes.

---

## Stage 0 — Vision & Strategy

**Goal:** Establish purpose, audience, and success criteria.

**Artifacts:**
| Document | Status | Location |
|---|---|---|
| Product Vision | Done | `game vision.md` |
| Curriculum Map | Done | `Reading Exercise to Game Mechanic.csv` |
| Skill → Plant Mapping | Done | In vision doc |
| Platform & Constraints | In progress | Browser-first, mobile-touch, no mic for Phase 1 |

**Open decisions to record:**
- Session length assumptions (5-min bursts? 15-min sessions?)
- Target device (iPad primary? Phone? Desktop browser?)

---

## Stage 1 — Discover (Research)

**Goal:** Understand learners, tutors, and families deeply.

### User Research Methods for Dyslexic Learners

**Special rules:**
- No text-heavy surveys or consent forms — use verbal, picture-based, or emoji scales
- 15-minute max sessions with kids (fatigue onset is fast)
- Pair kid with a trusted adult (tutor or parent nearby, not directing)
- Prefer observation + post-task debrief over think-aloud (verbalizing while reading adds cognitive load)
- Use "Show me" over "Tell me" — ask kids to point, act out, demonstrate

| Method | When | Who | Output |
|---|---|---|---|
| Contextual inquiry | Early | Watch OG tutor session | Journey map, pain points |
| Tutor interview | Early | 3–5 OG practitioners | Personas, insight log |
| Parent interview | Early | 3–5 caregivers | Home context, motivation |
| Analogous audit | Early | — | What cozy games do these kids already love? |
| Card sort | Define stage | Kids + tutors | Information architecture |

**Artifacts to produce:**
- 3 User Personas: The Learner, The Tutor, The Parent
- Empathy Maps for each
- Current-state Journey Map (a typical tutoring session, a typical homework struggle)
- Research Insights Log (tagged observations and quotes)

---

## Stage 2 — Define (Converge)

**Goal:** Turn research into clear problem statements and design principles.

**Activities:**
- Affinity diagram research insights
- Write "How Might We" questions
- Prioritize opportunity areas (learning impact × feasibility)
- Define design principles

**Design Principles (current):**
1. **Evidence-based first.** Every mechanic maps to a proven OG activity.
2. **Growth as metaphor.** The garden grows because the learner grew.
3. **Never punish absence.** Plants pause, never die.
4. **Mastery through play.** If it doesn't feel like a game, it's not ready.
5. **Multisensory always.** Visual + auditory + tactile, every time.
6. **Failure is fertilizer.** Hints escalate, never punish. Every attempt earns acknowledgment.

**Invoke:** `/curriculum-mapping`, `/game-based-learning`, `/octalysis`, `/mda`

---

## Stage 3 — Develop (Build & Test)

**Goal:** Build and playtest many mini-game prototypes. This is where we are now.

### Per-Game Build Pipeline

```
Concept → Storyboard → Lo-fi Build → Playtest → Hi-fi Build → Playtest → Polish → Curriculum Review → Done
```

Limit work-in-progress to **3 games in active build** at once.

### Game Design Document (One-Page GDD Template)

Fill this out before building any new game:

```
GAME:           [Fantasy name]
FILE:           game-XX-[slug].html
SKILL:          [Domain > Subskill]
CSV ROW:        [Row number]

MECHANIC:       [One sentence: what the player does]
GARDEN METAPHOR:[How this maps to plant growth]

INPUT MODALITY: [Visual / Auditory / Both]
OUTPUT MODALITY:[Tactile / Speech / Both]
INTERACTION:    [Tap / Swipe / Trace / Drag / etc.]

MDA BREAKDOWN:
  Mechanics:    [Rules, components, algorithms]
  Dynamics:     [Run-time behavior that emerges]
  Aesthetics:   [Target feelings: Challenge, Fantasy, Discovery, etc.]

OCTALYSIS:
  Primary drives: [Which of the 8 core drives does this game activate?]
  Watch out for:  [Any Black Hat drives to use carefully?]

LEARN PHASE:
  Step 1:       [Introduce concept]
  Step 2:       [Show contrast]
  Step 3:       [Guided practice]

PRACTICE:
  Round 1:      [Items/content]
  Round 2:      [Items/content]
  Round 3:      [Items/content]

SAMPLE ITEMS:   [From CSV — real words / nonsense?]

SUCCESS CRITERIA:
  - Player can [specific skill] independently after Practice
  - Average completion time: ~[X] minutes
  - Hint escalation used in < 50% of rounds (after 3+ plays)
```

### Invoke during build: `/game-storyboard`, `/ui-ux`, `/mda`, `/octalysis`

---

## Stage 4 — Deliver (Polish & Ship)

**Goal:** Finalize, validate, and release.

**Checklist:**
- [ ] All games pass curriculum alignment review (tutor sign-off)
- [ ] Accessibility audit (contrast, touch targets, audio support, dyslexia-friendly fonts)
- [ ] Full session playtest (overworld → 3+ games in sequence → return to garden)
- [ ] Device testing (mobile Safari, Chrome, tablet)
- [ ] Analytics instrumented (completion rate, error patterns, retry rate, time on task)
- [ ] Onboarding flow designed (first-time kid experience, first-time tutor experience)
- [ ] Retrospective written

---

## Decision Log

Record every significant design decision. Store in `decisions.md` in project root.

### Template

```
## DEC-[NNN]: [Short title]

**Date:** YYYY-MM-DD
**Stage:** [Vision / Discover / Define / Develop / Deliver]
**Domain:** [Overworld / Mini-game-N / Brand / Curriculum / Tech]

**Question:** [What were we deciding?]

**Options considered:**
- (A) [Option] — [Pros] / [Cons]
- (B) [Option] — [Pros] / [Cons]
- (C) [Option] — [Pros] / [Cons]

**Decision:** [Which option, stated clearly]

**Rationale:** [Why — including evidence, playtest data, or principle cited]

**Status:** Active / Revisit by [date] / Superseded by DEC-[NNN]
```

### Decisions already made (to retroactively log):
- Garden overworld as hub between mini-games
- Plants pause but never die (encouragement architecture)
- 5-screen storyboard structure (Landing → Learn → Transition → Practice → Win)
- 3-tier hint escalation replacing lives/hearts
- Process feedback on every answer (not just outcome)
- Cozy pixel farm aesthetic (Stardew Valley / PvZ style)
- Press Start 2P for UI font
- Seeds + Sunshine as dual currency
- One skill per game, no exceptions

---

## Branding & Visual Identity

### Current Status: Established (iterate as needed)

| Element | Status | Details |
|---|---|---|
| Brand personality | Defined | Encouraging, whimsical, patient, cozy |
| Tone of voice | Defined | Warm, never condescending, celebrates effort |
| Color palette | In use | Earthy greens, warm browns, sky blue, golden sunlight, flower pops |
| Typography | In use | Press Start 2P (UI), potential body font TBD |
| Illustration style | In use | PvZ-style illustrated, smooth curves, rich shading |
| Sound design | Partial | Ascending chime (correct), soft descending (wrong), speech via Web Speech API |
| Character design | Partial | Pixel gardener in overworld; no mascot character yet |

### Open branding work:
- [ ] Explore a mascot / guide character (NPC shop keeper personality)
- [ ] Audit font readability for dyslexic users (Press Start 2P is chunky but may need a sans-serif body alternative)
- [ ] Sound design brief: ambient garden music, plant growth sounds, daily check-in jingle

---

## Playtesting

### Report Template

```
## Playtest: [Game name] — [Stage: Paper / Lo-fi / Hi-fi / Polished]

**Date:**
**Participants:** [Count, ages, relevant context]
**Facilitator:**
**Device/Environment:**

### Hypothesis
[What we expected to learn]

### Setup
[Instructions given, any priming]

### Observations
- [Timestamped or sequenced notes]
- [Direct quotes]
- [Moments of confusion, delight, frustration]

### Metrics (if hi-fi+)
- Completion rate:
- Avg attempts to succeed:
- Time on task:
- Error patterns:

### Findings
1. [Finding + evidence]
2. [Finding + evidence]

### Changes to make
- [ ] [Change, priority: P1/P2/P3]

### Open questions
- [What we still don't know]
```

### Playtest cadence
- **Paper prototype:** 1-2 kids, 15 min each, before any code
- **Lo-fi build:** 3-5 kids moderated, after core loop works
- **Hi-fi build:** 3-5 kids unmoderated, with pre/post skill check
- **Polished:** Tutor-led full session in realistic conditions

---

## Game Backlog Tracker

Maintain in `backlog.md` or a spreadsheet. Current state:

| # | Game | Skill Domain | CSV | Status | Playtest | Priority |
|---|------|-------------|-----|--------|----------|----------|
| 01 | Rune Stones | PA — Phoneme Sequence | 19 | Done (legacy) | 0 | — |
| 02 | Enchanted Harp | PA — Phoneme Sequence | 19 | Done (legacy) | 0 | — |
| 03 | Whispering Stones | PA — Rhyme Detection | 18 | Done | 0 | — |
| 04 | Block Breaker | Letter Knowledge — Tap | 9 | Done | 0 | — |
| 05 | Seed Script | Letter Knowledge — Trace | 10 | Done | 0 | — |
| 06 | Syllable Sprout | PA — Syllable Count | 20 | Done | 0 | — |
| 07 | TBD | Print Concepts — Tap | 2–6 | Backlog | — | P1 |
| 08 | TBD | Alphabetic Principle | 29–31 | Backlog | — | P1 |
| 09 | TBD | PA — Phoneme Count | 21 | Backlog | — | P2 |
| 10 | TBD | PA — Syllable Blending | 22 | Backlog | — | P2 |
| 11 | TBD | PA — Phoneme Blending | 23 | Backlog | — | P2 |
| 12 | TBD | Decoding — Letter by Letter | 38-42 | Backlog | — | P2 |
| 13 | TBD | Encoding — Letter by Letter | 47-50 | Backlog | — | P3 |
| ... | ... | ... | ... | Backlog | — | P3 |

### Prioritization weights
- **Curriculum sequence (40%):** Earlier OG skills are more foundational
- **Mechanic diversity (20%):** Don't build 5 tapping games in a row
- **Reusability (20%):** Games whose engine enables other games
- **Risk/unknowns (20%):** Build novel mechanics early to learn faster

---

## Success Metrics

### Per game
| Metric | Target | How to measure |
|---|---|---|
| Session completion rate | >80% | Player finishes all 3 practice rounds |
| Hint escalation rate | <50% (after 3+ plays) | Fewer hints needed over time |
| Voluntary replay rate | >30% | Player chooses "Play Again" |
| Time to complete | 3-5 minutes | Timer in game |
| Skill transfer | Tutor-verified | Can kid apply skill outside game? |

### Overall product
| Metric | Target | How to measure |
|---|---|---|
| Daily return rate | >40% | Same user returns next day |
| Games per session | 2-3 | Session tracking |
| Garden engagement | >60% interact with garden between games | Overworld time |
| Tutor NPS | >50 | Survey |
| Parent satisfaction | >4/5 | Survey |

---

## When to Use This Skill vs Others

| I need to... | Invoke |
|---|---|
| Plan what to build next | `/product-management` |
| Log a design decision | `/product-management` |
| Plan a playtest | `/product-management` |
| Choose a skill target for a new game | `/curriculum-mapping` |
| Design the game's screen-by-screen flow | `/game-storyboard` |
| Check if the game teaches effectively | `/game-based-learning` |
| Check if the game feels right | `/mda` |
| Check if the game motivates return | `/octalysis` |
| Audit the UI/accessibility | `/ui-ux` |
| Check if it fits the product vision | `/game-vision` |
