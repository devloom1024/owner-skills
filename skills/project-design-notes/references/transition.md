# 提案转换

交付变更时执行同一变更内的收敛：

1. 对照每条 Acceptance criteria；
2. 逐项记录通过、偏差、取消或延期；
3. 将 Proposal 改写为现在时态的 Decision；
4. 将 Risks 改写为 Consequences 和当前限制；
5. 更新路径、名称、机制、生成器、测试和验证；
6. 同步当前 subsystem、包 README、契约、指南和升级记录；
7. 对改变原始取舍的偏差创建或链接新的设计记录。

实现完成但仍保留 `Status: proposed` 是生命周期错误；实现未完成时不能提前标记 `implemented`。
