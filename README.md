# prathameshg.com — Static Portfolio

**Live:** https://prathameshg.com / https://prathamesh-ghatole.github.io/

A minimalist, single-page portfolio site built as a **fully static** artifact, generated from **human-readable content** (Markdown + YAML frontmatter) using a small **Python + Jinja2** pipeline.

## Why this exists

I wanted a portfolio that is:

- **Fast & static by design** -- no runtime backend required
- **Easy to maintain** -- edit content in Markdown, not HTML
- **Structured and scalable** -- repeatable sections like Experience/Projects/Stack are data-driven

## Highlights

- **Content-driven** -- update the site by editing Markdown (structured via frontmatter).
- **Custom generator** -- a small Python + Jinja2 pipeline that produces a clean static build.
- **Live reload (local dev)** -- auto rebuild + browser refresh while editing content/templates.
- **Automated deploy** -- GitHub Actions publishes `./public` to `gh-pages` on every push to `main`.

## Tech

- Python 3.12+
- Jinja2 (templating)
- Markdown + python-frontmatter (content parsing)
- uv (dependency management)

## Local development

Install dependencies:

```bash
uv sync
```

Generate the site:

```bash
uv run scripts/generate_site.py
```

Serve locally:

```bash
uv run scripts/dev_server.py
```

Open: http://localhost:8000

### Live reload (auto refresh)

For local development, you can run a live-reload server. Any changes to
`content/`, `templates/`, or `static/` will trigger a rebuild + browser refresh.

```bash
uv sync --group dev
uv run python scripts/dev_server.py
```

## Deployment

Deployment is handled by `.github/workflows/gh-pages.yml`:

- Build with uv
- Run the generator
- Deploy `./public` to `gh-pages`

## Roadmap / future additions

- **Resume handler**
  - Store resume source (LaTeX / Markdown) in-repo
  - Add a CI job that validates/optimizes the resume artifact and publishes it automatically (e.g. `/assets/resume.pdf`)
  - Optional: versioned resume URLs and cache-busting

- **Site Exporter**
  - Export site content in a well formatted Markdown or PDF format for easy sharing
  - Add a CI job that generates this export on every content change
