# 使用者项目工作流

## 通用流程

```text
安装 Skill
  -> Agent 发现 Skill
  -> 选择主 Skill
  -> 读取目标项目规则和相关 references
  -> 执行 audit / edit / publish
  -> 运行适用验证
  -> 报告结果、证据和未验证项
```

这不是固定流水线。一个任务不需要依次调用所有 Skill。

## 推荐路由

| 场景 | 主 Skill | 按需辅助 |
|---|---|---|
| 新建、整理或审计项目文档 | `project-docs` | `project-prose-standard`、`project-design-notes` |
| 设计长期取舍或维护 ADR | `project-design-notes` | `project-docs` |
| 审查 PR、commit、worktree 或分支 | `project-code-review` | `project-change-sync`、`project-test-reliability` |
| 检查代码变化是否漏同步文档 | `project-change-sync` | `project-docs` |
| 诊断 flaky test 或 CI 不稳定 | `project-test-reliability` | `project-code-review` |
| 审查技术文案、注释或提示词 | `project-prose-standard` | `project-docs` |
| 识别破坏性变化 | `project-upgrade-guide` | `project-change-sync`、`project-pr-description` |
| 生成 PR 描述 | `project-pr-description` | `project-code-review` |
| 发现重复、过度抽象或无消费者接口 | `project-simplification` | `project-design-notes`、`project-code-review` |
| 实现或审查 UI | `ui-design-system` | `project-code-review`、`project-prose-standard` |

不知道从哪里开始时，显式调用 `project-skill-router`。

## 典型路线

### 代码审查

```text
project-code-review
  -> project-change-sync（影响文档、契约或规范时）
  -> project-test-reliability（影响测试拓扑、并发或清理时）
  -> project-pr-description（需要 PR 描述时）
```

### 文档任务

```text
project-docs
  -> project-prose-standard（涉及术语、注释或用户可见文案时）
  -> project-design-notes（产生长期设计决策时）
```

### 外部可见变化

```text
project-upgrade-guide
  -> project-change-sync
  -> project-pr-description（需要 PR 描述时）
```

## 目标项目适配

Skill 会读取目标项目自己的 `AGENTS.md`、README、测试入口、文档 owner 和决策记录。没有这些文件时，Skill 应报告证据缺口，而不是把通用模板当成项目事实。
