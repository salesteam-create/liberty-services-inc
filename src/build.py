"""Generate the static site into the repository root.

Usage:  python3 src/build.py
Edit content in src/data.py and src/pages.py, then rebuild. Output pages are
plain HTML that GitHub Pages serves directly.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pages  # noqa: E402
from components import CTX  # noqa: E402
from data import POSTS, SERVICES  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def routes():
    yield "", pages.home
    yield "about-liberty-services/", pages.about_liberty
    yield "about-filtershine/", pages.about_filtershine
    yield "services/", pages.services_index
    for s in SERVICES:
        yield f"services/{s['slug']}/", (lambda slug=s["slug"]: pages.service_page(slug))
    yield "blogs/", pages.blog_index
    for p in POSTS:
        yield f"blogs/{p['slug']}/", (lambda post=p: pages.blog_post(post))
    yield "contact/", pages.contact
    yield "privacy-page/", pages.privacy
    yield "legal/", pages.terms


def main():
    count = 0
    for path, fn in routes():
        CTX["path"] = path
        CTX["prefix"] = "../" * path.count("/")
        html = fn()
        out_dir = os.path.join(ROOT, path)
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html)
        count += 1
        print(f"  /{path}")
    # GitHub Pages: serve files as-is (no Jekyll processing).
    open(os.path.join(ROOT, ".nojekyll"), "w").close()
    print(f"Built {count} pages.")


if __name__ == "__main__":
    main()
