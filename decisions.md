# Design Decision Log

## DEC-001: Garden overworld as hub

**Date:** 2026-04-15
**Stage:** Define
**Domain:** Overworld

**Question:** How should mini-games be connected?

**Options considered:**
- (A) Linear playlist — games play in sequence like levels
- (B) Menu screen — grid of game icons to tap
- (C) Garden overworld — walk around a persistent world, approach plots to launch games

**Decision:** (C) Garden overworld

**Rationale:** The overworld provides intrinsic narrative (CD1), ownership (CD4), and discovery (CD7) per the Octalysis framework. A menu screen would feel like a worksheet. The garden creates emotional attachment and a reason to return (Tamagotchi effect). Growth-as-metaphor ties the learning directly to something visible and alive.

**Status:** Active

---

## DEC-002: Plants pause but never die

**Date:** 2026-04-15
**Stage:** Define
**Domain:** Overworld

**Question:** What happens to the garden when the player doesn't return?

**Options considered:**
- (A) Plants die — loss aversion drives return
- (B) Plants pause — droop slightly, perk up when player returns
- (C) Nothing changes — no daily return incentive

**Decision:** (B) Plants pause

**Rationale:** Dyslexic learners have experienced significant failure already (UI/UX encouragement architecture principle). A dying garden punishes absence. The Octalysis skill recommends CD8 (Loss & Avoidance) capped at 2/10 for this audience. Gentle wilting creates incentive without punishment.

**Status:** Active

---

## DEC-003: Learn & Practice two-phase game structure

**Date:** 2026-04-15
**Stage:** Define
**Domain:** Mini-games

**Question:** Should games jump straight into gameplay or teach the skill first?

**Options considered:**
- (A) Gameplay only — learn by doing (old structure: 3 rounds with fading scaffolds)
- (B) Learn then Practice — explicit pretraining phase, then independent practice
- (C) Interleaved — alternate teaching and testing

**Decision:** (B) Learn then Practice

**Rationale:** GBL pretraining principle (d=0.8 effect size). The Learn phase teaches the literacy skill itself (not just the game mechanic) per OG methodology. Zero stakes in Learn builds understanding. Practice proves the skill independently. The storyboard skill codifies this as: Landing → Learn (3 steps) → Transition → Practice (3 rounds) → Win.

**Status:** Active

---

## DEC-004: 3-tier hint escalation replaces lives

**Date:** 2026-04-15
**Stage:** Define
**Domain:** Mini-games

**Question:** How should wrong answers be handled?

**Options considered:**
- (A) Lives/hearts — lose a life per wrong answer, reset round at 0
- (B) Hint escalation — wrong answers produce increasingly specific help, never reset
- (C) Unlimited retries with no feedback change

**Decision:** (B) 3-tier hint escalation: nudge → directive → bottom-out

**Rationale:** GBL research: process feedback (explaining WHY) has d=1.31 effect size vs outcome-only. Lives create anxiety (UI/UX: never punish). The Octalysis skill says CD8 must stay at 2/10. Escalating hints means the game only increases support, never decreases access. Bottom-out reveals the answer with full explanation and advances — the player always progresses.

**Status:** Active

---

## DEC-005: Cozy pixel-to-illustrated aesthetic (Stardew Valley / PvZ)

**Date:** 2026-04-15
**Stage:** Define
**Domain:** Brand

**Question:** What visual style for the game?

**Options considered:**
- (A) Dark fantasy RPG (original direction — emerald tones, mysterious stones)
- (B) Bright pixel RPG (Mario-style blocks, pixel font)
- (C) Cozy illustrated farm (Stardew Valley / PvZ — smooth, detailed, warm)

**Decision:** (C) Cozy illustrated farm, evolving from (B)

**Rationale:** User directed the shift from dark fantasy → bright pixel → illustrated cozy. PvZ-level detail with smooth curves and rich shading. Stardew Valley's farm loop matches our garden mechanic. GBL emotional design: warm, bright, saturated colors trigger positive emotions. The aesthetic should feel inviting, not stressful.

**Status:** Active

---

## DEC-006: Seeds + Sunshine dual currency

**Date:** 2026-04-15
**Stage:** Define
**Domain:** Overworld

**Question:** How should player progress translate to garden upgrades?

**Options considered:**
- (A) Single currency (coins or stars)
- (B) Dual currency — Seeds (from Learn) + Sunshine (from Practice)
- (C) No currency — growth is automatic based on completion

**Decision:** (B) Dual currency

**Rationale:** Dual currencies create meaningful choices (CD3: Empowerment of Creativity). Seeds reward understanding, Sunshine rewards mastery. Spent in the shop on cosmetic upgrades (fences, tools, decorations) — never pay-to-win. The economy IS the curriculum — currency is earned through learning, never purchased.

**Status:** Active

---

## DEC-007: One literacy skill per game

**Date:** 2026-04-13
**Stage:** Define
**Domain:** Curriculum

**Question:** Can a game target multiple skills?

**Decision:** One skill per game, no exceptions.

**Rationale:** Curriculum-mapping skill rule. Mixing skills confuses the assessment signal — you can't know if the child struggled with rhyme detection or syllable counting if both are in one game. Each game = one CSV row = one clear skill target.

**Status:** Active
