#!/usr/bin/env python3
"""Fail if the skill bundle has broken routes, links, or policy metadata."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "caddie"
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
PLAYBOOK_LESSONS = {
    "getting-started.md": "01-getting-started.md",
    "context-engineering.md": "02-context-engineering.md",
    "memory-knowledge.md": "03-memory-knowledge.md",
    "tools.md": "04-tools.md",
    "coding-agent.md": "05-coding-agent.md",
    "interaction.md": "06-interaction.md",
    "evaluating-agents.md": "07-evaluating-agents.md",
    "post-training.md": "08-post-training.md",
    "continual-evolution.md": "09-continual-evolution.md",
    "multi-agent.md": "10-multi-agent.md",
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

ID_RE = re.compile(r"\b[a-z0-9]+(?:-[a-z0-9]+)+\b")
HEADING_ID_RE = re.compile(r"^###\s+`(?P<id>[a-z0-9]+(?:-[a-z0-9]+)+)`\s*$", re.M)
SOURCE_DEFINITION_RE = re.compile(r"\bsource-ids:\s*(?P<ids>[^\n]+)", re.I)
SOURCE_REFERENCE_RE = re.compile(
    r"\bsource-ids?\b(?:\s*:\s*|\s+(?=(?:`|\(|[a-z0-9]+-)))(?P<ids>[^\n]*)",
    re.I,
)
CITE_REFERENCE_RE = re.compile(r"\b[Cc]ite\s+(?!source-ids?\b)(?P<ids>[^\n]*)")
MARKDOWN_LINK_RE = re.compile(
    r"!?\[[^\]]*\]\((?P<destination><[^>]+>|[^)\s]+)(?:\s+['\"][^)]*['\"])?\)"
)
PLAYBOOK_H2S = ("Use when", "Steps", "Open next", "Reply")
H1_RE = re.compile(r"^#(?!#)\s+\S.*$", re.M)
H2_RE = re.compile(r"^##(?!#)\s+(?P<title>.+?)\s*$", re.M)
H3_RE = re.compile(r"^###(?!#)\s+(?P<title>.+?)\s*$", re.M)
STEP_HEADING_RE = re.compile(r"(?P<number>0|[1-9][0-9]*)\.\s+\S.*")
YAML_MAPPING_RE = re.compile(
    r"(?P<indent> *)(?P<key>[A-Za-z0-9_-]+):(?P<value>.*)$"
)


def nlines(path: Path) -> int:
    return path.read_text().count("\n") + 1


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def frontmatter(text: str) -> dict[str, str] | None:
    """Read the small scalar/block frontmatter subset this bundle needs."""
    if not text.startswith("---\n"):
        return None
    closing = re.search(r"^---\s*$", text[4:], re.M)
    if closing is None:
        return None
    block = text[4 : 4 + closing.start()]
    fields: dict[str, str] = {}
    lines = block.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        match = re.fullmatch(r"(?P<key>[A-Za-z0-9_-]+):(?:\s*(?P<value>.*))?", line)
        if match is None:
            index += 1
            continue
        key = match.group("key")
        value = (match.group("value") or "").strip()
        if value in {">", ">-", ">+", "|", "|-", "|+"}:
            continuation: list[str] = []
            index += 1
            while index < len(lines) and (not lines[index] or lines[index][0].isspace()):
                if lines[index].strip():
                    continuation.append(lines[index].strip())
                index += 1
            fields[key] = " ".join(continuation)
            continue
        fields[key] = value.strip("'\"")
        index += 1
    return fields


def policy_allows_only_explicit_invocation(path: Path) -> bool:
    """Require one root policy mapping with one direct false child."""
    lines = [raw_line.split("#", 1)[0].rstrip() for raw_line in path.read_text().splitlines()]
    top_level_policies: list[tuple[int, str]] = []
    for number, line in enumerate(lines):
        match = YAML_MAPPING_RE.fullmatch(line)
        if match and not match.group("indent") and match.group("key") == "policy":
            top_level_policies.append((number, match.group("value").strip()))

    if len(top_level_policies) != 1:
        return False
    policy_line, policy_value = top_level_policies[0]
    if policy_value:
        return False

    child_indent: int | None = None
    allow_values: list[str] = []
    for line in lines[policy_line + 1 :]:
        if not line.strip():
            continue
        if not line.startswith((" ", "\t")):
            break
        match = YAML_MAPPING_RE.fullmatch(line)
        if match is None:
            continue
        indent = len(match.group("indent"))
        if child_indent is None:
            child_indent = indent
        if match.group("key") != "allow_implicit_invocation":
            continue
        if indent != child_indent:
            return False
        allow_values.append(match.group("value").strip())

    return allow_values == ["false"]


def is_local_link(destination: str) -> bool:
    parsed = urlsplit(destination)
    return not destination.startswith("#") and not parsed.scheme and not parsed.netloc


def validate_playbook_schema(name: str, body: str, errors: list[str]) -> None:
    """Check the fixed H1/H2/H3 layout that keeps playbooks scannable."""
    h1s = list(H1_RE.finditer(body))
    if len(h1s) != 1:
        errors.append(f"playbooks/{name} must contain exactly one H1 (found {len(h1s)})")

    h2s = list(H2_RE.finditer(body))
    h2_titles = tuple(match.group("title") for match in h2s)
    if h2_titles != PLAYBOOK_H2S:
        found = ", ".join(h2_titles) or "none"
        errors.append(
            f"playbooks/{name} H2 sections must be Use when, Steps, Open next, Reply "
            f"(found: {found})"
        )
    if h1s and h2s and h1s[0].start() > h2s[0].start():
        errors.append(f"playbooks/{name} H1 must precede its H2 sections")

    section = ""
    step_numbers: list[int] = []
    for number, line in enumerate(body.splitlines(), start=1):
        if match := H2_RE.fullmatch(line):
            section = match.group("title")
            continue
        if match := H3_RE.fullmatch(line):
            if section != "Steps":
                errors.append(f"playbooks/{name}:{number} step heading is outside ## Steps")
            step_match = STEP_HEADING_RE.fullmatch(match.group("title"))
            if step_match is None:
                errors.append(f"playbooks/{name}:{number} step heading must match ### N. ...")
                continue
            step_numbers.append(int(step_match.group("number")))

    expected_numbers = list(range(len(step_numbers)))
    if not step_numbers:
        errors.append(f"playbooks/{name} has no numbered step headings")
    elif step_numbers != expected_numbers:
        found = ", ".join(map(str, step_numbers))
        errors.append(
            f"playbooks/{name} step numbers must begin at 0 and be contiguous "
            f"(found: {found})"
        )


def validate_local_markdown_links(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        text = path.read_text()
        for match in MARKDOWN_LINK_RE.finditer(text):
            destination = match.group("destination").strip("<>")
            if not is_local_link(destination):
                continue
            relative = unquote(urlsplit(destination).path)
            if not relative:
                continue
            target = (path.parent / relative).resolve()
            try:
                target.relative_to(ROOT)
            except ValueError:
                errors.append(
                    f"{path.relative_to(ROOT)}:{line_number(text, match.start())} "
                    f"link leaves bundle: {destination}"
                )
                continue
            if not target.exists():
                errors.append(
                    f"{path.relative_to(ROOT)}:{line_number(text, match.start())} "
                    f"missing local link target: {destination}"
                )


def main() -> int:
    errors: list[str] = []
    skill = ROOT / "SKILL.md"
    if not skill.is_file():
        print("missing SKILL.md")
        return 1
    text = skill.read_text()
    metadata = frontmatter(text)
    if metadata is None:
        errors.append("SKILL.md missing or malformed frontmatter")
    else:
        if metadata.get("name") != SKILL_NAME:
            errors.append(f"SKILL.md name must be {SKILL_NAME}")
        if not metadata.get("description", "").strip():
            errors.append("SKILL.md description must be nonempty")
        if "disable-model-invocation" in metadata:
            errors.append("SKILL.md uses unsupported disable-model-invocation metadata")

    policy_path = ROOT / "agents" / "openai.yaml"
    if not policy_path.is_file():
        errors.append("missing agents/openai.yaml explicit-invocation policy")
    elif not policy_allows_only_explicit_invocation(policy_path):
        errors.append("agents/openai.yaml must set policy.allow_implicit_invocation: false")

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
        validate_playbook_schema(name, body, errors)
        lesson_name = PLAYBOOK_LESSONS[name]
        if lesson_name not in body:
            errors.append(f"playbooks/{name} never names lessons/{lesson_name}")

    for name in REFS:
        if not (ROOT / "references" / name).is_file():
            errors.append(f"missing references/{name}")

    id_hits: dict[str, list[str]] = {}
    source_ids_by_lesson: dict[str, set[str]] = {}
    cluster_ids_by_lesson: dict[str, set[str]] = {}
    heading_ids: dict[str, list[str]] = {}
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

        source_ids: set[str] = set()
        for match in SOURCE_DEFINITION_RE.finditer(body):
            defined_ids = ID_RE.findall(match.group("ids"))
            if not defined_ids:
                errors.append(f"lessons/{name}:{line_number(body, match.start())} has no source ids")
            for source_id in defined_ids:
                source_ids.add(source_id)
                id_hits.setdefault(source_id, []).append(name)
        source_ids_by_lesson[name] = source_ids

        clusters = set(HEADING_ID_RE.findall(body))
        cluster_ids_by_lesson[name] = clusters
        for cluster in clusters:
            heading_ids.setdefault(cluster, []).append(name)

    for cluster, files in heading_ids.items():
        if len(files) > 1:
            errors.append(f"duplicate lesson heading id {cluster} in {', '.join(files)}")

    for name in PLAYBOOKS:
        path = ROOT / "playbooks" / name
        if not path.is_file():
            continue
        body = path.read_text()
        lesson_name = PLAYBOOK_LESSONS[name]
        known_source_ids = source_ids_by_lesson.get(lesson_name, set())
        known_clusters = cluster_ids_by_lesson.get(lesson_name, set())
        for number, line in enumerate(body.splitlines(), start=1):
            for cluster_match in re.finditer(
                r"\bclusters?\b(?P<ids>.*?)(?=\b(?:source-ids?|[Cc]ite)\b|$)",
                line,
                re.I,
            ):
                for cluster in re.findall(
                    r"`([a-z0-9]+(?:-[a-z0-9]+)+)`", cluster_match.group("ids")
                ):
                    if cluster != "source-ids" and cluster not in known_clusters:
                        errors.append(
                            f"playbooks/{name}:{number} unknown cluster {cluster} "
                            f"in lessons/{lesson_name}"
                        )
            for reference_match in (
                *SOURCE_REFERENCE_RE.finditer(line),
                *CITE_REFERENCE_RE.finditer(line),
            ):
                for source_id in ID_RE.findall(reference_match.group("ids")):
                    if source_id not in known_source_ids:
                        definitions = ", ".join(id_hits.get(source_id, [])) or "none"
                        errors.append(
                            f"playbooks/{name}:{number} unknown source id {source_id} "
                            f"in lessons/{lesson_name} (defined in: {definitions})"
                        )

    validate_local_markdown_links(errors)

    if errors:
        print("\n".join(errors))
        return 1
    print(f"PASS bundle playbooks={len(PLAYBOOKS)} lessons={len(LESSONS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
