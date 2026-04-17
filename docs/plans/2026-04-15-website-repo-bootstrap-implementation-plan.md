# Website Repo Bootstrap Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Initialize the repository and add the agreed lightweight root rules and documentation scaffold for the research-group website rebuild.

**Architecture:** Keep the repo intentionally small: root guidance files, a `docs/` tree organized by artifact type, and an empty `site/` placeholder for future implementation. Put durable workflow rules into Markdown files so later research, specs, plans, and reviews have stable homes.

**Tech Stack:** Git, Markdown, plain directory structure

---

### Task 1: Initialize the repository

**Files:**
- Create: `.git/` via `git init`

- [ ] **Step 1: Confirm the workspace is not already a git repository**

Run: `git rev-parse --is-inside-work-tree`
Expected: non-zero exit or an error indicating there is no git repository

- [ ] **Step 2: Initialize the repository**

Run: `git init`
Expected: output indicating an empty Git repository was initialized in `/Users/jingweiling/coding/webpage_develop/.git/`

- [ ] **Step 3: Verify the repository now exists**

Run: `git status --short`
Expected: no fatal git error; status output may be empty because tracked files are not yet added

### Task 2: Create the folder scaffold

**Files:**
- Create: `docs/research/`
- Create: `docs/specs/`
- Create: `docs/plans/`
- Create: `docs/reviews/`
- Create: `site/`

- [ ] **Step 1: Create the directories**

Run: `mkdir -p docs/research docs/specs docs/plans docs/reviews site`
Expected: command succeeds with no output

- [ ] **Step 2: Verify the directory layout**

Run: `find . -maxdepth 2 -type d | sort`
Expected: output includes `./docs`, `./docs/research`, `./docs/specs`, `./docs/plans`, `./docs/reviews`, and `./site`

### Task 3: Add root and docs guidance files

**Files:**
- Create: `README.md`
- Create: `agent.md`
- Create: `.gitignore`
- Create: `docs/README.md`
- Create: `docs/research/README.md`
- Modify: `docs/specs/2026-04-15-website-repo-bootstrap-design.md`
- Modify: `docs/plans/2026-04-15-website-repo-bootstrap-implementation-plan.md`
- Create: `docs/specs/README.md`
- Create: `docs/plans/README.md`
- Create: `docs/reviews/README.md`
- Create: `site/.gitkeep`

- [ ] **Step 1: Add the root project README**

Write `README.md` with:

```md
# Research Group Website Rebuild

This repository is the scratch rebuild workspace for a research group website.

## Current Phase

The project is in repository bootstrap and discovery mode. We are setting up rules,
documentation lanes, and a future code surface before choosing a website stack.

## Working Model

- research findings go into `docs/research/`
- approved design decisions go into `docs/specs/`
- implementation plans go into `docs/plans/`
- review and verification notes go into `docs/reviews/`
- website code will live in `site/` once implementation begins

## Directory Guide

- `agent.md`: agent operating rules and sub-agent posture
- `docs/`: durable project artifacts
- `site/`: reserved future website code
```

- [ ] **Step 2: Add the agent operating note**

Write `agent.md` with:

```md
# Agent Notes

## Purpose

This repo uses Codex as the controller inside a single workspace. Work may be split
across sub-agents, but durable outputs must be written back into this repository.

## Core Rules

- do not treat chat alone as the source of truth for durable decisions
- write research notes into `docs/research/`
- write approved designs into `docs/specs/`
- write execution plans into `docs/plans/`
- write reviews, checks, and validation notes into `docs/reviews/`
- prefer spec-first and plan-first execution
- do not choose the frontend stack until discovery on the existing site is done

## Harness Posture

There is no external engineering agent split in this repo. Codex may dispatch
sub-agents for research, implementation, or review, but the repo stays organized by
artifact type instead of permanent agent domains.
```

- [ ] **Step 3: Add the gitignore**

Write `.gitignore` with:

```gitignore
.DS_Store
Thumbs.db
node_modules/
dist/
build/
.vite/
.cache/
coverage/
*.log
```

- [ ] **Step 4: Add the docs index and per-folder README files**

Write `docs/README.md` with:

```md
# Docs Index

Use this folder for durable project artifacts.

- `research/`: observations from the existing site, content inventory, and references
- `specs/`: approved design documents
- `plans/`: implementation plans derived from approved specs
- `reviews/`: review notes, verification notes, and sub-agent summaries
```

Write `docs/research/README.md` with:

```md
# Research Docs

Store discovery notes, existing-site observations, reference captures, and reusable
patterns from other projects here.
```

Write `docs/specs/README.md` with:

```md
# Specs

Store approved design documents and scoped feature specs here.
```

Write `docs/plans/README.md` with:

```md
# Plans

Store implementation plans here. Plans should follow approved specs and be concrete
enough for direct execution.
```

Write `docs/reviews/README.md` with:

```md
# Reviews

Store review notes, verification summaries, and sub-agent check results here.
```

- [ ] **Step 5: Add the site placeholder**

Write `site/.gitkeep` as an empty file.

- [ ] **Step 6: Run git status to confirm the expected new files appear**

Run: `git status --short`
Expected: new files listed for `README.md`, `agent.md`, `.gitignore`, the `docs/` files, and `site/.gitkeep`

### Task 4: Verify the bootstrap state

**Files:**
- Test: repository structure and created Markdown files

- [ ] **Step 1: Review the root and docs structure**

Run: `find . -maxdepth 2 | sort`
Expected: output shows the root files plus `docs/` and `site/`

- [ ] **Step 2: Review the key root files**

Run: `sed -n '1,220p' README.md && printf '\n' && sed -n '1,240p' agent.md && printf '\n' && sed -n '1,220p' docs/README.md`
Expected: file contents match the agreed lightweight workflow

- [ ] **Step 3: Final status check**

Run: `git status --short`
Expected: all newly created files appear as untracked files, ready for the first commit
