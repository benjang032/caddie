#!/usr/bin/env python3
"""Copy the canonical Caddie bundle into each host plugin package."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CODEX_DESTINATION = ROOT / "plugins" / "caddie" / "skills" / "caddie"
CLAUDE_DESTINATION = ROOT / "plugins" / "caddie-claude" / "skills" / "caddie"
DESTINATIONS = (CODEX_DESTINATION, CLAUDE_DESTINATION)
PLUGIN_ROOTS = (CODEX_DESTINATION.parents[1], CLAUDE_DESTINATION.parents[1])
DIRECTORIES = ("lessons", "playbooks", "references")
FILES = ("scripts/validate-bundle.py", "assets/caddie-logo.png")
PACKAGE_FILES = ("LICENSE",)
SKILL_SOURCE = ROOT / "SKILL.md"
AGENT_SOURCE = ROOT / "agents" / "openai.yaml"


def source_files() -> list[Path]:
    """Return every canonical file copied without content adaptation."""
    files = [ROOT / path for path in FILES]
    for directory in DIRECTORIES:
        source_directory = ROOT / directory
        for source in sorted(source_directory.rglob("*")):
            if source.is_file():
                files.append(source)
    return files


def expected_skill_paths() -> set[Path]:
    """Return the complete relative file set for a generated skill copy."""
    paths = {source.relative_to(ROOT) for source in source_files()}
    paths.update((Path("SKILL.md"), Path("agents/openai.yaml")))
    return paths


def adapted_agent() -> bytes:
    """Keep Codex's explicit-only policy while making icon paths skill-local."""
    return AGENT_SOURCE.read_bytes().replace(b'"./assets/', b'"assets/')


def claude_skill() -> bytes:
    """Add Claude's explicit-only frontmatter to the canonical instructions."""
    source = SKILL_SOURCE.read_bytes()
    frontmatter_end = source.find(b"\n---", 4)
    if not source.startswith(b"---\n") or frontmatter_end == -1:
        raise ValueError("canonical SKILL.md must have YAML frontmatter")
    return source[:frontmatter_end] + b"\ndisable-model-invocation: true" + source[frontmatter_end:]


def check() -> list[str]:
    """Return every missing, drifting, or symlinked generated copy."""
    errors: list[str] = []
    for source in source_files():
        if source.is_symlink():
            errors.append(f"canonical source must not be a symlink: {source.relative_to(ROOT)}")
            continue
        for root in DESTINATIONS:
            destination = root / source.relative_to(ROOT)
            if not destination.is_file():
                errors.append(f"missing generated copy: {destination.relative_to(ROOT)}")
            elif destination.is_symlink():
                errors.append(f"generated copy must not be a symlink: {destination.relative_to(ROOT)}")
            elif destination.read_bytes() != source.read_bytes():
                errors.append(f"generated copy drifted: {destination.relative_to(ROOT)}")
    adapted = {
        CODEX_DESTINATION / "SKILL.md": SKILL_SOURCE.read_bytes() if SKILL_SOURCE.is_file() else None,
        CLAUDE_DESTINATION / "SKILL.md": claude_skill() if SKILL_SOURCE.is_file() else None,
        CODEX_DESTINATION / "agents" / "openai.yaml": adapted_agent() if AGENT_SOURCE.is_file() else None,
        CLAUDE_DESTINATION / "agents" / "openai.yaml": adapted_agent() if AGENT_SOURCE.is_file() else None,
    }
    if not SKILL_SOURCE.is_file():
        errors.append("missing canonical SKILL.md")
    if not AGENT_SOURCE.is_file():
        errors.append("missing canonical agents/openai.yaml")
    for destination, expected in adapted.items():
        if expected is None:
            continue
        if not destination.is_file():
            errors.append(f"missing generated copy: {destination.relative_to(ROOT)}")
        elif destination.is_symlink():
            errors.append(f"generated copy must not be a symlink: {destination.relative_to(ROOT)}")
        elif destination.read_bytes() != expected:
            errors.append(f"generated copy drifted: {destination.relative_to(ROOT)}")
    expected_paths = expected_skill_paths()
    for root in DESTINATIONS:
        for path in sorted(root.rglob("*")):
            if path.is_file() and path.relative_to(root) not in expected_paths:
                errors.append(f"unexpected generated file: {path.relative_to(ROOT)}")
    for relative_path in PACKAGE_FILES:
        source = ROOT / relative_path
        for plugin_root in PLUGIN_ROOTS:
            destination = plugin_root / relative_path
            if not destination.is_file():
                errors.append(f"missing generated copy: {destination.relative_to(ROOT)}")
            elif destination.is_symlink():
                errors.append(f"generated copy must not be a symlink: {destination.relative_to(ROOT)}")
            elif destination.read_bytes() != source.read_bytes():
                errors.append(f"generated copy drifted: {destination.relative_to(ROOT)}")
    return errors


def sync() -> None:
    """Update only generated files whose canonical bytes have changed."""
    expected_paths = expected_skill_paths()
    for root in DESTINATIONS:
        for path in sorted(root.rglob("*"), reverse=True):
            if path.is_file() and path.relative_to(root) not in expected_paths:
                path.unlink()
            elif path.is_dir() and not any(path.iterdir()):
                path.rmdir()
    for root in DESTINATIONS:
        for source in source_files():
            destination = root / source.relative_to(ROOT)
            destination.parent.mkdir(parents=True, exist_ok=True)
            if not destination.is_file() or destination.read_bytes() != source.read_bytes():
                shutil.copyfile(source, destination)
    generated = {
        CODEX_DESTINATION / "SKILL.md": SKILL_SOURCE.read_bytes(),
        CLAUDE_DESTINATION / "SKILL.md": claude_skill(),
        CODEX_DESTINATION / "agents" / "openai.yaml": adapted_agent(),
        CLAUDE_DESTINATION / "agents" / "openai.yaml": adapted_agent(),
    }
    for destination, content in generated.items():
        destination.parent.mkdir(parents=True, exist_ok=True)
        if not destination.is_file() or destination.read_bytes() != content:
            destination.write_bytes(content)
    for relative_path in PACKAGE_FILES:
        source = ROOT / relative_path
        for plugin_root in PLUGIN_ROOTS:
            destination = plugin_root / relative_path
            if not destination.is_file() or destination.read_bytes() != source.read_bytes():
                shutil.copyfile(source, destination)


def main() -> int:
    """Synchronize by default, or check generated copies without mutating them."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        errors = check()
        if errors:
            print("\n".join(errors))
            return 1
        print("PASS plugin-skill-copies")
        return 0
    sync()
    print("SYNC plugin-skill-copies")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
