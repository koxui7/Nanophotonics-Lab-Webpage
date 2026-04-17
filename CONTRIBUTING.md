# Contributing

This repository is open for collaborative maintenance of the Laboratory for Nanophotonics website rebuild.

The goal is to let many contributors work in parallel without turning the repository into a free-for-all.

## Branch Policy

- `main` is a protected integration branch.
- `master` is also protected for compatibility with older workflows.
- Do not push directly to `main` or `master`.
- Create your own working branch for every change.
- Do not push commits onto somebody else's branch unless they explicitly asked you to help there.

Recommended branch naming:

- `yourname/feature-name`
- `yourname/publication-update-2026`
- `yourname/site2-ui-fix`

Examples:

- `alice/publications-2025-refresh`
- `bob/member-photo-cleanup`

## Expected Workflow

1. Pull the latest protected branch.
2. Create your own branch.
3. Make changes locally.
4. Regenerate the site outputs if you changed generator logic.
5. Run tests.
6. Open a pull request into `main`.

Typical command flow:

```bash
git checkout main
git pull origin main
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

## Maintainer Notes

GitHub branch protection can enforce the protected status of `main` and `master`.

The "do not modify someone else's branch without permission" rule is a repository policy and collaboration norm. Contributors are expected to follow it even though GitHub does not automatically infer personal ownership for every non-protected branch.
