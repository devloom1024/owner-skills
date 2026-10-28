---
name: project-change-sync
description: 检查代码、配置、契约、生成器和设计变更是否同步到正确的当前事实、包 README、Agent Notes、规范、postmortem、指南、契约和升级记录。用于 PR、commit、worktree 和 retarget 后审计；默认只读，不自动改文档。
---

# 代码变更同步

把完整变更范围映射到 canonical owners，判断每条路径的文档同步状态。文档修改交给 `project-docs`，设计生命周期交给 `project-design-notes`；本 Skill 只分析和报告。

## 读取参考资料

按任务读取：

1. [范围预检](references/scope-preflight.md)；
2. [来源与所有权](references/ownership-mapping.md)；
3. [更新矩阵](references/update-matrix.md)；
4. [变更影响报告](references/change-impact-report.md)；
5. [报告模板](templates/change-impact-report.md) 和 [项目映射模板](templates/docs-governance.yml)。

## 工作流

1. **固定范围**：优先验证 PR base/exact head。项目有 `change-scope` 命令时先运行它；没有 PR 时分别记录 staged、unstaged、untracked、renamed 和 deleted paths。base/head 变化、retarget 或 merge 后重新运行范围预检。
2. **读取路由**：读取根及每个变更路径祖先的 `AGENTS.md`、项目 `docs/AGENTS.md`、任务/PR、设计记录、当前事实所有者和验证入口。排除依赖、缓存、归档快照和第三方代码，但记录排除项。
3. **收集全量路径**：不只读取 Markdown；包括源码、测试、配置、manifest、契约源、生成器、生成物、脚本、快照、双语文件和升级记录。
4. **解析所有权**：优先使用项目 `docs-governance.yml`；否则根据源码边界、文档链接、生成器、测试和 AGENTS 路由推断，并标注 `configured` / `inferred` 和置信度。
5. **判断语义影响**：结合 diff、公开 API、消费者、配置 precedence、状态/失败/兼容性、生成关系、测试和任务描述。代码 diff 不是语义变化的唯一证据。
6. **检查设计收敛**：`proposed` 只作目标和验收标准；实现完成时必须检查是否同变更转写为 `implemented`。`archived` 不作为当前权威；`rejected` 只作历史或防止重提的理由。
7. **检查派生门禁**：按项目能力检查 generated freshness、type equivalence、doc-typecheck、链接、双语、快照、文档预算、契约重生成和升级指南；未运行或失败的门禁标记 `unverified`。
8. **生成报告**：每条相关路径给出状态、canonical owner、owner evidence、contract delta、命令及结果、未验证原因和下一步。必要时生成 Lesson/postmortem/defensive-patterns 候选，但不自动提升规范。

## 状态

- `covered`：canonical owner 已更新，并且相关生成/链接/双语/类型/测试门禁已验证；或有完整证据证明契约未变。
- `not-needed`：证明没有 owner contract、公开行为、生成区域、JSDoc、双语或兼容性变化，并列出完成的 consumer/API/gate 检查。
- `review-required`：可能有语义变化、所有权是推断的、门禁未运行/失败，或项目规则无法判断。
- `missing`：疑似改变契约但 owner 未更新，也没有足够理由或验证。

## 项目差异

`docs-governance.yml` 是项目覆盖配置，不是通用事实。项目可以声明 `architecture`、`subsystem`、`package_readme`、`agent_note`、`postmortem`、`defensive_pattern`、`generated`、`i18n`、`upgrade_guide` 和 `gates`。没有配置时不得把占位路径当作正式所有权。

## 安全边界

只读；不移动、删除、重写项目文件。不把设计记录当实现证据，不把 observed 规则提升为 adopted，不把命令未运行写成通过。

## 评估

正常、边界和失败/不确定场景见 [evals/evals.json](evals/evals.json)，输入 fixture 位于 `evals/files/`。
