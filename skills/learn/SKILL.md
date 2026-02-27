---
name: learn
description: Full learning-to-implementation pipeline for mastering a new topic. Chains survey, prototype, deep-dive, synthesis, and execution skills into one flow.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task, WebSearch, WebFetch, TaskCreate, TaskUpdate, TaskList, TaskGet
---

# Learn Skill

## Purpose
Orchestrate a complete learning pipeline for any new topic. One command triggers a structured flow: survey the landscape, run a micro-prototype, deep-dive informed by reality, synthesize contradictions, then execute iteratively — while capturing every lesson learned.

## Commands

### `/learn "<topic>"`
Start a full learning pipeline on a new topic.

### `/learn resume`
Resume the current learning pipeline from where it left off.

### `/learn status`
Show current phase, progress, and next actions.

### `/learn phase <N>`
Jump to a specific phase (use when earlier phases are already done).

## The Pipeline

There are 6 phases. Each phase has a gate — a checkpoint where the user reviews and approves before proceeding.

```
Phase 1: Survey ──> Phase 2: Prototype ──> Phase 3: Deep Dive
    │                    │                      │
    ▼                    ▼                      ▼
  /dispatch            hands-on              /dispatch
  /notes               test                  /notes
  /reading-guide       reality-check         /reading-guide
                                              │
Phase 6: Iterate <── Phase 5: Build <── Phase 4: Synthesize
    │                    │                      │
    ▼                    ▼                      ▼
  /self-improving      /executing-plans       direction memo
  /dashboard           /dashboard             /dashboard
  feedback loop        batch execution        contradictions
```

---

## Phase 1: Survey the Landscape

**Goal:** Map the territory before picking a destination.

**Actions:**
1. Create project scaffold:
   - `.claude/context/project.md` — topic overview
   - `.claude/plans/active/` — plan directory
   - `.claude/notes/active/` — notes directory
   - `.claude/dashboard/components/` — dashboard components
   - `.learnings/` — self-improving logs

2. Ask the user 3 questions:
   - "What is the topic and why do you care about it?"
   - "What do you already know? (so we skip basics)"
   - "What's the end goal — a paper, a tool, a skill, or understanding?"

3. Create 3-5 parallel survey dispatch plans using `/dispatch create`:
   - Track A: Historical context — how did this field develop?
   - Track B: Current state of the art — what are the best methods?
   - Track C: Key datasets and benchmarks — what data exists?
   - Track D: Open problems and gaps — where are the opportunities?
   - (Optional) Track E: Adjacent fields — what can we borrow?

4. Execute all tracks in parallel using Task agents:
   - Each agent reads web sources, papers, repos
   - Each agent writes structured notes via `/note add`
   - Each agent logs findings to its plan file

5. Build initial reading guide via `/reading-guide create`

6. Render Phase 1 dashboard via `/dashboard`

**Gate:** Present survey summary to user. Ask: "Which 2-3 areas should we dig deeper into? Anything missing?"

---

## Phase 2: Micro-Prototype

**Goal:** Ground theory in reality before investing in deep dives.

This is the key differentiator from a purely reading-based approach. Before spending hours on deep dives, run ONE quick experiment to test feasibility.

**Actions:**
1. Based on Phase 1 findings, identify the simplest possible test:
   - Can we load the data?
   - Can we run the baseline tool?
   - Does the environment support the required libraries?
   - Can we reproduce one number from one paper?

2. Create a single dispatch plan: `micro_prototype.md`
   - Maximum 3 subtasks
   - Maximum 2 hours of work
   - Must produce a concrete output (a number, a plot, a working script)

3. Execute the prototype

4. Log all issues encountered to `.learnings/ERRORS.md` via self-improving skill

5. Update notes with reality-check findings:
   - `/note add --plan micro_prototype --type finding "X works / doesn't work"`
   - `/note add --plan micro_prototype --type blocker "Y is broken because Z"`

**Gate:** Present prototype results. Ask: "Here's what works and what doesn't. Does this change our priorities for deep dives?"

---

## Phase 3: Deep Dive (Informed by Prototype)

**Goal:** Go deep on the 2-3 areas the user selected, now informed by real-world constraints from the prototype.

**Actions:**
1. Create deep-dive dispatch plans (one per area) using `/dispatch create`:
   - Each plan has 5-8 subtasks
   - Each plan references prototype findings
   - Each plan includes "feasibility check" subtask informed by Phase 2

2. Execute deep-dive plans in parallel using Task agents:
   - Agents produce detailed notes (500+ lines each)
   - Agents cross-reference with survey findings
   - Agents flag contradictions between sources

3. Expand reading guides with new papers via `/reading-guide add`

4. Update dashboard with deep-dive progress

**Gate:** Present deep-dive summaries. Ask: "Ready to synthesize? Any area needs more depth?"

---

## Phase 4: Synthesize Contradictions

**Goal:** Find where experts disagree — that's where the opportunities live.

**Actions:**
1. Create a cross-track synthesis dispatch plan:
   - Subtask 1: Identify converging themes across all tracks
   - Subtask 2: Identify contradictions between sources
   - Subtask 3: Map contradictions to research opportunities
   - Subtask 4: Rank opportunities by feasibility (informed by prototype)
   - Subtask 5: Write a direction memo

2. Execute the synthesis plan

3. Produce a **direction memo** (saved to `.claude/notes/active/direction_memo.txt`):
   - Top 3 ranked directions with pros/cons
   - Feasibility assessment for each (referencing prototype results)
   - Recommended direction with justification

4. Update dashboard to show synthesis complete

**Gate:** Present direction memo. Ask: "Which direction do you want to pursue? Any concerns?"

---

## Phase 5: Build (Iterative Execution)

**Goal:** Implement the chosen direction in controlled batches.

**Actions:**
1. Create an implementation plan using `/dispatch create`:
   - Break into bite-sized tasks (2-5 per batch)
   - Each task has clear inputs, outputs, and verification steps
   - First batch is always environment/data setup

2. Execute using the executing-plans skill:
   - Load plan, review critically
   - Execute batch of 3 tasks
   - Report results, wait for feedback
   - Apply feedback, continue next batch

3. After each batch:
   - Log learnings via self-improving skill
   - Update dashboard progress
   - Check if direction needs adjustment based on results

4. Between batches, check `.learnings/` for patterns:
   - Recurring errors -> fix the root cause
   - Repeated corrections -> update CLAUDE.md
   - Discovered best practices -> promote to memory

**Gate:** After each batch: "Here's what was built and verified. Ready for next batch?"

---

## Phase 6: Reflect and Iterate

**Goal:** Close the feedback loop. Make the next learning cycle faster.

**Actions:**
1. Review all `.learnings/` files:
   - Resolve pending items
   - Promote valuable learnings to memory or CLAUDE.md
   - Extract recurring patterns into new skills

2. Update the reading guide with papers discovered during implementation

3. Render final dashboard showing full pipeline completion

4. Write a **lessons-learned note** (`.claude/notes/active/lessons_learned.txt`):
   - What worked well in this learning cycle
   - What should change for next time
   - Skills or tools that were missing
   - Time spent per phase (estimate)

5. Archive completed plans: move from `active/` to `completed/`

6. Ask: "What's next? Extend this topic, or start a new `/learn` on something else?"

---

## State Tracking

The learn skill tracks its state in `.claude/learn_state.json`:

```json
{
  "topic": "Perturbation prediction with causal priors",
  "started": "2026-02-27T00:00:00Z",
  "current_phase": 3,
  "phases": {
    "1_survey": {"status": "done", "plans": ["hist_dev", "foundation_models", "benchmarks"]},
    "2_prototype": {"status": "done", "plans": ["micro_prototype"]},
    "3_deep_dive": {"status": "in_progress", "plans": ["perturbation_methods", "uq_scfm"]},
    "4_synthesis": {"status": "pending", "plans": []},
    "5_build": {"status": "pending", "plans": []},
    "6_reflect": {"status": "pending", "plans": []}
  },
  "user_selections": {
    "deep_dive_areas": ["perturbation methods", "uncertainty quantification"],
    "chosen_direction": null
  },
  "prototype_findings": [],
  "learnings_promoted": 0
}
```

**On `/learn resume`:** Read this file, report current phase, list next actions.
**On `/learn status`:** Display phase progress from this file + dashboard summary.

---

## Skill Dependencies

This skill orchestrates these sub-skills (all must be installed):

| Skill | Used In Phase | Role |
|-------|---------------|------|
| dispatch | 1, 2, 3, 4, 5 | Creates and manages plans |
| notes | 1, 2, 3, 4, 6 | Captures structured findings |
| reading-guide | 1, 3, 6 | Builds paper dependency maps |
| dashboard | 1, 3, 4, 5, 6 | Visualizes progress |
| executing-plans | 5 | Batch execution with checkpoints |
| self-improving | 2, 5, 6 | Logs errors and corrections |
| history | resume | Reviews past session context |

---

## Example Usage

```
User: /learn "single-cell foundation models for drug response prediction"

Agent: I'm using the learn skill to start a new learning pipeline.

Phase 1: Survey
- Creating project scaffold...
- 3 questions for you before I start:
  1. What's your background with single-cell analysis?
  2. What do you already know about foundation models in biology?
  3. End goal: paper, tool, or understanding?

[User answers]

- Dispatching 4 parallel survey tracks...
  Track A: Historical context (mechanistic -> statistical -> DL -> FM)
  Track B: Current SOTA (scGPT, Geneformer, scFoundation, ...)
  Track C: Datasets (Norman, Replogle, scPerturb, ...)
  Track D: Open problems (OOD, calibration, causal, ...)

[Agents complete surveys]

- Survey complete. Building reading guide...
- Rendering dashboard...

GATE: Here's what I found across 4 tracks. [Summary]
Which 2-3 areas should we dig deeper? Anything missing?
```

---

## Principles

1. **Wide before deep** — Survey broadly, then focus
2. **Prototype early** — Ground theory in reality before investing
3. **Contradictions are gold** — Disagreements reveal opportunities
4. **Batch and checkpoint** — Never go dark; report after every batch
5. **Log everything** — Errors and corrections make the next cycle faster
6. **Ask, don't assume** — Every phase gate is a conversation with the user
