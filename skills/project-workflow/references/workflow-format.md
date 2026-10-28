# Workflow 定义格式

项目工作流定义保存为 `.agents/workflow.yaml`。它是用户显式创建的项目配置；创建后保持不变，只有用户明确要求更新时才修改。

## 顶层结构

```yaml
version: 1

workflow:
  id: <kebab-case-id>
  description: <workflow description>
  provider: <matt|superpowers>
  policy: <policy mapping>
  entrypoints: <entrypoint to flow id mapping>
  flows: <flow mapping>
```

### `workflow.id`

必填，使用小写 kebab-case。它标识一份项目工作流定义，不因运行次数变化。

### `workflow.description`

必填，说明这份工作流服务的项目范围和研发目标。它描述工作流，不重复阶段细节。

### `workflow.provider`

必填，只能是 `matt` 或 `superpowers`。创建后不能自动更换；更换必须是用户明确要求的工作流更新。

### `workflow.policy`

支持以下字段：

| 字段 | 类型 | 含义 |
|---|---|---|
| `immutable` | boolean | 是否禁止未经明确请求的定义修改，必须为 `true` |
| `update_requires_explicit_request` | boolean | 是否要求用户明确请求更新，必须为 `true` |
| `missing_definition` | string | 定义缺失时的行为，必须为 `require_create` |
| `missing_skill` | string | Skill 缺失时的行为，必须为 `stop_and_report` |
| `unknown_entrypoint` | string | 入口不存在时的行为，必须为 `stop_and_report` |
| `allow_direct_skill_for_simple_tasks` | boolean | 是否允许简单任务直接调用专项 Skill |

### `workflow.entrypoints`

入口名称到 flow ID 的映射。核心入口包含 `feature` 和 `bug`，也可以添加独立的维护或发布入口：

```yaml
entrypoints:
  feature: feature-development
  bug: bug-fix
  simplification: simplification
  publish: publish
```

### `workflow.flows`

每个 flow 是一个端到端研发流程：

```yaml
flows:
  feature-development:
    description: <flow description>
    stages: []
```

flow 的 key 使用小写 kebab-case。`description` 必填，说明该流程的最终研发结果。

## Stage 格式

```yaml
- id: <kebab-case-id>
  description: <stage description>
  activate:
    - source: <source-id>
      skill: <skill-name>
  required: <boolean>
  when: <optional condition list>
  gate: <optional gate>
  consumes: <optional artifact list>
  produces: <optional artifact list>
  conditional: <optional conditional activations>
```

### `stage.id`

在同一个 flow 内唯一，使用小写 kebab-case。Stage 按 YAML 列表顺序执行。

### `stage.description`

必填，说明该阶段要完成的工作和可观察结果。它不能只重复 Skill 名称。

### `stage.activate`

必填的 Skill 激活列表。每项必须包含：

- `source`：Skill 来源，例如 `owner-skills`、`obra/superpowers` 或 `mattpocock/skills`；
- `skill`：来源中的 Skill 名称。

同一个阶段可以激活多个 Skill，例如实现阶段同时激活 TDD 和项目 UI 规范。

### `stage.required`

必填 boolean。`false` 代表可选阶段；可选阶段必须配合 `when` 或用户明确选择。

### `stage.when`

可选条件列表。条件依据任务意图和当前工作流上下文，不使用 owner-skills 内置的项目路径 glob。常见值包括：

- `user_requested`；
- `architectural_decision`；
- `public_contract_change`；
- `persistent_state_change`；
- `cross_subsystem_change`；
- `security_or_lifecycle_decision`；
- `reusable_root_cause`；
- `ui_task`。
- `docs_owner_update_required`；
- `external_contract_changed`；
- `publish_requested`；
- `user_visible_text_changed`；

### `stage.gate`

可选用户门禁。目前支持 `user-approval`。需要用户确认的设计记录或外部方案应设置门禁。

### `consumes` 与 `produces`

它们是阶段之间的可观察产物名称，不是运行时状态文件。常见产物包括：

- `design-input`；
- `agent-note`；
- `implementation`；
- `tests`；
- `verification-evidence`；
- `bug-fix-note`；
- `regression-test`。

### `stage.conditional`

用于在当前阶段根据影响激活辅助 Skill：

```yaml
conditional:
  - when: ui_task
    activate:
      - source: owner-skills
        skill: ui-design-system
```

UI 任务应在设计、实现和审查阶段分别使用 `ui-design-system` 的相关规则；是否为 UI 任务依据请求意图和当前工作流上下文判断。

## 语义约束

- `version` 必须为支持的正整数，目前为 `1`；
- 必须有 `workflow.id`、`workflow.description`、`workflow.provider`、`workflow.entrypoints` 和 `workflow.flows`；
- provider 只能是 `matt` 或 `superpowers`；
- 每个 entrypoint 必须指向存在的 flow；
- 每个 flow 必须有非空 `description` 和非空 `stages`；
- 每个 stage 必须有唯一 `id`、非空 `description`、非空 `activate` 和 boolean `required`；
- `required: false` 的 stage 必须有 `when` 或明确的用户选择路径；
- `consumes` 中的产物应由前序阶段产生，除非它来自用户任务或项目现有文件；
- workflow 定义不记录运行状态，不能出现 `workflow-state` 或运行次数字段；
- 定义中的 Skill 缺失由执行时报告，不通过修改 provider 或跳过 required stage 解决。
