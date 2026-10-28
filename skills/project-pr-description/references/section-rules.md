# PR 章节规则

以下用于无项目模板时的四章节默认结构；已有模板优先，相关内容放入其等价位置。

## Motivation

说明问题、目标和可关联的 Issue/任务；区分 `Fixes/Closes/Resolves` 与仅上下文引用。Stacked PR 只描述本层相对 base 的变化。上下文链接放在本节。

## Changes

分别说明接口变化（命令、配置、环境变量、导出、协议、持久化）和行为变化（用户、模型、系统可见结果）。只写 diff 和测试能证明的行为。相关设计、文档、契约、升级链接和风险放在本节。

## Testing

先写 test design，再写 test entries：

- 行为变化：场景 × before × after × covering test；
- 性能变化：阶段/场景的前后值、机器、次数和采样方式；
- 无行为重构：快照、字节对比或 old/new comparison；
- 文档变化：链接、配对、示例编译和文档门禁。

每条已运行测试给命令、结果、local/CI 来源和 proof；未运行项放在本节的未验证区域。

## AI Usage

按项目披露约定或 [AI 使用说明](ai-usage.md) 记录实际参与，不猜测人的操作。

### 按变化类型补充

现有测试行为变化、门禁预算和 UI 证据放在 Testing；翻译术语、生成产物和升级指南放在 Changes。只补充与本次变化有关的内容。
