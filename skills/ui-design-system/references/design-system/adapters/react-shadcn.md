# Adapter — React + TypeScript + shadcn/ui（可选实现指南）

> 本文件解释“怎样映射”，**不是可复制运行的组件库**，不提供固定业务组件 API。

## 基础落地

1. 先检查项目已有组件源码、`components.json`、package manifest/lockfile、导入和本地改动，确定实际 API 与底层原语。只有项目已采用或用户选择 shadcn/ui 时才按需补组件；不为符合本 Skill 自动初始化、升级或替换组件库。
2. 沿用项目语义主题，将 [Tokens](../02-foundations/design-tokens.md) 的概念映射到已有的 `background`、`foreground`、`primary`、`muted`、`destructive`、`border`、`ring` 等变量。不同版本/变体可能使用 Radix UI、Base UI 或其他原语，不假定它们 API 和行为相同。
3. 利用主题变量及统一的密度策略映射文字与高度；不对每个按钮硬编码一次高度和圆角。
4. 页面开发先指定 Pattern，例如 `settings`；按 `overview.md` 实现共享结构，再对照 桌面端/移动端 文件实现布局与交互。
5. 如果多个项目需要复用 SettingsRow 等组合组件，先在项目中验证，再决定是否抽出公共包；规范本身不强制某个 TSX API。

## 组件映射（规范概念 → shadcn/ui 组件）

> 下表是候选映射，不是组件存在或能力内置的保证。核对项目实际源码和对应版本/变体的官方文档；新文档与旧组件不匹配时先说明差异，不隐式升级依赖。所有映射仍需验证标签、键盘、焦点和目标平台行为。

| 规范概念 | shadcn/ui 组件 | 说明 |
|---|---|---|
| Dialog | `dialog` | 需完成/取消的短任务模态 |
| AlertDialog | `alert-dialog` | 危险确认；不默认聚焦危险按钮 |
| Dropdown / Context Menu | `dropdown-menu` / `context-menu` | 收纳对象动作，不作为唯一入口 |
| Popover / Tooltip | `popover` / `tooltip` | 锚定辅助信息，核心内容不只放 Tooltip |
| Sheet（侧边抽屉） | `sheet` | 通用侧边滑出层 |
| Drawer / Bottom Sheet（移动端底部） | `drawer`（若项目版本提供） | 底部动作层；确认项目版本的 API、焦点和安全区行为 |
| Navigation 侧栏 / Rail / 移动端抽屉 | 已有导航组合或 `sidebar` | 验证实际折叠、移动入口和焦点行为，不因组件名称假定已满足 Pattern |
| Form 字段（Label + 控件 + 说明/错误） | 项目表单组合或可用的 `field` | 验证标签、描述、错误与控件关联，不要求替换已有表单方案 |
| Empty 状态 | 项目 Empty 组件或可用的 `empty` | 空数据/无结果配说明与下一步动作 |
| Search / Combobox（搜索过滤与选择） | 项目已有 Combobox、对应变体的 `combobox`，或 `popover` + `command` 组合 | 独立 Combobox API 与旧组合不能混用；按实际实现验证输入、选中、焦点和键盘语义 |
| Segmented（少量互斥切换） | 项目对应组件、`tabs` 或单选 `toggle-group` | 按切换内容还是选择值决定语义，不凭外观互换 |

## 项目集成建议（非强制）

本 adapter 由已安装的 `ui-design-system` Skill 按需读取。以下项目路径只描述实现代码的组织方式，不要求把规范文档复制到项目中。

- `src/components/ui`：已有 shadcn 基础组件。
- `src/components/patterns`：项目自己的 Pattern 组合实现。
- `src/pages` 或路由目录：业务页面。
- 组件库/样式变更以视觉回归与清单为准，不以 HTML 结构相同为目标。

参见 [shadcn/ui Installation](https://ui.shadcn.com/docs/installation) · [Combobox](https://ui.shadcn.com/docs/components/combobox) · [Theming](https://ui.shadcn.com/docs/theming) · [Tailwind Tokens 映射](tailwind-tokens.md)。
