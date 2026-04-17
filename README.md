# PhotonLab Website Rebuild

This repository contains two static website options for the Laboratory for Nanophotonics.

The repository is designed for agent-assisted maintenance and open-source collaboration. Future contributors should be able to clone the repo, regenerate both site options locally, understand where the content comes from, and update the site without relying on prior chat history.

## Current Site Options

- `site1/`: the primary `Hyperspace`-based version
- `site2/`: the alternative `Editorial`-based version

Both versions use the same content set. The difference between them is presentation, layout, and template structure rather than wording.

## Repository Layout

- `site1/`: generated static output for option 1
- `site2/`: generated static output for option 2
- `scripts/build_site.py`: main generator for both site options
- `scripts/mirror_site.py`: crawler used to mirror the legacy site
- `vendor/html5up-editorial/`: vendored `Editorial` template assets used by `site2`
- `tests/`: regression tests for the crawler and generated sites
- `docs/research/`: archived copy of the legacy website and research notes
- `docs/plans/`: implementation plans used during the rebuild
- `docs/maintenance.md`: maintainer-oriented update guide
- `skills/photonlab-site-maintenance/`: repo-local maintenance skill for future agents and contributors
- `agent.md`: repo-level operating notes
- `CONTRIBUTING.md`: branch, PR, and collaboration rules for open-source contributors

## How The Repo Works

The intended workflow is generator-first, not hand-edit-first.

That means:

1. change structured content or generation logic in `scripts/build_site.py`
2. rebuild both site options
3. run tests
4. review generated output in `site1/` and `site2/`

In normal maintenance, do not start by editing generated HTML directly.

## Build Command

Generate both options:

```bash
python3 scripts/build_site.py
```

After running that command:

- `site1/` is regenerated as the `Hyperspace` option
- `site2/` is regenerated as the `Editorial` option

## Test Commands

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

## Where To Make Changes

Most important maintenance logic lives in `scripts/build_site.py`.

Key areas inside that file:

- `ABOUT_ITEMS`
- `RESEARCH_ITEMS`
- `MEMBER_PREVIEW`
- `PUBLICATION_PREVIEW`
- `RECENT_PUBLICATIONS`
- `RECENT_CONFERENCE_PUBLICATIONS`
- `LAB_CSS` for the `site1` styling layer
- `EDITORIAL_LAB_CSS` for the `site2` styling layer

If you need to update homepage structure, member previews, publication data, conference additions, or layout overrides, this is the first file to inspect.

## Content Rules

- prefer `restructure`, not `rewrite`
- preserve existing lab wording unless explicit approval says otherwise
- layout, grouping, navigation, and formatting changes are allowed
- publication additions are allowed when they preserve the existing citation style
- conference additions should remain in descending year order
- the homepage `Publications` preview is curated and should not automatically become "the latest 3 papers"

## Publications Model

There are two publication surfaces:

1. homepage `Publications` preview
2. full `Publications` archive page

The homepage preview is intentionally selective and should contain representative, high-impact papers.

The full publication archive combines:

- legacy archived publications from the mirrored site
- newer journal entries from `RECENT_PUBLICATIONS`
- newer conference entries from `RECENT_CONFERENCE_PUBLICATIONS`

When updating publications:

1. edit the data structures in `scripts/build_site.py`
2. keep years in descending order
3. rebuild both site options
4. run tests

## Legacy Source Material

The mirrored legacy website is stored under:

`docs/research/photonlab-2026-04-15/`

Use that archive as the reference source for:

- original wording
- original member details
- original publication archive
- original research text and images

## Suggested Update Workflow

For most future changes:

1. inspect the relevant legacy content in `docs/research/`
2. edit `scripts/build_site.py`
3. run `python3 scripts/build_site.py`
4. run `python3 -m unittest discover -s tests -v`
5. compare `site1/` and `site2/`
6. commit the generator, generated output, and any related docs together

## Collaboration Model

This repository is intended to be open for lab collaborators, but not as a free-for-all on the mainline branches.

- `main` and `master` are treated as protected branches
- contributors should create and push their own working branches
- changes should flow back through pull requests
- contributors should not push changes onto somebody else's branch unless they have that person's explicit permission
- recommended branch format: `yourname/topic`

See `CONTRIBUTING.md` for the expected branch naming and collaboration policy.

## Notes For Future Agents

If you are maintaining this repo through an agent workflow, start with:

- `README.md`
- `docs/maintenance.md`
- `skills/photonlab-site-maintenance/SKILL.md`

These files define the intended maintenance model for this open-source repository.
