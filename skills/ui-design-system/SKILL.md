---
name: ui-design-system
description: Apply and review a specification-first, cross-platform UI design system for implementing, auditing, or extending product interfaces across desktop, mobile, touch, keyboard, and responsive layouts. Use it for design decisions and UI implementation guidance, not as a React component library or pixel-perfect asset pack.
metadata:
  short-description: Cross-platform UI design and review
---

# UI Design System

Use this skill when a UI task needs consistent patterns, design tokens, platform adaptation, accessibility checks, or a documented exception. The reference tree is a normative design specification; it is not a drop-in component library.

## Workflow

1. Identify the task mode: implement a UI, review/audit an existing UI, or extend the system (new Pattern, Token, or adapter).
2. Identify the primary Pattern, runtime/platform, available container space, and input modes. Do not equate a narrow window with a phone or a touch screen with a small layout.
3. Apply this priority order when guidance conflicts: accessibility and platform constraints, global Tokens and component semantics, Pattern `overview.md`, Pattern `desktop.md`/`mobile.md`, then a documented project exception.
4. Read only the references needed for the mode and Pattern. Keep examples and technology adapters conditional.
5. Implement or review against the selected references, then report the Pattern, references used, reused components/Tokens, tested viewport and input conditions, states checked, and exceptions.

## Reference Routing

Start with [the design-system index](references/design-system/README.md), then load the shared references below.

| Task | Shared references | Conditional references |
|---|---|---|
| Implement a page | `01-principles/design-philosophy.md`, `01-principles/platform-philosophy.md`, `02-foundations/design-tokens.md`, `03-components/overview.md`, `05-platforms/responsive.md`, `05-platforms/input-methods.md`, `06-governance/accessibility.md`, `06-governance/review-checklist.md` | The selected Pattern's `overview.md`, `desktop.md`, and `mobile.md`; adapters only for the chosen stack |
| Review or audit UI | `01-principles/design-philosophy.md`, `02-foundations/design-tokens.md`, `05-platforms/responsive.md`, `05-platforms/input-methods.md`, `06-governance/accessibility.md`, `06-governance/review-checklist.md` | The selected Pattern files and examples when they clarify the finding |
| Extend a Pattern or Token | `README.md`, the relevant principles, `02-foundations/design-tokens.md`, `06-governance/exceptions-versioning.md` | The closest existing Pattern, affected platform files, examples, and adapters |
| React/shadcn/Tailwind implementation | The shared references for the selected task | `adapters/react-shadcn.md` and/or `adapters/tailwind-tokens.md` |

Pattern references live under `references/design-system/04-patterns/<pattern>/`. Examples under `07-examples/` are structural guidance, not mandatory templates.

## Single Source of Truth

- Use this installed Skill as the only UI design-system source. Read the references through the paths above; do not create or maintain a second copy under the product repository.
- `AGENTS.example.md` is an optional project contract for invoking this Skill. It does not replace `SKILL.md` or duplicate the reference documents.

## Normative Strength

Treat accessibility requirements, semantic behavior, keyboard reachability, focus handling, and platform safety constraints as required. Treat dimensions, breakpoints, density, and visual values described as recommended baselines as defaults that may be adapted when the project records the reason, impact, owner, and review condition using the exceptions template.

## Completion Report

For implementation or review work, include:

- Pattern and Shared/Desktop/Mobile references used.
- Reused components and Tokens, plus any new semantic value.
- Container widths, input modes, theme/zoom, and states verified.
- Accessibility and keyboard/touch checks.
- Exceptions and their rationale; write “none” when there are no exceptions.
