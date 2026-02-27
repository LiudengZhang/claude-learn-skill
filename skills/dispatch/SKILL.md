---
name: dispatch
description: Create and manage task plans for multi-agent execution. Commander/Executor pattern where one terminal creates plans and others execute them.
allowed-tools: Read, Write, Bash, Glob, TaskList, TaskGet
attribution: Original work (https://github.com/LiudengZhang/Core_Skills_4_Projects)
---

# Dispatch Skill

## Purpose
Create and manage task plans that can be executed by separate Claude Code sessions (Executors). Enables a Commander/Executor pattern where one terminal creates plans and other terminals execute them.

## Architecture

Commander creates plans -> saves to .claude/plans/active/
Executor reads plan -> executes subtasks -> updates dashboard -> moves to completed/

## Folder Structure

.claude/
  context/         <- Project background (executors read first)
  plans/active/    <- Plans ready for execution
  plans/completed/ <- Finished plans (archive)
  plans/templates/ <- Reusable plan templates
  dashboard/components/ <- Executor updates status here
  notes/active/    <- Related notes

## Commands

### /dispatch create "<task description>"
Commander creates a new plan through structured interview.
Workflow: Ask clarifying questions -> Break into subtasks -> Identify resources -> Generate completion checklist -> Save to .claude/plans/active/{plan_name}.md

### /dispatch list
List all plans and their status.

### /dispatch execute <plan_name>
Executor picks up and executes a plan.
Workflow:
1. Read context files first (.claude/context/project.md)
2. Read the plan file
3. Claim the plan (update Assigned field)
4. Check existing notes: /note show --plan <plan_name>
5. Execute subtasks one by one
   - Log findings: /note add --plan <plan_name> --type finding "..."
   - If blocked: /note add --plan <plan_name> --type blocker "..."
6. Check off items as completed
7. Run completion checklist (ALL must pass)
8. Summarize key findings in a final note
9. Update dashboard component
10. Move plan to completed/

### /dispatch status <plan_name>
Check status of a specific plan.

### /dispatch template <template_name>
Create a plan from a template.

## Plan File Format

# Plan: {Title}
## Meta
- ID: plan_{short_name}_{timestamp}
- Created: {ISO datetime}
- Status: ready | in_progress | blocked | done
- Assigned: {executor terminal or "unassigned"}

## Context
Read first: .claude/context/project.md

## Goal
{Clear, concise description}

## Subtasks
- [ ] 1. {First subtask}
- [ ] 2. {Second subtask}

## Resources
- Data: {paths}
- Output: {paths}
- Skills: {relevant skills}

## Completion Checklist
- [ ] Output quality checks
- [ ] Documentation complete
- [ ] Dashboard updated

## Notes
{Executor adds notes during execution}

## Dashboard Integration
When executor completes a plan, create/update component JSON in .claude/dashboard/components/ with id, label, status, progress, description, items, and recent_outputs.

## Interview Questions (for /dispatch create)

For Literature Research:
- What is the scope of the survey?
- Which databases to search?
- Key terms and inclusion/exclusion criteria?
- Expected deliverable format?

For Analysis:
- What data to use?
- What method/pipeline?
- Where to save results?

## Completion Checklist Template for Literature Research
- [ ] All key papers identified and catalogued
- [ ] Search terms documented
- [ ] Findings organized by theme
- [ ] Multiple databases searched
- [ ] Recent preprints included
- [ ] Notes saved with citations
- [ ] Dashboard updated
