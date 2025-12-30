# Active Context

## Current state
- The site generator and template system are in place.
- Main sections are rendered from content collections under `content/`:
  - experience, projects, stack, achievements, education, writing
- Output is generated to `public/` and deployed via GitHub Actions → `gh-pages`.

## Current work focus
- Memory Bank initialization.

## Decisions (important)
- Static site only; no runtime backend.
- Content is Markdown + YAML frontmatter (one file per item).
- Tailwind CDN is acceptable.
- Output folder is `public/` (not committed to source branch).

## Next likely tasks
- Improve content schema validation (optional).
- Add a resume handler (resume artifact built/published via CI).

