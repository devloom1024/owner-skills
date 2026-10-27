---
name: project-change-sync
description: 检查代码、配置、契约和设计变更是否同步到当前事实文档、包 README、Agent Notes、规范、Lessons、指南和契约入口。用于 PR、commit 和工作树审计；默认只读，不自动改文档。
---

# 代码变更同步

把变更路径映射到文档所有者，判断同步状态。文档修改交给 `project-docs`，设计生命周期交给 `project-design-notes`。

## 工作流

1. 固定并验证 base/head；没有提供时报告 worktree 范围。
2. 读取根和祖先 `AGENTS.md`、设计记录、当前子系统、包 README、规范和项目映射。
3. 收集全部 changed paths，不只检查 Markdown；包括源码、测试、配置、契约、生成器和脚本。
4. 为每条路径找到候选所有者，并标注证据和置信度。
5. 结合 diff、公开 API、状态、失败、兼容性、测试和任务描述判断语义影响。
6. 检查 proposed 设计、implemented 决策、subsystem 和 README 是否与实现一致。
7. 检查是否需要 Lesson、规范提升、契约重新生成或升级指南。
8. 使用 [变更矩阵](references/update-matrix.md) 输出 `covered`、`not-needed`、`review-required` 或 `missing`。

## 状态

- `covered`：所有者已更新，或证据证明契约未变。
- `not-needed`：纯内部变化且证据充分。
- `review-required`：可能有语义变化但无法安全判断。
- `missing`：疑似改变契约且没有所有者更新或理由。

## 边界

不把设计记录当实现证据，不把代码 diff 当语义变化的唯一证据，不把 observed 规范提升为 adopted，也不自动编辑项目文件。
