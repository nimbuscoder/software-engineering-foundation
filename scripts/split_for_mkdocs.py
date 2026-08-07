#!/usr/bin/env python3
"""Generate docs/ from root-level syllabus and module markdown files."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

MODULE_TITLES = {
    "01": "Module 01: Building Computational Thinking",
    "02": "Module 02: Understanding Under the Hood",
    "03": "Module 03: Core Computer Science Foundations",
    "04": "Module 04: Higher-Level Software Engineering Skills",
    "05": "Module 05: Collaborating with Generative Tools",
    "06": "Module 06: Projects for the New Reality",
    "07": "Module 07: Broadening Perspective",
}

MODULE_NAV = [
    ("01", "Module 01 — Computational Thinking"),
    ("02", "Module 02 — Under the Hood"),
    ("03", "Module 03 — CS Foundations"),
    ("04", "Module 04 — Software Engineering"),
    ("05", "Module 05 — Generative Tools"),
    ("06", "Module 06 — Projects"),
    ("07", "Module 07 — Perspective"),
]


def lesson_filename(lesson_number: str) -> str:
    return f"lesson-{lesson_number.replace('.', '-')}.md"


def split_module(path: Path) -> str:
    match = re.match(r"(\d+)_Module_", path.name)
    if not match:
        raise ValueError(f"Unexpected module filename: {path.name}")

    module_number = match.group(1)
    module_dir = DOCS / f"module-{module_number}"
    module_dir.mkdir(parents=True, exist_ok=True)

    content = path.read_text(encoding="utf-8")
    parts = re.split(r"(?=^## Lesson )", content, flags=re.MULTILINE)
    overview = parts[0].rstrip() + "\n"
    (module_dir / "index.md").write_text(overview, encoding="utf-8")

    lesson_files: list[str] = []
    for part in parts[1:]:
        heading_match = re.match(r"^## (Lesson [\d.]+ – .+)$", part, flags=re.MULTILINE)
        if not heading_match:
            continue

        heading = heading_match.group(1)
        number_match = re.search(r"Lesson ([\d.]+)", heading)
        if not number_match:
            continue

        lesson_number = number_match.group(1)
        filename = lesson_filename(lesson_number)
        lesson_body = part.strip()
        lesson_body = re.sub(
            rf"^## {re.escape(heading.removeprefix('## '))}$",
            f"# {heading.removeprefix('## ')}",
            lesson_body,
            count=1,
            flags=re.MULTILINE,
        )
        (module_dir / filename).write_text(lesson_body + "\n", encoding="utf-8")
        lesson_files.append(filename)

    pages_content = f'title: "{MODULE_TITLES[module_number]}"\n'
    (module_dir / ".pages").write_text(pages_content, encoding="utf-8")
    return module_number


def write_root_pages() -> None:
    nav_lines = ["nav:", "  - Home: index.md"]
    for module_number, nav_title in MODULE_NAV:
        nav_lines.append(f"  - {nav_title}: module-{module_number}")

    (DOCS / ".pages").write_text("\n".join(nav_lines) + "\n", encoding="utf-8")


def main() -> None:
    preserved: dict[str, bytes] = {}
    preserve_dirs = ("stylesheets", "javascripts", "assets")

    if DOCS.exists():
        for directory in preserve_dirs:
            source_dir = DOCS / directory
            if source_dir.exists():
                for path in source_dir.rglob("*"):
                    if path.is_file():
                        preserved[str(path.relative_to(DOCS))] = path.read_bytes()
        shutil.rmtree(DOCS)

    DOCS.mkdir()

    syllabus = ROOT / "00_Syllabus_Overview.md"
    if not syllabus.exists():
        raise FileNotFoundError("Missing 00_Syllabus_Overview.md")

    syllabus_content = syllabus.read_text(encoding="utf-8")
    start_banner = """
<div class="course-start-banner" markdown="1">

**New here?** Start with [Module 01 — Computational Thinking](module-01/index.md) and work through the modules in order.

**Try code online:** [Online IDE Pro Python Playground](https://www.onlineide.pro/playground/python?utm_source=online-python&utm_medium=navbar&utm_campaign=onlineidepro)

</div>
"""
    if "course-start-banner" not in syllabus_content:
        syllabus_content = syllabus_content.replace(
            "\n### Purpose of This Syllabus\n",
            f"\n{start_banner}\n### Purpose of This Syllabus\n",
            1,
        )

    (DOCS / "index.md").write_text(syllabus_content, encoding="utf-8")

    module_files = sorted(ROOT.glob("*_Module_*.md"))
    if not module_files:
        raise FileNotFoundError("No module markdown files found")

    for module_file in module_files:
        split_module(module_file)

    write_root_pages()

    for relative_path, content in preserved.items():
        target = DOCS / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)

    print(f"Generated {DOCS} from {len(module_files)} module files.")


if __name__ == "__main__":
    main()
