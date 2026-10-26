# Feedback & States — 系统状态与反馈

## 六大状态

| 状态 | 最低规范 |
|---|---|
| Loading | 告知进行中，防重复提交，长耗时任务说明进度或阶段 |
| Empty | 说明为什么为空，给出合理下一步（创建/清空过滤） |
| Error | 明确问题、影响、恢复路径；错误信息在相关区域展示 |
| Success | 提供及时且不过度打断的反馈，如 Toast / 行内状态 |
| Disabled | 视觉可辨、语义禁用；必要时解释解锁条件 |
| Offline / Sync | 标注离线或同步中，对可能丢失的数据提出明确说明 |

## Pattern 状态扩展

六大状态是跨页面的基础集合；下列状态按 Pattern 追加，不要用空白页或通用 Error 代替：

| Pattern | 追加状态 | 最低反馈 |
|---|---|---|
| Settings | Policy-managed / Permission-limited | 显示来源、限制原因和可执行的替代路径 |
| List | No Results / Partial Updating | 保留搜索与筛选条件，提供清除、重试或局部更新反馈 |
| Detail | Not Found / Permission Denied / Stale Data | 说明对象身份、原因、返回路径和可恢复动作 |
| Form | Unsaved / Conflict | 保留输入，说明保存状态、冲突范围和覆盖/合并选择 |
| Navigation | Deep Link / Destination Unavailable | 显示当前位置、可返回的上级目的地和权限结果 |
| Overlays | Validation / Dismissal Blocked | 在浮层内显示错误；未保存时阻止静默关闭 |

## 通用规则

- 保存成功、失败、待保存状态必须可辨；不能只有 spinner 没有结果。
- Toast 用于短暂反馈，**不能承载唯一的关键错误信息**。
- 错误内容应可复制/复试，不能只提供“发生未知错误”。
- 页面切换时保护未保存内容；按风险提供阻止/确认/自动保存。
- 乐观更新失败必须回滚并告知用户；不要静默丢失变更。

## 验收

为每个新增页面写出适用的基础状态（Loading、Empty、Error、Success、Disabled、Offline/Sync）和 Pattern 扩展状态的展示与恢复入口；在窄窗口/触屏/键盘下分别核查。
