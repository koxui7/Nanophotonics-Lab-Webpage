from __future__ import annotations

from pathlib import Path
import shutil


PROJECT_ROOT = Path("/Users/jingweiling/coding/webpage_develop")
SOURCE_ROOT = PROJECT_ROOT / "docs/research/photonlab-2026-04-15/photonlab.hajim.rochester.edu"
SITE1_ROOT = PROJECT_ROOT / "site1"
SITE2_ROOT = PROJECT_ROOT / "site2"
TEMPLATE_ORIGIN = "https://html5up.net/uploads/demos/hyperspace"
EDITORIAL_VENDOR_ROOT = PROJECT_ROOT / "vendor/html5up-editorial"

INTRO_IMAGE_SOURCE = Path("/Users/jingweiling/Downloads/image.png")
INTRO_IMAGE_TARGET = SITE1_ROOT / "images" / "image.png"


ABOUT_ITEMS = [
    (
        "Who We Are",
        "We are an energetic and synergistic team of scholars with strong curiosity and passion for micro/nanophotonic technology. We come from very different backgrounds in physics, optics, photonics, electrical engineering, and others. But we share a common interest in using our creativity and combining our expertise to explore new physics and to develop new applications via engineered micro/nanoscopic photonic structures.",
    ),
    (
        "What We Do",
        "Our research focuses primarily on understanding the fundamental physics of novel nonlinear optical, quantum optical, and optomechanical phenomena in micro-/nanoscopic photonic structures, and on finding their potential applications towards chip-scale photonic signal processing, sensing, and wavefront  engineering, in both classical and quantum regimes.",
    ),
    (
        "Why Choose Us",
        "Here, you will find a fun playground for both experimentalists and theoreticians to explore new phenomena, physics, and applications, where your imagination may thrive and where your knowledge, experience, and intuition will have important impacts. Here, you will have great opportunities in exploring the forefront of scientific research and in conquering scientific and engineering challenges, in a friendly and constructive environment, working together with people from diverse backgrounds.",
    ),
]


RESEARCH_ITEMS = [
    {
        "title": "Integrated Quantum Photonics",
        "href": "research/integrated-quantum-photonics.html",
        "image": "images/index_research/inte.jpg",
        "summary": "Advance of quantum optical science in the past few decades has now come to the engineering era of real practical application, which has been witnessed in recent years in the areas of secure communication, metrology, sensing, and potentially future advanced computing.",
        "source": "research1.html",
    },
    {
        "title": "Integrated Nonlinear Photonics",
        "href": "research/integrated-nonlinear-photonics.html",
        "image": "images/index_research/comb.jpg",
        "summary": "Nonlinear optical processes have attracted long-lasting interest ever since the first observation of second-harmonic generation, which have found very broad application ranging from photonic signal processing, tunable coherent radiation, frequency metrology, optical microscopy, to quantum information processing.",
        "source": "research2.html",
    },
    {
        "title": "LN&SiC Photonics",
        "href": "research/ln-sic-photonics.html",
        "image": "images/index_research/ln.jpg",
        "summary": "Functionalities of nanophotonic devices/circuits rely crucially on the properties of underlying device materials. We explore new material platforms with outstanding characteristics (electrical, optical, mechanical, thermal, etc.) for diverse applications, with current specific focus on lithium niobate and silicon carbide.",
        "source": "research3.html",
    },
    {
        "title": "Integrated Photonic Sensing",
        "href": "research/integrated-photonic-sensing.html",
        "image": "images/index_research/sensor.jpg",
        "summary": "Integrated photonic platforms are ideal for sensing application. On one hand, a variety of physical mechanisms can be flexibly implemented and integrated for diverse and multi-modal sensing applications.",
        "source": "research4.html",
    },
]


MEMBER_PREVIEW = [
    {
        "name": "Qiang Lin",
        "lines": [
            "Professor, Electrical and Computer Engineering",
            "Professor, Optics",
            "Office: 721 CSB",
            "Email: qiang.lin@rochester.edu",
        ],
    },
    {
        "name": "Austin Graf",
        "lines": [
            "Graduate Student",
            "B.S., University of Illinois Urbana-Champaign, 2016",
            "Office: 626 CSB",
            "Email: agraf@ur.rochester.edu",
        ],
    },
    {
        "name": "Jeremy Staffa",
        "lines": [
            "Graduate Student",
            "B.S., University of Rochester, The Institute of Optics, 2018",
            "Office: 626 CSB",
            "Email: jstaffa@u.rochester.edu",
        ],
    },
    {
        "name": "Raymond Lopez-Rios",
        "lines": [
            "Graduate Student",
            "B.S. , University of Rochester, the Institute of Optics, 2017",
            "Office: 625 CSB",
            "Email: rlopezri@ur.rochester.edu",
        ],
    },
    {
        "name": "Shixin Xue",
        "lines": [
            "Graduate Student",
            "B.S. , University of Illinois Urbana-Champaign, 2018",
            "Office: 625 CSB",
            "Email: sxue4@ur.rochester.edu",
        ],
    },
    {
        "name": "Zhengdong Gao",
        "lines": [
            "Graduate Student",
            "B.S., Shanghai Jiao Tong University, 2019",
            "Office: 625 CSB",
            "Email: zgao14@ur.rochester.edu",
        ],
    },
]


PUBLICATION_PREVIEW = [
    "M. Li, J. Ling, Y. He, U. A. Javid, S. Xue, and Q. Lin, “Lithium niobate photonic-crystal electro-optic modulator,” Nat. Commun. 11, 4123 (2020).",
    "Y. He, Q. F. Yang, J. Ling, R. Luo, H. Liang, M. Li, B. Shen, H. Wang, K. Vahala, and Q. Lin, “Self-starting bi-chromatic LiNbO3 soliton microcomb,” Optica 6, 1138-1144 (2019).",
    "R. Luo, Y. He, H. Liang, M. Li, and Q. Lin, “Highly tunable efficient second-harmonic generation in a lithium niobate nanophotonic waveguide,” Optica 5, 1006-1011 (2018).",
    "R. Luo, H. Jiang, S. Rogers, H. Liang, Y. He, and Q. Lin, “On-chip second-harmonic generation and broadband parametric down-conversion in a lithium niobate microresonator,” Opt. Express 25, 24531-24539 (2017).",
]

RECENT_PUBLICATIONS = {
    "2025": [
        "Shixin Xue, Mingxiao Li, Raymond Lopez-Rios, Jingwei Ling, Zhengdong Gao, Qili Hu, Tian Qiu, Jeremy Staffa, Lin Chang, Heming Wang, Chao Xiang, John E. Bowers, and Q. Lin, “Pockels laser directly driving ultrafast optical metrology,” Light Sci. Appl. 14, 209 (2025).",
        "Shixin Xue, Mingxiao Li, Yueteng Zhang, Qili Hu, Zhengdong Gao, Sanket Bohora, Jeremy Staffa, Raymond Lopez-Rios, John E. Bowers, and Q. Lin, “Narrow linewidth on-chip III-V/TFLT laser,” Opt. Lett. 50, 4754-4757 (2025).",
    ],
    "2024": [
        "Jingwei Ling, Zhengdong Gao, Shixin Xue, Qili Hu, Mingxiao Li, Kaibo Zhang, Usman A. Javid, Raymond Lopez-Rios, Jeremy Staffa, and Q. Lin, “Electrically empowered microcomb laser,” Nat. Commun. 15, 4192 (2024).",
    ],
    "2023": [
        "Yang He, Raymond Lopez-Rios, Usman A. Javid, Jingwei Ling, Mingxiao Li, Shixin Xue, Kerry Vahala, and Q. Lin, “High-speed tunable microwave-rate soliton microcomb,” Nat. Commun. 14, 3467 (2023).",
        "Jingwei Ling, Jeremy Staffa, Heming Wang, Boqiang Shen, Lin Chang, Usman A. Javid, Lue Wu, Zhiquan Yuan, Raymond Lopez-Rios, Mingxiao Li, Yang He, Bohan Li, John E. Bowers, Kerry Vahala, and Q. Lin, “Self-Injection Locked Frequency Conversion Laser,” Laser Photon. Rev. 17, 2200663 (2023).",
    ],
    "2022": [
        "Mingxiao Li, Lin Chang, Lue Wu, Jeremy Staffa, Jingwei Ling, Usman A. Javid, Boqiang Shen, Heming Wang, Siwei Zeng, Lin Zhu, John E. Bowers, Kerry J. Vahala, and Q. Lin, “Integrated Pockels laser,” Nat. Commun. 13, 5344 (2022).",
    ],
    "2021": [
        "Usman A. Javid, Jingwei Ling, Jeremy Staffa, Mingxiao Li, Yang He, and Q. Lin, “Ultrabroadband Entangled Photons on a Nanophotonic Chip,” Phys. Rev. Lett. 127, 183601 (2021).",
    ],
}

RECENT_CONFERENCE_PUBLICATIONS = {
    "2025": [
        'Shixin Xue, Mingxiao Li, Raymond Lopez-Rios, Jingwei Ling, Zhengdong Gao, Qili Hu, Tian Qiu, Jeremy Staffa, Lin Chang, Heming Wang, Chao Xiang, John E. Bowers, and Q. Lin, "Pockels Laser For Driving Ultrafast Optical Metrology," in CLEO 2025, Technical Digest Series (Optica Publishing Group, 2025), paper SS124_3.',
        'Qili Hu, Jingwei Ling, Zhengdong Gao, Raymond Lopez-Rios, Shixin Xue, and Q. Lin, "Broadband soliton microcomb laser," in Optica Nonlinear Optics 2025 (NLO), Technical Digest Series (Optica Publishing Group, 2025), paper W3A.6.',
        'Jeremy Staffa, Raymond Lopez-Rios, Qili Hu, Shixin Xue, Zhengdong Gao, Austin Graf, and Q. Lin, "Actively Mode-Locked OPO Microcomb on Integrated Lithium Niobate," in Optica Nonlinear Optics 2025 (NLO), Technical Digest Series (Optica Publishing Group, 2025), paper W3A.7.',
        'Zhengdong Gao, Jeremy Staffa, Raymond Lopez-Rios, Austin Graf, Qili Hu, Shixin Xue, and Q. Lin, "Ultrabroad band second-order nonlinear optics based on periodic poled thin film lithium niobate," in CLEO 2025, Technical Digest Series (Optica Publishing Group, 2025), paper SS100_3.',
    ],
    "2024": [
        'Jingwei Ling, Zhengdong Gao, Shixin Xue, Qili Hu, Mingxiao Li, Kaibo Zhang, Usman Javid, Raymond Lopez-Rios, Jeremy Staffa, and Q. Lin, "On-chip InP/LiNbO3 microcomb laser," in CLEO 2024, Technical Digest Series (Optica Publishing Group, 2024), paper SW3O.5.',
        'Zhengdong Gao, Jingwei Ling, Shixin Xue, Qili Hu, Kaibo Zhang, Usman Javid, Raymond Lopez-Rios, Jeremy Staffa, and Q. Lin, "Harmonic mode locked InP/LiNbO3 microcomb laser," in CLEO 2024, Technical Digest Series (Optica Publishing Group, 2024), paper SM4G.2.',
        'Zhengdong Gao, Jingwei Ling, Shixin Xue, Qili Hu, Mingxiao Li, Kaibo Zhang, Usman Javid, Raymond Lopez-Rios, Jeremy Staffa, and Q. Lin, "Passive-mode-locked InP/LiNbO3 integrated soliton laser," in CLEO 2024, Technical Digest Series (Optica Publishing Group, 2024), paper SF3E.6.',
    ],
    "2023": [
        'Shixin Xue, Mingxiao Li, Lin Chang, Jingwei Ling, Zhengdong Gao, Qili Hu, Kaibo Zhang, Chao Xiang, Heming Wang, John E. Bowers, and Q. Lin, "Integrated DBR-based Pockels Laser," in CLEO 2023, Technical Digest Series (Optica Publishing Group, 2023), paper SM2J.6.',
        'Shixin Xue, Zhimin Shi, Jingwei Ling, Zhengdong Gao, Qili Hu, Kaibo Zhang, Gareth Valentine, Xi Wu, Jeremy Staffa, Usman A. Javid, and Q. Lin, "Full-spectrum visible electro-optic modulator," in CLEO 2023, Technical Digest Series (Optica Publishing Group, 2023), paper SF3K.2.',
    ],
    "2022": [
        'Mingxiao Li, Lin Chang, Lue Wu, Jeremy Staffa, Jingwei Ling, Usman A. Javid, Yang He, Shixin Xue, Theodore J. Morin, Boqiang Shen, Heming Wang, Siwei Zeng, Lin Zhu, Kerry J. Vahala, John E. Bowers, and Q. Lin, "Integrated III-V/Lithium Niobate Nonlinear Laser," in Conference on Lasers and Electro-Optics, Technical Digest Series (Optica Publishing Group, 2022), paper STu4G.3.',
        'Yang He, Raymond Lopez-Rios, Mingxiao Li, Jingwei Ling, Usman A. Javid, Kerry Vahala, and Q. Lin, "Dynamically tunable microwave-rate soliton microcombs on a monolithic LiNbO3 platform," in Conference on Lasers and Electro-Optics, Technical Digest Series (Optica Publishing Group, 2022), paper STh2F.2.',
        'Jingwei Ling, Jeremy Staffa, Lue Wu, Lin Chang, Boqiang Shen, Usman A. Javid, Heming Wang, Shixin Xue, Mingxiao Li, Yang He, John E. Bowers, Kerry J. Vahala, and Q. Lin, "Third-harmonic generation on chip through cascaded χ(2) processes," in Conference on Lasers and Electro-Optics, Technical Digest Series (Optica Publishing Group, 2022), paper SF4G.3.',
    ],
    "2021": [
        'Usman A. Javid, Jingwei Ling, Jeremy Staffa, Mingxiao Li, Yang He, and Q. Lin, "An efficient nanophotonic source of ultra-broadband entangled photons," in Conference on Lasers and Electro-Optics, OSA Technical Digest (Optica Publishing Group, 2021), paper JM3F.2.',
        'Yang He, Raymond Lopez-Rios, Qifan Yang, Jingwei Ling, Mingxiao Li, Kerry Vahala, and Q. Lin, "Octave-spanning lithium niobate soliton microcombs," in Conference on Lasers and Electro-Optics, OSA Technical Digest (Optica Publishing Group, 2021), paper STu2G.1.',
    ],
}


LAB_CSS = """
body {
  background: #0a0f1c;
}

body, input, select, textarea {
  color: rgba(235, 241, 255, 0.78);
}

a:hover {
  color: #ffffff;
}

#sidebar {
  background: #081223;
}

#sidebar nav a:before {
  background: rgba(96, 130, 188, 0.22);
}

#sidebar nav a:after,
h1.major:after,
h2.major:after,
h3.major:after {
  background-image: linear-gradient(to right, #0e4b92, #2ca7ff);
}

.wrapper.style1,
.wrapper.style1-alt {
  background-color: #0d182b;
}

.wrapper.style2,
.wrapper.style2-alt {
  background-color: #101f39;
}

.wrapper.style3,
.wrapper.style3-alt {
  background-color: #152846;
}

#intro.lab-intro {
  background-image:
    linear-gradient(90deg, rgba(4, 11, 22, 0.86) 0%, rgba(4, 11, 22, 0.62) 46%, rgba(4, 11, 22, 0.38) 100%),
    linear-gradient(180deg, rgba(8, 18, 36, 0.18) 0%, rgba(8, 18, 36, 0.52) 100%),
    url("../images/image.png");
  background-size: cover;
  background-position: center center;
}

#intro.lab-intro .inner {
  background: rgba(7, 14, 26, 0.18);
  border: 1px solid rgba(174, 205, 255, 0.16);
  border-radius: 0.5em;
  padding: 2.75em 3em;
  backdrop-filter: blur(6px);
  box-shadow: 0 2.5rem 5rem rgba(0, 0, 0, 0.22);
}

#intro.lab-intro p {
  max-width: 34rem;
}

.features.plain section {
  padding-left: 2.25em;
}

.features.plain section .icon {
  display: none;
}

.features.plain section p:last-child,
.member-preview p:last-child {
  margin-bottom: 0;
}

.member-preview h3,
.legacy-copy h1,
.legacy-copy h2,
.legacy-copy h3,
.legacy-copy h4 {
  color: #ffffff;
}

.member-preview p {
  margin-bottom: 0.35em;
}

.pub-preview {
  margin: 0 0 2em 0;
}

.pub-preview li {
  margin-bottom: 1.1em;
}

.pub-preview li:last-child {
  margin-bottom: 0;
}

.lab-overview {
  padding-top: 0;
}

.lab-overview .inner {
  padding-top: 0;
}

.lab-overview-intro {
  margin-bottom: 0;
}

.lab-page-spotlights > section > .content > .inner {
  padding-top: 2.5em;
  padding-bottom: 2.5em;
}

.legacy-copy,
.legacy-archive {
  color: rgba(235, 241, 255, 0.78);
}

.legacy-copy img,
.legacy-archive img {
  max-width: 100%;
  height: auto;
  border-radius: 0.35em;
}

.legacy-copy p,
.legacy-archive p,
.legacy-archive li {
  color: rgba(235, 241, 255, 0.78);
}

.legacy-archive .categories {
  margin-bottom: 2em;
}

.legacy-archive .type {
  display: flex;
  flex-wrap: wrap;
  gap: 0.7em;
  align-items: center;
  padding-left: 0;
}

.legacy-archive .type li {
  margin: 0;
  list-style: none;
}

.legacy-archive .type a {
  border-bottom: 0;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 2.4em;
  padding: 0.45em 0.95em;
  border: 1px solid rgba(174, 205, 255, 0.18);
  border-radius: 999px;
  white-space: nowrap;
  background: rgba(255, 255, 255, 0.03);
}

.legacy-archive .portfolio-items > div {
  margin-bottom: 2.5em;
}

.legacy-archive .thumbnail,
.legacy-archive .portfolio-item {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(174, 205, 255, 0.14);
  border-radius: 0.45em;
  padding: 1.5em;
  min-width: 0;
}

.legacy-archive .thumbnail {
  display: flex;
  flex-direction: column;
  gap: 1em;
  height: 100%;
}

.legacy-archive .thumbnail img {
  width: 100%;
  aspect-ratio: 1 / 1;
  object-fit: cover;
  object-position: center;
}

.legacy-archive .row {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5em;
  row-gap: 1.5em;
}

.legacy-archive .row > [class*="col-lg-12"] {
  width: 100%;
}

.legacy-archive .row > [class*="col-md-4"] {
  width: calc(20% - 1.2em);
}

.legacy-archive .row > [class*="col-md-3"] {
  width: calc(20% - 1.2em);
}

.legacy-archive .caption {
  min-width: 0;
  font-size: 0.88em;
}

.legacy-archive .caption h3 {
  margin-bottom: 0.65em;
  line-height: 1.25;
  font-size: 1.05em;
  overflow-wrap: anywhere;
  word-break: break-word;
}

.legacy-archive .caption p,
.member-preview p {
  overflow-wrap: anywhere;
  word-break: break-word;
}

.legacy-archive hr {
  border-bottom-color: rgba(255, 255, 255, 0.08);
}

#footer .menu {
  color: rgba(235, 241, 255, 0.45);
}

@media screen and (max-width: 1280px) {
  .legacy-archive .row > [class*="col-md-4"],
  .legacy-archive .row > [class*="col-md-3"] {
    width: calc(50% - 0.75em);
  }
}

@media screen and (max-width: 980px) {
  #intro.lab-intro .inner {
    padding: 2.25em 2em;
  }

  .legacy-archive .row > [class*="col-md-4"],
  .legacy-archive .row > [class*="col-md-3"] {
    width: calc(50% - 0.75em);
  }
}

@media screen and (max-width: 736px) {
  #intro.lab-intro {
    background-position: 65% center;
  }

  #intro.lab-intro .inner {
    padding: 1.85em 1.5em;
  }

  .legacy-archive .row > [class*="col-md-4"],
  .legacy-archive .row > [class*="col-md-3"] {
    width: 100%;
  }
}
"""


LAB_JS = """
const filterLinks = document.querySelectorAll('[data-filter]');
const filterItems = document.querySelectorAll('.portfolio-items > div');

for (const link of filterLinks) {
  link.addEventListener('click', (event) => {
    event.preventDefault();
    const target = link.dataset.filter || '*';

    for (const candidate of filterLinks) {
      candidate.classList.remove('active');
    }

    link.classList.add('active');

    for (const item of filterItems) {
      if (target === '*' || item.classList.contains(target.replace('.', ''))) {
        item.style.display = '';
      } else {
        item.style.display = 'none';
      }
    }
  });
}
"""


def read_source(name: str) -> str:
    return (SOURCE_ROOT / name).read_text(encoding="utf-8", errors="ignore")


def extract_between(text: str, start_marker: str, end_marker: str) -> str:
    start = text.index(start_marker)
    end = text.index(end_marker, start)
    return text[start:end]


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def copy_tree(source: Path, target: Path) -> None:
    if not source.exists():
        return
    shutil.copytree(source, target, dirs_exist_ok=True)


def reset_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)


def copy_assets() -> None:
    INTRO_IMAGE_TARGET.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(INTRO_IMAGE_SOURCE, INTRO_IMAGE_TARGET)
    copy_tree(SOURCE_ROOT / "img" / "index_research", SITE1_ROOT / "images" / "index_research")
    copy_tree(SOURCE_ROOT / "img" / "research", SITE1_ROOT / "images" / "research")
    copy_tree(SOURCE_ROOT / "img" / "team", SITE1_ROOT / "images" / "team")


def copy_common_images(target_root: Path) -> None:
    intro_target = target_root / "images" / "image.png"
    intro_target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(INTRO_IMAGE_SOURCE, intro_target)
    copy_tree(SOURCE_ROOT / "img" / "index_research", target_root / "images" / "index_research")
    copy_tree(SOURCE_ROOT / "img" / "research", target_root / "images" / "research")
    copy_tree(SOURCE_ROOT / "img" / "team", target_root / "images" / "team")


def copy_editorial_assets(target_root: Path) -> None:
    copy_tree(EDITORIAL_VENDOR_ROOT / "assets", target_root / "assets")
    copy_common_images(target_root)


def recent_publication_filters() -> str:
    return "".join(
        f'\n            <li><a href="#" data-filter=".{year}">{year}</a></li>'
        for year in sorted(RECENT_PUBLICATIONS, reverse=True)
    )


def publication_block(year: str, entries: list[str]) -> str:
    items = "\n".join(f"            <p>{entry}</p>" for entry in entries)
    return f"""
        <div class="col-sm-6 col-md-3 {year} col-lg-12">
          <div class="portfolio-item">
            <div class="hover-bg">
            </div>
{items}
          </div>
        </div>"""


def conference_entries_block(entries_by_year: dict[str, list[str]]) -> str:
    ordered_entries: list[str] = []
    for year in sorted(entries_by_year, reverse=True):
        ordered_entries.extend(entries_by_year[year])
    return "\n".join(f"            <p> {entry} </p>" for entry in ordered_entries)


def inject_recent_publications(archive: str) -> str:
    archive = archive.replace(
        '<li><a href="#" data-filter="*" class="active">All</a></li>',
        '<li><a href="#" data-filter="*" class="active">All</a></li>' + recent_publication_filters(),
        1,
    )
    new_blocks = "\n".join(
        publication_block(year, RECENT_PUBLICATIONS[year])
        for year in sorted(RECENT_PUBLICATIONS, reverse=True)
    )
    archive = archive.replace('<div class="portfolio-items">', f'<div class="portfolio-items">\n{new_blocks}', 1)
    archive = archive.replace(
        '<div class="col-sm-6 col-md-3 conference col-lg-12">\n          <div class="portfolio-item">\n            <div class="hover-bg"> \n            </div>\n',
        '<div class="col-sm-6 col-md-3 conference col-lg-12">\n          <div class="portfolio-item">\n            <div class="hover-bg"> \n            </div>\n'
        + conference_entries_block(RECENT_CONFERENCE_PUBLICATIONS)
        + "\n",
        1,
    )
    return archive


def page_head(title: str, depth: int = 0) -> str:
    prefix = "../" * depth
    return f"""<!DOCTYPE HTML>
<!--
    Hyperspace by HTML5 UP
    html5up.net | @ajlkn
    Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
    <head>
        <title>{title}</title>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
        <link rel="stylesheet" href="{TEMPLATE_ORIGIN}/assets/css/main.css" />
        <link rel="stylesheet" href="{prefix}assets/lab.css" />
        <noscript><link rel="stylesheet" href="{TEMPLATE_ORIGIN}/assets/css/noscript.css" /></noscript>
    </head>
"""


def page_scripts(prefix: str = "") -> str:
    return f"""
        <script src="{TEMPLATE_ORIGIN}/assets/js/jquery.min.js"></script>
        <script src="{TEMPLATE_ORIGIN}/assets/js/jquery.scrollex.min.js"></script>
        <script src="{TEMPLATE_ORIGIN}/assets/js/jquery.scrolly.min.js"></script>
        <script src="{TEMPLATE_ORIGIN}/assets/js/browser.min.js"></script>
        <script src="{TEMPLATE_ORIGIN}/assets/js/breakpoints.min.js"></script>
        <script src="{TEMPLATE_ORIGIN}/assets/js/util.js"></script>
        <script src="{TEMPLATE_ORIGIN}/assets/js/main.js"></script>
        <script src="{prefix}assets/lab.js"></script>
"""


def build_home() -> str:
    about_sections = "\n".join(
        f"""
                        <section>
                            <h3>{title}</h3>
                            <p>{text}</p>
                        </section>"""
        for title, text in ABOUT_ITEMS
    )
    research_sections = "\n".join(
        f"""
                    <section>
                        <a href="{item["href"]}" class="image"><img src="{item["image"]}" alt="{item["title"]}" data-position="center center" /></a>
                        <div class="content">
                            <div class="inner">
                                <h2>{item["title"]}</h2>
                                <p>{item["summary"]}</p>
                                <ul class="actions">
                                    <li><a href="{item["href"]}" class="button">Learn More</a></li>
                                </ul>
                            </div>
                        </div>
                    </section>"""
        for item in RESEARCH_ITEMS
    )
    member_sections = "\n".join(
        f"""
                        <section class="member-preview">
                            <h3>{member["name"]}</h3>
                            {"".join(f"<p>{line}</p>" for line in member["lines"])}
                        </section>"""
        for member in MEMBER_PREVIEW
    )
    publication_items = "\n".join(f"<li>{entry}</li>" for entry in PUBLICATION_PREVIEW)
    return f"""{page_head("Laboratory for Nanophotonics")}
    <body class="is-preload">

        <section id="sidebar">
            <div class="inner">
                <nav>
                    <ul>
                        <li><a href="#intro">Home</a></li>
                        <li><a href="#about-us">About Us</a></li>
                        <li><a href="#research">Research</a></li>
                        <li><a href="#members">Members</a></li>
                        <li><a href="#publications">Publications</a></li>
                    </ul>
                </nav>
            </div>
        </section>

        <div id="wrapper">

            <section id="intro" class="wrapper style1 fullscreen fade-up lab-intro">
                <div class="inner">
                    <h1>Laboratory for Nanophotonics</h1>
                    <p>Quantum, Nonlinear and Mechanical Photonics</p>
                    <ul class="actions">
                        <li><a href="#about-us" class="button scrolly">About Us</a></li>
                    </ul>
                </div>
            </section>

            <section id="about-us" class="wrapper style3 fade-up">
                <div class="inner">
                    <h2>About Us</h2>
                    <div class="features plain">
                        {about_sections}
                    </div>
                </div>
            </section>

            <section id="research" class="wrapper style2 spotlights">
                {research_sections}
            </section>

            <section id="members" class="wrapper style1 fade-up">
                <div class="inner">
                    <h2>Members</h2>
                    <div class="features plain">
                        {member_sections}
                    </div>
                    <ul class="actions">
                        <li><a href="members.html" class="button">Members</a></li>
                    </ul>
                </div>
            </section>

            <section id="publications" class="wrapper style3 fade-up">
                <div class="inner">
                    <h2>Publications</h2>
                    <ul class="alt pub-preview">
                        {publication_items}
                    </ul>
                    <ul class="actions">
                        <li><a href="publications.html" class="button">Publications</a></li>
                    </ul>
                </div>
            </section>

        </div>

        <footer id="footer" class="wrapper style1-alt">
            <div class="inner">
                <ul class="menu">
                    <li>&copy; Laboratory for Nanophotonics.</li>
                    <li>Design: <a href="https://html5up.net">HTML5 UP</a></li>
                </ul>
            </div>
        </footer>
{page_scripts()}
    </body>
</html>
"""


def generic_header(active: str, depth: int = 0) -> str:
    prefix = "../" * depth

    def nav_item(label: str, href: str, name: str) -> str:
        active_attr = ' class="active"' if active == name else ""
        return f'<li><a href="{href}"{active_attr}>{label}</a></li>'

    return f"""
        <header id="header">
            <a href="{prefix}index.html" class="title">Laboratory for Nanophotonics</a>
            <nav>
                <ul>
                    {nav_item("Home", f"{prefix}index.html", "home")}
                    {nav_item("About Us", f"{prefix}index.html#about-us", "about")}
                    {nav_item("Research", f"{prefix}research.html", "research")}
                    {nav_item("Members", f"{prefix}members.html", "members")}
                    {nav_item("Publications", f"{prefix}publications.html", "publications")}
                </ul>
            </nav>
        </header>
"""


def generic_page(title: str, body: str, active: str, depth: int = 0) -> str:
    prefix = "../" * depth
    return f"""{page_head(title, depth)}
    <body class="is-preload">
{generic_header(active, depth)}
        <div id="wrapper">
{body}
        </div>

        <footer id="footer" class="wrapper alt">
            <div class="inner">
                <ul class="menu">
                    <li>&copy; Laboratory for Nanophotonics.</li>
                    <li>Design: <a href="https://html5up.net">HTML5 UP</a></li>
                </ul>
            </div>
        </footer>
{page_scripts(prefix)}
    </body>
</html>
"""


EDITORIAL_LAB_CSS = """
body {
  background: #f6f7fb;
}

@media screen and (min-width: 1281px) {
  #sidebar {
    width: 22.5em;
  }

  #sidebar > .inner {
    width: 22.5em;
  }

  #sidebar .toggle {
    left: 22.5em;
  }

  #sidebar.inactive {
    margin-left: -22.5em;
  }
}

#main > .inner {
  max-width: 90rem;
}

#header .logo {
  letter-spacing: 0.02em;
}

#sidebar > .inner > section:first-child h2 {
  font-size: 1.85em;
  line-height: 1.15;
}

#banner .content p {
  max-width: 38rem;
}

#banner .image.object.intro-art img {
  border-radius: 0.5em;
  box-shadow: 0 1.5rem 3rem rgba(17, 24, 39, 0.16);
}

.about-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1.5rem;
  align-items: stretch;
  margin-top: 0.75rem;
}

.about-card {
  display: flex;
  flex-direction: column;
  min-width: 0;
  height: 100%;
  padding: 1.8rem 1.5rem;
  border: 1px solid rgba(33, 43, 54, 0.12);
  border-radius: 0.6rem;
  background: #ffffff;
  box-shadow: 0 1rem 2.4rem rgba(17, 24, 39, 0.06);
}

.about-card-header {
  display: flex;
  align-items: flex-end;
  min-height: 3.75rem;
  margin-bottom: 1rem;
  padding-bottom: 0.95rem;
  border-bottom: 1px solid rgba(33, 43, 54, 0.1);
}

.about-card-header h3 {
  margin: 0;
  line-height: 1.25;
}

.about-card-body {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}

.about-card-body p {
  margin: 0;
}

.research-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1.75rem;
  align-items: stretch;
  margin-top: 0.75rem;
}

.research-card {
  display: flex;
  flex-direction: column;
  min-width: 0;
  height: 100%;
  border: 1px solid rgba(33, 43, 54, 0.12);
  border-radius: 0.65rem;
  overflow: hidden;
  background: #ffffff;
  box-shadow: 0 1.2rem 2.6rem rgba(17, 24, 39, 0.07);
}

.research-card-image {
  display: block;
  aspect-ratio: 1.65 / 1;
  overflow: hidden;
}

.research-card-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.research-card-body {
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
  min-height: 14rem;
  padding: 1.5rem 1.6rem 1rem;
}

.research-card-body h3 {
  margin: 0;
  line-height: 1.25;
}

.research-card-body p {
  margin: 0;
}

.research-card-actions {
  margin-top: auto;
  padding: 0 1.6rem 1.5rem;
  display: flex;
  align-items: flex-end;
}

.research-card-actions .actions {
  margin: 0;
}

.research-card-actions .actions li:first-child {
  padding-left: 0;
}

.research-card-actions .button {
  margin: 0;
}

.member-grid {
  display: grid;
  grid-template-columns: repeat(5, minmax(0, 1fr));
  gap: 1rem;
}

.member-grid article {
  border: 1px solid rgba(33, 43, 54, 0.1);
  border-radius: 0.5rem;
  padding: 1.2rem 1rem;
  background: #ffffff;
  min-width: 0;
}

.member-grid h3 {
  font-size: 1rem;
  line-height: 1.25;
  margin-bottom: 0.6rem;
  overflow-wrap: anywhere;
  word-break: break-word;
}

.member-grid p {
  margin: 0 0 0.35rem 0;
  font-size: 0.92rem;
  overflow-wrap: anywhere;
  word-break: break-word;
}

.curated-publications li {
  margin-bottom: 1rem;
}

.editorial-archive .categories {
  margin-bottom: 2rem;
}

.editorial-archive .type {
  display: flex;
  flex-wrap: wrap;
  gap: 0.7rem;
  padding-left: 0;
}

.editorial-archive .type li {
  list-style: none;
  margin: 0;
}

.editorial-archive .type a {
  border-bottom: 0;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 2.4rem;
  padding: 0.45rem 0.95rem;
  border: 1px solid rgba(33, 43, 54, 0.14);
  border-radius: 999px;
  white-space: nowrap;
  background: rgba(255, 255, 255, 0.86);
}

.editorial-archive .portfolio-items > div {
  margin-bottom: 2rem;
}

.editorial-archive .thumbnail,
.editorial-archive .portfolio-item {
  background: #ffffff;
  border: 1px solid rgba(33, 43, 54, 0.08);
  border-radius: 0.45rem;
  padding: 1.4rem;
  min-width: 0;
}

.editorial-archive .thumbnail {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  height: 100%;
}

.editorial-archive .thumbnail img {
  width: 100%;
  aspect-ratio: 1 / 1;
  object-fit: cover;
  object-position: center;
}

.editorial-archive .row {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  row-gap: 1rem;
}

.editorial-archive .row > [class*="col-lg-12"] {
  width: 100%;
}

.editorial-archive .row > [class*="col-md-4"],
.editorial-archive .row > [class*="col-md-3"] {
  width: calc(20% - 0.8rem);
}

.editorial-archive .caption {
  min-width: 0;
  font-size: 0.88em;
}

.editorial-archive .caption h3 {
  margin-bottom: 0.65em;
  line-height: 1.25;
  font-size: 1.05em;
  overflow-wrap: anywhere;
  word-break: break-word;
}

.editorial-archive .caption p,
.editorial-archive p,
.editorial-archive li {
  overflow-wrap: anywhere;
  word-break: break-word;
}

@media screen and (max-width: 1280px) {
  .about-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .research-grid {
    grid-template-columns: 1fr;
  }

  .member-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .editorial-archive .row > [class*="col-md-4"],
  .editorial-archive .row > [class*="col-md-3"] {
    width: calc(50% - 0.75rem);
  }
}

@media screen and (max-width: 980px) {
  #sidebar {
    width: 100vw;
  }

  #sidebar > .inner {
    width: 100vw;
  }

  #sidebar .toggle {
    left: 100vw;
  }

  #sidebar.inactive {
    margin-left: -100vw;
  }

  .about-grid,
  .research-grid {
    grid-template-columns: 1fr;
  }

  .member-grid {
    grid-template-columns: 1fr;
  }

  .editorial-archive .row > [class*="col-md-4"],
  .editorial-archive .row > [class*="col-md-3"] {
    width: 100%;
  }
}

@media screen and (max-width: 736px) {
  .about-card,
  .research-card-body {
    padding-left: 1.25rem;
    padding-right: 1.25rem;
  }

  .research-card-actions {
    padding-left: 1.25rem;
    padding-right: 1.25rem;
  }

  .member-grid {
    grid-template-columns: 1fr;
  }

  .editorial-archive .row > [class*="col-md-4"],
  .editorial-archive .row > [class*="col-md-3"] {
    width: 100%;
  }
}
"""


def editorial_head(title: str, depth: int = 0) -> str:
    prefix = "../" * depth
    return f"""<!DOCTYPE HTML>
<!--
    Editorial by HTML5 UP
    html5up.net | @ajlkn
    Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
    <head>
        <title>{title}</title>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
        <link rel="stylesheet" href="{prefix}assets/css/main.css" />
        <link rel="stylesheet" href="{prefix}assets/editorial-lab.css" />
    </head>
"""


def editorial_scripts(prefix: str = "") -> str:
    return f"""
        <script src="{prefix}assets/js/jquery.min.js"></script>
        <script src="{prefix}assets/js/browser.min.js"></script>
        <script src="{prefix}assets/js/breakpoints.min.js"></script>
        <script src="{prefix}assets/js/util.js"></script>
        <script src="{prefix}assets/js/main.js"></script>
        <script src="{prefix}assets/editorial-lab.js"></script>
"""


def editorial_menu_items(depth: int = 0) -> str:
    prefix = "../" * depth
    return f"""
                                    <ul>
                                        <li><a href="{prefix}index.html">Home</a></li>
                                        <li><a href="{prefix}index.html#about-us">About Us</a></li>
                                        <li><a href="{prefix}research.html">Research</a></li>
                                        <li><a href="{prefix}members.html">Members</a></li>
                                        <li><a href="{prefix}publications.html">Publications</a></li>
                                    </ul>
"""


def editorial_page(title: str, body: str, depth: int = 0) -> str:
    prefix = "../" * depth
    return f"""{editorial_head(title, depth)}
    <body class="is-preload">
        <div id="wrapper">
            <div id="main">
                <div class="inner">
{body}
                </div>
            </div>

            <div id="sidebar">
                <div class="inner">
                    <section>
                        <header class="major">
                            <h2>Laboratory for Nanophotonics</h2>
                        </header>
                        <p>Quantum, Nonlinear and Mechanical Photonics</p>
                    </section>
                    <nav id="menu">
                        <header class="major">
                            <h2>Menu</h2>
                        </header>
{editorial_menu_items(depth)}
                    </nav>
                </div>
            </div>
        </div>
{editorial_scripts(prefix)}
    </body>
</html>
"""


def build_editorial_home() -> str:
    about_sections = "\n".join(
        f"""
                                        <article class="about-card">
                                            <div class="about-card-header">
                                                <h3>{title}</h3>
                                            </div>
                                            <div class="about-card-body">
                                                <p>{text}</p>
                                            </div>
                                        </article>"""
        for title, text in ABOUT_ITEMS
    )
    research_posts = "\n".join(
        f"""
                                        <article class="research-card">
                                            <a href="{item["href"]}" class="research-card-image"><img src="{item["image"]}" alt="{item["title"]}" /></a>
                                            <div class="research-card-body">
                                                <h3>{item["title"]}</h3>
                                                <p>{item["summary"]}</p>
                                            </div>
                                            <div class="research-card-actions">
                                                <ul class="actions">
                                                <li><a href="{item["href"]}" class="button">Learn More</a></li>
                                                </ul>
                                            </div>
                                        </article>"""
        for item in RESEARCH_ITEMS
    )
    member_cards = "\n".join(
        f"""
                                    <article>
                                        <h3>{member["name"]}</h3>
                                        {"".join(f"<p>{line}</p>" for line in member["lines"])}
                                    </article>"""
        for member in MEMBER_PREVIEW
    )
    publication_items = "\n".join(f"                                <li>{entry}</li>" for entry in PUBLICATION_PREVIEW)
    body = f"""
                    <section id="banner">
                        <div class="content">
                            <header>
                                <h1>Laboratory for Nanophotonics</h1>
                                <p>Quantum, Nonlinear and Mechanical Photonics</p>
                            </header>
                            <p>{ABOUT_ITEMS[1][1]}</p>
                            <ul class="actions">
                                <li><a href="#about-us" class="button big">About Us</a></li>
                            </ul>
                        </div>
                        <span class="image object intro-art">
                            <img src="images/image.png" alt="Photonic integrated circuit" />
                        </span>
                    </section>

                    <section id="about-us" class="photonlab-section">
                        <header class="major">
                            <h2>About Us</h2>
                        </header>
                        <div class="about-grid">
{about_sections}
                        </div>
                    </section>

                    <section id="research" class="photonlab-section">
                        <header class="major">
                            <h2>Research</h2>
                        </header>
                        <div class="research-grid">
{research_posts}
                        </div>
                    </section>

                    <section id="members" class="photonlab-section">
                        <header class="major">
                            <h2>Members</h2>
                        </header>
                        <div class="member-grid">
{member_cards}
                        </div>
                        <ul class="actions" style="margin-top: 2rem;">
                            <li><a href="members.html" class="button">Members</a></li>
                        </ul>
                    </section>

                    <section id="publications" class="photonlab-section">
                        <header class="major">
                            <h2>Publications</h2>
                        </header>
                        <ul class="curated-publications">
{publication_items}
                        </ul>
                        <ul class="actions">
                            <li><a href="publications.html" class="button">Publications</a></li>
                        </ul>
                    </section>
"""
    return editorial_page("Laboratory for Nanophotonics", body)


def build_editorial_research_overview() -> str:
    research_posts = "\n".join(
        f"""
                                <article class="research-card">
                                    <a href="{item["href"]}" class="research-card-image"><img src="{item["image"]}" alt="{item["title"]}" /></a>
                                    <div class="research-card-body">
                                        <h3>{item["title"]}</h3>
                                        <p>{item["summary"]}</p>
                                    </div>
                                    <div class="research-card-actions">
                                        <ul class="actions">
                                            <li><a href="{item["href"]}" class="button">Learn More</a></li>
                                        </ul>
                                    </div>
                                </article>"""
        for item in RESEARCH_ITEMS
    )
    body = f"""
                    <section>
                        <header class="main">
                            <h1>Research</h1>
                        </header>
                        <div class="research-grid">
{research_posts}
                        </div>
                    </section>
"""
    return editorial_page("Research", body)


def build_editorial_research_detail(source_name: str, title: str) -> str:
    source = read_source(source_name)
    article = extract_between(source, "<h2>", "<!-- Contact Section -->")
    article = article.replace('src="img/research/', 'src="../images/research/')
    body = f"""
                    <section>
                        <header class="main">
                            <h1>{title}</h1>
                        </header>
                        <div class="legacy-copy">
                            {article}
                        </div>
                    </section>
"""
    return editorial_page(title, body, depth=1)


def build_editorial_members() -> str:
    source = read_source("member.html")
    archive = extract_between(source, '<div id="works-section">', "<!-- Contact Section -->")
    archive = archive.replace('src="img/team/', 'src="images/team/')
    archive = archive.replace("<h2>Members</h2>", "<h2>Current Members</h2>", 1)
    body = f"""
                    <section>
                        <header class="main">
                            <h1>Members</h1>
                        </header>
                        <div class="editorial-archive">
                            {archive}
                        </div>
                    </section>
"""
    return editorial_page("Members", body)


def build_editorial_publications() -> str:
    source = read_source("publication.html")
    archive = extract_between(source, '<div id="works-section">', "<!-- Team Section --><!-- Contact Section -->")
    archive = inject_recent_publications(archive)
    body = f"""
                    <section>
                        <header class="main">
                            <h1>Publications</h1>
                        </header>
                        <div class="editorial-archive">
                            {archive}
                        </div>
                    </section>
"""
    return editorial_page("Publications", body)


def build_research_overview() -> str:
    research_sections = "\n".join(
        f"""
                <section>
                    <a href="{item["href"]}" class="image"><img src="{item["image"]}" alt="{item["title"]}" data-position="center center" /></a>
                    <div class="content">
                        <div class="inner">
                            <h2>{item["title"]}</h2>
                            <p>{item["summary"]}</p>
                            <ul class="actions">
                                <li><a href="{item["href"]}" class="button">Learn More</a></li>
                            </ul>
                        </div>
                    </div>
                </section>"""
        for item in RESEARCH_ITEMS
    )
    body = f"""
            <section id="main" class="wrapper style1 lab-overview">
                <div class="inner lab-overview-intro">
                    <h1 class="major">Research</h1>
                </div>
            </section>
            <section class="wrapper style2 spotlights lab-page-spotlights">
{research_sections}
            </section>
"""
    return generic_page("Research", body, "research")


def build_research_detail(source_name: str, title: str) -> str:
    source = read_source(source_name)
    article = extract_between(source, "<h2>", "<!-- Contact Section -->")
    article = article.replace('src="img/research/', 'src="../images/research/')
    body = f"""
            <section id="main" class="wrapper">
                <div class="inner legacy-copy">
                    <h1 class="major">{title}</h1>
                    {article}
                </div>
            </section>
"""
    return generic_page(title, body, "research", depth=1)


def build_members() -> str:
    source = read_source("member.html")
    archive = extract_between(source, '<div id="works-section">', "<!-- Contact Section -->")
    archive = archive.replace('src="img/team/', 'src="images/team/')
    archive = archive.replace("<h2>Members</h2>", "<h2>Current Members</h2>", 1)
    body = f"""
            <section id="main" class="wrapper">
                <div class="inner legacy-archive">
                    <h1 class="major">Members</h1>
                    {archive}
                </div>
            </section>
"""
    return generic_page("Members", body, "members")


def build_publications() -> str:
    source = read_source("publication.html")
    archive = extract_between(source, '<div id="works-section">', "<!-- Team Section --><!-- Contact Section -->")
    archive = inject_recent_publications(archive)
    body = f"""
            <section id="main" class="wrapper">
                <div class="inner legacy-archive">
                    <h1 class="major">Publications</h1>
                    {archive}
                </div>
            </section>
"""
    return generic_page("Publications", body, "publications")


def write_editorial_site() -> None:
    reset_dir(SITE2_ROOT)
    copy_editorial_assets(SITE2_ROOT)
    write_text(SITE2_ROOT / "assets" / "editorial-lab.css", EDITORIAL_LAB_CSS.strip() + "\n")
    write_text(SITE2_ROOT / "assets" / "editorial-lab.js", LAB_JS.strip() + "\n")
    write_text(SITE2_ROOT / "index.html", build_editorial_home())
    write_text(SITE2_ROOT / "research.html", build_editorial_research_overview())
    write_text(SITE2_ROOT / "members.html", build_editorial_members())
    write_text(SITE2_ROOT / "publications.html", build_editorial_publications())
    write_text(
        SITE2_ROOT / "research" / "integrated-quantum-photonics.html",
        build_editorial_research_detail("research1.html", "Integrated Quantum Photonics"),
    )
    write_text(
        SITE2_ROOT / "research" / "integrated-nonlinear-photonics.html",
        build_editorial_research_detail("research2.html", "Integrated Nonlinear Photonics"),
    )
    write_text(
        SITE2_ROOT / "research" / "ln-sic-photonics.html",
        build_editorial_research_detail("research3.html", "LN&SiC Photonics"),
    )
    write_text(
        SITE2_ROOT / "research" / "integrated-photonic-sensing.html",
        build_editorial_research_detail("research4.html", "Integrated Photonic Sensing"),
    )


def main() -> int:
    reset_dir(SITE1_ROOT)
    copy_assets()
    write_text(SITE1_ROOT / "assets" / "lab.css", LAB_CSS.strip() + "\n")
    write_text(SITE1_ROOT / "assets" / "lab.js", LAB_JS.strip() + "\n")
    write_text(SITE1_ROOT / "index.html", build_home())
    write_text(SITE1_ROOT / "research.html", build_research_overview())
    write_text(SITE1_ROOT / "members.html", build_members())
    write_text(SITE1_ROOT / "publications.html", build_publications())
    write_text(
        SITE1_ROOT / "research" / "integrated-quantum-photonics.html",
        build_research_detail("research1.html", "Integrated Quantum Photonics"),
    )
    write_text(
        SITE1_ROOT / "research" / "integrated-nonlinear-photonics.html",
        build_research_detail("research2.html", "Integrated Nonlinear Photonics"),
    )
    write_text(
        SITE1_ROOT / "research" / "ln-sic-photonics.html",
        build_research_detail("research3.html", "LN&SiC Photonics"),
    )
    write_text(
        SITE1_ROOT / "research" / "integrated-photonic-sensing.html",
        build_research_detail("research4.html", "Integrated Photonic Sensing"),
    )
    write_editorial_site()
    print(f"Built site options into {SITE1_ROOT} and {SITE2_ROOT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
