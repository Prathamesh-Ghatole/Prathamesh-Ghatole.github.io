# Portfolio site (static)

**Live Demo**: https://prathameshg.com/

This repository contains a **single-page static portfolio** generated from **Markdown + YAML frontmatter** using a small **Python + Jinja2** generator.

## Local development

Install dependencies (uv):

```bash
uv sync
```

Generate the site:

```bash
uv run python scripts/generate_site.py
```

Serve the output:

```bash
python -m http.server -d public 8000
```

Open: http://localhost:8000

## Content editing

- Site-wide config + about copy: `content/pages/index.md`
- Experience entries: `content/experience/*.md`
- Projects: `content/projects/*.md`
- Writing (external links for now): `content/writing/*.md`

Images:
- Put repo-managed assets in `static/assets/...`
- Reference them as `/assets/...` in frontmatter (or use `https://...` URLs)

## Deployment

GitHub Actions builds on push to `main` and publishes `./public` to the `gh-pages` branch (GitHub Pages).

