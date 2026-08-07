#!/usr/bin/env python3
"""Generate Jekyll pages from root-level syllabus and module markdown files."""

from __future__ import annotations

import base64
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

MODULES = [
    (
        "01",
        "01_Module_Building_Computational_Thinking.md",
        "Module 01 — Building Computational Thinking",
        "Building Computational Thinking and Basic Programming Intuition",
        "Computational Thinking",
    ),
    (
        "02",
        "02_Module_Understanding_Under_the_Hood.md",
        "Module 02 — Understanding Under the Hood",
        "Understanding What Happens Under the Hood",
        "Under the Hood",
    ),
    (
        "03",
        "03_Module_Core_Computer_Science_Foundations.md",
        "Module 03 — Core Computer Science Foundations",
        "Core Computer Science Foundations",
        "Core CS Foundations",
    ),
    (
        "04",
        "04_Module_Higher_Level_Software_Engineering_Skills.md",
        "Module 04 — Higher-Level Software Engineering Skills",
        "Higher-Level Software Engineering Skills",
        "Software Engineering Skills",
    ),
    (
        "05",
        "05_Module_Collaborating_with_Generative_Tools.md",
        "Module 05 — Collaborating with Generative Tools",
        "Collaborating with Generative Tools",
        "Collaborating with AI",
    ),
    (
        "06",
        "06_Module_Projects_Reflecting_the_New_Reality.md",
        "Module 06 — Projects for the New Reality",
        "Projects That Reflect the New Reality",
        "Realistic Projects",
    ),
    (
        "07",
        "07_Module_Broadening_Perspective.md",
        "Module 07 — Broadening Perspective",
        "Broadening Perspective and Complementary Strengths",
        "Perspective & Responsibility",
    ),
]

MODULE_MENU_LABELS = {number: menu_label for number, *_rest, menu_label in MODULES}

MODULE_PLAYGROUND_CODE = {
    "01": (
        "# Try code from this module here\n"
        "student_age = 12\n"
        'favourite_subject = "Mathematics"\n'
        'print("Age:", student_age)\n'
        'print("Favourite subject:", favourite_subject)\n'
    ),
    "02": (
        "# Explore how Python runs your instructions\n"
        'message = "Hello from Python"\n'
        "print(message)\n"
    ),
    "03": (
        "# Experiment with data structures\n"
        "scores = [85, 92, 78]\n"
        'print("Scores:", scores)\n'
        'print("Average:", sum(scores) / len(scores))\n'
    ),
    "04": (
        "temperature = 28\n\n"
        "if temperature > 25:\n"
        '    print("It is warm. Wear light clothes.")\n'
        "else:\n"
        '    print("It is cool. Wear a jacket.")\n'
    ),
    "05": (
        "# Test small Python snippets while designing structured requests\n"
        'print("Ready to experiment.")\n'
    ),
    "06": (
        "# Sketch and test project ideas here\n"
        'print("Project workspace ready.")\n'
    ),
    "07": (
        "# Optional: try small examples that support your analysis\n"
        'print("Ready to explore.")\n'
    ),
}

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


def write_navigation_data() -> None:
    NAVIGATION_DATA.parent.mkdir(parents=True, exist_ok=True)
    lines = ["modules:"]

    for number, source_name, page_title, full_title, menu_label in MODULES:
        source_path = ROOT / source_name
        sections = split_module_sections(source_path.read_text(encoding="utf-8"))[1]

        lines.append(f"  - number: {yaml_string(number)}")
        lines.append(f"    title: {yaml_string(full_title)}")
        lines.append(f"    short_title: {yaml_string(menu_label)}")
        lines.append(f"    url: {yaml_string(section_url(number, 'module-overview'))}")
        lines.append("    sections:")

        for section in sections:
            url = section_url(number, section["slug"])
            lines.append(f"      - title: {yaml_string(section['title'])}")
            lines.append(f"        short_title: {yaml_string(section['short_title'])}")
            lines.append(f"        slug: {yaml_string(section['slug'])}")
            lines.append(f"        url: {yaml_string(url)}")

    lines.append("pages:")
    lines.append(f"  - label: {yaml_string('Home')}")
    lines.append(f"    url: {yaml_string('/')}")
    lines.append(f"    key: {yaml_string('home')}")

    for number, source_name, _page_title, _full_title, menu_label in MODULES:
        source_path = ROOT / source_name
        sections = split_module_sections(source_path.read_text(encoding="utf-8"))[1]

        for section in sections:
            slug = section["slug"]
            label = menu_label if slug == "module-overview" else section["short_title"]
            lines.append(f"  - label: {yaml_string(label)}")
            lines.append(f"    url: {yaml_string(section_url(number, slug))}")
            lines.append(f"    module: {yaml_string(number)}")
            lines.append(f"    section: {yaml_string(slug)}")

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


PLAYGROUND_LINE = re.compile(
    r"\*\*Python playground:\*\* Use the \[Online IDE Pro[^\]]+\]\([^\)]+\)[^\n]*\n?"
)

PYTHON_FENCE = re.compile(r"```python\n(.*?)```", re.DOTALL)


def coddy_b64(text: str) -> str:
    return base64.b64encode(text.encode("utf-8")).decode("ascii")


def coddy_embed(code: str, stdin: str = "") -> str:
    encoded_code = coddy_b64(code)
    if stdin:
        encoded_stdin = coddy_b64(stdin)
        return (
            f'{{% include coddy-editor.html encoded_code="{encoded_code}" '
            f'encoded_stdin="{encoded_stdin}" %}}'
        )
    return f'{{% include coddy-editor.html encoded_code="{encoded_code}" %}}'


def ensure_module_playground(content: str, module_number: str) -> str:
    content = PLAYGROUND_LINE.sub("", content)
    if "### Try it yourself" in content:
        return content

    starter = MODULE_PLAYGROUND_CODE.get(
        module_number,
        '# Use this editor to try code from this module.\nprint("Ready.")\n',
    )
    embed_section = f"### Try it yourself\n\n{coddy_embed(starter)}\n\n"
    for marker in ("**Estimated total time:**", "### Core objectives"):
        if marker in content:
            return content.replace(marker, embed_section + marker, 1)
    return f"{content.rstrip()}\n\n{embed_section}"


def inject_coddy_after_python_blocks(content: str) -> str:
    def append_embed(match: re.Match[str]) -> str:
        code = match.group(1).strip("\n")
        if not code:
            return match.group(0)
        return f"{match.group(0)}\n\n{coddy_embed(code + chr(10))}\n"

    return PYTHON_FENCE.sub(append_embed, content)


MODULE_LINK = re.compile(
    r"\[([^\]]+)\]\("
    r"(\{\{\s*['\"]/module-(\d+)/['\"]\s*\|\s*relative_url\s*\}\}|/module-(\d+)/)"
    r"\)"
)


def module_link_titles() -> dict[str, set[str]]:
    titles: dict[str, set[str]] = {}
    for number, _source, page_title, full_title, menu_label in MODULES:
        titles[number] = {
            page_title,
            full_title,
            f"Module {number}",
            f"Module {int(number)}",
        }
    return titles


MODULE_LINK_TITLES = module_link_titles()


def should_rewrite_module_link(link_text: str, number: str) -> bool:
    if link_text in MODULE_LINK_TITLES.get(number, set()):
        return True
    return bool(re.match(rf"Module {number}\s*[—:-]", link_text))


def rewrite_module_link_text(content: str) -> str:
    """Use menu labels for links to module overview pages."""

    def replace(match: re.Match[str]) -> str:
        link_text = match.group(1)
        url = match.group(2)
        number = match.group(3) or match.group(4)
        menu_label = MODULE_MENU_LABELS.get(number)
        if menu_label is None or not should_rewrite_module_link(link_text, number):
            return match.group(0)
        return f"[{menu_label}]({url})"

    return MODULE_LINK.sub(replace, content)


def enhance_syllabus(content: str) -> str:
    first_label = MODULE_MENU_LABELS["01"]
    start_banner = f"""
> **New here?** Start with [{first_label}]({{{{ '/module-01/' | relative_url }}}}) and work through the modules in order.
>
> **Try code online:** The [{first_label}]({{{{ '/module-01/' | relative_url }}}}) module includes an in-page Python editor — no setup required.
"""
    if "New here?" not in content:
        content = content.replace(
            "\n---\n",
            f"\n{start_banner}\n---\n",
            1,
        )
    return rewrite_module_link_text(content)


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


def prepare_section_body(
    content: str, module_number: str, is_overview: bool = False
) -> str:
    content = tag_expected_outcomes_lists(content)
    if is_overview:
        content = ensure_module_playground(content, module_number)
    content = inject_coddy_after_python_blocks(content)
    return rewrite_module_link_text(content)


def clean_generated_pages() -> None:
    index = ROOT / "index.md"
    if index.exists():
        index.unlink()

    for path in sorted(ROOT.glob("module-*")):
        if path.is_dir():
            shutil.rmtree(path)
        elif path.is_file():
            path.unlink()


def generate_module_pages(
    number: str, source_name: str, module_title: str, menu_label: str
) -> int:
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
            page_title = f"{section['title']} — {menu_label}"
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
            prepare_section_body(body, number, slug == "module-overview"),
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
    for number, source_name, module_title, _full_title, menu_label in MODULES:
        if not (ROOT / source_name).exists():
            raise FileNotFoundError(f"Missing {source_name}")
        total_pages += generate_module_pages(
            number, source_name, module_title, menu_label
        )

    print(f"Generated {total_pages} Jekyll pages.")


if __name__ == "__main__":
    main()
