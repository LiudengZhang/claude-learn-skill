---
name: history
description: Parse and display conversation history to track what was done across sessions.
allowed-tools: Read, Bash, Glob, Grep
---

# History Skill

## Purpose
Parse Claude Code conversation transcripts to extract a structured timeline of actions, decisions, and outputs. Provides session-level summaries so you can quickly understand what happened in previous sessions without reading raw transcripts.

## Commands

### `/history`
Show a summary of all sessions for this project.

**Workflow:**
1. Find transcript files in the Claude projects directory
2. Run `parse_history.py` to extract structured events
3. Display session summaries sorted by date

**Output:**
```
Session History:
  2026-02-25 — Infrastructure setup: created .claude/ scaffold, installed 4 skills,
               created 5 dispatch plans, rendered initial dashboard
  (1 session total)
```

### `/history last`
Show detailed summary of the most recent session.

### `/history search "<query>"`
Search across all session summaries for matching content.

### `/history export`
Export full session history to `.claude/dashboard/shared/history.json` for dashboard integration.

## How It Works

The skill uses `parse_history.py` (located alongside this SKILL.md) to:
1. Read JSONL transcript files from the Claude projects directory
2. Extract tool calls, file operations, and key decisions
3. Group actions into logical sessions
4. Generate concise summaries

## Session Summary Format

Each session summary includes:
- **Date** — When the session occurred
- **Duration** — Approximate session length
- **Actions** — Key tool calls and operations performed
- **Files Modified** — List of files created or edited
- **Decisions** — Any notable choices made
- **Outcome** — What was accomplished

## Integration with Dashboard

Session history feeds into the dashboard timeline, showing project evolution over time.
