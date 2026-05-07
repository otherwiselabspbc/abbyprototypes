---
name: mda
description: Evaluate a game's effectiveness using the MDA Framework (Mechanics, Dynamics, Aesthetics). Use when auditing whether a mini-game achieves its design goals — does the mechanic produce the right behavior, and does that behavior create the right feeling? Source — Hunicke, LeBlanc, Zubek (GDC 2001–2004).
---

When this skill is invoked, evaluate $ARGUMENTS using the MDA framework. If no argument is given, evaluate the most recently discussed game or feature.

---

## What is MDA?

MDA decomposes games into three layers that are **causally linked**:

```
DESIGNER'S VIEW (builds left → right):
  Mechanics  →  Dynamics  →  Aesthetics

PLAYER'S VIEW (experiences right → left):
  Aesthetics  →  Dynamics  →  Mechanics
```

| Layer | What it is | Example |
|---|---|---|
| **Mechanics** | The rules, components, data, and algorithms — what the designer builds | "4 stones each speak a word when tapped. Player taps the odd one out." |
| **Dynamics** | The run-time behavior that emerges when the player interacts with the mechanics | "Player listens to all 4, compares endings, forms a hypothesis, tests it" |
| **Aesthetics** | The emotional experience the player has as a result | "Curiosity while listening, pride when correct, gentle surprise when wrong" |

**The key insight:** Designers build mechanics, but players experience aesthetics. Changes in mechanics cascade through dynamics into aesthetics. A small rule change can completely alter how the game *feels*.

---

## The 8 Aesthetic Categories

These replace vague words like "fun" with specific emotional targets:

| Aesthetic | What it feels like | Example |
|---|---|---|
| **Sensation** | Game as sense-pleasure | Rich visuals, satisfying sounds, tactile feedback |
| **Fantasy** | Game as make-believe | "I'm a gardener growing magical plants" |
| **Narrative** | Game as drama / unfolding story | Plant growth arc: seed → sprout → bloom → harvest |
| **Challenge** | Game as obstacle course | Tracing a letter correctly, finding the odd rhyme |
| **Fellowship** | Game as social connection | NPC shop keeper warmth, visiting friends' gardens (Phase 2+) |
| **Discovery** | Game as uncharted territory | New plants, mystery seeds, exploring the garden |
| **Expression** | Game as self-discovery / creativity | Decorating your garden, choosing what to grow |
| **Submission** | Game as pastime / comfort zone | Cozy daily garden tending, ambient atmosphere |

**Every game should name its target aesthetics.** Different games prioritize different ones. Knowing which aesthetics you're designing for prevents feature creep and misaligned mechanics.

---

## How to Evaluate a Game with MDA

### Step 1: Name the Target Aesthetics

What should the player FEEL? List 3–4 primary aesthetics in priority order.

**Example for OL garden games:**
1. **Challenge** — "I figured it out!" (the literacy skill)
2. **Fantasy** — "I'm growing a magical garden" (the narrative frame)
3. **Discovery** — "What will this plant look like?" (curiosity drives return)
4. **Expression** — "This is MY garden" (ownership, customization)

### Step 2: Identify the Dynamics That Produce Those Aesthetics

For each target aesthetic, what run-time behaviors create it?

| Target Aesthetic | Required Dynamics |
|---|---|
| Challenge | Barely-manageable difficulty, clear win condition, process feedback on failure, escalating hints |
| Fantasy | Garden grows visibly as a result of learning, plants respond to player actions, world feels alive |
| Discovery | New plant species as rewards, mystery seeds, ambient surprises (butterflies, weather) |
| Expression | Shop choices, garden layout, which skills to practice in what order |

### Step 3: Trace Dynamics Back to Mechanics

For each dynamic, what mechanics produce it?

| Dynamic | Supporting Mechanics |
|---|---|
| Barely-manageable difficulty | 3-tier hint escalation, no lives/punishment, forgiving input tolerance |
| Visible garden growth | 5 growth stages per plant, sprout animation on correct answer, persistent golden plants |
| New species as rewards | 6 plant types mapped to skill domains, each unlocked by starting a new domain |
| Shop choices | Seeds + Sunshine currency, purchasable items, cosmetic upgrades |

### Step 4: Check for Cascading Problems

**Work backwards from any negative player experience:**

If the player feels **bored** (missing Challenge):
- Check dynamics: Is difficulty too low? Are there no meaningful choices?
- Check mechanics: Are rounds identical? Is hint escalation too aggressive?

If the player feels **frustrated** (Challenge gone wrong):
- Check dynamics: Is feedback clear? Can the player understand WHY they failed?
- Check mechanics: Is the input tolerance too tight? Is the speech cutting off?

If the player feels **disconnected** (missing Fantasy):
- Check dynamics: Does completing a round produce visible garden growth?
- Check mechanics: Is the sprout animation firing? Does the win screen reference the garden?

If the player feels **anxious** (unwanted negative aesthetic):
- Check dynamics: Is there time pressure? Loss framing? Social comparison?
- Check mechanics: Remove timers, death mechanics, leaderboards.

---

## MDA Audit Template

When evaluating a game, fill in this table:

```
GAME: [name]
SKILL: [literacy target]

TARGET AESTHETICS (ranked):
1. _______________
2. _______________
3. _______________
4. _______________

MECHANICS → DYNAMICS → AESTHETICS CHAIN:

Mechanic: _______________
  → Produces dynamic: _______________
    → Creates aesthetic: _______________
    → Is this the INTENDED aesthetic? YES / NO
    → If NO, what's wrong?

[Repeat for each core mechanic]

UNINTENDED AESTHETICS:
- Is the player feeling anything we DIDN'T design for?
- Are any mechanics producing dynamics that undermine our target aesthetics?

MISSING AESTHETICS:
- Which target aesthetics are under-served?
- What mechanics/dynamics could we add to strengthen them?
```

---

## MDA Applied to OL Prototypes

### The Garden Overworld

| Layer | Implementation |
|---|---|
| **Mechanics** | Tile map, player movement, 6 plots, currency (Seeds/Sunshine), shop, growth stages, game links |
| **Dynamics** | Player walks to a plot → sees growth status → chooses to play → earns currency → buys upgrades → returns daily to tend |
| **Aesthetics** | Fantasy (I'm a gardener), Expression (my garden is unique), Discovery (what grows next?), Submission (cozy daily ritual) |

### A Mini-Game (e.g., Seed Script)

| Layer | Implementation |
|---|---|
| **Mechanics** | Letter path data, trace input detection, tolerance radius, stroke tracking, sprout animation, hint escalation, speech API |
| **Dynamics** | Player sees dotted letter → traces with finger → trail persists → sprout grows as progress increases → correct trace triggers celebration → wrong lift triggers gentle hint |
| **Aesthetics** | Challenge (trace accurately), Sensation (satisfying green trail, sprout animation, chime), Fantasy (tracing plants a seed), Discovery (what letter comes next?) |

---

## Common MDA Pitfalls

### 1. "Feature-driven" instead of "experience-driven" design
Adding mechanics because they sound cool, without tracing them to a target aesthetic. Ask: "What will the player FEEL because of this feature?" If you can't answer, don't build it.

### 2. Aesthetic mismatch
The designer targets Challenge but the mechanics produce Frustration (too hard) or Boredom (too easy). Always test whether the dynamic actually creates the intended aesthetic, not just a nearby one.

### 3. Ignoring the player's perspective
Designers see Mechanics → Dynamics → Aesthetics. Players see Aesthetics first. If the game doesn't FEEL right in the first 10 seconds, the player won't stay long enough to appreciate the mechanics.

### 4. Mechanics evaluated in isolation
"Is this a good tracing algorithm?" is the wrong question. "Does this tracing algorithm produce dynamics that create the feeling of challenge + satisfaction?" is the right one. No mechanic has value outside its effect on the player experience.

### 5. Tuning without aesthetic targets
Adjusting numbers (tolerance radius, hint timing, currency rates) without knowing which aesthetic you're optimizing for leads to aimless iteration. Name the target first, then tune toward it.

---

## When to Use MDA vs Other Skills

| Question | Use this skill |
|---|---|
| "Does this game produce the right *feelings*?" | `/mda` |
| "Does this game follow evidence-based learning principles?" | `/game-based-learning` |
| "Does this game activate all 8 motivation drives?" | `/octalysis` |
| "Does this game target the right literacy skill?" | `/curriculum-mapping` |
| "Does this game follow the correct screen-by-screen structure?" | `/game-storyboard` |
| "Is the UI accessible and well-designed?" | `/ui-ux` |

MDA is the **"does it feel right?"** skill. The others handle **"is it correct?"** Use MDA after the game is structurally sound to verify the experience matches the intent.
