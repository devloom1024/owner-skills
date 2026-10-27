# owner-skills

由 `devloom1024` 维护的中文 Codex Skill 仓库。

当前版本：`1.0.0`

## Skill 目录

### 设计与文档

- [`project-docs`](skills/project-docs/SKILL.md)：建立、整理、审计和验证项目文档。
- [`project-design-notes`](skills/project-design-notes/SKILL.md)：管理 MVP 设计、提案、已实现决策和生命周期。
- [`project-change-sync`](skills/project-change-sync/SKILL.md)：检查代码变化是否同步到正确的文档所有者。
- [`project-prose-standard`](skills/project-prose-standard/SKILL.md)：审查文档、注释、JSDoc、提示词和诊断文案。

### 开发与审查

- [`project-code-review`](skills/project-code-review/SKILL.md)：根据目标、设计、代码、文档和测试审查变更。
- [`project-test-reliability`](skills/project-test-reliability/SKILL.md)：诊断测试隔离、并发、异步清理和 CI 不稳定。
- [`project-pr-description`](skills/project-pr-description/SKILL.md)：根据变更证据生成 PR 描述。
- [`project-upgrade-guide`](skills/project-upgrade-guide/SKILL.md)：为外部可见破坏性变化生成升级指南。
- [`project-simplification`](skills/project-simplification/SKILL.md)：发现重复、过度设计和可删除的复杂性。

### Skill 仓库维护

- [`skill-maintenance`](skills/skill-maintenance/SKILL.md)：维护 Skill 目录、版本、评估和变更记录。

### 现有设计系统

- [`ui-design-system`](skills/ui-design-system/SKILL.md)：跨桌面、移动、触控、键盘和响应式布局的 UI 设计规范。

## 推荐组合

一次非平凡功能开发可以按以下顺序使用：

```text
project-design-notes
    ↓
project-docs
    ↓
project-change-sync
    ↓
project-code-review
    ↓
project-prose-standard
    ↓
project-test-reliability
    ↓
project-pr-description
```

如果变更影响外部用户或兼容性，增加 `project-upgrade-guide`。如果变更暴露出重复结构或不必要的复杂度，增加 `project-simplification`。

## 使用规则

每个 Skill 只拥有自己的执行流程、参考资料、模板、脚本和评估用例。仓库级说明、版本变化和授权信息分别由本文件、根 `CHANGELOG.md` 和根 `LICENSE` 统一维护。

Skill 的人类可读内容使用中文。Skill 名称、目录名、路径、命令、代码、API、协议字段和机器状态值保留原样。

## 验证

使用 Skill Creator 的快速验证脚本检查单个 Skill：

```bash
python3 /Users/huangkl/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  skills/<skill-name>
```

检查整个仓库：

```bash
for skill in skills/*; do
  test -f "$skill/SKILL.md" || continue
  python3 /Users/huangkl/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$skill"
done
```

完整变更记录见 [CHANGELOG.md](CHANGELOG.md)，授权信息见 [LICENSE](LICENSE)。
