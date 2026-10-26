# Changelog

## v1.1.1 — 2026-10-25

- **可发现性修复**：README 目录表、design-tokens、review-checklist、AGENTS 示例补齐所有分项文档入口；accessibility、exceptions-versioning、platform-philosophy、Foundations 分项、05-platforms 分项、tailwind-tokens 不再是孤立文档。AGENTS 必读清单加入 accessibility.md。
- **Token 总表补齐既有数值**（仅同步总表，不改变规则）：`type.label`、`type.micro`、`layout.width.detail=880px`、`size.row.list=44–52px`、`size.icon.visual=16–24px`。
- adapters 新增“规范概念 → shadcn/ui 组件”映射表；明确 Action Sheet / Bottom Sheet 对应 `drawer`（经官方文档核实：shadcn 组件现默认基于 Base UI，提供 Base UI / React Aria / Radix 变体，Drawer 已从 vaul 迁移至 Base UI），并补充官方组合组件映射（`sidebar`/`field`/`empty`/`command`）。
- 新增 CC BY 4.0 许可证，匹配“复制规范到项目”的分发方式。

## v1.1.0 — 2026-10-25

- **Breaking (documentation structure)**：从 v1.0 的“规范 + TSX 示例”调整为 Specification First；从仓库核心移除 React 组件源码。
- Patterns 采用 `overview.md`（共享） + `desktop.md` + `mobile.md`，覆盖 Settings、List、Detail、Form、Navigation、Overlays。
- 增加输入方式、导航适配、窗口宽度与触摸密度解耦、例外审批、跨平台 Do/Don't 和文字页面示例。
- 工程落地仅作为 `adapters/` 中的可选指导，Design Tokens 为语言中立的规范值。
- v1.0 的 `04-patterns/settings.md` → `04-patterns/settings/overview.md` 等；建议按 [README](README.md) 的入口更新旧 `AGENTS.md` 引用。

## v1.0.0 — 2026-10-25

- 首个多文件版本，含设计基础、组件与工程实践以及 Settings TSX 示例。
