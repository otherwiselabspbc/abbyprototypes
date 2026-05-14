---
name: explicit-instruction
description: Defines how instruction within each mini-game should be structured. Based on evidence-based reading curriculum principles (OG, Lindamood-Bell, Wilson Reading). Covers the 80/20 instruction-to-practice ratio, the 3-stage learning structure, systematic concept linking, and how to translate explicit instruction into game format. Source — Tyler Ogata meeting notes (2026-05-07).
---

When this skill is invoked, use it to evaluate or design the instructional structure of $ARGUMENTS. If no argument is given, audit the most recent game or design discussion.

---

## Core Principle: Explicit and Systematic

Evidence-based reading instruction requires two things:

1. **Explicit** — The game directly tells the student what needs to be learned. Students do not infer, discover, or extract the rule on their own. The concept is stated clearly before any practice begins.
2. **Systematic** — Concepts are taught in a specific order. Each concept builds on the previous one. You cannot teach a complex rule before teaching its prerequisites.

**This is non-negotiable.** Every mini-game must include explicit instruction of the skill it targets, not just practice of that skill.

---

## The 80/20 Ratio

A well-structured lesson is approximately:

| Component | Proportion | In-game equivalent |
|---|---|---|
| **Explicit instruction** | 80% | Tutorial phase, concept introduction, supervised learning, feedback loops, re-teaching after errors |
| **Practice** | 20% | The actual mini-game sprint (independent play) |

**What this means for game design:** The mini-game itself (the timed sprint, the challenge) is only 20% of the experience. The other 80% is the game teaching the concept, showing examples, providing guided practice with feedback, and re-teaching when the student gets it wrong.

The 80% does NOT have to feel like a lecture. It can be:
- An NPC explaining a rule in-character
- A visual demonstration with animation
- A guided round where the game walks the student through the answer
- Process feedback after a wrong answer that re-teaches the concept

**The practice (20%) is where the student proves they've learned.** It's the independent sprint — timer running, no scaffolding, real challenge.

---

## The 3-Stage Learning Structure

Every mini-game session follows three stages:

### Stage 1: Tutorial (Explicit Instruction)

**What happens:** The concept is directly introduced alongside the game mechanic. The student learns both WHAT the skill is and HOW to demonstrate it in the game.

**Rules:**
- Directly state the rule or concept. "When the letter I is followed by LD, it says its name — like in WILD."
- Show, don't just tell. Visual and auditory examples alongside the stated rule.
- The game mechanic is taught simultaneously — "You'll hear a word. Drag the letters to build it."
- The student should understand the learning objective. They should know WHAT they're practicing and WHY.

**Key insight from meeting:** Explicit instruction should involve BOTH teaching how to play the game AND teaching the underlying concept. Not one or the other — both at once.

### Stage 2: Supervised Learning

**What happens:** The student attempts the task, but cannot progress until they demonstrate understanding. The game actively monitors and intervenes.

**Rules:**
- If the student gets it right → proceed to Stage 3
- If the student gets it wrong → the game provides process feedback (explains WHY it's wrong), then either:
  - Returns to more explicit instruction (re-teaches the concept)
  - Provides a guided attempt (walks through the answer step by step)
- The student cannot skip this stage. They must demonstrate understanding before independent practice.

**This is where hint escalation lives:** Nudge → Directive → Bottom-out (reveal answer with explanation). Each escalation level is a form of returning to explicit instruction.

### Stage 3: Independent Practice (The Sprint)

**What happens:** The student practices the skill independently. Timer running, no scaffolding, real challenge. This is the mini-game sprint.

**Rules:**
- Minimal support — the student has already been taught
- Speed and accuracy matter (timer, urgency)
- Feedback is still provided on errors, but lighter than Stage 2
- Success = the student has demonstrated the skill

---

## Systematic Concept Linking

Concepts must be taught in order. Each concept depends on prerequisites.

**Example from meeting:**
> You can't teach "when I is followed by LD, it says its name" (as in WILD) unless the student already knows:
> 1. What a long vowel is
> 2. What the letter I sounds like normally
> 3. What it means for a vowel to "say its name"

**Rule:** Before introducing a complex rule in a game, verify that all prerequisite concepts have been taught in earlier games or in this game's tutorial phase. If not, teach the prerequisites first.

**How to apply:**
- Check the curriculum sequence (use `/curriculum-mapping`)
- Each game's tutorial phase must establish or confirm prerequisites
- Never assume the student knows something — either teach it or reference where they learned it ("Remember how we learned that vowels have two sounds?")

---

## Translating Explicit Instruction into Game Format

### What explicit instruction looks like in a classroom:
1. Teacher states the rule directly
2. Teacher shows examples
3. Teacher does guided practice with students
4. Students practice independently
5. Teacher provides feedback on errors and re-teaches as needed

### What explicit instruction looks like in a mini-game:
1. **NPC or oracle states the concept** — spoken aloud, with visual support
2. **Animated demonstration** — the game shows the concept in action (auto-play a round)
3. **Guided round** — the student tries, but with heavy scaffolding (highlights, spoken hints)
4. **Independent sprint** — the timed challenge (this is the "game" part)
5. **Process feedback on errors** — wrong answers explain WHY and re-teach the concept

### Contextualization (from Robert Borges)

Learning is more motivating when it's contextualized:
- **Good:** "You need to decode this word to unlock the passage" (the skill serves the quest)
- **Bad:** "Practice reading this word" (the skill is the point, no context)

The explicit instruction should frame WHY the student needs this skill — within the game's narrative. The vocabulary word helps solve the quest. The decoded spell opens the door. The phoneme identifies the right gem.

---

## Concealing Failure

**From the meeting:** Students should not realize they are failing.

**How to implement:**
- No "WRONG" screens, red X marks, or failure counts
- Wrong answers trigger re-teaching, not punishment: "That's K — listen again" (names what they tapped, replays the target)
- Hint escalation naturally guides toward the answer — the student always succeeds eventually
- The bottom-out (revealing the answer) is framed as learning, not failure: "The answer is SHRINE. It ends with a silent E."
- Timer expiration is framed as the spell fading or the quest pausing — not the student failing

**The student should feel:** "I'm learning this" — not "I got it wrong."

---

## Student Awareness of Learning

**From the meeting:** Students are motivated when they feel they are learning. Don't hide the fact that this is educational.

This seems contradictory to "conceal failure," but it's not:
- **Show the student they are GROWING** — "You decoded that word!" "You matched the sound!"
- **Hide when they are STRUGGLING** — errors feel like part of the process, not setbacks
- **Appropriate difficulty is key** — if the challenge matches their level, getting it right feels earned and motivating

**The student should feel:** "I just learned something real" — pride and competence, not shame.

---

## Session Structure (Multiple Games)

A longer play session should follow this pattern:

```
Quick Drill (review) → Teach Concept (explicit) → Practice (game) → Teach New Concept → Practice → ...
```

Each mini-game fits into a broader unit. Within a session:
1. **Review drill** — a quick sprint on previously mastered skills (retention)
2. **New concept introduction** — explicit instruction on the new skill
3. **Supervised practice** — guided attempts at the new skill
4. **Independent practice** — the timed sprint
5. **Return to explicit instruction** — feedback on errors, reinforce what was learned
6. **Next concept** — repeat the cycle

**One lesson plan may correspond to multiple mini-games** — each covering a different activity within the lesson.

---

## WRS Lesson Plan Structure (Reference)

The Wilson Reading System lesson plan is a 10-step sequence that shows how a full structured literacy session is organized. Each step maps to potential mini-game types.

### Steps 1-5: Reading (Sound → Word → Sentence)

| Step | Name | What it does | Mini-game mapping |
|---|---|---|---|
| **1** | Sounds Quick Drill | Quick automatic letter-sound recognition | **Enchanted Gems** — hear sound, identify letter. Fast drill, timed. |
| **2** | Teach & Review Concepts for Reading | Teach word structure, segment and decode words with target patterns | Explicit instruction phase — NPC teaches the rule, then guided practice |
| **3** | Word Cards | Whole-word recognition, vocabulary, high-frequency word automaticity | Flash-style word recognition game — see word, hear it, build automaticity |
| **4** | Wordlist Reading | Independent single-word decoding, progress tracking | **Spell Caster** — hear word, build it from letters. Independent sprint. |
| **5** | Sentence Reading | Decode in context, reinforce vocabulary and comprehension | **Quest Catcher** — vocabulary in sentence context |

### Steps 6-8: Spelling (Reverse Direction)

| Step | Name | What it does | Mini-game mapping |
|---|---|---|---|
| **6** | Quick Drill in Reverse | Hear sound → write/identify letter (opposite of Step 1) | Sound-to-letter matching game (encoding direction) |
| **7** | Teach & Review Concepts for Spelling | Break words into parts, count elements | Explicit instruction on spelling patterns |
| **8** | Written Work Dictation | Independent spelling and proofreading | Encoding game — hear word, spell it letter by letter |

### Steps 9-10: Fluency & Comprehension

| Step | Name | What it does | Mini-game mapping |
|---|---|---|---|
| **9** | Controlled Text Passage Reading | Fluency, silent reading, comprehension with visualization | Passage reading with comprehension questions (future) |
| **10** | Listening/Reading Fluency & Comprehension | Age-appropriate literature, retell, background knowledge | Story comprehension with narrative (future) |

### Key structural insight:

The lesson flows from **smallest unit to largest:**
```
Sound → Letter → Word → Sentence → Passage → Story
```

And then reverses for encoding:
```
Sound → Letter → Word (spelling direction)
```

**Each mini-game should know where it sits in this sequence.** A sounds drill game (Step 1) is different from a word-building game (Step 4) which is different from a comprehension game (Step 9). The explicit instruction for each must match the level of complexity.

**The 10 steps also show the rhythm of a session:** quick drill → teach → practice → teach → practice → extended reading. Mini-games can be sequenced to follow this same rhythm within a play session.

---

## Checklist — Apply to Every Game

- [ ] The game explicitly states the concept being practiced (not just the mechanic)
- [ ] The concept is stated BEFORE any practice begins
- [ ] Prerequisites are taught or confirmed before introducing the concept
- [ ] The tutorial teaches BOTH the skill AND the game mechanic simultaneously
- [ ] There is a supervised learning phase where the student must demonstrate understanding
- [ ] Wrong answers return to explicit instruction (re-teaching), not just "try again"
- [ ] The student cannot skip to independent practice without passing supervised learning
- [ ] Failure is concealed — errors feel like learning, not setbacks
- [ ] The student knows WHAT they are learning and WHY (within the narrative context)
- [ ] The independent practice sprint is ~20% of the total experience
- [ ] Process feedback on every error explains WHY and re-teaches

---

## When to Use This Skill

| Situation | Invoke |
|---|---|
| Designing the tutorial/intro for a new game | `/explicit-instruction` |
| Deciding how much scaffolding to include | `/explicit-instruction` |
| Designing error feedback | `/explicit-instruction` |
| Structuring a multi-game session | `/explicit-instruction` |
| Evaluating if a game is "just practice" without teaching | `/explicit-instruction` |

Use alongside `/game-storyboard` (screen structure) and `/game-based-learning` (learning science) when building any new game.
