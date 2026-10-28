# 路由目录

## 任务到 Skill

| 任务 | 主 Skill | 可能的辅助 Skill | 不默认加载 |
|---|---|---|---|
| 新建、整理或审计项目文档 | `project-docs` | `project-prose-standard`、`project-design-notes` | `project-upgrade-guide` |
| 设计长期取舍或维护 ADR | `project-design-notes` | `project-docs` | `project-simplification` |
| 审查 PR、commit、worktree 或分支 | `project-code-review` | `project-change-sync`、`project-test-reliability` | `project-docs` |
| 检查代码变化是否漏同步文档或规范 | `project-change-sync` | `project-docs` | `project-code-review` |
| 诊断 flaky test、并发、异步清理或 CI 不稳定 | `project-test-reliability` | `project-code-review` | `project-simplification` |
| 审查技术文案、注释、JSDoc 或提示词 | `project-prose-standard` | `project-docs` | `project-code-review` |
| 识别外部可见的破坏性变化 | `project-upgrade-guide` | `project-change-sync`、`project-pr-description` | `project-docs` |
| 生成或更新 PR 描述 | `project-pr-description` | `project-code-review` | `project-upgrade-guide` |
| 发现重复、过度抽象或无消费者接口 | `project-simplification` | `project-design-notes`、`project-code-review` | `project-docs` |
| 实现或审查 UI | `ui-design-system` | `project-code-review`、`project-prose-standard` | `project-upgrade-guide` |

## 常见路线

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
