---
name: project-pr-description
description: 根据任务目标、设计记录、代码 diff、文档影响和测试证据生成或更新中文 PR 描述。用于创建 PR、变更后更新描述、stacked PR 和审查回复；不替作者决定未验证事实。
---

# 项目 PR 描述

PR 描述是变更证据的入口，不是实现流水账。它只描述当前 PR 相对自身 base 的内容。

## 先读什么

读取完整 diff、任务/Issue、设计记录、`project-change-sync` 报告、测试输出、升级影响和项目 PR 模板。读取 [章节规则](references/section-rules.md)、[AI 使用说明](references/ai-usage.md)、[PR 模板](templates/pr-body.md) 和 [评估场景](evals/evals.json)。

## 固定结构

项目没有既有格式时使用四个二级章节：

```text
## Motivation
## Changes
## Testing
## AI Usage
```

中文正文可以保留项目规定的固定英文标题，必须说明目标、Issue/上下文、接口变化、行为变化、文档/契约/升级影响、测试设计、已运行测试、未验证项、风险和 AI 参与决策。

## 工作流

1. 确认 PR base、stack layer 和 changed paths；
2. 从任务、设计和 diff 写一句目标及 before/after；
3. 将接口变化和行为变化分开，明确写 `None` 或不适用；
4. 按变化类型写测试设计：行为矩阵、性能基准、无行为重构对比或文档检查；
5. 每个已运行测试单独列命令、来源（local/CI）、结果和 proof；不把未运行的测试写入通过列表；
6. 披露 generated、双语、UI、升级、预算和设计偏差；
7. 写 AI Usage 的 breakdown/design/testing/implementation/review 阶段、参与度和人工决定；
8. PR 更新后重新读取描述，删除已过期事实，只修改受影响章节。

## 边界

不把审查意见、CI 计划或推断当成已完成结果，不把 AI 参与替代代码、测试或文档证据。默认只生成草案，不直接发布 PR。
