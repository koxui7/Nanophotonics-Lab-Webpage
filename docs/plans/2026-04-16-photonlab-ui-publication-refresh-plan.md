# Photon Lab UI and Publication Refresh Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix the current Hyperspace-based site polish issues in `Members` and `Publications`, extend the homepage member preview, and add verified 2024–2025 recent publications for Qiang Lin's group without rewriting existing site text.

**Architecture:** Keep the current build-driven static site workflow centered in `scripts/build_site.py`, so layout fixes and publication updates are regenerated from one source of truth. Apply the user-facing behavior changes through failing structural tests first, then adjust the generator and stylesheet with minimal template overrides.

**Tech Stack:** Static HTML, CSS, JavaScript, Python `unittest`, web verification of publication metadata

---

### Task 1: Lock the new UI and publication expectations into tests

**Files:**
- Modify: `/Users/jingweiling/coding/webpage_develop/tests/test_site_structure.py`

- [ ] **Step 1: Keep failing tests for homepage member preview expansion**

Expected coverage:
- homepage includes `Qiang Lin`
- homepage includes `Austin Graf`
- homepage includes `Jeremy Staffa`
- homepage includes `Raymond Lopez-Rios`
- homepage includes `Shixin Xue`
- homepage includes `Zhengdong Gao`

- [ ] **Step 2: Keep failing tests for member-card resilience**

Expected coverage:
- `site/assets/lab.css` contains the uniform image crop rule
- `site/assets/lab.css` contains `overflow-wrap: anywhere`

- [ ] **Step 3: Keep failing tests for recent publications**

Expected coverage:
- `site/publications.html` contains `data-filter=".2025"`
- `site/publications.html` contains `data-filter=".2024"`
- `site/publications.html` contains the three verified titles:
  - `Electrically empowered microcomb laser`
  - `Pockels laser directly driving ultrafast optical metrology`
  - `Narrow linewidth on-chip III-V/TFLT laser`
- `site/assets/lab.css` contains `.legacy-archive .type a`
- `site/assets/lab.css` contains `display: inline-flex`

### Task 2: Fix the Members layout and homepage preview in the generator

**Files:**
- Modify: `/Users/jingweiling/coding/webpage_develop/scripts/build_site.py`

- [ ] **Step 1: Expand `MEMBER_PREVIEW` from 3 entries to 6 entries**

Use:
- `Qiang Lin`
- `Austin Graf`
- `Jeremy Staffa`
- `Raymond Lopez-Rios`
- `Shixin Xue`
- `Zhengdong Gao`

- [ ] **Step 2: Preserve the full legacy members archive**

Do not remove alumni from the generated `Members` page. The page should continue to render the full mirrored archive from `member.html`.

- [ ] **Step 3: Adjust member-card CSS generation**

Update `LAB_CSS` so that:
- desktop shows denser member tiles than the current 4-column layout
- mid-width layouts fall back to 3 columns
- emails and long lines wrap inside the card instead of overflowing

### Task 3: Repair the Publications year filter layout and inject recent items

**Files:**
- Modify: `/Users/jingweiling/coding/webpage_develop/scripts/build_site.py`

- [ ] **Step 1: Add a structured recent-publications source in the generator**

Store verified metadata for:
- 2024: `Electrically empowered microcomb laser`
- 2025: `Pockels laser directly driving ultrafast optical metrology`
- 2025: `Narrow linewidth on-chip III-V/TFLT laser`

- [ ] **Step 2: Inject new year filters before the older archive years**

Add `2025` and `2024` to the filter list while preserving the existing archive structure.

- [ ] **Step 3: Inject year blocks before the existing 2020 archive section**

Use the same overall publication block style already used by the old site so the added entries match the page’s archive format.

- [ ] **Step 4: Improve filter-chip CSS**

Update `LAB_CSS` so year links:
- wrap cleanly
- do not overlap
- remain easy to click on desktop and mobile

### Task 4: Rebuild, verify, and capture updated previews

**Files:**
- Verify: `/Users/jingweiling/coding/webpage_develop/site/index.html`
- Verify: `/Users/jingweiling/coding/webpage_develop/site/members.html`
- Verify: `/Users/jingweiling/coding/webpage_develop/site/publications.html`

- [ ] **Step 1: Rebuild the site**

Run:
`python3 /Users/jingweiling/coding/webpage_develop/scripts/build_site.py`

- [ ] **Step 2: Run the full site test suite**

Run:
`python3 -m unittest discover -s /Users/jingweiling/coding/webpage_develop/tests -v`

- [ ] **Step 3: Capture visual proof**

Capture updated screenshots for:
- homepage
- members page
- publications page

- [ ] **Step 4: Report evidence and limits**

If no verified 2026 publication can be confirmed from current public sources, state that explicitly instead of inventing a 2026 entry.
