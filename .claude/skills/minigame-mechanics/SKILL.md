---
name: minigame-mechanics
description: Defines the structure, pacing, and UI rules for sprint mini-games — short pop-up challenges (~20-30 seconds) that test a single skill during longer play sessions. Use when building or auditing any mini-game prototype.
---

When this skill is invoked, audit or build $ARGUMENTS against the mini-game rules below. If no argument is given, audit the most recently discussed mini-game.

---

## What is a Mini-Game?

A mini-game is a **pop-up sprint challenge** that emerges during a longer play session or lesson plan. It is NOT a lesson. It does not teach — it tests a skill the player has already learned elsewhere.

Mini-games are the **20% practice** in the 80/20 instruction model. The 80% explicit instruction happens in narrative lesson sessions (e.g., The Locked Door). Mini-games are the fast, focused skill checks that punctuate those sessions.

**Think of mini-games like boss fights in an RPG:** the player has been learning skills throughout the level, and the mini-game is where they prove they can use them.

---

## Mini-Game vs Lesson Session

| | Mini-Game (Sprint) | Lesson Session (Narrative) |
|---|---|---|
| **Duration** | 20–30 seconds | 5–15 minutes |
| **Purpose** | Test a skill | Teach a skill |
| **Structure** | Landing → Practice rounds | Landing → Learn → Guided → Practice → Win |
| **Instruction** | None or 1 spoken sentence | Full explicit instruction with NPC/narrative |
| **When it appears** | Pops up during a longer session | IS the longer session |
| **Scaffolding** | Minimal — hint escalation only | Full — 80% of the time is instruction |
| **Examples** | Enchanted Gems, Spell Caster, Whispering Stones, Block Breaker | The Locked Door, Lesson: Letter Sounds |

---

## Structure

Every mini-game has exactly 2 screens:

```
LANDING → PRACTICE (multiple rounds)
```

That's it. No Learn screen. No Transition screen. No How-To-Play screen.

### Screen 1: Landing

The landing page contains:

| Element | Required? | Details |
|---|---|---|
| **Game name** | Yes | Large, prominent title |
| **Skill tag** | Yes | Small text identifying the literacy skill being tested (e.g., "Rhyme Detection", "Phoneme ID") |
| **Begin button** | Yes | Single primary CTA — should pulse or glow so the player knows to tap it |
| **Brief instruction** | Optional | Maximum 1 sentence. If present, it describes the mechanic, not the skill. |
| **Demo animation** | No | Remove demos — they slow down the sprint feel |
| **Age range** | No | Remove — not useful to the player |
| **Tagline/description** | No | Remove — the game teaches through play |

**Rules:**
- The landing page should feel like a title card, not an instruction manual
- The Begin button should be the most prominent element — use a pulsing glow animation
- No text walls. Zero or one sentence max.

### Screen 2: Practice (the game)

The practice screen contains multiple rounds of the same mechanic with different content.

| Element | Required? | Details |
|---|---|---|
| **Round dots** | Yes | Visual indicator showing progress through rounds (e.g., 1/6) |
| **Round label** | Yes | "Round X of Y" text |
| **Spoken instruction** | Yes | Read aloud when the first round starts |
| **Game area** | Yes | The interactive elements (stones, blocks, tiles, etc.) |
| **Hint escalation** | Yes | Wrong answers get increasing support (3 tiers) |

---

## Pacing Rules

- **Total duration:** 20–30 seconds of active play (not counting instruction speech)
- **Rounds:** 4–6 rounds per game
- **No timer** unless the mechanic specifically requires time pressure
- **No lives/hearts** — replaced by hint escalation
- **Auto-advance** between rounds — no "Continue" button unless it's a reward moment

---

## Instruction Rules

### On the landing page:
- Zero or one sentence of text, max
- Do NOT read instructions aloud on the landing page

### When the game starts (first round):
- Instructions are **always read aloud**
- Instructions are spoken in a **warm, natural voice** — never robotic
- Use pre-recorded audio files (ElevenLabs) when available; fall back to Web Speech API with a preferred female voice
- When using Web Speech API, always cache a natural-sounding voice (Samantha, Karen, Moira, etc.)

### Instruction phrasing:
- Instructions must **command an action** — they tell the player what to do
- Use imperative verbs: "Listen", "Tap", "Trace", "Find", "Match"
- Always specify the input AND the output: what the player receives, then what they do

**Good instructions:**
- "Listen to the sound, then tap the correct letter."
- "Listen carefully to each word. Which one doesn't rhyme? Tap it!"
- "Touch each stone to hear its sound."
- "Listen to the spell, then cast it yourself by matching the sound to the letter in the correct order."
- "Trace the letter. Follow the dotted path with your finger."

**Bad instructions:**
- "Welcome to the game!" (not an action)
- "In this game, you will learn about rhyming." (describes, doesn't command)
- "Phoneme identification exercise." (jargon, not an action)
- "Tap the correct answer." (too vague — what are they listening to? What makes it correct?)

### After the first round:
- Do NOT repeat the full instruction on subsequent rounds
- Prompts can be shorter: "Which one doesn't rhyme?" or just the spoken target
- The player already knows the mechanic — don't slow them down

---

## Voice Rules

The voice in mini-games must feel warm and human, not robotic.

### Priority order for voice:
1. **Pre-recorded audio files** (ElevenLabs WAV/MP3) — best quality
2. **Web Speech API with cached natural voice** — acceptable fallback

### Web Speech API voice selection:
Always cache a voice on load. Prefer these voices (in order):
`samantha, karen, moira, tessa, fiona, victoria, zira, jenny, google uk english female, google us english`

Filter for English (`lang.startsWith('en')`) and prefer `localService` voices.

### Speech parameters:
- `rate`: 0.85–0.95 (slightly slower than normal for clarity)
- `pitch`: 1.0–1.1 (natural, not cartoonish)
- `volume`: 1.0

### Phoneme pronunciation:
- When speaking individual letter sounds, pass **lowercase** to the Speech API to avoid "capital B"
- When pre-recorded phoneme audio is available (e.g., `audio/harp/`), always use it instead of Speech API
- Audio path from `minigame prototypes/` folder: use `../audio/` prefix

---

## Feedback Rules

### Correct answer:
- Ascending chime SFX
- Visual celebration (glow, particles, shatter, confetti — match the game's aesthetic)
- Brief spoken confirmation: "That's T!" or "Pan doesn't rhyme!"
- Auto-advance to next round after ~1 second

### Wrong answer — 3-tier hint escalation:
| Tier | Trigger | Response |
|---|---|---|
| **1 — Nudge** | 1st wrong | Process feedback: "That's [wrong answer]. Try again!" |
| **2 — Directive** | 2nd wrong | More specific help, may replay sounds for comparison |
| **3 — Bottom-out** | 3rd wrong | Reveal the answer with explanation, auto-advance |

### Wrong answer SFX:
- Soft descending tone — never a harsh buzzer
- The sound should say "not quite" not "you failed"

---

## Visual Rules

- **No text walls** — all instructions are spoken, not displayed as paragraphs
- **Interactive elements glow visibly** when they are the focus (being spoken, being played)
- The glow should be dramatic enough that there is no ambiguity about which element is active
- **Begin button** always pulses/glows on the landing page
- **Round dots** show progress — filled for complete, highlighted for current, empty for upcoming
- Match the game's existing aesthetic — don't introduce new design systems per game

---

## What NOT to Include in Mini-Games

- Learn screens or tutorial phases
- Transition screens ("Ready to Practice?")
- How-to-play screens with numbered steps
- Timers (unless the mechanic requires it)
- Lives, hearts, or health bars
- Score counters or leaderboards
- "Back to Garden" or overworld navigation
- Session storage guards or redirect logic
- Age range labels on the landing page
- Demo animations on the landing page

---

## Checklist — Run Before Shipping Any Mini-Game

- [ ] Landing page has: game name, skill tag, glowing Begin button
- [ ] Landing page does NOT have: instructions paragraph, demo, age range, how-to-play
- [ ] No Learn or Transition screens exist
- [ ] First round speaks instructions aloud (imperative action command)
- [ ] Subsequent rounds do NOT repeat full instructions
- [ ] Voice sounds natural (pre-recorded or cached natural voice)
- [ ] Letters spoken lowercase to avoid "capital" prefix
- [ ] 4–6 rounds of practice
- [ ] No timer (unless mechanic requires it)
- [ ] No lives/hearts — hint escalation instead
- [ ] Correct answers: chime + visual celebration + spoken confirmation
- [ ] Wrong answers: soft tone + process feedback + hint escalation
- [ ] No garden overworld redirect or session storage guard
- [ ] Game opens directly to landing page from URL
