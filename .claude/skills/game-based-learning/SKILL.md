---
name: game-based-learning
description: Review or apply evidence-based game-based learning principles when designing, auditing, or iterating on any mini-game. Covers cognitive load, feedback, motivation, emotional design, narrative, adaptivity, and common pitfalls. Source — Handbook of Game-Based Learning (Plass, Mayer, Homer, 2019).
---

When this skill is invoked, audit or guide the design of a mini-game against the principles below. If $ARGUMENTS names a specific game file, review that file. Otherwise review the currently open game file or the most recent design discussion.

---

## What Makes a Game Educational (not just fun)

Game-based learning means the **gameplay IS the learning** — mechanics are designed from the ground up so that exercising the target skill is the core player action. This is NOT gamification (bolting points/badges onto drills) or "chocolate-covered broccoli" (a tedious task with a game wrapper).

**The fundamental tension:** Too much focus on learning objectives kills playfulness and choice. Too much focus on gameplay lets fun distract from content. Every design decision must balance both.

---

## 1. Cognitive Load — The Balancing Act

Three types of processing the player's brain is doing at all times:

| Type | What it is | Design goal |
|---|---|---|
| **Extraneous** | Effort wasted on irrelevant detail (decorative art, confusing UI, unclear rules) | MINIMIZE |
| **Essential** | Effort to represent the material in working memory | MANAGE |
| **Generative** | Deep sense-making — organizing, integrating with prior knowledge | MAXIMIZE |

### Rules
- For every visual/audio/narrative element, ask: "Does this serve the learning goal or add extraneous load?"
- **Signaling principle:** Visually distinguish interactive elements from decorative ones (glow, highlight, motion). Reduces extraneous load.
- **Spatial contiguity:** Place related text and visuals near each other. Don't make the player hunt for corresponding info.
- **Modality principle:** Spoken narration > on-screen text for instructions (d=1.4 effect size). Frees the visual channel for gameplay.
- **Redundancy penalty:** Do NOT show spoken + printed text simultaneously (d=-0.23). Pick one modality.
- **Pretraining principle:** Introduce key concepts briefly before gameplay begins (d=0.8). This is the "Learn" phase.

---

## 2. Feedback — Explain, Don't Just Score

| What works | What doesn't |
|---|---|
| Process feedback ("That word ends with -og, not -at — different ending sounds") | Outcome-only feedback (just a chime or "Wrong!") |
| Detailed feedback early, fading to general as mastery grows | Uniform feedback at all skill levels |
| Immediate feedback during skill acquisition | Delayed feedback when goal is error-prevention |
| Explanatory feedback paired with a correctness signal | Points/tones alone |

### Rules
- Every wrong answer must explain WHY it's wrong, not just that it is.
- Every correct answer should reinforce the principle, not just celebrate.
- Use a **3-tier hint escalation**: conceptual nudge → specific directive → bottom-out (give the answer).
- Plot-contingent feedback (story advances on success) lets you give feedback without emphasizing failure.

---

## 3. Motivation — Self-Determination Theory

Three psychological needs that drive intrinsic motivation:

| Need | What it means | How to satisfy it |
|---|---|---|
| **Competence** | "I can do this" | Barely-manageable challenges, clear proximal goals, rich immediate feedback, real capability unlocks (not cosmetic) |
| **Autonomy** | "I chose to do this" | Meaningful choices (avatar, strategy, difficulty), exploration, player impact on the world |
| **Relatedness** | "I belong here" | Cooperative tasks, NPC warmth, characters the learner identifies with |

### Critical warnings
- **External rewards (points, badges, leaderboards) frequently UNDERMINE intrinsic motivation.** They reduce autonomy. Use sparingly and never as the primary motivator.
- **The "Toll" problem:** If learning content feels like a tax the player pays to reach the fun, the design has failed. Learning must be the player's ALLY in achieving need satisfaction — not an obstacle between the player and the game.
- **Players are brutally efficient.** They skip anything not in the satisfaction loop. If learning material isn't directly tied to need satisfaction, game content becomes a COMPETITOR for attention.

---

## 4. Emotional Design — Feelings Drive Learning

Cognition and emotion are causally linked. Positive activating emotions (enjoyment, curiosity, pride) enhance attention, flexible thinking, and memory. Boredom and hopelessness destroy all strategic effort.

### What triggers positive emotions
- **Warm, bright, saturated colors** (not dark/muted). Yellow, green, coral, sky blue.
- **Round shapes and face-like characters** (baby-face bias). Expressive faces > neutral.
- **Natural-feeling environments** (higher positive affect, lower stress than urban).
- **Appropriate challenge** — too easy OR too hard both produce boredom.
- **Scaffolding increases enjoyment** (via increased perceived control) — but over-scaffolding kills autonomy.

### What triggers negative emotions
- Misaligned mechanics (game actions don't match learning goals → frustration)
- Unclear UI or rules (→ technology frustration)
- Evaluative/pressuring language ("You need to..." → anxiety). Use polite, face-saving phrasing ("How about we...")
- Social comparison / competitive structures (→ shame for weaker players)

### Confusion can be productive
But ONLY when: (a) the learner has the capability to resolve it, and (b) the game provides scaffolds. Unresolved confusion degrades into frustration or boredom.

---

## 5. Sound & Music

- Sound feedback increases perceived pleasantness and engagement.
- **Tempo drives arousal** (faster = more energized). **Mode drives mood** (major key = positive).
- Human voice > synthetic voice for pedagogical agents / narration.
- Sound can **downplay failure** (soft tone) and **celebrate success** (ascending chime).
- Audio explanations paired with visual diagrams improve retention (modality principle).

---

## 6. Narrative — Story Must BE the Problem

| Effective | Ineffective |
|---|---|
| **Intrinsic narrative** — story is inseparable from gameplay and learning | **Extrinsic narrative** — story is wallpaper that doesn't affect gameplay |
| The reading skill IS the quest / conflict | Literacy drills bolted onto an unrelated theme |
| Learner cast as protagonist with agency | Learner is passive viewer of cutscenes |
| Thin, accessible, entertaining narratives | Thick, complex narratives that overwhelm processing |
| Narrative dispersed in environment (characters, objects, data) | All story in cutscenes |

### Rules
- Embed the learning problem as the central narrative conflict.
- Small quests within an overarching narrative is a proven structural pattern (aligns with OL's mini-game approach).
- **Beware "seductive details."** Every narrative element not tied to the learning objective is a potential distractor.

---

## 7. Scaffolding & Adaptivity

### Scaffolding rules
- Start with maximum support, then **fade as mastery is demonstrated**. Scaffolds must be temporary.
- Adaptive scaffolding that intervenes only when necessary is most effective.
- **Partial agency > full agency.** Constrained paths with meaningful choices outperform both railroad and sandbox.

### Adaptivity loop
1. **Diagnose** — measure learner performance (knowledge, emotional state, cognitive load)
2. **Decide** — determine what should change (difficulty, scaffolding, content)
3. **Respond** — modify the game feature (hints, level generation, feedback detail)

### What to adapt for
- Performance/knowledge (proven)
- Emotional state and motivation (emerging, high opportunity)
- **NOT learning styles** — debunked, no empirical support

### Adaptive difficulty
- If player demonstrates competence → skip remaining practice at that tier, advance
- If player struggles → generate new content targeting the same skill (don't just repeat the same level)

---

## 8. Collaboration vs. Competition

- **Cooperation** generally produces more positive emotions and benefits weaker students.
- **Competition** increases situational interest and in-game performance.
- **Best blend:** Intragroup cooperation + intergroup competition.
- Just changing scoring rules without changing the core mechanic does NOT create real collaboration/competition. The social mode must be embedded in the core action.
- Competition can trigger performance-avoidance goals and negative emotions for losing players. Use with care in a dyslexia context.

---

## Design Checklist — Run Before Shipping Any Game

- [ ] The gameplay IS the learning (not drills with a game wrapper)
- [ ] One specific skill targeted per game
- [ ] Spoken narration for instructions (not on-screen text walls)
- [ ] Conversational, friendly language (first/second person)
- [ ] Brief pre-game orientation to the skill concept (Learn phase)
- [ ] Process feedback on every answer (explains WHY, not just correct/incorrect)
- [ ] Hint escalation: nudge → directive → answer
- [ ] Graceful failure — low consequences, failure as a step, not a punishment
- [ ] Warm/bright colors, round shapes, expressive characters
- [ ] Every visual and audio element serves the learning goal (no seductive details)
- [ ] Interactive elements are visually distinct from decorative ones
- [ ] Scaffolding fades as mastery grows
- [ ] Player has meaningful choices (not micromanaged)
- [ ] Learning content is inside the need-satisfaction loop, not a toll before the fun
- [ ] Sound celebrates success, softens failure
- [ ] Difficulty adapts to performance (not learning styles)
- [ ] Narrative conflict IS the learning problem
