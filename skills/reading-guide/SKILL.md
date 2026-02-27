---
name: reading-guide
description: Create, edit, and maintain structured reading guides with Obsidian-compatible Mermaid flowcharts and paper tables.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# Reading Guide Skill

## Purpose
Manage structured reading guides for literature review. Each guide contains a Mermaid dependency flowchart, a reading order table, and a quick reference table. All Mermaid diagrams follow strict Obsidian compatibility rules.

## Commands

### `/reading-guide create "<topic>"`
Create a new reading guide from scratch.

**Workflow:**
1. Ask the user for the topic and 3-10 core papers
2. For each paper, collect: short name, year, venue, role, dependencies
3. Assign colors by role using the standard color scheme
4. Generate the three sections: flowchart, reading order table, quick reference
5. Save to `reading_guide_{topic_slug}.md` at project root

**Output file structure:**
```
# Reading Guide: {Topic Title}

## Reading Dependency Flowchart
(Mermaid flowchart TD)

**Legend:**
(Color to role mapping)

## Recommended Reading Order
(Table with columns: #, Paper, Year, Role, Read After, Why Read This)

## Quick Reference: What Each Paper Gives You
(Table with columns: Paper, Core Takeaway for Thesis)
```

### `/reading-guide add <guide> --paper "<citation>" --after <N> --role <role>`
Add a paper to an existing reading guide.

**Parameters:**
- `<guide>` — Filename slug (e.g., `perturbation_methods`)
- `--paper` — Short citation string (e.g., "CellFlow, Theislab, bioRxiv 2025")
- `--after` — Paper number(s) this depends on (e.g., `4` or `4,7`)
- `--role` — One of the standard roles (see Role Color Scheme below)

**Workflow:**
1. Read the existing guide file
2. Assign the next available number
3. Add a new node to the Mermaid flowchart with correct style
4. Add dependency arrows from `--after` papers
5. Add a row to the reading order table
6. Add a row to the quick reference table
7. Write the updated file

### `/reading-guide remove <guide> --paper <N>`
Remove a paper from an existing guide.

**Workflow:**
1. Read the existing guide file
2. Remove the Mermaid node and all arrows pointing to/from it
3. Remove the table rows
4. Re-number remaining papers sequentially
5. Update all arrow references to use new numbers
6. Write the updated file

### `/reading-guide reorder <guide>`
Re-number all papers and re-wire the flowchart after manual edits.

**Workflow:**
1. Read the existing guide file
2. Parse the reading order table to get current sequence
3. Re-assign node IDs (A, B, C...) in table order
4. Rebuild all Mermaid arrows from the "Read After" column
5. Re-apply styles by role
6. Write the updated file

### `/reading-guide list`
Show all reading guides with paper counts.

**Workflow:**
1. Glob for `reading_guide_*.md` at project root
2. For each file, count table rows in "Recommended Reading Order"
3. Display summary

**Output format:**
```
Reading Guides:
  perturbation_methods    10 papers   D1 - Perturbation Prediction
  uq_for_scfms            10 papers   D2 - Uncertainty Quantification
  benchmark_datasets      11 papers   Data and Evaluation
```

### `/reading-guide validate <guide>`
Check a guide for Obsidian Mermaid compatibility violations.

**Checks:**
1. No `\n` or literal newlines inside node labels
2. No special Unicode characters inside labels (no arrows, inequality signs, etc.)
3. No parentheses inside node labels
4. All labels wrapped in `["..."]`
5. No `<br>` tags
6. Labels are short: name/title only
7. Only safe characters: alphanumeric, hyphens, periods, spaces
8. Node IDs are single uppercase letters (A-Z)
9. Style declarations match the number of nodes

**Output:** List of violations with line numbers, or "All clear."

## Obsidian Mermaid Rules — ENFORCED ON EVERY WRITE

These rules are non-negotiable. Every flowchart must pass validation before saving.

1. **Single-line labels only** — no `\n` or literal newlines inside node labels
2. **No special Unicode** — no special characters like arrows or inequality signs. Use ASCII alternatives
3. **No parentheses inside labels** — they conflict with Mermaid node shape syntax
4. **Keep labels short** — name/title only, no metadata like venue or year
5. **Always wrap labels in** `["..."]`
6. **No `<br>` tags** — Obsidian renderer ignores them
7. **Test-safe characters only** — alphanumeric, hyphens, periods, spaces

**Good examples:**
```
A["1. Systema - Evaluation standard"]
B["2. Kendiukhov - Attention is not regulation"]
```

**Bad examples:**
```
A["1. Systema\n(Nat Biotech 2025)\nEvaluation standard"]   <-- multiline
B["2. Kendiukhov - Attention ≠ regulation"]                 <-- Unicode
C["3. scDFM (ICLR 2026)"]                                   <-- parentheses
```

## Role Color Scheme — Standard Across All Guides

| Role | Color | Hex | Use When |
|------|-------|-----|----------|
| Foundation | Red | #e74c3c | Must-read-first papers that frame the field |
| Critique | Orange | #e67e22 | Papers that expose flaws or challenge assumptions |
| Breakthrough | Green | #2ecc71 | Papers that advance the state of the art |
| Baseline | Blue | #3498db | Established methods to compare against |
| Building block | Purple | #9b59b6 | Components to integrate into your method |
| Benchmark | Teal | #1abc9c | Evaluation frameworks and meta-analyses |
| Synthesis | Dark | #34495e | Field-direction papers and convergence nodes |
| Motivation | Red | #e74c3c | Papers proving a problem exists (alias of Foundation) |
| Analogy | Green | #2ecc71 | How other fields solved similar problems (alias of Breakthrough) |
| Regulatory | Teal | #1abc9c | Policy and regulatory documents (alias of Benchmark) |
| Data description | Red | #e74c3c | Dataset papers (alias of Foundation) |
| Infrastructure | Blue | #3498db | Tools and platforms (alias of Baseline) |
| Evaluation critique | Orange | #e67e22 | Papers questioning metrics (alias of Critique) |

## Mermaid Node ID Convention

- Use single uppercase letters: A, B, C, ... Z
- If more than 26 nodes needed, continue with AA, AB, AC...
- Node IDs map to paper numbers: A = paper 1, B = paper 2, etc.
- Special nodes (CONVERGENCE, decision nodes) use descriptive IDs: J, K, START, CONV

## File Naming Convention

All reading guides live at project root:
```
reading_guide_{topic_slug}.md
```

Where `topic_slug` is lowercase, underscores, no spaces:
- `perturbation_methods`
- `uq_for_scfms`
- `benchmark_datasets`

## Integration with Other Skills

- **references.bib**: Every paper in a reading guide should have a matching BibTeX entry
- **Dashboard**: Reading guide completion can be tracked as a dashboard component
- **Notes**: Deep-read notes in `.claude/notes/active/` provide the source material for building guides
- **Dispatch**: A `/dispatch create` plan can include "Build reading guide for X" as a subtask

## Template for New Guide

When creating a new guide, start from this template:

```markdown
# Reading Guide: {Topic Title}

## Reading Dependency Flowchart

MERMAID_OPEN
flowchart TD
    A["1. {Paper} - {Short description}"] --> B["2. {Paper} - {Short description}"]

    style A fill:#e74c3c,color:#fff
    style B fill:#e67e22,color:#fff
MERMAID_CLOSE

**Legend:**
- Red: {Role description}
- Orange: {Role description}

## Recommended Reading Order

| # | Paper | Year | Role | Read After | Why Read This |
|---|-------|------|------|------------|---------------|
| 1 | **{Paper}** ({Authors}, {Venue}) | {Year} | {Role} | -- | {Why} |
| 2 | **{Paper}** ({Authors}, {Venue}) | {Year} | {Role} | 1 | {Why} |

## Quick Reference: What Each Paper Gives You

| Paper | Core Takeaway for Thesis |
|-------|-------------------------|
| {Paper} | {One-sentence takeaway} |
```

Note: Replace MERMAID_OPEN with triple-backtick mermaid and MERMAID_CLOSE with triple-backtick.
