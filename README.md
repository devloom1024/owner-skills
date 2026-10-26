# owner-skills

由 `devloom1024` 维护的 Codex Skill 仓库。

## 包含的 Skill

### `ui-design-system`

一个以规范优先（Specification First）为核心的 UI 设计 Skill，用于实现和审查覆盖桌面端、移动端、触控、键盘及响应式布局的跨平台界面。

主要内容包括：

- UI 设计原则与平台适配规则。
- 字体、间距、颜色、圆角、动效、焦点、层级和安全区等语义 Design Tokens。
- `Settings`、`List`、`Detail`、`Form`、`Navigation`、`Overlays` 六类页面与交互 Pattern。
- Desktop / Mobile 的布局和交互指导。
- 无障碍、状态处理、交付验收清单和例外治理。
- 可选的 React、shadcn/ui 和 Tailwind 适配指南。

本 Skill 是设计规范，不是 React 组件库，也不提供像素级设计稿或现成视觉资产。

## 使用方式

Skill 位于：

```text
skills/ui-design-system/
```

在 Codex 中使用：

```text
$ui-design-system
```

Skill 会根据任务需要，从自身的 `references/design-system/` 目录按需读取参考文档。它是 UI 设计规范的唯一来源，项目中不应再维护第二份设计规范副本。

## 验证

可以使用 Codex Skill 验证脚本检查 Skill 包：

```bash
python3 /Users/huangkl/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  skills/ui-design-system
```

## 许可证

UI 设计规范参考文档采用 [CC BY 4.0](skills/ui-design-system/LICENSE) 许可证。
