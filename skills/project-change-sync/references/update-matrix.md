# 更新矩阵

| 变化 | 首选所有者 | 需要检查的派生物和证据 |
|---|---|---|
| 系统组合、主循环、扩展点或高层运行路径 | `architecture.md` | 调用路径、架构图、集成测试 |
| 类型、语义、实现边界或生成 API | 对应 `subsystems/<name>.md` | 源类型、JSDoc、type-equiv、生成 freshness、测试 |
| 包配置、公开接口、限制、扩展点或消费者行为 | 包 README | manifest、exports、调用方、包测试 |
| 本地审查规则、资源/错误/安全模式 | `standards/` 或项目等价规则层 | 规则来源、门禁、负例和审查证据 |
| 持久化设计理由、替代方案或架构取舍 | `agent-notes/implemented/` | 决策、后果、当前路径、验证；提案完成需同步转换 |
| 真实事故和因果链 | `postmortem/` 或项目明确的 lessons 层 | 复现、影响、根因、预防和回归测试 |
| 机器契约源 | contract source + contract index | 生成器、漂移检查、兼容性和语义 owner |
| 生成参考或 catalog | canonical source/generator | freshness、生成命令、禁止手改 |
| 双语文档 | canonical pair + pairing metadata | 行结构、术语、链接和配对门禁 |
| 用户操作流程 | `guides/` / cookbook | 实际运行、失败恢复和结果验证 |
| 外部破坏性变化 | upgrade guide | 版本来源、旧/新行为、迁移和兼容性 |
| 没有可观察或契约变化的纯内部重构 | 通常无产品文档变化 | API/consumer 对比、相关 gate、测试和未验证项 |

`Lessons` 不是所有项目的默认类别；只有项目明确建立该层时才使用，否则按事故、Agent Note 或规范所有权映射。
