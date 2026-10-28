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

按变更类型加载项目等价规则：错误处理、UI/i18n、会话/投影、测试可靠性、生成类型、双语和升级指南。`project-change-sync` 的报告是文档影响输入；有契约或文档变化时必须检查，不是“需要时”可选调用。

## 审查流程

1. **固定范围**：验证 live base/exact head；项目有 `change-scope` 命令先运行；处理 rename/delete/untracked，retarget/merge 后重跑。没有 PR 时明确 staged/unstaged/worktree 范围。
2. **先读要求再读 diff**：按每条 changed path 找 canonical owner、设计记录、适用 AGENTS 和验证入口，再读完整 diff、调用方、消费者、生成器和上下文。
3. **意图和范围**：对照目标、MVP、验收标准和 before/after；识别无关重构、重复状态、 speculative generality 和不必要公共接口。
4. **接口和配置**：追踪 provider/consumer 两端、权威读取和 precedence，检查公开输入输出、配置、协议、持久化、生成物和模型可见面。
5. **状态和生命周期**：检查状态转换、取消、重试、错误恢复、资源所有权、回调、并发、dispose-to-quiescence 和失败时状态保证。
6. **安全和边界**：检查权限、信任边界、敏感数据、错误报告、绕过 schema/prompt/facade 的 alternate callers 和真实执行入口。
7. **设计收敛**：`proposed` 只作目标/验收；实现提案时同变更转为 `implemented` 的现在时态并同步 owner。`archived` 不作当前依据，`rejected` 不作实现证据。
8. **测试证据**：检查真实 Loader/bin/worker/ACP/subprocess/浏览器入口（若适用）、失败路径、边界、负例、外部状态、快照、清理和并发拓扑；未跑命令明确列出。
9. **文档同步**：运行或读取 `project-change-sync` 报告，检查 architecture/subsystem/README/设计/生成/双语/升级 owner；绿色 gate 不替代语义审查。
10. **报告**：每条发现给出 priority、最紧 diff range、影响、证据、修复方向和验证方式；区分 blocker、major、minor 和建议。

## 条件检查

- 改变新 prose、JSDoc、README、注释或 UI 文案：加载 `project-prose-standard`；
- 改变 async、资源、进程、端口、全局状态或 flaky test：加载 `project-test-reliability`；
- 改变 UI：检查平台、键盘/触控、locale、快照和真实入口；
- 改变 schema、类型等价、生成 API 或双语：运行项目对应 freshness/type/i18n gates；
- 改变外部接口、配置、协议或持久化：加载 `project-upgrade-guide`；
- 实现 proposed note：必须检查同变更生命周期转换。

## 结论

明确 `blocker/major/minor`、无阻塞项、未验证项、被绿色 gate 覆盖的检查和人工决定。不修改代码、文档或作者设计。

## 评估

正常、边界和失败/不确定场景见 [evals/evals.json](evals/evals.json)，输入 fixture 位于 `evals/files/`。
