# Adapter — Tailwind / Theme Tokens（可选映射规则）

> 本仓库不提供强制 CSS 文件；这里说明 React + Tailwind / shadcn 项目如何保持唯一 Token 来源。

## 映射原则

- 基础颜色沿用 shadcn 语义：`background`、`foreground`、`card`、`muted`、`accent`、`primary`、`destructive`、`border`、`ring`。
- 新增业务语义优先声明在项目全局主题层，并在 Light/Dark 两种模式定义。
- 字体等级、圆角、间距、控件高度及密度作为项目统一的语义样式/变量；不可散落在页面中的无名 Utility 组合。
- 当规范中有 `space.6=24px` 时，项目可以映射到 Tailwind 合法的间距级别，但不能让相同语义在一个页面是 24px，另一个页面是 28px。
- Tailwind v4 可通过 `@theme` / `@theme inline` 将变量连接到实用类；跟随实际安装的 shadcn/ui 版本，不应照抄旧版主题配置。

## 每次主题升级应检查

1. shadcn/ui 基础组件或底层原语更新是否改变默认 Radius、Spacing、状态色与可访问性行为。
2. 语义颜色是否在 Light/Dark 有对应值，文本对比度是否合格。
3. Compact/Comfortable 密度是否可以单独控制，未因断点强制改成手机密度。
4. 是否存在 `px-[13px]`、`rounded-[11px]` 一类缺乏 Token 依据的独立数值。

参见 [Tailwind Theme Variables](https://tailwindcss.com/docs/theme) · [shadcn/ui Theming](https://ui.shadcn.com/docs/theming)。
