#!/usr/bin/env python3
"""Check one chapter worker against its TOC. Exit 0 only on PASS."""
from __future__ import annotations

import json
import sys
from pathlib import Path

REQUIRED = ("coverage.json", "lessons.json", "LESSON.md", "STATUS.txt")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate-worker.py /tmp/aiaid/workers/<slug>", file=sys.stderr)
        return 2
    root = Path(sys.argv[1])
    slug = root.name
    errors: list[str] = []
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append(f"missing {name}")
    if errors:
        print("\n".join(errors))
        return 1

    status = (root / "STATUS.txt").read_text().strip().splitlines()
    if not status or status[0] not in {"PASS", "ISSUES", "BLOCKED"}:
        errors.append("STATUS.txt must start with PASS, ISSUES, or BLOCKED")

    try:
        coverage = json.loads((root / "coverage.json").read_text())
        lessons = json.loads((root / "lessons.md" if False else root / "lessons.json").read_text())
    except json.JSONDecodeError as e:
        print(f"json parse: {e}")
        return 1

    toc_path = Path(f"/tmp/aiaid/toc-{slug}.json")
    toc = json.loads(toc_path.read_text())
    toc_titles = [h["title"] for h in toc]
    cov_titles = [h.get("title") for h in coverage.get("headings", [])]
    if cov_titles != toc_titles:
        missing = [t for t in toc_titles if t not in cov_titles]
        extra = [t for t in cov_titles if t not in toc_titles]
        if missing:
            errors.append("coverage missing headings: " + " | ".join(missing[:8]))
        if extra:
            errors.append("coverage extra headings: " + " | ".join(extra[:8]))
        if len(cov_titles) != len(toc_titles):
            errors.append(f"heading count toc={len(toc_titles)} coverage={len(cov_titles)}")

    allowed_absent = {"Acknowledgments"}
    for h in coverage.get("headings", []):
        st = h.get("status")
        title = h.get("title") or ""
        if st == "absent" and title not in allowed_absent:
            errors.append(f"absent not allowed: {title}")
        if st not in {"covered", "thin", "absent"}:
            errors.append(f"bad status for {title}: {st}")
        if st in {"covered", "thin"} and not h.get("lesson_ids"):
            errors.append(f"no lesson_ids: {title}")

    lesson_ids = {x.get("id") for x in lessons.get("lessons", [])}
    if not lesson_ids:
        errors.append("lessons.json has no lessons")
    for lesson in lessons.get("lessons", []):
        for field in ("id", "source_heading", "title", "when", "rule", "check"):
            if not lesson.get(field):
                errors.append(f"lesson {lesson.get('id')} missing {field}")
                break
        if not lesson.get("procedure"):
            errors.append(f"lesson {lesson.get('id')} missing procedure")

    lesson_md = (root / "LESSON.md").read_text()
    if len(lesson_md) < 2000:
        errors.append(f"LESSON.md too short ({len(lesson_md)} chars)")

    if status[0] != "PASS":
        errors.append("worker STATUS is " + status[0])

    if errors:
        print("\n".join(errors))
        return 1
    print(f"PASS {slug} lessons={len(lesson_ids)} headings={len(toc_titles)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
