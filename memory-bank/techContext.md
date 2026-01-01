# Tech Context

## Languages & runtime
- Python >= 3.12

## Dependency management
- **uv** via `pyproject.toml` and `uv.lock`

## Core dependencies
- `jinja2`: HTML templating
- `markdown`: Markdown → HTML
- `python-frontmatter`: parse YAML frontmatter from Markdown

## Frontend
- Tailwind CSS via CDN (no local Tailwind build step)
- Google Fonts + Material Symbols via CDN

## Local development commands
```bash
uv sync
uv run scripts/generate_site.py
uv run scripts/dev_server.py
```

## Deployment
- GitHub Actions workflow: `.github/workflows/gh-pages.yml`
- Publishes to `gh-pages` branch

