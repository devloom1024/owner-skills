#!/usr/bin/env python3
"""Install selected owner-skills into a consumer project's .agents/skills."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True, type=Path, help="consumer project root")
    parser.add_argument(
        "--profile",
        choices=("core", "quality", "ui", "full"),
        default="core",
        help="predefined skill profile (default: core)",
    )
    parser.add_argument(
        "--skill",
        action="append",
        dest="skills",
        help="install one skill; repeat for multiple skills (overrides --profile)",
    )
    parser.add_argument(
        "--mode",
        choices=("copy", "link"),
        default="copy",
        help="copy files or create symlinks (default: copy)",
    )
    parser.add_argument(
        "--replace",
        action="store_true",
        help="replace an existing installed skill after checking its path",
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=ROOT,
        help="local owner-skills checkout (default: this checkout)",
    )
    return parser.parse_args()


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Unable to read {path}: {exc}") from exc


def remove_existing(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.exists():
        shutil.rmtree(path)


def main() -> int:
    args = parse_args()
    source = args.source.expanduser().resolve()
    target = args.target.expanduser().resolve()
    profiles = read_json(source / "profiles.json")
    plugin = read_json(source / ".codex-plugin" / "plugin.json")

    if not target.is_dir():
        print(f"Target project does not exist: {target}", file=sys.stderr)
        return 2
    if source == target:
        print("Refusing to install owner-skills into its own source checkout.", file=sys.stderr)
        return 2

    selected = args.skills or profiles[args.profile]
    if not selected:
        print("No skills selected.", file=sys.stderr)
        return 2

    skills_root = source / "skills"
    destination_root = target / ".agents" / "skills"
    destination_root.mkdir(parents=True, exist_ok=True)
    installed = []

    for name in dict.fromkeys(selected):
        skill_source = skills_root / name
        destination = destination_root / name
        if not (skill_source / "SKILL.md").is_file():
            print(f"Skill does not exist: {name}", file=sys.stderr)
            return 2
        if destination.is_symlink() and destination.resolve() == skill_source:
            installed.append(name)
            print(f"Already linked: {name}")
            continue
        if destination.is_symlink() or destination.exists():
            if not args.replace:
                print(
                    f"Destination already exists: {destination}; use --replace to replace it.",
                    file=sys.stderr,
                )
                return 2
            remove_existing(destination)

        if args.mode == "link":
            os.symlink(skill_source, destination, target_is_directory=True)
        else:
            shutil.copytree(skill_source, destination)
        installed.append(name)
        print(f"Installed {name} ({args.mode})")

    record_path = target / ".agents" / "owner-skills.json"
    previous = {}
    if record_path.is_file():
        try:
            previous = json.loads(record_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            previous = {}
    all_skills = list(dict.fromkeys(previous.get("skills", []) + installed))
    record = {
        "name": plugin.get("name", "owner-skills"),
        "version": plugin.get("version"),
        "source": str(source),
        "skills": all_skills,
        "last_install": {
            "profile": None if args.skills else args.profile,
            "mode": args.mode,
            "skills": installed,
            "installed_at": datetime.now(timezone.utc).isoformat(),
        },
    }
    record_path.write_text(
        json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Recorded installation at {record_path}")
    print("Restart the host if the newly installed skills do not appear.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
