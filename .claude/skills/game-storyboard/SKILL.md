---
name: game-storyboard
description: Use when designing a new mini-game from scratch. Provides the complete screen-by-screen structure every game must follow, including the Learn and Practice phases. Synthesizes curriculum mapping, game-based learning research, and OL design principles into a single storyboarding template.
---

When this skill is invoked, use it to storyboard a new mini-game targeting $ARGUMENTS. If no target is given, walk the user through identifying a target skill first.

Before using this skill, identify the target skill using `/curriculum-mapping`. You need:
- **Target domain** (e.g., Phonological Awareness)
- **Target skill** (e.g., Detection > Rhyme)
- **Input modality** (Visual, Auditory, or Both)
- **Output modality** (Tactile, Speech, or Both)
- **Interaction type** (Tap, Swipe, Trace, Drag, etc.)
- **Sample items** from the CSV

---

## Every Mini-Game Has 5 Screens

```
LANDING → LEARN (3 steps) → TRANSITION → PRACTICE (3 rounds) → WIN
```

---

## Screen 1: Landing

**Purpose:** Set the tone, preview the mechanic, invite the player in.

| Element | Details |
|---|---|
| **Title** | The game's fantasy name (e.g., "The Whispering Stones") |
| **Eyebrow** | The skill domain in small text (e.g., "Phonological Awareness") |
| **Tagline** | 1–2 sentences describing what the player will do, in plain language |
| **Demo** | A looping animation that shows the core mechanic in action — no text explanation, just the game playing itself |
| **Begin button** | Single primary CTA |
| **Skill tag** | Small footer: skill name + age range |

### Rules
- The demo teaches the mechanic through observation, not reading (UI/UX: onboarding through play, not text walls)
- No instructions — the demo IS the instruction
- The demo must use the same visual language as the actual game (same stones, strings, items)

---

## Screen 2: Learn (3 Steps)

**Purpose:** Teach the literacy skill itself — not the game mechanic, but the reading concept. This is the pretraining principle (d=0.8 effect size).

The Learn phase is zero-stakes. The player cannot fail. Every interaction builds understanding.

### Step 1 — Introduce the Concept

Show the simplest possible example of the target skill.

| What to show | How |
|---|---|
| The core concept in one sentence | Title text, spoken aloud |
| Two items that demonstrate the concept | Interactive elements (stones, strings, etc.) that auto-play |
| The key pattern highlighted | Visual emphasis on the shared feature (e.g., ending sound highlighted in gold) |
| A caption explaining what just happened | Dialog box with highlighted keywords, spoken aloud |

**Example (Rhyme Detection):**
- Title: "Words that end with the same sound are called rhyming words."
- Two stones auto-speak "cat" and "hat"
- Endings "-at" and "-at" reveal in gold
- Caption: '"Cat" and "hat" both end with **-at**. They rhyme!'

### Step 2 — Show the Contrast

Show what the concept looks like when it DOESN'T apply — the negative example.

| What to show | How |
|---|---|
| The same format as Step 1 | Identical layout and interaction pattern |
| Two items that do NOT match | Auto-play both |
| The difference highlighted | Different endings/sounds shown in contrasting colors |
| A caption explaining the difference | Spoken aloud |

**Example (Rhyme Detection):**
- Title: "Words with different ending sounds do not rhyme."
- Two stones auto-speak "cat" and "dog"
- Endings "-at" and "-og" reveal — one green, one gold
- Caption: '"Cat" ends with **-at**. "Dog" ends with **-og**. Different sounds — no rhyme.'

### Step 3 — Guided Practice

The player exercises the skill with full scaffolding. They can tap and explore, but the answer is gently guided.

| What to show | How |
|---|---|
| 3 items (not 4 — reduced complexity) | Player taps each to hear/see |
| A prompt to identify the target | Spoken aloud + dialog box |
| Wrong answers get gentle redirection | No penalty, just "That one rhymes. Try the one that sounds different." (spoken) |
| Correct answer gets full explanation | Highlights + caption + spoken explanation |

### Learn Phase Rules

- **All text is spoken aloud.** Titles, captions, prompts, nudges — everything. (Modality principle: audio frees the visual channel. Phase 1 literacy: zero reliance on reading.)
- **Captions use highlighted keywords.** Key terms in `<em>` (gold) and key patterns in `<strong>` (gold). This is visual signaling — draws the eye to the important information.
- **Each line of text is a complete clause.** Use `<br>` to control line breaks. Never let the browser wrap mid-phrase. Students must be able to read each line left-to-right as a single thought.
- **Generous spacing.** `word-spacing: 0.15em`, `line-height: 2.4+`, padding around highlighted words.
- **Continue button appears only after speech finishes.** The player cannot skip the explanation.
- **No lives, no scoring, no failure.** The Learn phase exists to build understanding, not test it.

---

## Screen 3: Transition

**Purpose:** Mark the shift from learning to practicing. Set expectations.

| Element | Details |
|---|---|
| **Eyebrow** | "Learn Complete" |
| **Title** | "Ready to Practice?" |
| **Subtitle** | 1 sentence describing what Practice asks the player to do |
| **Begin button** | "Start Practice" |

Keep this screen brief — it's a breath between phases, not a wall of text.

---

## Screen 4: Practice (3 Rounds)

**Purpose:** The player demonstrates the skill independently. No scaffolding, no hints on first attempt. The gameplay IS the learning.

### Round Structure

All 3 rounds use the same mechanic and the same UI. The only difference is the content (different word sets, different items). Difficulty is consistent — the Learn phase already handled progression.

| Element | Details |
|---|---|
| **HUD** | "Practice" label, round dots (1/3, 2/3, 3/3), round number |
| **Instruction** | Brief prompt shown as a centered overlay, spoken aloud, auto-dismisses after ~2.5s |
| **Game area** | The interactive elements (4 stones, strings, tiles, etc.) |
| **No lives or hearts** | Replaced by hint escalation |

### Listening → Answering Flow

1. **Listening phase:** Player must interact with every element before answering (e.g., tap all 4 stones to hear their words). Instruction overlay: "Tap each stone to hear its word."
2. **Answer phase:** Once all elements are heard, the instruction changes: "Now tap the stone that does not rhyme with the others." Player selects their answer.

### Feedback: 3-Tier Hint Escalation

No lives. No round resets. Instead, wrong answers escalate support:

| Tier | Trigger | What happens |
|---|---|---|
| **1 — Nudge** | 1st wrong answer | Process feedback explaining WHY the tapped item was wrong. "Nap ends with -ap, so it rhymes with the others. Try to find the one that sounds different!" Spoken aloud. Player tries again. |
| **2 — Directive** | 2nd wrong answer | Auto-plays the correct answer and a wrong answer back-to-back. "Cap ends with -ap and pan ends with -an. Can you find the one that is different?" Spoken aloud. Player tries again. |
| **3 — Bottom-out** | 3rd wrong answer | Reveals the answer with full explanation. "The answer is pan. It ends with -an, but the others end with -ap." Highlights the correct item. Auto-advances to next round. |

### Feedback: Correct Answer

- Play ascending chime
- Show process feedback: "Pan ends with -an, but the others end with -ap."
- Spoken aloud
- Correct item animates (shatter/disappear), others celebrate
- Auto-advance to next round after ~2s

### Practice Phase Rules

- **All instructions are spoken aloud** and shown as a centered overlay that auto-dismisses
- **Process feedback on EVERY answer** — correct or wrong. Always explain WHY.
- **Hint escalation replaces lives.** The game never punishes. It only increases support.
- **Wrong answer feedback stays visible longer** (4–5s) than prompts (2.5s) — the player needs time to process
- **Sound celebrates success** (ascending arpeggio) **and softens failure** (gentle descending tone, not a buzzer)
- **Items come from the CSV sample items.** Real words only unless the CSV notes column says otherwise.
- **3 rounds minimum.** Each round uses a different word/item set from the CSV.

---

## Screen 5: Win

**Purpose:** Celebrate mastery. Make the player feel powerful.

| Element | Details |
|---|---|
| **Eyebrow** | "Quest Complete" |
| **Title** | "Well Done!" (large, celebratory) |
| **Subtitle** | 1–2 sentences reinforcing what the player learned |
| **Badge** | Skill name + icon. "Skill Unlocked: Rhyme Detection" |
| **Particle burst** | Full-screen celebration (rainbow colors, confetti feel) |
| **Play Again button** | Restarts Practice (not Learn) |

### Win Screen Rules
- This is a **full-screen reward moment.** Go big — particles, chime, scale animation.
- The badge names the real literacy skill, not the game mechanic. The player should feel they gained a reading power, not just beat a level.

---

## Content Requirements (from Curriculum Mapping)

Before storyboarding, fill in this table:

| Field | Value |
|---|---|
| Target domain | |
| Target skill | |
| CSV row | |
| Input modality | |
| Output modality | |
| Interaction type | |
| Sample items (Learn) | |
| Sample items (Practice, 3 sets) | |
| Real words or nonsense? | |
| Magic metaphor | |

### Modality Chain

The game must implement the full modality chain from the CSV:

1. **Stimulus** — how the child receives the information (Visual, Auditory, or Both)
2. **Response** — how the child responds (Tactile, Speech, or Both)
3. **Feedback** — how the game confirms (Visual, Auditory, or Both)

Never skip the input before asking for output. The child must HEAR the sound before tapping. They must SEE the letter before tracing. The CSV defines this chain — follow it exactly.

---

## Visual & Audio Checklist

- [ ] Warm, bright, inviting aesthetic — not dark or clinical
- [ ] Appropriate to the game's theme and narrative (magic, adventure, exploration)
- [ ] Interactive elements are visually distinct from decorative ones
- [ ] Correct = ascending chime + visual celebration
- [ ] Wrong = gentle tone + soft visual feedback (never a harsh buzzer)
- [ ] All instructions spoken in warm, friendly voice
- [ ] Text uses generous spacing for readability
- [ ] Highlighted keywords in accent color
- [ ] Line breaks at clause boundaries, never mid-phrase
- [ ] Background: ambient elements that support the theme without distracting

---

## Storyboard Output Format

When storyboarding a new game, output this structure:

```
GAME: [Fantasy name]
SKILL: [Domain > Subskill > Specific skill]
CSV ROW: [Row number]
MECHANIC: [Core interaction in one sentence]
MAGIC METAPHOR: [How the reading skill becomes a magical act]

LANDING
- Title: ...
- Tagline: ...
- Demo: [describe the looping animation]

LEARN STEP 1 — Introduce
- Title: "..."
- Items: [word1], [word2]
- Caption: "..."

LEARN STEP 2 — Contrast
- Title: "..."
- Items: [word1], [word2]
- Caption: "..."

LEARN STEP 3 — Guided Practice
- Title: "..."
- Items: [word1], [word2], [word3]
- Correct: [which item]
- Caption (correct): "..."

PRACTICE ROUND 1: [item1], [item2], [item3], [item4] — odd: [which]
PRACTICE ROUND 2: [item1], [item2], [item3], [item4] — odd: [which]
PRACTICE ROUND 3: [item1], [item2], [item3], [item4] — odd: [which]

WIN
- Badge: "Skill Unlocked: [Skill Name]"
```
