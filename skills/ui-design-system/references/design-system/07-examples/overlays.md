# Overlays — 类型选择与反例

规范：[共享](../04-patterns/overlays/overview.md) · [桌面](../04-patterns/overlays/desktop.md) · [移动](../04-patterns/overlays/mobile.md)

## 同一操作的不同呈现

| 用户任务 | 桌面端 | 移动端 | 共同行为 |
|---|---|---|---|
| 对象“更多” | DropdownMenu | Action Sheet / 可见菜单 | 相同动作列表和后果 |
| 删除确认 | AlertDialog | AlertDialog / 明确确认 Sheet | 显示对象和不可逆后果 |
| 选择过滤条件 | Popover/侧面筛选区 | Filter Drawer | 选中、取消、重置语义相同 |
| 多步骤编辑 | 独立 Form Page | 独立 Form Page | 错误/草稿/提交一致 |

## 示例：删除操作

```text
触发（可见：删除）
       ↓
确认弹层：删除「Project Alpha」？
说明：该操作不可恢复，将移除项目及其关联记录。
[取消]             [删除项目（危险操作）]
       ↓
成功：列表更新 + 可理解反馈
失败：保留对象 + 提供重试信息
```

## 应该 / 不应该

✅ 可见入口、清楚后果、焦点恢复；移动端 Sheet 处理软键盘/安全区。
❌ 三层弹窗连续叠加；不显示后果、默认按钮直接删除；用 Tooltip 隐藏必需输入说明。

## 验收

Escape/Back/遮罩点击、无保存内容与有未保存内容、错误反馈、横屏与软键盘、键盘焦点归还。
