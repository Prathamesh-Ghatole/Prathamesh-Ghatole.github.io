# Project Brief

## Overview
This repository powers **prathameshg.com**, a single-page developer portfolio site.

The site is generated as a **fully static** build from **human-editable content** (Markdown with YAML frontmatter) using a small **Python + Jinja2** static-site generator.

## Goals
- Maintain a **static site** (no runtime backend).
- Keep content easy to update using **Markdown**.
- Keep the design close to the Tailwind-based Jinja template in `templates/layout.html`.
- Support a clean deployment workflow to GitHub Pages using a dedicated `gh-pages` branch.

## Non-Goals (for now)
- No local blog engine (writing section links out externally).
- No CMS.
- No Node-based build pipeline (Tailwind is currently via CDN).

## Deliverables
- Content model under `content/`.
- Jinja templates under `templates/`.
- Static generator script `scripts/generate_site.py`.
- Output directory `public/` (generated; not committed on main).
- GitHub Actions workflow to publish `public/` to `gh-pages`.
