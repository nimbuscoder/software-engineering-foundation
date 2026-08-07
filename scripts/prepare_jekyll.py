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

NAVIGATION_DATA = ROOT / "_data" / "navigation.yml"

H2_HEADING = re.compile(r"^## (.+)$", re.MULTILINE)
LESSON_HEADING = re.compile(r"^Lesson (\d+)\.(\d+)\s*[–-]\s*(.+)$")
COMPLETION_HEADING = re.compile(r"^Module (\d+) Completion Check$")


def heading_slug(title: str) -> str:
    lesson = LESSON_HEADING.match(title)
    if lesson:
        return f"lesson-{lesson.group(1)}-{lesson.group(2)}"

    if title == "Module Overview":
        return "module-overview"

    completion = COMPLETION_HEADING.match(title)
    if completion:
        return f"module-{completion.group(1)}-completion-check"

    slug = title.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug).strip("-")
    return slug


def section_short_title(title: str) -> str:
    lesson = LESSON_HEADING.match(title)
    if lesson:
        return f"{lesson.group(1)}.{lesson.group(2)} {lesson.group(3)}"

    if title == "Module Overview":
        return "Overview"

    completion = COMPLETION_HEADING.match(title)
    if completion:
        return "Completion check"

    return title


def section_url(module_number: str, slug: str) -> str:
    if slug == "module-overview":
        return f"/module-{module_number}/"
    return f"/module-{module_number}/{slug}/"


def split_module_sections(content: str) -> tuple[str, list[dict[str, str]]]:
    lines = content.splitlines()
    module_heading = ""
    start_idx = 0
    if lines and lines[0].startswith("# "):
        module_heading = lines[0]
        start_idx = 1
        while start_idx < len(lines) and not lines[start_idx].strip():
            start_idx += 1

    sections: list[dict[str, str]] = []
    current_title: str | None = None
    current_lines: list[str] = []

    def flush_section() -> None:
        nonlocal current_title, current_lines
        if current_title is None:
            return

        body_lines: list[str] = []
        for line in current_lines:
            if line.strip() == "---":
                continue
            body_lines.append(line)

        slug = heading_slug(current_title)
        sections.append(
            {
                "title": current_title,
                "short_title": section_short_title(current_title),
                "slug": slug,
                "body": "\n".join(body_lines).strip(),
            }
        )
        current_title = None
        current_lines = []

    for line in lines[start_idx:]:
        h2_match = H2_HEADING.match(line)
        if h2_match:
            flush_section()
            current_title = h2_match.group(1).strip()
            current_lines = [line]
        elif current_title is not None:
            current_lines.append(line)

    flush_section()
    return module_heading, sections


def module_short_title(full_title: str) -> str:
    prefix = "Module "
    if full_title.startswith(prefix):
        return full_title.split(" — ", 1)[0]
    return full_title


def write_navigation_data() -> None:
    NAVIGATION_DATA.parent.mkdir(parents=True, exist_ok=True)
    lines = ["modules:"]

    for number, source_name, title in MODULES:
        source_path = ROOT / source_name
        sections = split_module_sections(source_path.read_text(encoding="utf-8"))[1]
        short_title = module_short_title(title)

        lines.append(f"  - number: {yaml_string(number)}")
        lines.append(f"    title: {yaml_string(title)}")
        lines.append(f"    short_title: {yaml_string(short_title)}")
        lines.append(f"    url: {yaml_string(section_url(number, 'module-overview'))}")
        lines.append("    sections:")

        for section in sections:
            url = section_url(number, section["slug"])
            lines.append(f"      - title: {yaml_string(section['title'])}")
            lines.append(f"        short_title: {yaml_string(section['short_title'])}")
            lines.append(f"        slug: {yaml_string(section['slug'])}")
            lines.append(f"        url: {yaml_string(url)}")

    NAVIGATION_DATA.write_text("\n".join(lines) + "\n", encoding="utf-8")


def yaml_string(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def write_page(path: Path, front_matter: dict[str, str], body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fm_lines = ["---"]
    for key, value in front_matter.items():
        fm_lines.append(f"{key}: {yaml_string(value)}")
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


def tag_expected_outcomes_lists(content: str) -> str:
    """Add a Kramdown class to bullet lists under **Expected outcomes**."""
    lines = content.splitlines()
    result: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip() == "**Expected outcomes**":
            result.append(line)
            i += 1
            if i < len(lines) and lines[i].startswith("By the end of"):
                result.append(lines[i])
                i += 1
            list_items: list[str] = []
            while i < len(lines) and lines[i].startswith("- "):
                list_items.append(lines[i])
                i += 1
            result.extend(list_items)
            if list_items:
                result.append("{: .expected-outcomes}")
            continue
        result.append(line)
        i += 1
    return "\n".join(result)


def prepare_section_body(content: str) -> str:
    return tag_expected_outcomes_lists(content)


def clean_generated_pages() -> None:
    index = ROOT / "index.md"
    if index.exists():
        index.unlink()

    for path in sorted(ROOT.glob("module-*")):
        if path.is_dir():
            shutil.rmtree(path)
        elif path.is_file():
            path.unlink()


def generate_module_pages(number: str, source_name: str, module_title: str) -> int:
    source_path = ROOT / source_name
    module_heading, sections = split_module_sections(
        source_path.read_text(encoding="utf-8")
    )
    module_dir = ROOT / f"module-{number}"
    page_count = 0

    for section in sections:
        slug = section["slug"]
        permalink = section_url(number, slug)

        if slug == "module-overview":
            path = module_dir / "index.md"
            page_title = module_title
            body = section["body"]
            if module_heading:
                body = f"{module_heading}\n\n{body}"
        else:
            path = module_dir / f"{slug}.md"
            page_title = f"{section['title']} — {module_short_title(module_title)}"
            body = section["body"]

        write_page(
            path,
            {
                "layout": "default",
                "title": page_title,
                "permalink": permalink,
                "module": number,
                "section": slug,
            },
            prepare_section_body(body),
        )
        page_count += 1

    return page_count


def main() -> None:
    clean_generated_pages()
    write_navigation_data()

    syllabus_path = ROOT / "00_Syllabus_Overview.md"
    if not syllabus_path.exists():
        raise FileNotFoundError("Missing 00_Syllabus_Overview.md")

    syllabus = enhance_syllabus(syllabus_path.read_text(encoding="utf-8"))
    write_page(
        ROOT / "index.md",
        {"layout": "default", "title": "Home", "permalink": "/"},
        syllabus,
    )

    total_pages = 1
    for number, source_name, title in MODULES:
        if not (ROOT / source_name).exists():
            raise FileNotFoundError(f"Missing {source_name}")
        total_pages += generate_module_pages(number, source_name, title)

    print(f"Generated {total_pages} Jekyll pages.")


if __name__ == "__main__":
    main()
