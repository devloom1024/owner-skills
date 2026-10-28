# 设计记录生命周期

设计记录使用 `proposed`、`implemented`、`rejected` 和 `archived` 状态，并通过路径或头部表达状态。

- `proposed`：目标、方案、验收标准、风险和未决问题；可以描述未实现行为。
- `implemented`：已交付 Decision、实际 Consequences、测试和验证；当前子系统和包 README 必须同步。
- `rejected`：保存否决理由，只有仍能阻止有意义误用时才保留。
- `archived`：历史快照，不是当前事实来源；项目如有冻结规则，归档后不得修改正文。

状态移动不是改名：必须同时调整正文结构、链接、当前事实文档和验证结果。
