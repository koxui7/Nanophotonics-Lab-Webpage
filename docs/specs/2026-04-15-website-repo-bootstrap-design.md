# Website Repo Bootstrap Design

## Context

This repository will host a rebuilt research group website starting from scratch.
The current phase is not website implementation yet. The immediate goal is to create
a lightweight but durable repository structure that supports:

- future research on the existing website
- spec-first planning
- plan-first execution
- Codex-controlled sub-agent dispatch inside this same repo

Unlike the game repo at `/Users/jingweiling/coding/game/hello_game`, this repo will
not use a split between Codex planning and an external engineering agent. The repo
should still borrow the useful workflow habits from that project, but in a much more
minimal form suitable for a small website rebuild.

## Goals

- Create a clean repo root that is easy to understand.
- Preserve a clear path from research to spec to execution.
- Support future sub-agent work without introducing heavy governance overhead.
- Avoid locking the project into a frontend stack before the existing site has been reviewed.

## Non-Goals

- Do not scaffold the website frontend yet.
- Do not choose a deployment platform yet.
- Do not introduce heavy mirrored governance like separate planning and engineering domains.
- Do not create a complex branch, ownership, or review system at bootstrap time.

## Chosen Approach

The repo will use a minimal structured layout:

- `README.md` as the human-facing project entry
- `agent.md` as the agent-facing operating note
- `docs/` for durable written artifacts
- `site/` as an empty placeholder for future website code
- `.gitignore` for local artifact hygiene

Within `docs/`, the repo will separate research, specs, plans, and reviews so later
work has obvious destinations without needing a larger governance layer.

## Alternatives Considered

### 1. Ultra-minimal layout

Use only a root README plus a generic docs folder and maybe a site folder.

Why not chosen:
This is fast, but it would make later research, specs, execution notes, and reviews
mix together too easily. The project would likely need early cleanup once the rebuild
starts.

### 2. Minimal structured layout

Use a small number of stable folders with clear responsibilities.

Why chosen:
This gives enough structure for spec-first work and sub-agent execution while staying
lightweight. It matches the project size and the user's preference for a simple setup.

### 3. Game-lite mirrored governance

Adapt the game repo pattern into smaller `governance/`, `planning/`, `engineering/`,
and `subprojects/` areas.

Why not chosen:
It would import too much process too early for a website project that has not yet
entered implementation.

## Directory Design

### Root

- `README.md`
  Explains project purpose, current stage, directory guide, and recommended workflow.
- `agent.md`
  Defines the lightweight operating rules for Codex and any sub-agents working in this repo.
- `.gitignore`
  Prevents common local clutter from entering the repo.

### Documentation

- `docs/README.md`
  Index for all project documentation.
- `docs/research/`
  Notes from reviewing the current live or legacy website, content inventory, references,
  and reusable ideas from other repos.
- `docs/specs/`
  Approved design documents and scoped feature or architecture specs.
- `docs/plans/`
  Execution plans derived from approved specs.
- `docs/reviews/`
  Review notes, checkpoints, and sub-agent summaries.

Each docs subdirectory should contain a short `README.md` that explains what belongs
there and what does not.

### Future Code Area

- `site/`
  Reserved for future website implementation. It remains empty except for a placeholder
  file so the folder exists in version control.

## Operating Rules

The repo bootstrap should encode a few strong rules without adding heavy ceremony:

- durable decisions belong in repo docs, not only in chat
- research should precede implementation decisions
- specs should precede execution plans
- execution plans should precede implementation
- sub-agents may help with research, execution, or review, but their outputs should be
  written back into the repo

These rules will live in lightweight form inside `README.md`, `agent.md`, and the docs
index files rather than in a large governance tree.

## Sub-Agent Harness Posture

This repo will use Codex as the controller inside the same workspace. Sub-agents are
allowed, but they do not own separate permanent domains like planning versus engineering.

Instead, work is organized by artifact type:

- research outputs go to `docs/research/`
- design outputs go to `docs/specs/`
- execution plans go to `docs/plans/`
- reviews and verification notes go to `docs/reviews/`

This keeps the harness practical and visible without importing the more complex model
used in the game repo.

## Initial Files To Create After Approval

- `README.md`
- `agent.md`
- `.gitignore`
- `docs/README.md`
- `docs/research/README.md`
- `docs/specs/README.md`
- `docs/plans/README.md`
- `docs/reviews/README.md`
- `site/.gitkeep`

## Success Criteria

The bootstrap is successful when:

- a new collaborator can understand the repo by reading the root docs
- future website discovery work has a clear place to live
- future implementation planning has a clear place to live
- the repo can support Codex-directed sub-agent work without extra restructuring
- no website framework decision has been forced prematurely

## Risks And Mitigations

- Risk: the structure may feel too light once implementation starts
  Mitigation: the chosen layout is intentionally extensible; additional structure can be
  added later under `docs/` or by introducing more focused agent docs only when needed.

- Risk: decisions may still drift into chat instead of repo artifacts
  Mitigation: `agent.md` and the root README should explicitly direct durable decisions
  into specs, plans, research notes, and reviews.

- Risk: `site/` stays undefined for too long
  Mitigation: that is acceptable at bootstrap time; the folder exists to reserve the
  future implementation surface without constraining stack choice now.
