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

    def test_homepage_shows_extended_member_preview(self):
        html = (SITE_ROOT / "index.html").read_text(encoding="utf-8")
        for label in [
            "Qiang Lin",
            "Austin Graf",
            "Jeremy Staffa",
            "Raymond Lopez-Rios",
            "Shixin Xue",
            "Zhengdong Gao",
        ]:
            self.assertIn(label, html)

    def test_homepage_publication_preview_uses_high_citation_representative_works(self):
        html = (SITE_ROOT / "index.html").read_text(encoding="utf-8")
        preview_positions = [
            html.index("Lithium niobate photonic-crystal electro-optic modulator"),
            html.index("Self-starting bi-chromatic LiNbO3 soliton microcomb"),
            html.index("Highly tunable efficient second-harmonic generation in a lithium niobate nanophotonic waveguide"),
            html.index("On-chip second-harmonic generation and broadband parametric down-conversion in a lithium niobate microresonator"),
        ]
        self.assertEqual(preview_positions, sorted(preview_positions))

    def test_homepage_uses_hyperspace_structure_and_intro_image(self):
        html = (SITE_ROOT / "index.html").read_text(encoding="utf-8")
        css = (SITE_ROOT / "assets" / "lab.css").read_text(encoding="utf-8")
        for marker in [
            'body class="is-preload"',
            'section id="sidebar"',
            'section id="intro" class="wrapper style1 fullscreen fade-up',
            'section id="research" class="wrapper style2 spotlights"',
            'section id="about-us" class="wrapper style3 fade-up"',
            "assets/css/main.css",
            "assets/js/main.js",
        ]:
            self.assertIn(marker, html)
        self.assertIn("../images/image.png", css)
        self.assertTrue((SITE_ROOT / "images" / "image.png").exists())

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

    def test_members_and_publications_pages_have_archive_structure(self):
        members_html = (SITE_ROOT / "members.html").read_text(encoding="utf-8")
        publications_html = (SITE_ROOT / "publications.html").read_text(encoding="utf-8")
        self.assertIn("Qiang Lin", members_html)
        self.assertIn("Publications", publications_html)
        self.assertTrue(any(year in publications_html for year in ["2020", "2019", "2018"]))

    def test_member_images_are_cropped_to_a_uniform_frame(self):
        css = (SITE_ROOT / "assets" / "lab.css").read_text(encoding="utf-8")
        self.assertIn(".legacy-archive .thumbnail img", css)
        self.assertIn("aspect-ratio: 1 / 1", css)
        self.assertIn("object-fit: cover", css)
        self.assertIn(".legacy-archive .row {\n  display: flex;", css)
        self.assertIn('[class*="col-md-3"]', css)
        self.assertIn("overflow-wrap: anywhere", css)
        self.assertIn("font-size: 0.88em", css)
        self.assertIn(".legacy-archive .caption h3", css)
        self.assertIn("min-width: 0", css)

    def test_publications_page_includes_recent_years_and_titles(self):
        html = (SITE_ROOT / "publications.html").read_text(encoding="utf-8")
        css = (SITE_ROOT / "assets" / "lab.css").read_text(encoding="utf-8")
        for label in [
            'data-filter=".2025"',
            'data-filter=".2024"',
            'data-filter=".2023"',
            'data-filter=".2022"',
            'data-filter=".2021"',
            "Electrically empowered microcomb laser",
            "Pockels laser directly driving ultrafast optical metrology",
            "Narrow linewidth on-chip III-V/TFLT laser",
            "High-speed tunable microwave-rate soliton microcomb",
            "Integrated Pockels laser",
            "Ultrabroadband Entangled Photons on a Nanophotonic Chip",
            "On-chip InP/LiNbO3 microcomb laser",
            "Broadband soliton microcomb laser",
            "Integrated DBR-based Pockels Laser",
            "Integrated III-V/Lithium Niobate Nonlinear Laser",
            "An efficient nanophotonic source of ultra-broadband entangled photons",
        ]:
            self.assertIn(label, html)
        self.assertIn(".legacy-archive .type a", css)
        self.assertIn("display: inline-flex", css)

    def test_publications_and_conference_entries_follow_descending_year_order(self):
        html = (SITE_ROOT / "publications.html").read_text(encoding="utf-8")

        filter_positions = [
            html.index('data-filter=".2025"'),
            html.index('data-filter=".2024"'),
            html.index('data-filter=".2023"'),
            html.index('data-filter=".2022"'),
            html.index('data-filter=".2021"'),
            html.index('data-filter=".2020"'),
        ]
        self.assertEqual(filter_positions, sorted(filter_positions))

        conference_positions = [
            html.index("Pockels Laser For Driving Ultrafast Optical Metrology"),
            html.index("On-chip InP/LiNbO3 microcomb laser"),
            html.index("Integrated DBR-based Pockels Laser"),
            html.index("Integrated III-V/Lithium Niobate Nonlinear Laser"),
            html.index("An efficient nanophotonic source of ultra-broadband entangled photons"),
        ]
        self.assertEqual(conference_positions, sorted(conference_positions))


if __name__ == "__main__":
    unittest.main()
