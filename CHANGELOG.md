# 变更日志

本文件记录 owner-skills 仓库的版本变化。版本统一由仓库根目录管理，单个 Skill 不维护独立版本。

## [1.1.1] - 2026-10-28

### 调整

- 将语言规则调整为“中文说明 + English controlled vocabulary”。
- 保留 Pattern、Token、Desktop、Mobile、Accessibility、Review Checklist、source of truth、subsystem、contract、gate、fixture、benchmark 等稳定术语。
- 将 UI 参考标题改为中英并列，避免关键术语在中文化过程中失去可检索性和跨文档一致性。


### 修复

- 补齐所有项目 Skill 的入口路由、参考资料、模板和评估说明。
- 增加文档所有权、架构/子系统/包 README/生成物/事故/升级指南分层。
- 增加 proposed → implemented 的设计收敛、替代关系和归档边界。
- 增加变更范围预检、verified base/head、worktree dirty layers 和门禁结果。
- 扩充代码审查的真实入口、消费者、生命周期、失败、安全、负例和资源清理维度。
- 扩充测试可靠性、升级指南、PR 描述、简化和 Skill 仓库维护流程。
- 为所有 Skill 增加正常、边界和失败/不确定评估场景及 expectations。
- 完成 UI 设计系统的人类可读结构标题中文化，并修正验收清单编号。
- 移除 README 中依赖本机路径的验证命令，明确根 LICENSE 覆盖 JSON/YAML 和支持脚本。

### 兼容性

- 保留 v1.0.0 的 Skill 名称、目录和根元数据约定。
- `v1.1.0` 是内容和验证能力增强版本，不改变 Skill 调用名称。

## [1.0.0] - 2026-10-27

### 新增

- `project-docs`：项目文档建立、整理、审计和验证。
- `project-design-notes`：MVP 设计、提案和决策生命周期。
- `project-change-sync`：代码变化与文档所有者同步检查。
- `project-code-review`：设计、代码、文档和测试证据审查。
- `project-prose-standard`：中文技术文案、文档和注释审查。
- `project-upgrade-guide`：外部可见破坏性变化的升级指南。
- `project-test-reliability`：测试隔离、并发和 CI 可靠性检查。
- `project-pr-description`：基于证据生成 PR 描述。
- `project-simplification`：发现重复和不必要复杂度。
- `skill-maintenance`：维护 Skill 仓库结构、版本和评估。
- `ui-design-system`：纳入统一中文 Skill 仓库基线。

### 规范

- 根目录统一维护 README、CHANGELOG 和 LICENSE。
- Skill 入口和随附人类可读内容统一使用中文。
- 每个 Skill 只维护自身的入口、参考资料、模板、脚本和评估用例。
- Skill 仓库使用 Git tag 管理版本，首个版本为 `v1.0.0`。
