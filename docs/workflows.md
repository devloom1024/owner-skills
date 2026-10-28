# 使用者项目工作流

## 工作流定义

使用者通过 `project-workflow` 显式创建项目工作流。创建时在 Matt 和 Superpowers 之间选择一个流程提供者，定义写入项目根的 `.agents/workflow.yaml`。创建后保持不变，只有用户明确要求更新时才修改。

定义语法、描述字段、阶段产物和语义约束见 [Workflow 定义格式](../skills/project-workflow/references/workflow-format.md)。可以使用维护仓库提供的 `scripts/validate_workflow.py` 校验定义。

执行工作流前会检查定义是否存在。缺少定义时停止并提示先运行 `$project-workflow create`；缺少定义中引用的 Skill 时停止并报告安装建议，不自动切换流程提供者或修改定义。

简单的局部任务可以直接调用专项 Skill，不强制进入完整工作流。

## Feature 开发

```text
requirements-clarification
  -> project-design-notes（可选）
  -> implementation + test
  -> verification
  -> project-code-review
```

Feature 的前置阶段根据工作流提供者选择：

| Provider | 需求澄清 | 实现与测试 | 验证 |
|---|---|---|---|
| Matt | `grill-with-docs` | `tdd` | 工作流验证要求 |
| Superpowers | `brainstorming` | `test-driven-development` | `verification-before-completion` |

`project-design-notes` 只在用户要求或存在长期设计决策时激活。

## Bug 修复

```text
bug-diagnosis
  -> project-design-notes（可选）
  -> regression test + fix
  -> verification
  -> project-code-review
```

Bug 的前置阶段根据工作流提供者选择：

| Provider | 诊断 | 回归测试与修复 |
|---|---|---|
| Matt | `diagnosing-bugs` | `tdd` |
| Superpowers | `systematic-debugging` | `test-driven-development` |

## 项目简化

项目简化是独立的只读工作流：

```text
project-simplification
```

它输出重复事实、过度抽象、无消费者接口和维护成本候选，不自动删除代码或文档。用户接受候选后，再显式进入适合的实现流程。

## 发布材料

发布入口根据已经完成的变更准备外部材料：

```text
project-upgrade-guide（存在外部兼容性变化时）
  -> project-pr-description
```

`project-upgrade-guide` 只在存在外部可见破坏性变化时激活；`project-pr-description` 由用户运行 `publish` 入口时激活。

## 条件 Skill

`project-code-review` 是 Feature 和 Bug 的固定末尾阶段。根据实际影响激活辅助 Skill：

- UI 任务在设计、实现和审查阶段激活 `ui-design-system`；判断依据是任务意图和当前工作流上下文，不使用通用路径 glob；
- 影响文档、规范或契约时激活 `project-change-sync`；
- 影响异步、资源、并发、测试拓扑或 CI 时激活 `project-test-reliability`；
- 影响用户可见文案、注释、JSDoc 或提示词时激活 `project-prose-standard`；
- 影响外部消费者兼容性时激活 `project-upgrade-guide`；
- 需要发布材料时运行 `publish` 入口激活 `project-pr-description`。

`project-docs` 是大型项目文档的 owner。实现阶段发现代码改变了当前文档事实，或用户明确要求更新文档时，激活它；代码审查和 `project-change-sync` 负责查漏补缺，不直接替代文档维护。

`project-prose-standard` 是 Review 阶段的文案条件 Skill；`project-test-reliability` 是测试拓扑、资源、并发或 CI 受影响时的条件 Skill。它们都不是独立的主工作流。

## 入口

```text
$project-workflow create
$project-workflow run feature
$project-workflow run bug
$project-workflow run simplification
$project-workflow run publish
```

工作流是端到端研发过程；Skill 是阶段能力。`project-skill-router` 不再作为项目入口，`to-spec`、`to-tickets`、`writing-plans` 和 `implement-spec` 暂不属于核心工作流。
