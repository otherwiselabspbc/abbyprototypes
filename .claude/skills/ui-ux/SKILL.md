---
name: ui-ux
description: Review or apply UI/UX design principles to a game screen, component, or interaction. Covers general design principles plus literacy-specific pedagogy (OG & Lindamood-Bell alignment, phase-based UI, multisensory design, mastery progression). Use when designing or auditing any game screen or interaction.
---

When this skill is invoked, apply the following principles to whatever screen, component, or interaction is specified in $ARGUMENTS. If no target is given, audit the currently open file.

---

## 1. Visual Hierarchy

Establish clear reading order through size, weight, color, and contrast. The most important element should be unmistakably dominant — users should never wonder where to look first.

- The single most important element gets the largest size, highest contrast, and most prominent position.
- Body text minimum: 16px on mobile, 14px on desktop.
- Use no more than 2 typefaces and 3 type sizes per screen: title, body, label.
- Left-align body text. Center only short titles or single-line prompts.
- For dyslexic users: prefer warm cream on dark over pure white on black; avoid tight letter-spacing.

## 2. Consistency

Reuse the same patterns, colors, spacing, and interaction behaviors throughout. Users learn once, then apply everywhere. Define a small set of design tokens and never deviate.

- One color palette: 1 primary, 1 accent, 1 neutral, plus semantic colors (success/error).
- One border-radius value per element type (e.g., 8px cards, 24px pills, 50% circles) — applied consistently.
- Spacing system: multiples of 4px or 8px for all padding, margins, and gaps.
- If a pattern exists elsewhere in the product, reuse it before inventing something new.

## 3. Feedback & Affordance

Every interactive element must communicate its state: default, hover, active, disabled, loading, success, error. Buttons should look pressable. Inputs should look fillable. Never leave a user wondering if their action registered.

- Feedback must be immediate (< 100ms visual response), multimodal where possible: visual + audio.
- Hover: scale up slightly + glow or color shift. Active/press: scale down. Disabled: reduced opacity, no hover effects.
- Success: green glow, particle burst, or upward motion. Error: red flash, shake, or downward motion.
- Never hide a button — disable it instead, and explain why if not obvious.

## 4. Clarity over Cleverness

Labels, icons, and copy should be immediately understood without explanation. Avoid jargon. When in doubt, use words. A clever icon that requires a tooltip has failed.

- Action labels should be verbs: "Tap a string," not "String interaction."
- For children/educational contexts: use concrete, specific language. "Listen, then tap in order" not "Reproduce the phoneme sequence."
- Error messages: say what went wrong in plain language, and tell the user exactly how to fix it.

## 5. Fitts's Law / Target Sizing

Interactive targets should be large enough to hit comfortably. Place frequently used controls where they're easiest to reach.

- Minimum tap target: 44×44px (Apple HIG) / 48×48dp (Material). Larger for children or motor-impaired users.
- Primary actions belong in the thumb zone: bottom 40% of screen on mobile.
- Minimum 8px gap between adjacent tap targets to prevent mis-taps.
- Avoid hover-only interactions — everything must work by touch.
- Add `touch-action: none` on canvas elements to prevent scroll interference during gameplay.

## 6. Progressive Disclosure

Show only what's needed at each step. Hide complexity behind a secondary action. Reduces overwhelm without sacrificing depth.

- One primary action per screen. If two CTAs exist, one is primary (filled) and one is secondary (outlined/ghost).
- Onboarding: teach through play, not walls of text. Use the first interaction to demonstrate the mechanic — an animated demo beats written instructions.
- If instructions are necessary: 3 steps maximum, numbered, with icons or visuals.
- Avoid text blocks longer than 3 lines. Use whitespace as a structural tool.

## 7. Error Prevention & Recovery

Design to prevent errors before they happen. When errors occur, recover gracefully.

- Disable unavailable options rather than letting users select them and fail.
- Validate inline — don't wait for form submission.
- On wrong answer: show clearly what was wrong, reset to a recoverable state, allow retry.
- Where possible, give players a way to undo or recover from mistakes — lowers frustration, especially for children.

## 8. Proximity & Grouping (Gestalt)

Elements that belong together should be visually grouped. Use whitespace as structure.

- Tight spacing within a group; generous whitespace between groups.
- Related controls (e.g., replay + continue buttons) should be visually near each other.
- Don't mix unrelated elements in the same visual cluster.

## 9. Accessibility

- Color contrast: WCAG AA minimum 4.5:1 for body text, 3:1 for large text (>18px bold).
- Never rely on color alone to convey meaning — pair with shape, icon, or label.
- Support keyboard navigation with visible focus indicators.
- Use semantic HTML and ARIA roles where applicable.
- For dyslexic users: generous letter-spacing (0.05em+), rounded letterforms, avoid long italic passages.

## 10. Performance Perception

Perceived speed matters as much as actual speed. Keep users informed during any delay.

- Instant visual feedback (even just a state change) prevents repeated taps/clicks.
- Use skeleton screens or loading indicators for anything taking > 300ms.
- Animate entrances with ease-out (fast start, slow end). Animate exits with ease-in.
- Micro-interaction duration: 80–150ms. State transitions: 200–350ms. Page transitions: 300–500ms. Never animate longer than 600ms unless it's a deliberate reward moment.

## 11. Game-Specific Rules

- **Clear game state**: Score, health, round, timer — always visible and readable at a glance. Never bury this in a menu.
- **Reward moments**: Win states, level-ups, and completions deserve satisfying visual + audio punctuation. A correct answer with no feedback is a missed opportunity.
- **Delight without distraction**: Particle effects, glows, and sounds are rewards — use them for correct actions and wins, not as ambient decoration on every frame.
- **Undo & forgiveness**: Where possible, let players recover from mistakes. On wrong answer, reset progress within the round — don't punish with a full restart.
- **Onboarding**: The first interaction should teach the mechanic. Show a demo, then step aside. Never open a game with a wall of text.
- **State transitions**: A brief pause (200ms) before a new state begins lets the player process what just happened. Don't rush into the next moment.

---

## 12. Literacy-Pedagogy Alignment (OG & Lindamood-Bell)

These principles apply specifically to games targeting early literacy. The UI must mirror the three core properties of structured literacy: **structured, cumulative, and multisensory**.

### Phase-Based Interface Complexity

Never expose a child to interface complexity they aren't ready for linguistically. Match the UI to the literacy level:

**Phase 1 — Pre-literate / Phonemic Awareness**
- Zero reliance on written text for navigation or instructions
- All UI communicates via audio, animation, color, and iconography
- Animated characters or mascots deliver instructions via voice
- Tasks are purely auditory/oral: tapping sounds, matching mouth shapes, identifying rhymes
- Interactive mouth/sound animations the child can tap and replay (mirrors LiPS kinesthetic discovery)
- Tap targets must be extremely large and forgiving — motor precision is lowest at this stage

**Phase 2 — Letter-Sound Introduction**
- Letters always appear paired with their sound (audio fires on appearance, not just on tap)
- Letter names and sounds reinforced simultaneously — never one without the other
- Each new phonogram introduced feels like a distinct, celebratory "unlock" moment
- Short labels (1–2 letters/words max) can appear, always backed by audio
- Introduce simple CVC words only — words the child can fully decode from known sounds

**Phase 3 — Decoding & Blending**
- Short decodable words and sentences can appear; always paired with a read-aloud option
- Font size minimum: 18–22px; clean, high-contrast typeface — no decorative fonts for instructional text
- Instructions can include 3–5 word phrases, still audio-backed
- Finger-tap interactions that physically segment words into phonemes (mirrors OG tapping method)
- Introduce sight words alongside decodable words — visually distinguish them (e.g., a "star word" badge)

**Phase 4 — Fluency & Comprehension**
- Written instructions can stand without audio support, though audio remains available on demand
- UI complexity can increase moderately: multi-step tasks, more navigation options
- Support visualization prompts (e.g., "draw what you see in your head")
- Audio/read-aloud remains a persistent, accessible option — never remove it

### Multisensory Design Requirements

Support all three channels simultaneously wherever possible:

- **Visual**: High-contrast letters and words. Use color coding consistently — e.g., vowels always one color, consonants another (standard OG convention). Animate letter introductions.
- **Auditory**: Every letter, phonogram, word, and instruction has an associated audio. Tap anything to hear it. Never rely on silent reading for task comprehension.
- **Kinesthetic**: Drag-to-blend, tap-to-segment, trace-the-letter gestures. Physical interaction reinforces the neural pathway. Replicate OG air-writing and tapping with gesture/tap mechanics.

### Cumulative Review Must Be Visible

Previously mastered skills should resurface in new levels — don't let old content disappear.

- Show the child a visual "skill map" or constellation of what they've learned so far
- New concepts should visually connect to prior ones (e.g., a new letter "snapping" onto a chain of known letters)
- Frequent, distributed review is built into the progression — not optional

### Mastery Before Progression

Do not unlock the next level on a single correct answer — require demonstrated consistency.

- Show a visible mastery indicator (stars, filled bar, glowing badge) that fills across multiple correct attempts
- "Not ready yet" should feel encouraging, not punishing: "Almost there! Let's practice a little more" with a cheerful animation — never a red X

### Diagnostic Awareness (Invisible Scaffolding)

- Track which phonemes, patterns, and skills a child struggles with; surface more practice for those automatically
- If a child consistently misses a specific sound or pattern, gently re-route — don't just repeat the same failed task
- A parent/teacher dashboard (separate from the child-facing UI) should surface this data clearly

### Encouragement Architecture

Struggling readers have often already experienced significant failure. The UI must counteract this:

- Every attempt earns positive acknowledgment — not just correct ones
- Errors trigger gentle redirection, never a harsh buzzer or "wrong" visual
- Celebrate milestones loudly: completing a phoneme set, reading a first full word, finishing a level — these deserve full-screen celebration moments
- Frame the game as exploration and building, not testing and passing

---

## How to Apply This Skill

**When reviewing a file or component:**
1. Read the relevant HTML/CSS/JS for the target element.
2. Call out specific violations with line references.
3. Suggest concrete fixes — show corrected code, not just the principle.
4. Flag what's already working well so it isn't accidentally changed.

**When building something new:**
1. Start with hierarchy — establish what the user must see first.
2. Size tap targets before styling them.
3. Add all interaction states (hover, active, disabled) before calling it done.
4. Check contrast ratios for every text/background pair.
5. Add at least one piece of delight (sound, animation, or particle) for the primary success state.
