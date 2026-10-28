#!/usr/bin/env python3
"""Validate a project-workflow YAML definition."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - maintenance dependency guard
    print(
        f"Missing dependency: {exc.name}. Install requirements-dev.txt.",
        file=sys.stderr,
    )
    raise SystemExit(2) from exc


NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
PROVIDERS = {"matt", "superpowers"}
REQUIRED_POLICY = {
    "immutable": True,
    "update_requires_explicit_request": True,
    "missing_definition": "require_create",
    "missing_skill": "stop_and_report",
    "unknown_entrypoint": "stop_and_report",
}


class Validator:
    def __init__(self, path: Path):
        self.path = path
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, location: str, message: str) -> None:
        self.errors.append(f"{location}: {message}")

    def warning(self, location: str, message: str) -> None:
        self.warnings.append(f"{location}: {message}")

    def require_mapping(self, value: Any, location: str) -> dict[str, Any] | None:
        if not isinstance(value, dict):
            self.error(location, "must be a mapping")
            return None
        return value

    def require_string(self, value: Any, location: str) -> str | None:
        if not isinstance(value, str) or not value.strip():
            self.error(location, "must be a non-empty string")
            return None
        return value

    def check_name(self, value: Any, location: str) -> str | None:
        name = self.require_string(value, location)
        if name is not None and not NAME.fullmatch(name):
            self.error(location, "must use lowercase kebab-case")
        return name

    def check_skill_ref(self, value: Any, location: str) -> None:
        item = self.require_mapping(value, location)
        if item is None:
            return
        self.require_string(item.get("source"), f"{location}.source")
        self.check_name(item.get("skill"), f"{location}.skill")

    def check_stage(self, stage: Any, location: str) -> tuple[str | None, bool, list[str]]:
        item = self.require_mapping(stage, location)
        if item is None:
            return None, False, []
        stage_id = self.check_name(item.get("id"), f"{location}.id")
        self.require_string(item.get("description"), f"{location}.description")
        required = item.get("required")
        if not isinstance(required, bool):
            self.error(f"{location}.required", "must be a boolean")
            required = False

        activate = item.get("activate")
        if not isinstance(activate, list) or not activate:
            self.error(f"{location}.activate", "must be a non-empty list")
        else:
            for index, ref in enumerate(activate):
                self.check_skill_ref(ref, f"{location}.activate[{index}]")

        when = item.get("when")
        if not required and not when:
            self.error(
                location,
                "optional stage must define when or an explicit selection path",
            )
        if when is not None and not isinstance(when, (str, list)):
            self.error(f"{location}.when", "must be a string or list")

        for field in ("consumes", "produces"):
            values = item.get(field)
            if values is not None:
                if not isinstance(values, list) or not all(
                    isinstance(value, str) and value.strip() for value in values
                ):
                    self.error(f"{location}.{field}", "must be a list of strings")

        conditional = item.get("conditional")
        if conditional is not None:
            if not isinstance(conditional, list):
                self.error(f"{location}.conditional", "must be a list")
            else:
                for index, entry in enumerate(conditional):
                    entry_location = f"{location}.conditional[{index}]"
                    condition = self.require_mapping(entry, entry_location)
                    if condition is None:
                        continue
                    self.require_string(condition.get("when"), f"{entry_location}.when")
                    nested = condition.get("activate")
                    if not isinstance(nested, list) or not nested:
                        self.error(
                            f"{entry_location}.activate",
                            "must be a non-empty list",
                        )
                    else:
                        for nested_index, ref in enumerate(nested):
                            self.check_skill_ref(
                                ref, f"{entry_location}.activate[{nested_index}]"
                            )

        consumes = item.get("consumes") or []
        produces = item.get("produces") or []
        return stage_id, required, consumes + produces

    def check(self) -> None:
        try:
            data = yaml.safe_load(self.path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError) as exc:
            self.error(str(self.path), str(exc))
            return
        except yaml.YAMLError as exc:
            self.error(str(self.path), f"invalid YAML: {exc}")
            return

        root = self.require_mapping(data, "root")
        if root is None:
            return
        if root.get("version") != 1:
            self.error("version", "must be the integer 1")

        workflow = self.require_mapping(root.get("workflow"), "workflow")
        if workflow is None:
            return
        self.check_name(workflow.get("id"), "workflow.id")
        self.require_string(workflow.get("description"), "workflow.description")
        provider = self.require_string(workflow.get("provider"), "workflow.provider")
        if provider is not None and provider not in PROVIDERS:
            self.error("workflow.provider", f"must be one of {sorted(PROVIDERS)}")

        policy = self.require_mapping(workflow.get("policy"), "workflow.policy")
        if policy is None:
            return
        for key, expected in REQUIRED_POLICY.items():
            if policy.get(key) != expected:
                self.error(f"workflow.policy.{key}", f"must be {expected!r}")
        if not isinstance(policy.get("allow_direct_skill_for_simple_tasks"), bool):
            self.error(
                "workflow.policy.allow_direct_skill_for_simple_tasks",
                "must be a boolean",
            )

        entrypoints = self.require_mapping(
            workflow.get("entrypoints"), "workflow.entrypoints"
        )
        flows = self.require_mapping(workflow.get("flows"), "workflow.flows")
        if entrypoints is None or flows is None:
            return

        for entrypoint, flow_id in entrypoints.items():
            self.check_name(entrypoint, f"workflow.entrypoints.{entrypoint}")
            if not isinstance(flow_id, str) or flow_id not in flows:
                self.error(
                    f"workflow.entrypoints.{entrypoint}",
                    "must reference an existing flow",
                )

        for flow_id, flow in flows.items():
            location = f"workflow.flows.{flow_id}"
            self.check_name(flow_id, location)
            flow_mapping = self.require_mapping(flow, location)
            if flow_mapping is None:
                continue
            self.require_string(flow_mapping.get("description"), f"{location}.description")
            stages = flow_mapping.get("stages")
            if not isinstance(stages, list) or not stages:
                self.error(f"{location}.stages", "must be a non-empty list")
                continue

            seen: set[str] = set()
            available: set[str] = set()
            for index, stage in enumerate(stages):
                stage_id, _required, artifacts = self.check_stage(
                    stage, f"{location}.stages[{index}]"
                )
                if stage_id is not None:
                    if stage_id in seen:
                        self.error(
                            f"{location}.stages[{index}].id",
                            f"duplicate stage id {stage_id!r}",
                        )
                    seen.add(stage_id)
                item = stage if isinstance(stage, dict) else {}
                for artifact in item.get("consumes", []) if isinstance(item, dict) else []:
                    if artifact not in available:
                        self.warning(
                            f"{location}.stages[{index}].consumes",
                            f"artifact {artifact!r} is not produced by an earlier stage",
                        )
                if isinstance(item, dict):
                    available.update(item.get("produces") or [])

    def result(self) -> dict[str, Any]:
        return {
            "file": str(self.path),
            "errors": self.errors,
            "warnings": self.warnings,
            "ok": not self.errors,
        }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path, help="workflow YAML definition")
    parser.add_argument("--json", action="store_true", help="emit JSON output")
    args = parser.parse_args()

    validator = Validator(args.file.expanduser().resolve())
    validator.check()
    result = validator.result()
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Workflow: {result['file']}")
        for warning in result["warnings"]:
            print(f"WARNING {warning}")
        for error in result["errors"]:
            print(f"ERROR {error}", file=sys.stderr)
        print("Result: PASS" if result["ok"] else "Result: FAIL")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
