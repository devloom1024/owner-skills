---
name: project-design-notes
description: 创建、审查和维护需要长期保留理由的 MVP 设计、架构提案、ADR 和决策记录。用于方案取舍、替代关系、设计偏差和交付收敛；遵循项目既有生命周期，不为普通实现或文档修订强制建档。
---

# 项目设计记录

设计记录保存代码、测试和当前文档无法表达的长期理由。它可以描述未来目标，但不能冒充当前运行行为；当前行为由源码、测试、生成器、subsystem 和包 README 共同证明。

审查请求保持只读；明确要求创建、更新或转换记录时直接执行。先更新同主题现有 owner；只有产生新的长期取舍或决策反转时才新建记录。

## 先读什么

- 根和祖先 `AGENTS.md`；
- 当前 subsystem 和包 README；
- 项目生命周期；没有约定时参考 [默认生命周期](references/lifecycle.md)；
- 创建或改写记录时读 [记录格式](references/format.md)，按状态选择 [提案模板](templates/proposed-note.md)、[已实现模板](templates/implemented-note.md) 或 [被拒绝模板](templates/rejected-note.md)；
- 交付收敛时读 [提案转换](references/transition.md)，涉及方案替代时读 [替代关系](references/supersession.md)。

## 项目约定优先

保留项目既有 ADR 路径、状态、不可变历史和替代机制；例如 `accepted` 可能仅表示采纳而非已实现，不能机械替换成 `implemented`。以下生命周期和模板仅用于项目没有约定的情况，不强制迁移已有记录。

## 默认生命周期

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
3. 确有新决策时创建记录；按项目模板表达问题、方案、替代、验收和风险，复杂主题再补充 Goals、Scope、Open questions 和 Verification。
4. 实现时逐项检查验收标准；如果方案、边界或取舍变化，更新该记录或创建明确替代记录，不让旧提案继续代表新决策。
5. 交付时按项目规则记录实现状态、实际偏差、后果、测试和验证，并同步当前文档。采用默认生命周期时，将 `Proposal` 收敛为现在时态的 `Decision`；不可变 ADR 则通过索引或后续记录补充，不改写历史决定。
6. 被拒绝时写明拒绝理由；完整替代时建立可追溯关系，只有项目允许编辑的记录才补双向链接。

## 不变量

- `proposed` 是目标和验收来源，不是当前实现证据；
- 默认 `implemented` 记录不以未来计划冒充当前行为；历史验收记录可保留，但要明确完成状态；
- `archived` 不参与当前事实判断；
- 一个决定只有一个 active owner，不创建重复 note；
- 设计偏差必须能追溯到代码、测试、PR 或新的决策记录。

## 输出

报告项目状态含义、文件位置、替代关系、验收项、偏差、实际验证和未决问题。不擅自迁移项目生命周期、删除记录或重写冻结历史。
