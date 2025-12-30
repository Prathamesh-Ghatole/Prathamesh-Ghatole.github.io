# System Patterns

## Architecture
- **Static site generation** at build time.
- **Content layer**: Markdown + YAML frontmatter.
- **Template layer**: Jinja2 templates + partials.
- **Assets layer**: `static/` copied to output.
- **Output**: generated HTML/assets in `public/`.

## Key implementation patterns
- One file per content item (experience entry, project card, etc.) for clean diffs.
- Frontmatter carries structured fields; markdown body is optional (used for descriptions).
- Templates use loops over collections to render consistent UI sections.

## Directories
- `content/`: content collections
- `templates/`: Jinja templates
- `templates/partials/`: reusable UI components
- `static/`: static files copied to output
- `scripts/`: generator script(s)

## Deployment pattern
- GitHub Actions builds on push to `main`.
- Action publishes the `public/` directory to the `gh-pages` branch.

