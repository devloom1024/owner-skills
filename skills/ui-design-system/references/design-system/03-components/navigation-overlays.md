# Navigation & Overlays — 导航、菜单、弹层

## 选择规范

- **Navigation**：主要信息架构用 Sidebar/Rail/Tab；当前页内部用 Tabs；位置层级深时用 Back/Breadcrumb。
- **DropdownMenu**：收纳同一对象的动作，但重要路径须有明确可见入口。
- **Popover**：锚定上下文的小型非模态信息/控件；不是大型表单和长文档容器。
- **Dialog**：需用户完成或取消的短任务；不宜包含复杂多屏导航。
- **Sheet**：侧边滑出层，承载上下文相关的次级信息或简单任务；复杂、多步任务用页面。
- **Drawer / Bottom Sheet**：移动端底部动作选择或短任务容器；不要把复杂桌面导航压缩进底部抽屉。
- **AlertDialog**：高风险确认，描述后果及恢复方式；不应滥用“确认/取消”增加无意义点击。

## 语义映射

| 语义 | 典型平台载体 | 组件选择提示 |
|---|---|---|
| 侧边次级面板 | Desktop / 宽屏 | `Sheet`，必要时作为页面布局的一部分而非浮层 |
| 移动端动作列表 | Touch / 小屏 | `Drawer` / Bottom Sheet，动作可见且可返回 |
| 短任务模态 | All | `Dialog`，有标题、焦点约束和明确取消/完成 |
| 高风险确认 | All | `AlertDialog`，显示对象、后果和恢复方式 |

## 必须遵守

1. 所有模态层有明确标题与关闭策略；焦点进入、退出恢复、Escape/返回行为合理。
2. 非模态菜单失焦/选择后可以关闭；与主任务无关的弹层不抢焦点。
3. 动作顺序保持一致：主动作明显；危险动作与普通动作适度分离。
4. Overlay 不应覆盖软件键盘下方必须点击的提交按钮；移动端处理安全区。
5. 不用 Bottom Sheet 实现“桌面侧栏的缩小版”复杂导航。

具体的跨平台决策： [Navigation Pattern](../04-patterns/navigation/overview.md) / [Overlays Pattern](../04-patterns/overlays/overview.md)。React/shadcn 的底层映射见 [adapter](../adapters/react-shadcn.md)。
