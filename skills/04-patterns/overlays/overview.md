# Overlays — Shared Interaction Pattern

## 1. Purpose

用于当前上下文内的**次级操作、短期决策、补充信息或风险确认**；不应用弹窗替代复杂的主流程和完整页面信息架构。

## 2. 类型决策（最关键）

| 用户任务 | 首选容器 | 原因 |
|---|---|---|
| 少量上下文操作 | Dropdown / Context Menu | 锚定对象，操作量小 |
| 简短补充信息 | Tooltip / Popover | 不打断主任务；核心内容不只用 Tooltip |
| 用户必须完成/取消的短任务 | Dialog | 明确任务边界与焦点 |
| 危险/不可逆操作确认 | AlertDialog | 后果明确、避免误触 |
| 移动端动作选择 | Action Sheet / Bottom Sheet | 适合触摸、当前情境 |
| 多步骤或复杂信息编辑 | Full Page / Flow | 可返回、软键盘/内容增长更可控 |

## 3. Shared Anatomy & Behavior

1. **Trigger**：可见可理解，不允许只有 Hover/右键/长按。
2. **Title / Purpose**：模态层清楚说明任务；简单菜单可不用完整标题。
3. **Content**：重点信息和可操作项；避免背景上下文丢失。
4. **Actions / Dismissal**：关闭、取消、确认；危险操作有明确后果说明。
5. **Focus / History**：打开后焦点进入合适位置；关闭后焦点返回触发位置或合理后续区域。

## 4. 交互不变的约束

- 模态阻止背景交互时应符合焦点约束；关闭后恢复到合理对象与原状态。
- Escape、点击外部或移动系统返回是否关闭，取决于有无未保存数据和任务风险；同类浮层统一。
- 不把错误反馈仅放在自动消失的 Toast；错误应在相关表单/模态内可读。
- 不叠加 2–3 层模态；允许的确认子层应极简，避免焦点/返回混乱。
- 内容过长时先评估是否应该是完整页面；避免浮层被软键盘或安全区域遮挡。

## 5. Do / Don't

✅ 选择对象更多动作使用明确菜单，危险操作单独确认。  
❌ 用 Tooltip 隐藏登录必需条件。  
✅ 修改账户邮箱这种较长流程使用专门页面。  
❌ 在小 Bottom Sheet 中塞三屏长表单与嵌套滚动。

## 6. 相关规范与验收

[Desktop](desktop.md) · [Mobile](mobile.md) · [示例](../../07-examples/overlays.md) · [shadcn 组件映射](../../adapters/react-shadcn.md)

检查：触发入口、Escape/Back、点击外部、软键盘、焦点恢复、未保存内容、屏幕阅读器、危险操作确认。
