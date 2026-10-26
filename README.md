# owner-skills

Codex skills maintained by `devloom1024`.

## Included Skills

### `ui-design-system`

Specification-first UI design guidance for implementing and reviewing cross-platform interfaces across desktop, mobile, touch, keyboard, and responsive layouts.

The skill provides:

- Design principles and platform adaptation rules.
- Semantic design tokens for typography, spacing, color, radius, motion, focus, elevation, and safe areas.
- Shared `Settings`, `List`, `Detail`, `Form`, `Navigation`, and `Overlays` patterns with Desktop/Mobile guidance.
- Accessibility, state handling, review checklists, and exception governance.
- Optional React, shadcn/ui, and Tailwind adapters.

It is a design specification, not a React component library or a collection of pixel-perfect assets.

## Usage

Install or register the skill directory:

```text
skills/ui-design-system/
```

Then invoke it with:

```text
$ui-design-system
```

The skill is the single source of truth for this UI system. It loads the relevant references from its own `references/design-system/` directory as needed; projects should not maintain a second copy of the design-system documents.

## Validation

Validate the skill package with the Codex skill validator:

```bash
python3 /Users/huangkl/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  skills/ui-design-system
```

## License

The UI design-system reference documents are licensed under [CC BY 4.0](skills/ui-design-system/LICENSE).
