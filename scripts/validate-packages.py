#!/usr/bin/env python3
"""Validate Caddie's generated Claude Code and Codex packages."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_NAME = "caddie"
CANONICAL_SKILL = ROOT / "SKILL.md"
CODEX_PLUGIN_ROOT = ROOT / "plugins" / PLUGIN_NAME
CLAUDE_PLUGIN_ROOT = ROOT / "plugins" / "caddie-claude"
CODEX_SKILL = CODEX_PLUGIN_ROOT / "skills" / PLUGIN_NAME / "SKILL.md"
CLAUDE_SKILL = CLAUDE_PLUGIN_ROOT / "skills" / PLUGIN_NAME / "SKILL.md"
CODEX_MANIFEST = CODEX_PLUGIN_ROOT / ".codex-plugin" / "plugin.json"
CODEX_MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"
CLAUDE_MANIFEST = CLAUDE_PLUGIN_ROOT / ".claude-plugin" / "plugin.json"
CLAUDE_MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"


def load_json(path: Path, errors: list[str]) -> dict[str, Any] | None:
    """Return a JSON object or add one readable error."""
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"missing {path.relative_to(ROOT)}")
        return None
    except json.JSONDecodeError as error:
        errors.append(f"invalid JSON in {path.relative_to(ROOT)}: {error.msg}")
        return None
    if not isinstance(value, dict):
        errors.append(f"{path.relative_to(ROOT)} must contain a JSON object")
        return None
    return value


def is_archive_file(raw_path: Any) -> bool:
    """Check that a manifest asset resolves to a regular file inside this repo."""
    if not isinstance(raw_path, str):
        return False
    path = PurePosixPath(raw_path)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        return False
    candidate = CODEX_PLUGIN_ROOT / path
    return candidate.is_file() and not candidate.is_symlink()


def require(condition: bool, message: str, errors: list[str]) -> None:
    """Record an invariant failure without stopping subsequent diagnostics."""
    if not condition:
        errors.append(message)


def validate_packaged_skill(errors: list[str]) -> None:
    """Ensure both host packages are self-contained, synced bundle copies."""
    require(CANONICAL_SKILL.is_file(), "missing canonical SKILL.md", errors)
    for plugin_root in (CODEX_PLUGIN_ROOT, CLAUDE_PLUGIN_ROOT):
        license_path = plugin_root / "LICENSE"
        require(license_path.is_file(), f"missing {license_path.relative_to(ROOT)}", errors)
        if license_path.is_file():
            require(
                license_path.read_bytes() == (ROOT / "LICENSE").read_bytes(),
                f"{license_path.relative_to(ROOT)} drifted from LICENSE",
                errors,
            )
    require(CODEX_SKILL.is_file(), "missing Codex skills/caddie/SKILL.md", errors)
    require(CLAUDE_SKILL.is_file(), "missing Claude skills/caddie/SKILL.md", errors)
    if not CODEX_SKILL.is_file() or not CLAUDE_SKILL.is_file():
        return
    require(not CODEX_SKILL.is_symlink(), "Codex skills/caddie/SKILL.md must not be a symlink", errors)
    require(not CLAUDE_SKILL.is_symlink(), "Claude skills/caddie/SKILL.md must not be a symlink", errors)
    codex = CODEX_SKILL.read_text(encoding="utf-8")
    claude = CLAUDE_SKILL.read_text(encoding="utf-8")
    require(codex.startswith("---\nname: caddie\n"), "Codex skill must expose the caddie name", errors)
    require(claude.startswith("---\nname: caddie\n"), "Claude skill must expose the caddie name", errors)
    require(
        "disable-model-invocation" not in codex.split("---", 2)[1],
        "Codex skill must use agents/openai.yaml for explicit-only invocation",
        errors,
    )
    require(
        "disable-model-invocation: true" in claude.split("---", 2)[1],
        "Claude skill must disable implicit invocation",
        errors,
    )
    sync = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "sync-plugin-skill.py"), "--check"],
        check=False,
        capture_output=True,
        text=True,
    )
    require(sync.returncode == 0, sync.stdout.strip() or "plugin skill copy check failed", errors)


def validate_manifests(errors: list[str]) -> None:
    """Check the matching host manifests and both marketplace entries."""
    codex = load_json(CODEX_MANIFEST, errors)
    claude = load_json(CLAUDE_MANIFEST, errors)
    codex_marketplace = load_json(CODEX_MARKETPLACE, errors)
    claude_marketplace = load_json(CLAUDE_MARKETPLACE, errors)
    if codex is not None:
        require(codex.get("name") == PLUGIN_NAME, "Codex manifest name must be caddie", errors)
        require(codex.get("skills") == "./skills/", "Codex manifest must expose ./skills/", errors)
        interface = codex.get("interface")
        require(isinstance(interface, dict), "Codex manifest must have interface metadata", errors)
        if isinstance(interface, dict):
            for field in ("composerIcon", "logo"):
                require(
                    is_archive_file(interface.get(field)),
                    f"Codex interface.{field} must reference a non-symlink archive file",
                    errors,
                )
    if codex is not None and claude is not None:
        for field in ("name", "version", "description"):
            require(
                codex.get(field) == claude.get(field),
                f"Claude and Codex manifests disagree on {field}",
                errors,
            )
    if codex_marketplace is not None:
        plugins = codex_marketplace.get("plugins")
        require(codex_marketplace.get("name") == PLUGIN_NAME, "Codex marketplace name must be caddie", errors)
        require(isinstance(plugins, list) and len(plugins) == 1, "Codex marketplace must contain one plugin", errors)
        if isinstance(plugins, list) and len(plugins) == 1 and isinstance(plugins[0], dict):
            source = plugins[0].get("source")
            require(plugins[0].get("name") == PLUGIN_NAME, "Codex marketplace plugin name must be caddie", errors)
            require(isinstance(source, dict), "Codex marketplace plugin needs a source", errors)
            if isinstance(source, dict):
                require(source.get("source") == "local", "Codex marketplace source must be local to the marketplace", errors)
                require(source.get("path") == "./plugins/caddie", "Codex marketplace source must point at plugins/caddie", errors)
    if claude_marketplace is not None:
        plugins = claude_marketplace.get("plugins")
        require(claude_marketplace.get("name") == PLUGIN_NAME, "Claude marketplace name must be caddie", errors)
        metadata = claude_marketplace.get("metadata")
        require(
            isinstance(metadata, dict) and isinstance(metadata.get("description"), str) and metadata["description"].strip(),
            "Claude marketplace must have a metadata.description",
            errors,
        )
        require(isinstance(plugins, list) and len(plugins) == 1, "Claude marketplace must contain one plugin", errors)
        if isinstance(plugins, list) and len(plugins) == 1 and isinstance(plugins[0], dict):
            require(plugins[0].get("name") == PLUGIN_NAME, "Claude marketplace plugin name must be caddie", errors)
            require(
                plugins[0].get("source") == "./plugins/caddie-claude",
                "Claude marketplace source must point at plugins/caddie-claude",
                errors,
            )


def main() -> int:
    """Run all package invariants and print one concise result."""
    errors: list[str] = []
    validate_packaged_skill(errors)
    validate_manifests(errors)
    if errors:
        print("\n".join(errors))
        return 1
    print("PASS packages hosts=claude,codex skill-copy=synced")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
