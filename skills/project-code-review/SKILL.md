---
name: project-code-review
description: 审查项目变更是否符合任务目标、设计记录、AGENTS.md、架构与当前事实、规范、测试、生成门禁和验证证据。用于 PR、commit、worktree、retarget 后和设计落地审查；默认只读，不修改实现、文档或作者设计。
---

# 项目代码审查

这是证据驱动的审查，不是关键词清单。优先正确性、生命周期、安全、兼容性、所有权和必需行为；只报告可定位、可复现、有证据的问题。

## 审查前读取

依次读取：

1. [审查流程](references/review-workflow.md)；
2. [审查维度](references/review-axes.md)；
3. [发现格式](references/finding-format.md)；
4. [报告模板](templates/review-report.md)；
5. 根及变更路径祖先 `AGENTS.md`、任务/PR、架构地图、subsystem/package owner、规范、proposed/implemented notes 和测试入口。

按变更类型读取项目实际存在的规则，不要求每次审查串行运行整套 Skill。有契约或文档影响时检查同步，可复用范围和 head 一致的 `project-change-sync` 报告；辅助 Skill 未安装时直接追踪 owner、diff 和适用验证，报告证据缺口而非中止审查。

## 审查流程

1. **固定范围**：验证 live base/exact head；项目有 `change-scope` 命令先运行；处理 rename/delete/untracked，retarget/merge 后重跑。没有 PR 时明确 staged/unstaged/worktree 范围。
2. **先读要求再读 diff**：按每条 changed path 找 canonical owner、设计记录、适用 AGENTS 和验证入口，再读完整 diff、调用方、消费者、生成器和上下文。
3. **意图和范围**：对照目标、MVP、验收标准和 before/after；识别无关重构、重复状态、 speculative generality 和不必要公共接口。
4. **接口和配置**：追踪 provider/consumer 两端、权威读取和 precedence，检查公开输入输出、配置、协议、持久化、生成物和模型可见面。
5. **状态和生命周期**：检查状态转换、取消、重试、错误恢复、资源所有权、回调、并发、dispose-to-quiescence 和失败时状态保证。
6. **安全和边界**：检查权限、信任边界、敏感数据、错误报告、绕过 schema/prompt/facade 的 alternate callers 和真实执行入口。
7. **设计收敛**：区分目标、采纳与实现状态；依据项目 ADR/设计规则检查交付记录和当前 owner，不强制改写不可变 ADR 或采用特定状态名。历史和拒绝记录不作实现证据。
8. **测试证据**：检查真实 Loader/bin/worker/ACP/subprocess/浏览器入口（若适用）、失败路径、边界、负例、外部状态、快照、清理和并发拓扑；未跑命令明确列出。
9. **文档同步**：存在影响时检查相关 owner 和项目适用的派生物；只读检查或已有 gate 结果不等于生成命令执行授权，绿色 gate 也不替代语义审查。
10. **报告**：优先列出有证据的发现，按严重性排序并给出精确位置、影响、证据、修复方向和验证方式。假设、未验证事项和非阻塞建议单列；没有问题时明确说明，不制造 finding。

## 条件检查

- 契约文案、术语或时态存在实质影响：可加载 `project-prose-standard`；简单排版不强制完整文案审计；
- 改变 async、资源、进程、端口、全局状态或 flaky test：可加载 `project-test-reliability`，否则依据项目测试规则检查隔离和清理；
- 改变 UI：检查平台、键盘/触控、locale、快照和真实入口；
- 改变 schema、生成 API 或项目双语文档：检查实际适用的 freshness/type/i18n gates；
- 改变外部接口、配置、协议或持久化：检查兼容性；有破坏性影响时可加载 `project-upgrade-guide`；
- 实现设计记录：按项目约定检查实现状态、偏差和当前事实同步。

## 结论

明确 `blocker/major/minor`、无阻塞项、未验证项、被绿色 gate 覆盖的检查和人工决定。不修改代码、文档或作者设计。
