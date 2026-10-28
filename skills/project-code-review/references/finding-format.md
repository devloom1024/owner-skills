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

`blocker` 阻止合并或造成数据/安全/核心功能损坏；`major` 违反重要契约或项目明确要求的验证义务；`minor` 为局部正确性或维护风险。尚未运行测试本身不证明存在缺陷，普通验证缺口和待确认假设单列，不按严重性伪装成 finding。`suggestion` 单列为非阻塞建议且需要理由。

绿色 gate 只在范围、head 和覆盖内容均匹配时作为证据；不要重复已证实解决的纯机械问题，也不要用绿色结果否认直接观察到的错误。
