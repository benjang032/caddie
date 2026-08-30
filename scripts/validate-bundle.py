#!/usr/bin/env python3
"""Fail if the skill tree is missing routed files, aliases, or caps."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAYBOOKS = [
    "getting-started.md",
    "context-engineering.md",
    "memory-knowledge.md",
    "tools.md",
    "coding-agent.md",
    "interaction.md",
    "evaluating-agents.md",
    "post-training.md",
    "continual-evolution.md",
    "multi-agent.md",
]
H1 = {
    "getting-started.md": "first-agent-architecture-review",
    "context-engineering.md": "context-layout-review",
    "memory-knowledge.md": "user-memory-and-knowledge-base",
    "tools.md": "design-or-review-agent-tools",
    "coding-agent.md": "coding-agent-harness-review",
    "interaction.md": "expand-observation-action-timing",
    "evaluating-agents.md": "evaluation-driven-agent-improvement",
    "post-training.md": "choose-and-run-post-training",
    "continual-evolution.md": "continual-evolution-closed-loop",
    "multi-agent.md": "multi-agent-design-review",
}
REFS = ["source.md", "principles.md", "failure-modes.md", "data-shapes.md", "tensions.md"]
LESSONS = [
    "00-introduction.md",
    "01-getting-started.md",
    "02-context-engineering.md",
    "03-memory-knowledge.md",
    "04-tools.md",
    "05-coding-agent.md",
    "06-interaction.md",
    "07-evaluating-agents.md",
    "08-post-training.md",
    "09-continual-evolution.md",
    "10-multi-agent.md",
    "11-afterword.md",
]


def nlines(path: Path) -> int:
    return path.read_text().count("\n") + 1


def main() -> int:
    errors: list[str] = []
    skill = ROOT / "SKILL.md"
    if not skill.is_file():
        print("missing SKILL.md")
        return 1
    text = skill.read_text()
    if not text.startswith("---"):
        errors.append("SKILL.md missing frontmatter")
    fm = text.split("---", 2)
    if len(fm) < 3 or "name: ai-agents-in-depth" not in fm[1]:
        errors.append("SKILL.md name mismatch")
    if nlines(skill) > 500:
        errors.append(f"SKILL.md over 500 lines ({nlines(skill)})")
    if "After a model drop" not in text:
        errors.append("SKILL.md missing After a model drop")
    if "lessons/00-introduction.md" not in text:
        errors.append("SKILL.md missing lessons/00-introduction.md")
    if "lessons/11-afterword.md" not in text:
        errors.append("SKILL.md missing lessons/11-afterword.md")
    if "SFT memorizes. RL generalizes." in text:
        errors.append("SKILL.md still states SFT vs RL as a law")

    for name in PLAYBOOKS:
        path = ROOT / "playbooks" / name
        if not path.is_file():
            errors.append(f"missing playbooks/{name}")
            continue
        if "playbooks/" + name not in text:
            errors.append(f"SKILL.md does not route to playbooks/{name}")
        body = path.read_text()
        if len(body) < 800:
            errors.append(f"thin playbook {name} ({len(body)} chars)")
        if nlines(path) > 400:
            errors.append(f"playbook {name} over 400 lines ({nlines(path)})")
        alias = H1[name]
        if not re.search(rf"^#\s+{re.escape(alias)}\s*$", body, re.M):
            errors.append(f"playbooks/{name} missing H1 {alias}")
        if "lessons/" not in body:
            errors.append(f"playbooks/{name} never names lessons/")

    for name in REFS:
        if not (ROOT / "references" / name).is_file():
            errors.append(f"missing references/{name}")

    id_hits: dict[str, list[str]] = {}
    for name in LESSONS:
        path = ROOT / "lessons" / name
        if not path.is_file():
            errors.append(f"missing lessons/{name}")
            continue
        if nlines(path) > 400:
            errors.append(f"lesson {name} over 400 lines ({nlines(path)})")
        body = path.read_text()
        if len(body) < 800:
            errors.append(f"thin lesson {name} ({len(body)} chars)")
        for mid in re.findall(r"source-ids:\s*([^\n]+)", body):
            for lid in re.findall(r"[a-z0-9][a-z0-9\-]+", mid):
                id_hits.setdefault(lid, []).append(name)

    # Duplicate *definitions* of canonical ids would be `### id` style. Flag
    # any source-ids token that appears as a heading id twice.
    heading_ids: dict[str, list[str]] = {}
    for name in LESSONS:
        path = ROOT / "lessons" / name
        if not path.is_file():
            continue
        for hid in re.findall(r"^###\s+`([a-z0-9][a-z0-9\-]+)`", path.read_text(), re.M):
            heading_ids.setdefault(hid, []).append(name)
    for hid, files in heading_ids.items():
        if len(files) > 1:
            errors.append(f"duplicate lesson heading id {hid} in {', '.join(files)}")

    if errors:
        print("\n".join(errors))
        return 1
    print(f"PASS bundle playbooks={len(PLAYBOOKS)} lessons={len(LESSONS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
