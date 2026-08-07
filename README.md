# Software Engineering Foundations for the Age of Generative Systems

A self-study syllabus for young learners (ages 12–15) — systems thinking, precise problem formulation, and evaluating machine-generated solutions.

| | |
|---|---|
| **Course site** | [nimbuscoder-io.github.io/software-engineering-foundation](https://nimbuscoder-io.github.io/software-engineering-foundation/) |
| **Repository** | [github.com/nimbuscoder-io/software-engineering-foundation](https://github.com/nimbuscoder-io/software-engineering-foundation) |

## For students

Open the [course site](https://nimbuscoder-io.github.io/software-engineering-foundation/), start with **Home**, then **Module 01**. Work through the modules in order. Use the [Python playground](https://www.onlineide.pro/playground/python?utm_source=online-python&utm_medium=navbar&utm_campaign=onlineidepro) to try code examples.

## For contributors

### Quick start

**Prerequisites:** Python 3.10+, Git

```bash
git clone https://github.com/nimbuscoder-io/software-engineering-foundation.git
cd software-engineering-foundation
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
make serve
```

Preview at [http://127.0.0.1:8000/software-engineering-foundation/](http://127.0.0.1:8000/software-engineering-foundation/).  
Pushing to `main` deploys automatically via [GitHub Actions](.github/workflows/deploy.yml).

### What to edit

| Edit these | Do not edit |
|------------|-------------|
| `00_Syllabus_Overview.md` | `docs/module-*/` (generated) |
| `*_Module_*.md` | `docs/index.md`, `docs/.pages` (generated) |
| `docs/stylesheets/`, `docs/javascripts/`, `docs/assets/` | `site/` (build output) |
| `mkdocs.yml`, `scripts/`, `.github/workflows/` | |

**Source of truth:** root-level markdown files. The build script splits each module into lesson pages under `docs/`.

### Content conventions

When editing modules, keep these patterns so the site builds correctly:

- Module title: `# Module 0X: …`
- Module overview: `## Module Overview`
- Lessons: `## Lesson X.Y – Title` (exact heading format — the splitter relies on it)
- Python playground link in each module overview (see existing modules for wording)

After editing content, run `make serve` (or `make build`) to regenerate and verify before opening a pull request.

### Commands

| Command | Purpose |
|---------|---------|
| `make serve` | Regenerate lesson pages and start local preview |
| `make build` | Regenerate and run a strict production build |
| `make docs` | Regenerate `docs/` only |

### Pull requests

1. Fork the repository and create a branch from `main`.
2. Edit source markdown at the repository root.
3. Run `make build` locally and fix any errors.
4. Open a pull request with a short summary of what changed and why.
5. Note which module(s) or lessons are affected.

Suggestions and corrections are welcome via [issues](https://github.com/nimbuscoder-io/software-engineering-foundation/issues) or pull requests.

By submitting a contribution, you grant the repository owner permission to use it under the [Read-Only Access License v1.0](LICENSE). A pull request does not grant anyone else the right to copy or reuse the materials.

## Modules

| Module | Source file | Focus |
|--------|-------------|-------|
| 01 | [01_Module_Building_Computational_Thinking.md](01_Module_Building_Computational_Thinking.md) | Computational thinking and basic programming intuition |
| 02 | [02_Module_Understanding_Under_the_Hood.md](02_Module_Understanding_Under_the_Hood.md) | From human description to machine execution |
| 03 | [03_Module_Core_Computer_Science_Foundations.md](03_Module_Core_Computer_Science_Foundations.md) | Structure, efficiency, and system concepts |
| 04 | [04_Module_Higher_Level_Software_Engineering_Skills.md](04_Module_Higher_Level_Software_Engineering_Skills.md) | Specification, interfaces, constraints, evaluation |
| 05 | [05_Module_Collaborating_with_Generative_Tools.md](05_Module_Collaborating_with_Generative_Tools.md) | Working with generative tools |
| 06 | [06_Module_Projects_Reflecting_the_New_Reality.md](06_Module_Projects_Reflecting_the_New_Reality.md) | Constrained, realistic projects |
| 07 | [07_Module_Broadening_Perspective.md](07_Module_Broadening_Perspective.md) | Domain awareness, communication, responsibility |

## License

These materials are licensed under the [Read-Only Access License v1.0](LICENSE). You may read and view them for personal, non-commercial learning. Any other use requires [explicit written permission](https://github.com/nimbuscoder-io/software-engineering-foundation/issues).
