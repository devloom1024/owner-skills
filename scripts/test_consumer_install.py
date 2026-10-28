#!/usr/bin/env python3
"""Smoke-test installation into an isolated consumer project."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "scripts" / "install_skills.py"
DOCTOR = ROOT / "scripts" / "skill_doctor.py"
WORKFLOW_VALIDATOR = ROOT / "scripts" / "validate_workflow.py"
WORKFLOW_TEMPLATE = ROOT / "skills" / "project-workflow" / "templates" / "workflow.yaml"


def run(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        cwd=ROOT,
        check=check,
        text=True,
        capture_output=True,
    )


def main() -> int:
    workflow = run(str(WORKFLOW_VALIDATOR), str(WORKFLOW_TEMPLATE), "--json")
    assert json.loads(workflow.stdout)["ok"] is True

    with tempfile.TemporaryDirectory(prefix="owner-skills-consumer-") as directory:
        target = Path(directory)
        run(str(INSTALLER), "--target", str(target), "--profile", "core")
        doctor = run(str(DOCTOR), "--target", str(target), "--json")
        result = json.loads(doctor.stdout)
        expected = {
            "project-workflow",
            "project-docs",
            "project-code-review",
            "project-change-sync",
        }
        assert set(result["skills"]) == expected, result
        assert result["ok"] is True, result

        duplicate = run(
            str(INSTALLER),
            "--target",
            str(target),
            "--skill",
            "project-code-review",
            check=False,
        )
        assert duplicate.returncode != 0, duplicate.stdout

        run(
            str(INSTALLER),
            "--target",
            str(target),
            "--skill",
            "project-code-review",
            "--replace",
        )
        run(
            str(INSTALLER),
            "--target",
            str(target),
            "--profile",
            "ui",
            "--mode",
            "link",
        )
        final = json.loads(run(str(DOCTOR), "--target", str(target), "--json").stdout)
        assert set(final["skills"]) == expected | {"ui-design-system"}, final
        assert final["ok"] is True, final

    print("Consumer installation smoke test passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
