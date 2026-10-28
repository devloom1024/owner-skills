# 变更日志

本文件记录 owner-skills 仓库的版本变化。版本统一由仓库根目录管理，单个 Skill 不维护独立版本。

## [Unreleased]

### 精简

- 删除 11 个 Skill 的模板化 evals 目录、33 个样例场景及附带 fixture/日志，移除普通任务的必读评估入口。
- 将行为评估改为基于真实失败或专项比较的可选活动，不再强制三类场景、固定断言、benchmark 或运行记录。
- 以任务路由替代固定七步 Skill 流水线，支持按需选装和辅助 Skill 缺失时的回退。

### 修复

- 明确只读审计、授权编辑和发布的边界；已有文档结构、ADR 生命周期、发布约定和设计系统优先于通用模板。
- 区分 configured/declared/inferred 所有权来源，按证据而非是否存在 YAML 判定同步状态；区分已确认缺失和未确定影响。
- 代码审查以有证据的发现为先，将假设、未验证项和建议单列；按变化选择辅助检查。
- 修复升级指南 frontmatter 位置与 PR 四章节模板；补充文档 AGENTS 模板入口，取消普通编辑的强制迁移 manifest 和文案形式参数。
- 恢复有依据的 timeout 预算调整，继续拒绝用 sleep、盲目重试和串行化掩盖竞态。
- 修复 UI 项目适配优先级、MUST/SHOULD 边界、安全区合并与 shadcn 版本/原语假设；统一采用仓库 tag/commit，不再维护独立规范版本号。
- 保留有用途的导航 README，修复 UI 独立安装后的仓库根链接依赖；各 Skill 携带最小 NOTICE 保留来源和许可。

### 维护

- 补齐文档初始化的最小布局、证据驱动内容、subsystem/规范候选、初始所有权映射和未决语义；不要求固定目录、独立报告或 YAML。
- 增加按需读取的规范形成与采纳流程，分开记录项目决定和验证方式，避免把 observed、adopted、enforced 等混成单一状态链。
- 补充缺陷经验提升为规范的稳定性、范围、检测办法和项目决定条件；同步审计区分项目要求的缺失与可选建议，不自动建档或提升规范。
- 用内容边界补足 subsystem、规范、经验记录和契约索引，不恢复统一治理 Skill、模板配额、扫描器或 evals。
- 增加项目级/用户级安装、发现确认、选装、版本锁定与更新说明，不引入自动安装器或发布动作。
- 增加轻量结构校验及维护依赖声明，覆盖 frontmatter、本地链接、JSON/YAML、Python 语法、已声明的模板约束和独立分发边界；聚合失败并返回非零退出码。
- 结构校验不代替真实使用、模型行为评估或 UI 验证；本次为未发布变更，不创建新 tag。

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
