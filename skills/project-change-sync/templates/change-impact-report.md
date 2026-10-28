# 变更影响

## 1. 范围和预检

- Base/head 或 worktree：
- Scope command、输出、dirty layers 和重跑记录：
- changed paths（含 rename/delete/untracked）：
- 排除项和失败：

## 2. 路径影响

| 路径 | canonical owner | configured/declared/inferred | contract delta | 状态 | 证据 | 置信度 |
|---|---|---|---|---|---|---|
| `path` | `<owner>` | `<mode>` | `<变化>` | covered/not-needed/review-required/missing | `<path/command>` | high/medium/low |

## 3. 设计和事实

- 设计验收项与实现：
- 项目生命周期与交付状态同步：
- 当前文档准确性：
- 历史、拒绝和未实现记录的排除情况：

## 4. 派生物和门禁

| 门禁/生成器 | 命令 | 结果 | 未验证原因 |
|---|---|---|---|
| `<gate>` | `<command>` | pass/fail/not-run | `<reason>` |

## 5. 事故、规范、契约和升级

<!-- 仅保留相关项；区分项目要求的同步与新的改进建议，不要求新建记录。 -->

- 事故或缺陷经验及已有记录：
- 规范候选或已有规则、范围和采纳依据：
- 检测办法、实际结果、覆盖局限与待满足条件：
- 项目要求的同步、可选建议和待决定项：
- 契约重新生成或升级指南：

## 6. 结论和人工决定
