# Maintenance Guide

## Purpose

This document explains how the rebuilt PhotonLab website is maintained.

## Source Of Truth

The main source of truth for the rebuilt site is:

- `scripts/build_site.py` for generated structure and curated additions
- `docs/research/photonlab-2026-04-15/` for legacy content and wording

The generated HTML in `site/` is an output artifact.

## Key Maintenance Areas

### Homepage

Homepage sections are assembled in `build_home()` inside `scripts/build_site.py`.

The homepage includes:

- laboratory title and intro
- `About Us`
- `Research`
- `Members`
- `Publications`

The homepage publication preview uses `PUBLICATION_PREVIEW`.

### Members

Member preview cards on the homepage use `MEMBER_PREVIEW`.

The full members page is derived from the archived site content and then restyled through CSS overrides embedded in `LAB_CSS`.

If member cards overflow, the first place to check is:

- member grid widths in `LAB_CSS`
- caption font sizing in `LAB_CSS`
- wrapping behavior in `.legacy-archive .caption`

### Publications

Recent journal additions are defined in `RECENT_PUBLICATIONS`.

Recent conference additions are defined in `RECENT_CONFERENCE_PUBLICATIONS`.

Both are injected into the archived publication page through `inject_recent_publications()`.

The conference section is intentionally flattened into one conference block, but the inserted entries are ordered by descending year.

### Styling

Template-level overrides live inside the `LAB_CSS` string in `scripts/build_site.py` and are written out to `site/assets/lab.css`.

Use that layer for:

- layout fixes
- typography fixes
- responsive tuning
- color adjustments

Avoid editing generated CSS in `site/assets/lab.css` directly unless you are debugging and plan to port the change back into `scripts/build_site.py`.

## Safe Update Workflow

1. inspect the relevant source content in `docs/research/`
2. edit `scripts/build_site.py`
3. run `python3 scripts/build_site.py`
4. run `python3 -m unittest discover -s tests -v`
5. review generated output under `site/`

## What To Avoid

- do not rewrite lab copy without explicit approval
- do not manually patch generated HTML as the default workflow
- do not reorder publication years out of descending order
- do not remove archived legacy material from `docs/research/`
