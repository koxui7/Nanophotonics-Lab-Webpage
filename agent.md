# Agent Notes

## Purpose

This repository is intended to be maintainable by future contributors using agent workflows, not only by the original rebuild author.

## Durable Artifact Rules

- do not treat chat alone as the source of truth
- keep research notes in `docs/research/`
- keep approved designs in `docs/specs/`
- keep execution plans in `docs/plans/`
- keep verification-oriented notes in `docs/reviews/`
- keep reusable maintenance guidance inside the repository

## Website Maintenance Rules

- prefer changing `scripts/build_site.py` over directly editing generated files in `site/`
- preserve original lab wording unless explicit approval says otherwise
- treat `docs/research/photonlab-2026-04-15/` as the legacy reference archive
- keep publication additions in descending year order
- run tests after rebuilding

## Open Source Posture

This repository is structured so that its maintenance workflow can be published and reused remotely.

Repo-local guidance should therefore live in versioned files such as:

- `README.md`
- `docs/maintenance.md`
- `skills/photonlab-site-maintenance/SKILL.md`

## Harness Posture

Codex or other agents may dispatch sub-agents for research, implementation, or review, but durable outputs should always be written back into this repository in a way that a later contributor can understand without prior chat history.
