---
name: self-improving
description: Captures learnings, errors, and corrections to enable continuous improvement. Self-reflection + Self-criticism + learning from corrections.
attribution: Adapted from openclaw/skills by pskoett (https://github.com/openclaw/skills/blob/main/skills/pskoett/self-improving-agent/SKILL.md)
---

# Self-Improving Agent

## When to Log

Log entries when ANY of these occur:
- Command or tool fails
- User corrects the agent
- Missing feature identified
- External API/tool failure
- Outdated knowledge discovered
- Better approach found during work

## Logging Structure

Maintain three files in `.learnings/` directory:

### .learnings/LEARNINGS.md
For corrections, knowledge gaps, and best practices discovered.

### .learnings/ERRORS.md
For command failures, exceptions, and technical errors.

### .learnings/FEATURE_REQUESTS.md
For requested capabilities and improvements.

## Entry Format

Each entry must include:
- **ID**: LRN/ERR/FEAT-YYYYMMDD-XXX (unique sequential)
- **Timestamp**: ISO 8601
- **Priority**: critical | high | medium | low
- **Status**: pending | resolved | in_progress | wont_fix
- **Area**: frontend | backend | infra | tests | docs | config | data | modeling
- **Summary**: One-line description
- **Details**: Full context of what happened
- **Suggested Action**: What to do differently next time
- **Metadata**: Related files, tags, environment info

## Self-Reflection Protocol

After completing any significant task:
1. Review what went well
2. Review what could be improved
3. Check if any corrections were made during the task
4. Log relevant learnings

## Knowledge Promotion

When a learning is broadly applicable:
1. Promote to `CLAUDE.md` as a project fact or convention
2. Promote to memory files for cross-session persistence
3. Consider whether it should become a reusable skill

## Skill Extraction Criteria

A learning should become a skill when:
- It has been verified across multiple instances
- It is non-obvious (not common knowledge)
- It is broadly applicable across projects
- It can be described as a repeatable process

## Review Cycle

Periodically review `.learnings/` files to:
- Resolve pending items
- Promote valuable learnings
- Archive resolved errors
- Extract recurring patterns into skills
