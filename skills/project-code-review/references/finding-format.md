# 发现格式

每条发现使用以下字段：

- `priority`：`blocker`、`major`、`minor` 或 `suggestion`；
- `path` 和最紧 `line/range`；
- `problem`：可复述的问题；
- `impact`：用户、数据、生命周期、安全、兼容性或维护影响；
- `evidence`：设计、源码、调用方、测试、命令或 gate；
- `fix direction`：修复方向，不替作者写完整实现；
- `verification`：可复现命令、负例或观察结果；
- `owner`：代码、文档、设计或验证的 canonical owner。

`blocker` 阻止合并或造成数据/安全/核心功能损坏；`major` 违反重要契约或缺少必要验证；`minor` 为局部正确性或维护风险；`suggestion` 不阻塞且必须有理由。省略已经由绿色 gate 完整覆盖的纯机械问题。
