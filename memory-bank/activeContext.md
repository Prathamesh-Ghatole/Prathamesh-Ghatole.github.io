# Active Context

## Current state
- The site generator and template system are in place.
- Main sections are rendered from content collections under `content/`:
  - experience, projects, stack, achievements, education, writing
- Output is generated to `public/` and deployed via GitHub Actions → `gh-pages`.

## Current work focus
- Homepage layout refinements.

## Decisions (important)
- Static site only; no runtime backend.
- Content is Markdown + YAML frontmatter (one file per item).
- Tailwind CDN is acceptable.
- Output folder is `public/` (not committed to source branch).

## Next likely tasks
- Improve content schema validation (optional).
- Add a resume handler (resume artifact built/published via CI).

## Recent changes
- Reordered homepage sections to: Hero/About → Experience → Technical Stack → Achievements/Education → Projects → Blogs.
- Projects section now renders as a horizontally scrollable auto-scrolling carousel (pauses on hover/focus; respects prefers-reduced-motion).
- Project thumbnails now fill a 4:3 frame (bg-cover) for a wider image presentation.
