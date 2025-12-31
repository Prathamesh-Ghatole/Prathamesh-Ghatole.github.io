"""Static site generator.

Build-time only. Reads Markdown with YAML frontmatter from ./content,
renders Jinja templates from ./templates, and writes a fully static site
to ./public.

Usage:
  uv run python scripts/generate_site.py
"""

from __future__ import annotations

import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import frontmatter
import markdown as md
from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor
from markupsafe import Markup
from xml.etree import ElementTree as etree
from jinja2 import Environment, FileSystemLoader, select_autoescape


ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "content"
TEMPLATES_DIR = ROOT / "templates"
STATIC_DIR = ROOT / "static"
OUT_DIR = ROOT / "public"


def _is_url(value: str) -> bool:
    return value.startswith("http://") or value.startswith("https://")


def normalize_asset_ref(value: str | None) -> str | None:
    """Normalize a frontmatter image/url field.

    Supported:
    - absolute URLs: https://...
    - site-relative paths: /assets/...
    - relative-ish: assets/... or ./assets/... -> /assets/...
    """

    if not value:
        return None
    v = value.strip()
    if not v:
        return None
    if _is_url(v):
        return v
    # Normalize to site-root path.
    v = re.sub(r"^\./", "", v)
    if not v.startswith("/"):
        v = "/" + v
    return v


def slugify(value: str) -> str:
    v = value.strip().lower()
    v = re.sub(r"[^a-z0-9\s-]", "", v)
    v = re.sub(r"\s+", "-", v)
    v = re.sub(r"-+", "-", v)
    return v.strip("-")


def md_to_html(text: str) -> str:
    class HighlightInlineProcessor(InlineProcessor):
        """Render ==highlight== as <mark class="md-highlight">highlight</mark>."""

        def handleMatch(self, m, data):
            el = etree.Element("mark")
            el.set("class", "md-highlight")
            el.text = m.group(1)
            return el, m.start(0), m.end(0)

    class AccentInlineProcessor(InlineProcessor):
        """Render ^^accent^^ as <span class="md-accent">accent</span>."""

        def handleMatch(self, m, data):
            el = etree.Element("span")
            el.set("class", "md-accent")
            el.text = m.group(1)
            return el, m.start(0), m.end(0)

    class HighlightExtension(Extension):
        def extendMarkdown(self, markdown):
            # Match ==text== but avoid matching empty content.
            pattern = r"==(.+?)=="
            markdown.inlinePatterns.register(
                HighlightInlineProcessor(pattern, markdown),
                "md-highlight",
                175,
            )

            # Match ^^text^^ but avoid matching empty content.
            accent_pattern = r"\^\^(.+?)\^\^"
            markdown.inlinePatterns.register(
                AccentInlineProcessor(accent_pattern, markdown),
                "md-accent",
                174,
            )

    return md.markdown(
        text,
        extensions=[
            "extra",
            "smarty",
            "sane_lists",
            "toc",
            HighlightExtension(),
        ],
        output_format="html5",
    )


@dataclass(frozen=True)
class ContentItem:
    meta: dict[str, Any]
    body_md: str
    body_html: str
    source_path: Path

    @property
    def title(self) -> str:
        return str(self.meta.get("title") or self.meta.get("name") or "")

    @property
    def slug(self) -> str:
        s = self.meta.get("slug")
        if isinstance(s, str) and s.strip():
            return slugify(s)
        if self.title:
            return slugify(self.title)
        return slugify(self.source_path.stem)


def load_markdown_item(path: Path) -> ContentItem:
    post = frontmatter.load(path)
    meta = dict(post.metadata)

    # Normalize common image/url fields.
    for key in ("image", "image_url", "profile_image", "avatar", "cover"):
        if key in meta and isinstance(meta[key], str):
            meta[key] = normalize_asset_ref(meta[key])

    # Normalize links list items if present.
    links = meta.get("links")
    if isinstance(links, list):
        for link in links:
            if isinstance(link, dict) and isinstance(link.get("url"), str):
                link["url"] = normalize_asset_ref(
                    link["url"]
                )  # allow external or site-root

    body_md = post.content or ""
    body_html = md_to_html(body_md) if body_md.strip() else ""
    return ContentItem(
        meta=meta, body_md=body_md, body_html=body_html, source_path=path
    )


def load_collection(dir_path: Path) -> list[ContentItem]:
    if not dir_path.exists():
        return []
    items: list[ContentItem] = []
    for p in sorted(dir_path.glob("*.md")):
        items.append(load_markdown_item(p))
    return items


def sort_items(
    items: list[ContentItem], *, date_key: str = "date"
) -> list[ContentItem]:
    """Sort newest-first if date_key exists; otherwise stable order."""

    def key(i: ContentItem):
        # Allow per-item override for sorting while keeping display fields intact.
        # Example: experience items can use sort_start=YYYY-MM for correct ordering
        # while rendering start='Apr 2024'.
        v = i.meta.get(f"sort_{date_key}")
        if v is None:
            v = i.meta.get(date_key)
        if v is None:
            return ""
        return str(v)

    # Reverse for newest-first; empty date sorts last.
    return sorted(items, key=key, reverse=True)


def clean_out_dir() -> None:
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True, exist_ok=True)


def copy_static() -> None:
    if STATIC_DIR.exists():
        shutil.copytree(STATIC_DIR, OUT_DIR, dirs_exist_ok=True)

    cname = ROOT / "CNAME"
    if cname.exists():
        shutil.copy2(cname, OUT_DIR / "CNAME")


def build_env() -> Environment:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html", "xml"]),
    )

    def md_inline(value: Any) -> Markup:
        """Render a string as *inline* markdown (safe HTML).

        - Converts markdown to HTML using md_to_html (includes ==highlight==).
        - Strips a single surrounding <p>...</p> wrapper.
        - Returns Markup so templates can use it safely in text-node contexts.

        IMPORTANT: This should NOT be used in attribute contexts (href, style, src).
        """

        if value is None:
            return Markup("")
        s = str(value)
        if not s.strip():
            return Markup("")
        html = md_to_html(s).strip()
        # For single-line values markdown wraps in <p>...</p>
        if html.startswith("<p>") and html.endswith("</p>"):
            html = html[3:-4]
        return Markup(html)

    env.filters["md_inline"] = md_inline
    return env


def main() -> None:
    # Load site/page content
    index_md = CONTENT_DIR / "pages" / "index.md"
    if not index_md.exists():
        raise SystemExit(
            f"Missing {index_md}. Create it to store site-wide frontmatter and about copy."
        )

    index = load_markdown_item(index_md)

    experience = load_collection(CONTENT_DIR / "experience")
    projects = load_collection(CONTENT_DIR / "projects")
    writing = load_collection(CONTENT_DIR / "writing")

    stack = load_collection(CONTENT_DIR / "stack")
    achievements = load_collection(CONTENT_DIR / "achievements")
    education = load_collection(CONTENT_DIR / "education")

    # Sort collections
    experience = sort_items(experience, date_key="start")
    writing = sort_items(writing, date_key="date")

    # Build output
    clean_out_dir()
    copy_static()

    env = build_env()
    tpl = env.get_template("layout.html")

    html = tpl.render(
        site=index.meta,
        about_html=index.body_html,
        experience=experience,
        projects=projects,
        writing=writing,
        stack=stack,
        achievements=achievements,
        education=education,
    )

    (OUT_DIR / "index.html").write_text(html, encoding="utf-8")
    print(f"Generated: {OUT_DIR / 'index.html'}")


if __name__ == "__main__":
    main()
