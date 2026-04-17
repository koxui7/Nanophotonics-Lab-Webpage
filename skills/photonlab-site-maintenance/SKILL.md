---
name: photonlab-site-maintenance
description: Use when updating the PhotonLab static website in this repository, especially when changing homepage structure, member layouts, publication data, conference listings, or the site generator.
---

# PhotonLab Site Maintenance

## Overview

This repository maintains the PhotonLab website through a generated static-site workflow.

The core rule is:

- update the generator first
- regenerate the site
- verify with tests

## When To Use

Use this skill when:

- updating `Members`, `Publications`, or `Research`
- fixing homepage layout issues
- adding new journal or conference publications
- changing the generated site structure
- updating the mirrored legacy source workflow

Do not use this skill for unrelated repository administration.

## Source Of Truth

- `scripts/build_site.py` is the main implementation surface
- `docs/research/photonlab-2026-04-15/` preserves the legacy website
- `site/` is generated output

## Content Constraints

- prefer restructure over rewrite
- preserve existing lab wording unless explicit approval says otherwise
- keep publication formatting stylistically consistent with the archived site
- keep publication years in descending order

## Update Workflow

1. inspect the relevant content source
2. edit `scripts/build_site.py`
3. rebuild:

```bash
python3 scripts/build_site.py
```

4. run tests:

```bash
python3 -m unittest discover -s tests -v
```

5. review generated output in `site/`

## Important Data Structures

Inside `scripts/build_site.py`, check these first:

- `ABOUT_ITEMS`
- `RESEARCH_ITEMS`
- `MEMBER_PREVIEW`
- `PUBLICATION_PREVIEW`
- `RECENT_PUBLICATIONS`
- `RECENT_CONFERENCE_PUBLICATIONS`
- `LAB_CSS`

## Common Tasks

### Update homepage featured publications

Edit `PUBLICATION_PREVIEW`.

Do not automatically use the newest papers. This section is curated and should usually feature representative high-impact work.

### Add recent journal papers

Edit `RECENT_PUBLICATIONS` and keep the years in descending order.

### Add recent conference papers

Edit `RECENT_CONFERENCE_PUBLICATIONS` and keep the years in descending order.

### Fix member card overflow

Adjust the member grid and caption rules in `LAB_CSS`.

## Verification

Do not claim the update is complete until:

- the site is rebuilt
- tests pass
- the generated pages look structurally correct
