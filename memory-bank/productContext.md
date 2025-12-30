# Product Context

## Why this project exists
The portfolio is a public-facing representation of the author’s work. It needs to be:
- fast to load,
- easy to keep updated,
- and maintainable without a heavy toolchain.

## How it should work
- A single-page site with anchored sections (About, Experience, Work, Technical Stack, Achievements, Education, Writing).
- Content is stored in Markdown files with YAML frontmatter for structured fields.
- A generator converts content + templates into a static `public/` directory.

## User experience goals
- Minimalist aesthetic.
- Strong typography.
- Quick navigation via header anchors.
- Content updates should not require touching HTML.

