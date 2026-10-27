# 变更日志

本文件记录 owner-skills 仓库的版本变化。版本统一由仓库根目录管理，单个 Skill 不维护独立版本。

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
