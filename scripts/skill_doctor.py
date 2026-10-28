#!/usr/bin/env python3
"""Check owner-skills installation health in a consumer project."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True, type=Path, help="consumer project root")
    parser.add_argument("--json", action="store_true", dest="as_json", help="emit JSON output")
    return parser.parse_args()


def read_frontmatter(path: Path) -> tuple[str | None, str | None]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return None, None
    try:
        end = next(index for index, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration:
        return None, None
    values = {}
    for line in lines[1:end]:
        key, separator, value = line.partition(":")
        if separator:
            values[key.strip()] = value.strip().strip('"\'')
    return values.get("name"), values.get("description")


def main() -> int:
    args = parse_args()
    target = args.target.expanduser().resolve()
    skills_root = target / ".agents" / "skills"
    errors: list[str] = []
    warnings: list[str] = []
    skills: list[str] = []

    if not target.is_dir():
        errors.append(f"target project does not exist: {target}")
    elif not skills_root.is_dir():
        errors.append(f"skill directory is missing: {skills_root}")
    else:
        for path in sorted(skills_root.iterdir()):
            if path.name.startswith("."):
                continue
            skills.append(path.name)
            if path.is_symlink() and not path.exists():
                errors.append(f"broken skill symlink: {path}")
                continue
            if not path.is_dir():
                errors.append(f"skill entry is not a directory: {path}")
                continue
            skill_file = path / "SKILL.md"
            if not skill_file.is_file():
                errors.append(f"missing SKILL.md: {path}")
                continue
            try:
                name, description = read_frontmatter(skill_file)
            except (OSError, UnicodeError) as exc:
                errors.append(f"cannot read {skill_file}: {exc}")
                continue
            if name != path.name or not NAME.fullmatch(name or ""):
                errors.append(f"frontmatter name does not match directory: {skill_file}")
            if not description:
                errors.append(f"frontmatter description is empty: {skill_file}")
            if not ((path / "NOTICE").is_file() or (path / "LICENSE").is_file()):
                errors.append(f"missing NOTICE or LICENSE: {path}")

    record_path = target / ".agents" / "owner-skills.json"
    record = None
    if record_path.is_file():
        try:
            record = json.loads(record_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid installation record: {record_path}: {exc}")
    elif skills:
        warnings.append(f"installation record is missing: {record_path}")

    result = {
        "target": str(target),
        "skills": skills,
        "record": record,
        "warnings": warnings,
        "errors": errors,
        "ok": not errors,
    }
    if args.as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Target: {target}")
        print(f"Skills: {', '.join(skills) if skills else '(none)'}")
        for warning in warnings:
            print(f"WARNING {warning}")
        for error in errors:
            print(f"ERROR {error}", file=sys.stderr)
        print("Result: PASS" if not errors else "Result: FAIL")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
