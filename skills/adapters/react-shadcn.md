# Adapter — React + TypeScript + shadcn/ui（可选实现指南）

> 本文件解释“怎样映射”，**不是可复制运行的组件库**，不提供固定业务组件 API。

## 基础落地

1. 初始化项目自有 shadcn/ui 组件；不要把设计系统目录当成 React `src/components`。
2. 对照 [Tokens](../02-foundations/design-tokens.md) 把颜色语义映射到 shadcn 的 `background`、`foreground`、`primary`、`muted`、`destructive`、`border`、`ring` 等现有变量；shadcn/ui 组件基于 Base UI 原语，升级依赖时留意其行为与可访问性变化。
3. 利用主题变量及统一的密度策略映射文字与高度；不对每个按钮硬编码一次高度和圆角。
4. 页面开发先指定 Pattern，例如 `settings`；按 `overview.md` 实现共享结构，再对照 Desktop/Mobile 文件实现布局与交互。
5. 如果多个项目需要复用 SettingsRow 等组合组件，先在项目中验证，再决定是否抽出公共包；规范本身不强制某个 TSX API。

## 组件映射（规范概念 → shadcn/ui 组件）

> shadcn/ui 官方组件当前默认基于 **Base UI** 原语，文档同时提供 Base UI / React Aria / Radix 三种变体；Drawer 已由 vaul 迁移至 Base UI（旧版项目参见官方迁移指南，iOS Safari 需按文档为 `body` 设置定位）。规范只绑定下表的语义容器/概念，不绑定底层原语；实现以项目实际安装的 shadcn/ui 版本为准。

| 规范概念 | shadcn/ui 组件 | 说明 |
|---|---|---|
| Dialog | `dialog` | 需完成/取消的短任务模态 |
| AlertDialog | `alert-dialog` | 危险确认；不默认聚焦危险按钮 |
| Dropdown / Context Menu | `dropdown-menu` / `context-menu` | 收纳对象动作，不作为唯一入口 |
| Popover / Tooltip | `popover` / `tooltip` | 锚定辅助信息，核心内容不只放 Tooltip |
| Sheet（侧边抽屉） | `sheet` | 通用侧边滑出层 |
| Action Sheet / Bottom Sheet（移动端底部） | `drawer` | 底部抽屉（现基于 Base UI，替代 vaul）；Overlays Pattern 移动端动作选择首选 |
| Navigation 侧栏 / Rail / 移动端抽屉 | `sidebar` | 官方侧栏组合，折叠 Rail 与移动端行为已内置；Navigation Pattern 优先使用，不要自拼 |
| Form 字段（Label + 控件 + 说明/错误） | `field` | 官方字段组合；标签、描述、错误与控件的关联语义已内置 |
| Empty 状态 | `empty` | Feedback 六大状态中空数据/无结果的呈现，配说明与下一步动作 |
| Search / Combobox（搜索过滤与选择） | `command`（`combobox` 为其组合形态） | List Pattern 的搜索、筛选与选项输入 |
| Segmented（少量互斥切换） | 无官方组件 | 用 `tabs` 或 `toggle-group`（单选）实现，保持单一选中语义 |

## 项目集成建议（非强制）

- `docs/design-system`：版本化规范与 AI 约束。
- `src/components/ui`：已有 shadcn 基础组件。
- `src/components/patterns`：项目自己的 Pattern 组合实现。
- `src/pages` 或路由目录：业务页面。
- 组件库/样式变更以视觉回归与清单为准，不以 HTML 结构相同为目标。

参见 [shadcn/ui Theming](https://ui.shadcn.com/docs/theming) · [Tailwind Tokens 映射](tailwind-tokens.md)。
