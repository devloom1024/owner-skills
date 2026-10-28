# 提案转换

先采用项目自己的交付和 ADR 规则。采用默认 `proposed → implemented` 模型时，在交付变更中收敛：

1. 对照每条 Acceptance criteria；
2. 逐项记录通过、偏差、取消或延期；
3. 将 Proposal 改写为现在时态的 Decision；
4. 将 Risks 改写为 Consequences 和当前限制；
5. 更新路径、名称、机制、生成器、测试和验证；
6. 同步当前 subsystem、包 README、契约、指南和升级记录；
7. 对改变原始取舍的偏差创建或链接新的设计记录。

在该默认模型中，实现完成却仍标为 `proposed` 是状态遗漏；实现未完成时不能提前标记 `implemented`。不可变 ADR 或项目将“已采纳”和“已实现”分开管理时，更新其实现索引或关联记录，不强行改写正文和状态名。
