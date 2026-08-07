# Software Engineering Foundations for the Age of Generative Systems

A self-study syllabus for young learners (ages 12–15) who want to think clearly about software, work precisely with problems, and examine machine-generated solutions with confidence.

**Course site:** [nimbuscoder-io.github.io/software-engineering-foundation](https://nimbuscoder-io.github.io/software-engineering-foundation/)  
**Repository:** [github.com/nimbuscoder-io/software-engineering-foundation](https://github.com/nimbuscoder-io/software-engineering-foundation)

## For students

Open the [course site](https://nimbuscoder-io.github.io/software-engineering-foundation/) and start with **Home**, then **Module 01**. Each lesson includes checklists, examples, and links to the [Python playground](https://www.onlineide.pro/playground/python?utm_source=online-python&utm_medium=navbar&utm_campaign=onlineidepro).

## For contributors

Course content lives in the root-level markdown files (`00_Syllabus_Overview.md` and `*_Module_*.md`). The published site is built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

### Edit content

1. Edit the syllabus or module markdown files at the repository root.
2. Regenerate and preview locally:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/split_for_mkdocs.py
mkdocs serve
```

3. Open [http://127.0.0.1:8000/software-engineering-foundation/](http://127.0.0.1:8000/software-engineering-foundation/) to preview.

Pushing to `main` deploys the site automatically via GitHub Actions.

### Project layout

| Path | Purpose |
|------|---------|
| `00_Syllabus_Overview.md` | Syllabus home page (source) |
| `*_Module_*.md` | Module lesson content (source) |
| `scripts/split_for_mkdocs.py` | Splits modules into lesson pages under `docs/` |
| `docs/` | Generated site content + static assets (CSS, JS, icons) |
| `mkdocs.yml` | Site configuration |
| `.github/workflows/deploy.yml` | GitHub Pages deployment |

## Modules

| Module | Source file | Focus |
|--------|-------------|-------|
| 01 | [01_Module_Building_Computational_Thinking.md](01_Module_Building_Computational_Thinking.md) | Thinking in steps and expressing simple behaviour clearly |
| 02 | [02_Module_Understanding_Under_the_Hood.md](02_Module_Understanding_Under_the_Hood.md) | Connecting human description to machine execution |
| 03 | [03_Module_Core_Computer_Science_Foundations.md](03_Module_Core_Computer_Science_Foundations.md) | Structure, efficiency, and basic system concepts |
| 04 | [04_Module_Higher_Level_Software_Engineering_Skills.md](04_Module_Higher_Level_Software_Engineering_Skills.md) | Specification, interfaces, constraints, and evaluation |
| 05 | [05_Module_Collaborating_with_Generative_Tools.md](05_Module_Collaborating_with_Generative_Tools.md) | Directing, examining, and refining machine-generated solutions |
| 06 | [06_Module_Projects_Reflecting_the_New_Reality.md](06_Module_Projects_Reflecting_the_New_Reality.md) | Applying all skills to constrained, realistic projects |
| 07 | [07_Module_Broadening_Perspective.md](07_Module_Broadening_Perspective.md) | Domain awareness, communication, and responsibility |

## Recommended tools

- **[Online IDE Pro Python Playground](https://www.onlineide.pro/playground/python?utm_source=online-python&utm_medium=navbar&utm_campaign=onlineidepro)** — try code examples without installing anything
- A notebook (physical or digital) for specifications, reflections, and observations
- A generative AI assistant — use only after writing a clear specification, and always examine the output carefully

## Contributing

Suggestions, corrections, and improvements are welcome. Open an issue or pull request on GitHub.
