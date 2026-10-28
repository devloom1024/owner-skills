---
name: project-design-notes
description: 管理项目的 MVP 设计、提案、已实现决策、被拒绝方案、替代关系和历史归档。用户提到 MVP、架构方案、设计文档、ADR、决策记录、验收标准、设计偏差或提案落地时使用；默认只读，生命周期迁移需要明确授权。
---

# 项目设计记录

设计记录保存代码、测试和当前文档无法表达的长期理由。它可以描述未来目标，但不能冒充当前运行行为；当前行为由源码、测试、生成器、subsystem 和包 README 共同证明。

## 先读什么

- 根和祖先 `AGENTS.md`；
- 当前 subsystem 和包 README；
- [生命周期](references/lifecycle.md)；
- [记录格式](references/format.md)；
- [提案转换](references/transition.md)；
- [替代关系](references/supersession.md)；
- [提案模板](templates/proposed-note.md)、[已实现模板](templates/implemented-note.md) 和 [被拒绝模板](templates/rejected-note.md)；
- [评估场景](evals/evals.json)。

## 生命周期

```text
proposed → implemented
proposed → rejected
implemented → archived
```

- `proposed`：MVP/方案尚未完全实现，可以使用未来时态；
- `implemented`：决策已交付，只使用现在时态描述实际行为；
- `rejected`：方案被否决，保留仍能阻止重复误用的理由；
- `archived`：只保留历史价值，不作为当前权威，归档内容不可当作现状依据。

## 工作流

1. 固定设计主题、读者、范围、非目标和当前实现状态。
2. 搜索同主题 active notes，先处理完整或部分替代关系。
3. 创建 `proposed` 记录，包含 Problem、Goals、Scope、Proposal、Alternatives、Acceptance criteria、Risks、Open questions 和 Verification。
4. 实现时逐项检查验收标准；如果方案、边界或取舍变化，更新该记录或创建明确替代记录，不让旧提案继续代表新决策。
5. 交付时在同一变更中把 `Proposal` 改为现在时态的 `Decision`，记录实际偏差、Consequences、测试和验证；同步 subsystem、包 README、契约和升级指南。
6. 被拒绝时写明拒绝理由；完整替代或历史冻结时建立双向链接并按项目规则归档。

## 不变量

- `proposed` 是目标和验收来源，不是当前实现证据；
- `implemented` 不保留 Proposal、Plan 或 Acceptance checklist 式的未来语气；
- `archived` 不参与当前事实判断；
- 一个决定只有一个 active owner，不创建重复 note；
- 设计偏差必须能追溯到代码、测试、PR 或新的决策记录。

## 输出

报告状态、文件位置、替代关系、验收项、偏差、实际验证、当前文档同步结果和未决问题。默认不移动、不删除、不重写记录。
