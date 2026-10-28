#!/usr/bin/env python3
"""Validate skill structure without executing skill instructions or examples."""

import argparse
import ast
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

try:
    import yaml
    from markdown_it import MarkdownIt
except ImportError as exc:
    print(
        f"Missing dependency: {exc.name}. "
        "Install requirements-dev.txt in a virtual environment.",
        file=sys.stderr,
    )
    sys.exit(2)


MARKDOWN = MarkdownIt("commonmark")
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
PR_SECTIONS = ["Motivation", "Changes", "Testing", "AI Usage"]


def reject_json_constant(value):
    raise ValueError(f"non-standard JSON constant: {value}")


class Validator:
    def __init__(self):
        self.errors = []
        self.files = 0
        self.links = 0

    def error(self, path, message, line=None):
        location = f"{path}:{line}" if line else str(path)
        self.errors.append(f"{location}: {message}")

    def read(self, path):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            self.error(path, str(exc))
            return None
        self.files += 1
        return text

    def frontmatter(self, path, text, required=False):
        lines = text.splitlines(keepends=True)
        if not lines or lines[0].strip() != "---":
            if required:
                self.error(path, "YAML frontmatter must start on the first line")
            return {}, text, 0
        end = next(
            (i for i in range(1, len(lines)) if lines[i].strip() == "---"), None
        )
        if end is None:
            self.error(path, "YAML frontmatter has no closing delimiter")
            return {}, text, 0
        try:
            data = yaml.safe_load("".join(lines[1:end]))
            if not isinstance(data, dict):
                raise ValueError("frontmatter must be a mapping")
        except (yaml.YAMLError, ValueError) as exc:
            self.error(path, f"invalid frontmatter: {exc}")
            data = {}
        return data, "".join(lines[end + 1 :]), end + 1

    def check_link(self, source, target, boundary, line):
        try:
            url = urlsplit(target)
            if url.scheme == "file" or re.match(r"^[A-Za-z]:[\\/]", target):
                self.error(source, f"non-portable local link: {target}", line)
                return
            if url.scheme or url.netloc or not url.path:
                return
            self.links += 1
            local = Path(unquote(url.path))
            if local.is_absolute():
                self.error(source, f"absolute local link: {target}", line)
                return
            resolved = (source.parent / local).resolve()
            if not resolved.is_relative_to(boundary):
                self.error(source, f"link leaves distribution boundary: {target}", line)
            elif not resolved.exists():
                self.error(source, f"missing local link target: {target}", line)
        except (OSError, RuntimeError, ValueError) as exc:
            self.error(source, f"invalid local link {target!r}: {exc}", line)

    def check_tokens(self, path, tokens, boundary, offset=0, line=1):
        for token in tokens:
            token_line = offset + token.map[0] + 1 if token.map else line
            attribute = {"link_open": "href", "image": "src"}.get(token.type)
            if attribute:
                target = token.attrGet(attribute)
                if target:
                    self.check_link(path, target, boundary, token_line)
            if token.children:
                self.check_tokens(path, token.children, boundary, offset, token_line)

    def check_file(self, path, boundary, skill_name=None):
        text = self.read(path)
        if text is None:
            return
        suffix = path.suffix.lower()
        try:
            if suffix == ".json":
                json.loads(text, parse_constant=reject_json_constant)
            elif suffix in {".yaml", ".yml"}:
                list(yaml.safe_load_all(text))
            elif suffix == ".py":
                ast.parse(text, filename=str(path))
            elif suffix == ".md":
                entry = skill_name is not None and path.name == "SKILL.md"
                upgrade = (
                    skill_name == "project-upgrade-guide"
                    and path.parent.name == "templates"
                    and path.name == "upgrade-guide.md"
                )
                data, body, offset = self.frontmatter(path, text, entry or upgrade)
                if entry:
                    name = data.get("name")
                    if (
                        not isinstance(name, str)
                        or not NAME.fullmatch(name)
                        or len(name) > 64
                        or name != skill_name
                    ):
                        self.error(path, "name must be kebab-case and match the skill directory")
                    description = data.get("description")
                    if not isinstance(description, str) or not description.strip():
                        self.error(path, "description must be a non-empty string")
                if upgrade:
                    if data.get("kind") != "upgrade-guide":
                        self.error(path, "template kind must be upgrade-guide")
                    if not isinstance(data.get("description"), str) or not data["description"].strip():
                        self.error(path, "upgrade template needs a description")
                tokens = MARKDOWN.parse(body)
                self.check_tokens(path, tokens, boundary, offset)
                if (
                    skill_name == "project-pr-description"
                    and path.parent.name == "templates"
                    and path.name == "pr-body.md"
                ):
                    sections = [
                        tokens[i + 1].content
                        for i, token in enumerate(tokens)
                        if token.type == "heading_open" and token.tag == "h2"
                    ]
                    if sections != PR_SECTIONS:
                        self.error(path, f"default PR sections must be {PR_SECTIONS}; got {sections}")
        except (ValueError, yaml.YAMLError, SyntaxError) as exc:
            self.error(path, f"invalid {suffix} syntax: {exc}")

    def check_skill(self, folder):
        if not folder.is_dir():
            self.error(folder, "skill directory does not exist")
            return
        boundary = folder.resolve()
        required = ["SKILL.md"]
        if not any((folder / name).is_file() for name in ("NOTICE", "LICENSE")):
            self.error(folder, "required distribution file is missing: NOTICE or LICENSE")
        if folder.name == "project-pr-description":
            required.append("templates/pr-body.md")
        if folder.name == "project-upgrade-guide":
            required.append("templates/upgrade-guide.md")
        for name in required:
            if not (folder / name).is_file():
                self.error(folder / name, "required distribution file is missing")
        for path in sorted(folder.rglob("*")):
            if path.is_symlink():
                try:
                    if not path.resolve().is_relative_to(boundary) or not path.exists():
                        self.error(path, "broken symlink or dependency outside skill directory")
                        continue
                except (OSError, RuntimeError) as exc:
                    self.error(path, f"invalid symlink: {exc}")
                    continue
            if path.is_file() and path.suffix.lower() in {".md", ".json", ".yaml", ".yml", ".py"}:
                self.check_file(path, boundary, folder.name)

    def check_repository(self, root):
        for name in ("README.md", "CHANGELOG.md", "LICENSE"):
            if not (root / name).is_file():
                self.error(root / name, "required repository file is missing")
        for path in sorted(root.glob("*.md")):
            self.check_file(path, root)
        for path in sorted((root / "scripts").rglob("*.py")):
            self.check_file(path, root)
        skills_root = root / "skills"
        if not skills_root.is_dir():
            self.error(skills_root, "skills directory does not exist")
            return []
        folders = sorted(p for p in skills_root.iterdir() if p.is_dir() and not p.name.startswith("."))
        if not folders:
            self.error(skills_root, "no skill directories found")
        for folder in folders:
            self.check_skill(folder)
        return folders


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--root", type=Path, help="repository root (defaults to this script's repository)")
    group.add_argument("--skill", type=Path, help="validate one independently installed skill directory")
    args = parser.parse_args()
    validator = Validator()
    if args.skill is not None:
        folder = args.skill.expanduser().absolute()
        validator.check_skill(folder)
        count = 1
    else:
        root = (args.root or Path(__file__).resolve().parents[1]).expanduser().resolve()
        count = len(validator.check_repository(root))
    for error in validator.errors:
        print(f"ERROR {error}", file=sys.stderr)
    print(
        f"Checked {count} skill(s), {validator.files} file(s), "
        f"{validator.links} local link(s); {len(validator.errors)} error(s)."
    )
    return 1 if validator.errors else 0


if __name__ == "__main__":
    sys.exit(main())
