# PR 章节规则

## Motivation

说明问题、目标和可关联的 Issue/任务；区分 `Fixes/Closes/Resolves` 与仅上下文引用。Stacked PR 只描述本层相对 base 的变化。

## Changes

分别说明接口变化（命令、配置、环境变量、导出、协议、持久化）和行为变化（用户、模型、系统可见结果）。只写 diff 和测试能证明的行为。

## Testing

先写 test design，再写 test entries：

- 行为变化：场景 × before × after × covering test；
- 性能变化：阶段/场景的前后值、机器、次数和采样方式；
- 无行为重构：快照、字节对比或 old/new comparison；
- 文档变化：链接、配对、示例编译和文档门禁。

每条已运行测试给命令、结果、local/CI 来源和 proof；未运行项放在未验证区域。

## Change-specific disclosure

按项目要求披露现有测试行为变化、门禁预算、UI 证据、翻译术语、生成产物和升级指南。
