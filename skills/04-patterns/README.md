# Page & Interaction Patterns — 页面模式总则

## 组织原则

本目录的每种模式固定由三个文档构成：

- `overview.md`：平台无关的任务、Anatomy、共享状态、业务语义、Do/Don't 与验收。
- `desktop.md`：桌面（鼠标/键盘、通常更充裕空间）布局与交互的**推荐实现**。
- `mobile.md`：移动（触摸、有限空间）布局与交互的**推荐实现**。

**不是三种独立设计系统**。Desktop/Mobile 的差异不能改变 shared 文档定义的用户目标、数据含义、保存/删除后果。宽度和输入方式由 [Responsive](../05-platforms/responsive.md) 和 [Input Methods](../05-platforms/input-methods.md) 进一步调整。

## 模式清单

| 模式 | 主要职责 | 阅读顺序 |
|---|---|---|
| [Settings](settings/overview.md) | 用户偏好、账号、安全设置 | overview → desktop/mobile |
| [List](list/overview.md) | 搜索、筛选、选择、浏览集合 | 同上 |
| [Detail](detail/overview.md) | 阅读、操作单对象 | 同上 |
| [Form](form/overview.md) | 创建/编辑/提交数据 | 同上 |
| [Navigation](navigation/overview.md) | 顶层/层级/上下文导航 | 同上 |
| [Overlays](overlays/overview.md) | 弹窗、菜单、辅助任务 | 同上 |

## Page Shell 与组件如何配合

`App Shell` 决定全局导航；`Page Shell` 决定标题、工具栏、内容和滚动边界；Pattern 决定具体内容区组织。组件只管理内部状态与样式。参见 [Page Shell](page-shell.md)。

## 通用文档契约（后续新增模式必须遵守）

1. Purpose / Use Cases — 为什么存在、什么时候使用。
2. Anatomy — 由哪些区域构成、优先关系。
3. Specifications — 可验证的尺寸/顺序/边距（尽量引用全局 Token）。
4. Behavior & States — Loading/Empty/Error/Save/Back 等。
5. Platform Differences — Desktop/Mobile 专门文档链接。
6. Do / Don't — 正反例。
7. Exceptions & Acceptance — 哪些例外合理、如何检查。

## 模式组合示例

管理后台通常是 `App Navigation + List → Detail → Form`；个人工具的设置是 `Navigation + Settings`，Settings 里可以触发 `Form` 或 `Overlays`。不要因为页面里出现了表格，就把整个页面定义成 2 个并行顶层 Patterns；应该明确主任务和从属交互。
