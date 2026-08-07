#!/usr/bin/env python3
"""Generate Jekyll pages from root-level syllabus and module markdown files."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

MODULES = [
    (
        "01",
        "01_Module_Building_Computational_Thinking.md",
        "Module 01 — Building Computational Thinking",
    ),
    (
        "02",
        "02_Module_Understanding_Under_the_Hood.md",
        "Module 02 — Understanding Under the Hood",
    ),
    (
        "03",
        "03_Module_Core_Computer_Science_Foundations.md",
        "Module 03 — Core Computer Science Foundations",
    ),
    (
        "04",
        "04_Module_Higher_Level_Software_Engineering_Skills.md",
        "Module 04 — Higher-Level Software Engineering Skills",
    ),
    (
        "05",
        "05_Module_Collaborating_with_Generative_Tools.md",
        "Module 05 — Collaborating with Generative Tools",
    ),
    (
        "06",
        "06_Module_Projects_Reflecting_the_New_Reality.md",
        "Module 06 — Projects for the New Reality",
    ),
    (
        "07",
        "07_Module_Broadening_Perspective.md",
        "Module 07 — Broadening Perspective",
    ),
]

GENERATED_PAGES = ["index.md", *[f"module-{number}.md" for number, _, _ in MODULES]]


def module_nav(current: str) -> str:
    index = next(i for i, (number, _, _) in enumerate(MODULES) if number == current)
    parts = ["", "---", "", "**Navigate:** [Home]({{ '/' | relative_url }})"]

    if index > 0:
        prev_number = MODULES[index - 1][0]
        parts.append(f" · [Module {prev_number} ←]({{{{ '/module-{prev_number}/' | relative_url }}}})")

    if index < len(MODULES) - 1:
        next_number = MODULES[index + 1][0]
        parts.append(f" · [Module {next_number} →]({{{{ '/module-{next_number}/' | relative_url }}}})")

    parts.append("")
    return "\n".join(parts)


def write_page(path: Path, front_matter: dict[str, str], body: str) -> None:
    fm_lines = ["---"]
    for key, value in front_matter.items():
        fm_lines.append(f"{key}: {value}")
    fm_lines.append("---")
    path.write_text("\n".join(fm_lines) + "\n\n" + body.strip() + "\n", encoding="utf-8")


def enhance_syllabus(content: str) -> str:
    start_banner = """
> **New here?** Start with [Module 01 — Building Computational Thinking]({{ '/module-01/' | relative_url }}) and work through the modules in order.
>
> **Try code online:** [Online IDE Pro Python Playground](https://www.onlineide.pro/playground/python?utm_source=online-python&utm_medium=navbar&utm_campaign=onlineidepro)
"""
    if "New here?" not in content:
        content = content.replace(
            "\n### Purpose of This Syllabus\n",
            f"\n{start_banner}\n### Purpose of This Syllabus\n",
            1,
        )

    replacements = {
        "| 01 | Building Computational Thinking and Basic Programming Intuition |":
        "| 01 | [Building Computational Thinking and Basic Programming Intuition]({{ '/module-01/' | relative_url }}) |",
        "| 02 | Understanding What Happens Under the Hood |":
        "| 02 | [Understanding What Happens Under the Hood]({{ '/module-02/' | relative_url }}) |",
        "| 03 | Core Computer Science Foundations |":
        "| 03 | [Core Computer Science Foundations]({{ '/module-03/' | relative_url }}) |",
        "| 04 | Higher-Level Software Engineering Skills |":
        "| 04 | [Higher-Level Software Engineering Skills]({{ '/module-04/' | relative_url }}) |",
        "| 05 | Collaborating with Generative Tools |":
        "| 05 | [Collaborating with Generative Tools]({{ '/module-05/' | relative_url }}) |",
        "| 06 | Projects That Reflect the New Reality |":
        "| 06 | [Projects That Reflect the New Reality]({{ '/module-06/' | relative_url }}) |",
        "| 07 | Broadening Perspective and Complementary Strengths |":
        "| 07 | [Broadening Perspective and Complementary Strengths]({{ '/module-07/' | relative_url }}) |",
    }
    for old, new in replacements.items():
        content = content.replace(old, new)

    content = content.replace(
        "The detailed lessons for each module are provided in separate files. Begin with Module 01 and proceed sequentially.",
        "Begin with [Module 01]({{ '/module-01/' | relative_url }}) and proceed sequentially through each module.",
    )
    return content


def clean_generated_pages() -> None:
    for page in GENERATED_PAGES:
        path = ROOT / page
        if path.exists():
            path.unlink()


def main() -> None:
    clean_generated_pages()

    syllabus_path = ROOT / "00_Syllabus_Overview.md"
    if not syllabus_path.exists():
        raise FileNotFoundError("Missing 00_Syllabus_Overview.md")

    syllabus = enhance_syllabus(syllabus_path.read_text(encoding="utf-8"))
    write_page(
        ROOT / "index.md",
        {"layout": "default", "title": "Home", "permalink": "/"},
        syllabus,
    )

    for number, source_name, title in MODULES:
        source_path = ROOT / source_name
        if not source_path.exists():
            raise FileNotFoundError(f"Missing {source_name}")

        body = source_path.read_text(encoding="utf-8") + module_nav(number)
        write_page(
            ROOT / f"module-{number}.md",
            {"layout": "default", "title": title, "permalink": f"/module-{number}/"},
            body,
        )

    print(f"Generated {len(GENERATED_PAGES)} Jekyll pages.")


if __name__ == "__main__":
    main()
