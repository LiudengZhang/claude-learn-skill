---
name: dashboard
description: Render and manage a project dashboard that aggregates plan status, component progress, and notes into an HTML view.
allowed-tools: Read, Write, Bash, Glob
---

# Dashboard Skill

## Purpose
Generate and update an HTML dashboard that provides a single-page overview of all project plans, component progress, and recent notes. The dashboard reads from `.claude/dashboard/components/` JSON files and renders `dashboard.html` at project root.

## Commands

### `/dashboard`
Render (or re-render) the project dashboard.

**Workflow:**
1. Scan `.claude/dashboard/components/*.json` for all registered components
2. Scan `.claude/plans/active/` and `.claude/plans/completed/` for plan status
3. Scan `.claude/notes/active/` for recent notes
4. Read `.claude/dashboard/shared/config.json` for project metadata (if exists)
5. Generate `dashboard.html` at project root

### `/dashboard status`
Print a text summary of all components and their status without rendering HTML.

**Output:**
```
Dashboard Status:
  [pending]  Historical Development       0/6 subtasks
  [pending]  Foundation Models             0/5 subtasks
  [pending]  Benchmarks & Evaluation       0/5 subtasks
  [pending]  Open Problems & Gaps          0/5 subtasks
  [pending]  Applications & Translation    0/4 subtasks

Overall: 0/25 subtasks complete (0%)
Notes: 0 active
```

### `/dashboard update <component_id> <status>`
Update a specific component's status.

## Component JSON Format

Each component in `.claude/dashboard/components/` follows this schema:

```json
{
  "id": "plan_historical_development",
  "label": "Historical Development",
  "status": "pending",
  "progress": {"done": 0, "total": 6},
  "description": "Survey the evolution from mechanistic models to AI virtual cells",
  "plan_file": "historical_development.md",
  "items": [
    {"label": "Subtask 1", "status": "pending"},
    {"label": "Subtask 2", "status": "pending"}
  ],
  "recent_outputs": [],
  "notes": [],
  "updated": "2026-02-25T00:00:00Z"
}
```

### Status Values
- `pending` — Not started
- `in_progress` — Actively being worked on
- `blocked` — Waiting on dependency
- `done` — Completed

## HTML Dashboard Layout

The generated `dashboard.html` includes:
1. **Header** — Project name, last updated timestamp
2. **Progress Bar** — Overall completion percentage
3. **Components Grid** — Card for each component showing status, progress bar, description
4. **Plans Section** — Active and completed plans
5. **Notes Section** — Recent notes and findings

## Rendering Rules

- Status colors: pending=gray, in_progress=blue, blocked=orange, done=green
- Components sorted by status (in_progress first, then pending, blocked, done)
- Dashboard is self-contained (inline CSS, no external dependencies)
- Timestamps in CST (UTC-6)
