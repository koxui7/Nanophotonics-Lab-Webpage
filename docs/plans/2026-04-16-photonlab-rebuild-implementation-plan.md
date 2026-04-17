# Photon Lab Rebuild Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the first functional version of the new Photon Lab website as a static multi-page site that preserves existing content text while restructuring the information architecture and visual presentation.

**Architecture:** Implement the site in plain static HTML, CSS, and light JavaScript under `site/` so the rebuild stays close to the original content source and remains easy to host anywhere. Use one shared stylesheet and one shared script for navigation behavior, with separate HTML pages for `Home`, `Research`, `Members`, `Publications`, and the four research detail pages.

**Tech Stack:** Static HTML, CSS, JavaScript, Python `unittest` for structural checks

---

### Task 1: Add structural tests for the rebuilt site

**Files:**
- Create: `tests/test_site_structure.py`

- [ ] **Step 1: Write the failing test for required page files**

```python
from pathlib import Path
import unittest


SITE_ROOT = Path("/Users/jingweiling/coding/webpage_develop/site")


class SiteStructureTests(unittest.TestCase):
    def test_required_pages_exist(self):
        required = [
            SITE_ROOT / "index.html",
            SITE_ROOT / "research.html",
            SITE_ROOT / "members.html",
            SITE_ROOT / "publications.html",
            SITE_ROOT / "research" / "integrated-quantum-photonics.html",
            SITE_ROOT / "research" / "integrated-nonlinear-photonics.html",
            SITE_ROOT / "research" / "ln-sic-photonics.html",
            SITE_ROOT / "research" / "integrated-photonic-sensing.html",
        ]
        missing = [str(path) for path in required if not path.exists()]
        self.assertEqual(missing, [])
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_site_structure.SiteStructureTests.test_required_pages_exist -v`
Expected: FAIL because the new page files do not exist yet

- [ ] **Step 3: Extend the failing test to validate shared navigation labels**

```python
    def test_main_pages_share_primary_navigation(self):
        required_labels = ["Home", "About Us", "Research", "Members", "Publications"]
        pages = [
            SITE_ROOT / "index.html",
            SITE_ROOT / "research.html",
            SITE_ROOT / "members.html",
            SITE_ROOT / "publications.html",
        ]
        for page in pages:
            html = page.read_text(encoding="utf-8")
            for label in required_labels:
                self.assertIn(label, html, f"{label} missing from {page}")
```

- [ ] **Step 4: Run test to verify it fails**

Run: `python3 -m unittest tests.test_site_structure.SiteStructureTests.test_main_pages_share_primary_navigation -v`
Expected: FAIL because the new page files do not exist yet

### Task 2: Scaffold the shared site shell

**Files:**
- Create: `site/index.html`
- Create: `site/research.html`
- Create: `site/members.html`
- Create: `site/publications.html`
- Create: `site/research/integrated-quantum-photonics.html`
- Create: `site/research/integrated-nonlinear-photonics.html`
- Create: `site/research/ln-sic-photonics.html`
- Create: `site/research/integrated-photonic-sensing.html`
- Create: `site/assets/styles.css`
- Create: `site/assets/main.js`

- [ ] **Step 1: Create the page files and asset directories**

Run: `mkdir -p site/assets site/research`
Expected: command succeeds with no output

- [ ] **Step 2: Add the minimal HTML shell for `index.html`**

Write `site/index.html` with:

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Laboratory for Nanophotonics</title>
    <link rel="stylesheet" href="assets/styles.css" />
    <script src="assets/main.js" defer></script>
  </head>
  <body>
    <header class="site-header">
      <a class="site-mark" href="index.html">Laboratory for Nanophotonics</a>
      <nav class="site-nav" aria-label="Primary">
        <a href="index.html">Home</a>
        <a href="index.html#about-us">About Us</a>
        <a href="research.html">Research</a>
        <a href="members.html">Members</a>
        <a href="publications.html">Publications</a>
      </nav>
    </header>
    <main>
      <section class="page-introduction">
        <p class="eyebrow">Laboratory for Nanophotonics</p>
        <h1>Quantum, Nonlinear and Mechanical Photonics</h1>
      </section>
    </main>
  </body>
</html>
```

- [ ] **Step 3: Add minimal placeholder shells for the remaining main pages**

Write `site/research.html`, `site/members.html`, and `site/publications.html` using the same header and asset links, with `<h1>` titles of `Research`, `Members`, and `Publications`.

- [ ] **Step 4: Add minimal placeholder shells for the four research detail pages**

Write the four files under `site/research/` with the same navigation, but use `../assets/styles.css`, `../assets/main.js`, and `../index.html` style relative links.

- [ ] **Step 5: Add the base stylesheet**

Write `site/assets/styles.css` with:

```css
:root {
  --background: #f5f3ed;
  --surface: #fffdf8;
  --ink: #151515;
  --muted: #57534e;
  --line: #ded6c7;
  --accent: #0f3d63;
  --accent-soft: #d9e7f2;
  --max-width: 1180px;
}

* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: Georgia, "Times New Roman", serif;
  color: var(--ink);
  background: var(--background);
}

.site-header,
main {
  width: min(calc(100% - 48px), var(--max-width));
  margin: 0 auto;
}

.site-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 24px;
  padding: 24px 0;
  border-bottom: 1px solid var(--line);
}

.site-nav {
  display: flex;
  flex-wrap: wrap;
  gap: 18px;
}

.site-mark,
.site-nav a {
  color: var(--ink);
  text-decoration: none;
}

.page-introduction {
  padding: 72px 0;
}

.eyebrow {
  margin: 0 0 12px;
  font-size: 0.8rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
}
```

- [ ] **Step 6: Add the base script**

Write `site/assets/main.js` with:

```js
document.documentElement.classList.add("js");
```

- [ ] **Step 7: Run the structural tests**

Run: `python3 -m unittest tests.test_site_structure -v`
Expected: PASS for page existence and shared navigation

### Task 3: Implement the homepage structure with preserved source text

**Files:**
- Modify: `site/index.html`
- Test: `tests/test_site_structure.py`

- [ ] **Step 1: Write the failing test for homepage sections**

Add to `tests/test_site_structure.py`:

```python
    def test_homepage_contains_primary_sections(self):
        html = (SITE_ROOT / "index.html").read_text(encoding="utf-8")
        for label in [
            "Laboratory for Nanophotonics",
            "About Us",
            "Who We Are",
            "What We Do",
            "Why Choose Us",
            "Research",
            "Members",
            "Publications",
        ]:
            self.assertIn(label, html)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_site_structure.SiteStructureTests.test_homepage_contains_primary_sections -v`
Expected: FAIL because the homepage shell does not yet include all required sections

- [ ] **Step 3: Implement the homepage sections using existing text**

Update `site/index.html` so it includes:
- the existing laboratory title and subtitle
- the `About Us` section with the exact `Who We Are`, `What We Do`, and `Why Choose Us` text from the mirrored homepage
- the `Research` section with the four existing research titles and short descriptions from the mirrored homepage
- a reduced `Members` overview that links to `members.html`
- a reduced `Publications` overview that links to `publications.html`

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_site_structure.SiteStructureTests.test_homepage_contains_primary_sections -v`
Expected: PASS

### Task 4: Implement the `Research` overview and research detail pages

**Files:**
- Modify: `site/research.html`
- Modify: `site/research/integrated-quantum-photonics.html`
- Modify: `site/research/integrated-nonlinear-photonics.html`
- Modify: `site/research/ln-sic-photonics.html`
- Modify: `site/research/integrated-photonic-sensing.html`
- Test: `tests/test_site_structure.py`

- [ ] **Step 1: Write the failing test for research page titles**

Add to `tests/test_site_structure.py`:

```python
    def test_research_pages_preserve_original_titles(self):
        expectations = {
            SITE_ROOT / "research.html": ["Research"],
            SITE_ROOT / "research" / "integrated-quantum-photonics.html": ["Integrated Quantum Photonics"],
            SITE_ROOT / "research" / "integrated-nonlinear-photonics.html": ["Integrated Nonlinear Photonics"],
            SITE_ROOT / "research" / "ln-sic-photonics.html": ["LN&SiC", "Photonics"],
            SITE_ROOT / "research" / "integrated-photonic-sensing.html": ["Integrated Photonic Sensing"],
        }
        for path, labels in expectations.items():
            html = path.read_text(encoding="utf-8")
            for label in labels:
                self.assertIn(label, html, f"{label} missing from {path}")
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_site_structure.SiteStructureTests.test_research_pages_preserve_original_titles -v`
Expected: FAIL because the detail pages are placeholders

- [ ] **Step 3: Populate `site/research.html` with the four research entries**

Use the existing research titles and introductory summaries from the mirrored homepage. Add four linked entries that route to the detail pages.

- [ ] **Step 4: Populate the four research detail pages with preserved source text**

For each research detail page, move over the title, source text, and any figure captions from the corresponding mirrored HTML page without rewriting the wording.

- [ ] **Step 5: Run test to verify it passes**

Run: `python3 -m unittest tests.test_site_structure.SiteStructureTests.test_research_pages_preserve_original_titles -v`
Expected: PASS

### Task 5: Implement `Members` and `Publications` as separate archive pages

**Files:**
- Modify: `site/members.html`
- Modify: `site/publications.html`
- Test: `tests/test_site_structure.py`

- [ ] **Step 1: Write the failing test for members and publications content anchors**

Add to `tests/test_site_structure.py`:

```python
    def test_members_and_publications_pages_have_archive_structure(self):
        members_html = (SITE_ROOT / "members.html").read_text(encoding="utf-8")
        publications_html = (SITE_ROOT / "publications.html").read_text(encoding="utf-8")
        self.assertIn("Qiang Lin", members_html)
        self.assertIn("Publications", publications_html)
        self.assertTrue(any(year in publications_html for year in ["2023", "2022", "2021"]))
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_site_structure.SiteStructureTests.test_members_and_publications_pages_have_archive_structure -v`
Expected: FAIL because the pages are still placeholders

- [ ] **Step 3: Populate `site/members.html` with preserved member entries**

Move the member entries from the mirrored source into a full-page list. Keep names, roles, education lines, office lines, and email lines unchanged.

- [ ] **Step 4: Populate `site/publications.html` with preserved publication archive content**

Move the publication archive into the dedicated page, keeping the existing year grouping and entry wording unchanged.

- [ ] **Step 5: Run test to verify it passes**

Run: `python3 -m unittest tests.test_site_structure.SiteStructureTests.test_members_and_publications_pages_have_archive_structure -v`
Expected: PASS

### Task 6: Refine the visual system toward the approved direction

**Files:**
- Modify: `site/assets/styles.css`
- Modify: `site/assets/main.js`

- [ ] **Step 1: Expand the stylesheet with the approved visual direction**

Refine the shared stylesheet so the site feels like a restrained `Hyperspace` structure with `Editorial` tone:
- calm background and surface treatment
- strong typography hierarchy
- clear section spacing
- image blocks that support research entries without making the site feel like a product landing page
- mobile-safe navigation and page spacing

- [ ] **Step 2: Add minimal JavaScript only where the structure needs it**

Use `site/assets/main.js` only for small navigation or disclosure behavior. Do not add decorative motion.

- [ ] **Step 3: Verify the structural tests still pass**

Run: `python3 -m unittest tests.test_site_structure -v`
Expected: PASS

### Task 7: Final verification

**Files:**
- Test: `tests/test_site_structure.py`
- Test: static HTML output under `site/`

- [ ] **Step 1: Run the full Python test suite**

Run: `python3 -m unittest -v`
Expected: PASS for both crawler tests and site structure tests

- [ ] **Step 2: Review the new site tree**

Run: `find site -maxdepth 3 | sort`
Expected: output shows the main pages, the four research detail pages, and shared assets

- [ ] **Step 3: Spot-check the generated pages**

Run: `sed -n '1,220p' site/index.html && printf '\n' && sed -n '1,220p' site/publications.html`
Expected: the pages show preserved content text inside the new structure
