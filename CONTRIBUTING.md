# Contributing

This repository is open for collaborative maintenance of the Laboratory for Nanophotonics website rebuild.

The goal is to let many contributors contribute, while keeping the official upstream repository under a single maintainer-controlled review flow.

## Upstream Workflow

- `main` is the only protected integration branch.
- Do not push directly to `main`.
- The official upstream repository is intended to be merged by the maintainer only.
- External contributors should normally work from personal forks, not from direct write access on the upstream repository.
- Do not push commits onto somebody else's branch unless they explicitly asked you to help there.

Recommended branch naming in your fork:

- `yourname/feature-name`
- `yourname/publication-update-2026`
- `yourname/site2-ui-fix`

Examples:

- `alice/publications-2025-refresh`
- `bob/member-photo-cleanup`

## Expected Workflow

1. Fork the repository.
2. Pull the latest `main` from upstream.
3. Create your own branch in your fork.
4. Make changes locally.
5. Regenerate the site outputs if you changed generator logic.
6. Run tests.
7. Open a pull request into upstream `main`.

Typical command flow:

```bash
git remote add upstream git@github.com:koxui7/Nanophotonics-Lab-Webpage.git
git fetch upstream
git checkout main
git pull upstream main
git checkout -b yourname/short-change-name
python3 scripts/build_site.py
python3 -m unittest discover -s tests -v
git status
git add .
git commit -m "Describe the change"
git push -u origin yourname/short-change-name
```

## What To Edit

Most maintenance should start in:

- `scripts/build_site.py`
- `README.md`
- `docs/maintenance.md`

Generated site output lives in:

- `site1/`
- `site2/`

If you change the generator, commit the generated output together with the generator change.

## Content Rules

- Prefer restructuring over rewriting.
- Preserve existing lab wording unless content changes were explicitly approved.
- Publication additions should match the existing citation style.
- Publication years should stay in descending order.
- Conference entries should also stay in descending order.

## Collaboration Norms

- Respect branch ownership.
- Use pull requests for discussion and review.
- Keep commits focused and explain what changed.
- If you want to help on another contributor's branch, ask first and wait for explicit approval.
- Do not assume upstream write access.
- Upstream merge decisions are made by the maintainer after review.

## Maintainer Notes

GitHub branch protection is used on `main`, together with `CODEOWNERS`, so that the maintainer's review is part of the merge process.

The "do not modify someone else's branch without permission" rule is a repository policy and collaboration norm. The cleanest way to preserve that rule is to contribute through personal forks instead of shared upstream feature branches.
