---
name: notes
description: Create, search, and manage structured research notes linked to dispatch plans.
allowed-tools: Read, Write, Bash, Glob, Grep
---

# Notes Skill

## Purpose
Manage structured research notes that are linked to dispatch plans. Notes capture findings, blockers, decisions, and questions during plan execution. All notes live in `.claude/notes/active/` and are archived when their parent plan completes.

## Commands

### `/note add --plan <plan_name> --type <type> "<content>"`
Add a new note linked to a plan.

**Parameters:**
- `--plan` — Name of the dispatch plan (matches filename without .md)
- `--type` — One of: `finding`, `blocker`, `decision`, `question` (default: `finding`)
- Content — The note text (in quotes)

**Workflow:**
1. Create or append to `.claude/notes/active/{plan_name}.md`
2. Add timestamped entry with type tag
3. If type is `blocker`, also flag in the plan file

**Note Format:**
```
### [finding] 2026-02-25 14:30 CST
{Content of the note}

---
```

### `/note show`
Show all active notes, grouped by plan.

**Output:**
```
Notes for historical_development:
  [finding] 2026-02-25 — Key paper: Kitano 2002 computational systems biology
  [finding] 2026-02-25 — Karr et al. 2012 whole-cell model of M. genitalium

Notes for foundation_models:
  (no notes yet)
```

### `/note show --plan <plan_name>`
Show notes for a specific plan only.

### `/note search "<query>"`
Search across all notes for matching content.

### `/note archive --plan <plan_name>`
Move a plan's notes from `active/` to `archived/`.

**Triggered automatically when a dispatch plan moves to `completed/`.**

## Note Types

| Type | Use When | Icon |
|------|----------|------|
| `finding` | Discovered something noteworthy | 🔍 |
| `blocker` | Work is blocked, needs resolution | 🚫 |
| `decision` | Made a judgment call, document rationale | ⚖️ |
| `question` | Need clarification from user | ❓ |

## File Structure

```
.claude/notes/
├── active/
│   ├── historical_development.md
│   ├── foundation_models.md
│   └── ...
└── archived/
    └── {completed_plan_name}.md
```

## Integration with Dispatch

During `/dispatch execute`, the executor should:
1. Log findings as they work: `/note add --plan X --type finding "..."`
2. Flag blockers immediately: `/note add --plan X --type blocker "..."`
3. Document decisions: `/note add --plan X --type decision "..."`
4. On completion, notes are summarized and archived

## Integration with Dashboard

Recent notes appear in the dashboard's Notes section, showing the 10 most recent entries across all plans.
