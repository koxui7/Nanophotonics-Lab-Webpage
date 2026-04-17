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
