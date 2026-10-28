# 变更影响报告

## 范围

- Base/head 或 worktree basis：
- Scope command、输出和重跑记录：
- changed paths（含 rename/delete/untracked）：
- 排除项：

## 路径影响

| 路径 | canonical owner | owner resolution | contract delta | 状态 | 证据/置信度 |
|---|---|---|---|---|---|
| `path` | `<实际 owner>` | configured/declared/inferred | `<变化>` | covered/not-needed/review-required/missing | `<diff/test/gate>` / high/medium/low |

## 设计和当前事实

- 项目设计生命周期、记录和验收项：
- 实现状态和偏差是否按项目规则同步：
- 当前路径/机制是否准确：
- 历史、拒绝或未实现决定是否被错误当作当前依据：

## 派生物和门禁

| 门禁/生成器 | 是否需要 | 命令 | 结果 | 未验证原因 |
|---|---|---|---|---|
| generated/type-equiv/doc-typecheck/i18n/snapshot/contract/doc-sync | yes/no | `<command>` | pass/fail/not-run | `<reason>` |

## Lessons/事故/升级影响

- 事故或可复用缺陷：
- 是否需要 postmortem、规范、升级指南或契约迁移：

`missing` 或 `review-required` 是审查发现，不是自动重写授权。
