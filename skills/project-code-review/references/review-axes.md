# 审查维度

## 目标和范围

- 变更是否解决目标问题？
- 是否有无关重构、重复状态、无消费者接口或 speculative generality？

## 所有权和接口

- provider/consumer 两端是否匹配？
- 权威读取、配置 precedence、默认值、公开输入输出和协议是否正确？
- 类型、JSDoc、生成 API、快照和双语投影是否同步？

## 状态和生命周期

- 状态转换、取消、重试、错误恢复和失败时保证是否完整？
- 监听器、进程、任务、端口、临时目录和全局状态是否由明确 owner 获取并在 quiescence 后释放？
- 是否存在 race、重入、迟到回调或 alternate caller 绕过 enforcement？

## 错误、安全和兼容性

- 失败是否保持 unknown 而不是伪装成 empty/none/equal？
- 权限、信任边界、敏感数据和用户可见错误是否正确？
- API、配置、协议、持久化和外部用户是否需要升级指南？

## 测试证据

- 真实 Loader/bin/worker/ACP/subprocess/浏览器入口是否覆盖？
- 是否有失败路径、边界、invalid negative control、外部状态和 disposal 断言？
- 异步测试是否遵守 CI 拓扑、原子资源分配、明确 readiness、timeout budget 和 quiescent teardown？
- 模型/UI/协议可见变化是否有 snapshot、locale 或 wire 证据？

## 文档和设计

- proposed 验收是否满足？
- 实现是否按项目 ADR/设计规则记录交付状态并同步当前 owner，而非机械改名为 implemented？
- architecture、subsystem、package README、规范、postmortem、生成物和升级指南是否各归其主职责？
- archived 记录是否被错误当作当前依据？
