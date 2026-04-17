# PhotonLab Website Rebuild

This repository contains the rebuilt static website for the Laboratory for Nanophotonics.

It is designed for agent-assisted maintenance: the generated site lives in `site/`, the site is rebuilt from a Python generator in `scripts/`, and the original website snapshot plus planning documents live in `docs/`.

## Repository Layout

- `site/`: generated static website output
- `scripts/build_site.py`: main build entrypoint for regenerating the website
- `scripts/mirror_site.py`: crawler used to mirror the legacy site for reference
- `tests/`: regression tests for the crawler and the generated site structure
- `docs/research/`: archived copy of the legacy website and research notes
- `docs/plans/`: implementation plans used during the rebuild
- `skills/photonlab-site-maintenance/`: repo-local maintenance skill for future contributors and agents
- `agent.md`: repo-level operating notes for agent-based maintenance

## How The Site Works

The repo does not edit the generated HTML by hand as the primary workflow.

The intended maintenance loop is:

1. update the structured content or generation logic in `scripts/build_site.py`
2. rebuild the site into `site/`
3. run the test suite in `tests/`
4. review the generated pages in `site/`

Most important logic lives in `scripts/build_site.py`:

- homepage structure
- member preview entries
- publication preview entries on the homepage
- recent journal publication additions
- recent conference publication additions
- CSS overrides layered on top of the HTML5 UP template

## Rebuild Commands

Rebuild the site:

```bash
python3 scripts/build_site.py
```

Run all tests:

```bash
python3 -m unittest discover -s tests -v
```

Run only structure tests:

```bash
python3 -m unittest tests/test_site_structure.py -v
```

Run only crawler tests:

```bash
python3 -m unittest tests/test_mirror_site.py -v
```

## Content Rules

- Prefer `restructure`, not `rewrite`
- Do not change existing lab wording unless explicitly approved
- Layout, grouping, navigation, and formatting changes are allowed
- Publication updates are allowed when they preserve the existing citation style
- Conference additions should be appended in descending year order

## Updating Publications

There are two different publication surfaces:

1. homepage `Publications` preview
2. full `Publications` archive page

The homepage preview is intentionally curated and should contain representative, high-impact papers rather than simply the most recent ones.

The full archive page combines:

- legacy archived publications from the mirrored website
- newer journal publications defined in `RECENT_PUBLICATIONS`
- newer conference items defined in `RECENT_CONFERENCE_PUBLICATIONS`

When updating publications:

1. edit the publication data structures in `scripts/build_site.py`
2. keep years in descending order
3. rebuild
4. run tests

## Legacy Source Material

The mirrored legacy website is stored under:

`docs/research/photonlab-2026-04-15/`

This is the reference source for:

- original wording
- original member details
- original publication archive
- original research text and images

## Contributor Note

This repository is meant to be usable by future maintainers, not only the original author of this rebuild. If you are updating the site through an agent workflow, start with the repo skill in `skills/photonlab-site-maintenance/SKILL.md` and then work through `scripts/build_site.py` rather than patching generated pages directly unless there is a specific reason.
