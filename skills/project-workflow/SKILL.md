---
name: project-workflow
description: 创建、读取和执行项目固定研发工作流。用于选择 Matt 或 Superpowers 流程提供者、运行 feature-development 或 bug-fix 流程、按阶段激活已安装 Skill，以及在 workflow.yaml 缺失或依赖缺失时停止并提示；不自动修改已创建的工作流。
---

# 项目工作流

这是使用者项目的唯一工作流入口。工作流定义由用户显式创建，写入项目根的 `.agents/workflow.yaml`；创建完成后保持不变，只有用户明确要求更新时才修改。

## 入口

支持：

- `$project-workflow create`：检查项目、选择 `matt` 或 `superpowers`、确认阶段和依赖，生成工作流定义；
- `$project-workflow run feature`：执行 `feature-development`；
- `$project-workflow run bug`：执行 `bug-fix`；
- `$project-workflow run simplification`：执行独立的项目简化审计；
- `$project-workflow run publish`：根据已完成变更准备发布材料；
- `$project-workflow validate`：检查定义格式、阶段顺序和 Skill 引用。

创建或校验定义时读取 [Workflow 定义格式](references/workflow-format.md)。

简单的局部任务可以直接调用专项 Skill，不强制进入完整工作流。

## 执行前检查

1. 读取项目根的 `.agents/workflow.yaml`。
2. 文件不存在时停止，提示用户先运行 `$project-workflow create`；不得自动创建。
3. 校验 `provider`、入口和阶段顺序；定义无效时停止并报告具体字段。
4. 检查每个阶段引用的 Skill 是否已安装；缺失时停止并给出安装建议，不自动切换 provider 或改写定义。
5. 读取项目的 `AGENTS.md`、相关规范和当前任务上下文，再进入第一个阶段。

## 固定提供者

工作流只能选择一个过程提供者：

- `matt`：使用 Matt Pocock 的 Discovery、TDD 和 Bug Diagnosis Skill；
- `superpowers`：使用 Superpowers 的 Brainstorming、TDD、Debugging 和 Verification Skill。

两种提供者不能在同一份工作流中自动混用。owner-skills 的项目治理 Skill（例如 `project-code-review`）不属于提供者选择，按定义共同使用。

## 核心流程

### Feature

```text
requirements-clarification
  -> optional agent-notes
  -> implementation + test
  -> verification
  -> project-code-review
```

### Bug

```text
bug-diagnosis
  -> optional bug-fix note
  -> regression test + fix
  -> verification
  -> project-code-review
```

### Simplification

```text
project-simplification
```

这是独立的只读维护工作流。它输出简化候选和证据，不自动删除代码或文档；用户接受候选后，再显式进入适合的实现流程。

### Publish

```text
project-upgrade-guide（存在外部兼容性变化时）
  -> project-pr-description
```

`to-spec`、`to-tickets`、`writing-plans` 和 `implement-spec` 不属于当前核心工作流。

## 可选 Agent Notes

Discovery 或 diagnosis 后只有在以下情况才进入 `project-design-notes`：

- 用户明确要求记录；
- 存在跨模块、公共契约、持久化、安全或生命周期决策；
- Bug 根因或测试策略具有可复用价值。

没有 Agent Note 时，前一阶段的结果直接作为实现输入。创建 Note 时，它承载目标、范围、方案、取舍、验收条件和验证计划，不另建实现计划。

## UI 条件阶段

如果任务语义表明正在开发或修复页面、组件、交互或响应式 UI，则在设计、实现和审查阶段激活 `ui-design-system`：

- `design`：页面结构、交互模式、平台和响应式策略；
- `implementation`：Token、组件、布局、输入方式和可访问性；
- `review`：UI 规范、状态、键盘/触控和真实入口。

UI 判断依据是任务意图和当前工作流上下文，不使用通用路径 glob。项目自己的 `AGENTS.md` 或设计系统可以补充项目特定范围。

## Review 条件阶段

`project-code-review` 是 Feature 和 Bug 的固定末尾阶段。根据实际影响再激活：

- `project-change-sync`：影响文档、规范或契约；
- `project-test-reliability`：影响异步、资源、并发、测试拓扑或 CI；
- `project-prose-standard`：影响用户可见文案、注释、JSDoc 或提示词；
- `project-docs`：实现改变当前文档事实或用户明确要求更新文档；应在验证前完成，代码审查负责查漏补缺；
- `project-upgrade-guide`：用户运行 `publish` 且存在外部消费者兼容性变化时激活；
- `project-pr-description`：用户运行 `publish` 入口准备 PR 材料。

这些 Skill 提供审计或审查视角，不改变工作流定义，也不自动编辑作者文件。

## 边界

- 不把每个 Skill 都提升为工作流；工作流表达端到端研发结果，Skill 表达阶段能力；
- 不为简单任务强制创建 Agent Note；
- 不自动修改 `.agents/workflow.yaml`；
- 不自动安装、替换或升级外部 Skill；
- 不将审查、同步或发布材料误报为实现完成；
- 阶段完成以可观察产物、用户批准和验证证据为准。
