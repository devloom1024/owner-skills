# Components — 基础组件使用规范

> 本层规定**什么时候用什么组件**、组件间的视觉/交互关系及状态，不重新封装或发布 React 组件。

## 组件选择矩阵

| 用户意图 | 首选 | 不应使用 |
|---|---|---|
| 执行立即动作 | Button | 用文字模拟按钮却不可键盘激活 |
| 进入另一页面 | Link / 可访问导航项 | 无描述的图标按钮 |
| 布尔开/关且即时生效 | Switch | 无操作时机提示的 Checkbox |
| 多选选项或提交时生效 | Checkbox | 把多选放在 Radio 中 |
| 互斥选一 | Radio / Select / Segmented（少量） | 多个独立 Switch |
| 筛选当前结果 | Search / Filter / Combobox | 无反馈的自由输入 |
| 补充说明 | Tooltip（Desktop 辅助）/ 帮助文本 | 把关键信息只藏在 Hover |
| 重要确认 | AlertDialog | 仅 Toast 后立即不可逆删除 |
| 临时次级任务 | Dialog / Sheet | 为每个简单动作强制跳独立页 |

## 使用顺序

1. 首先选择 Pattern 指定的语义组件；其次选 shadcn/ui 对应基础组件。
2. 使用全局 Design Tokens，不因新页面改变 Button 高度/圆角。
3. 在所有组件状态下保持相同标签、位置、反馈；禁止仅通过颜色表达状态。
4. 只有当确实存在未覆盖的业务交互，才能新增业务组合模式，并进入例外/版本流程。

## 组件必须定义的状态

- Default / Hover（如设备支持） / Active / Focus-visible / Disabled。
- Loading / Success / Error / Empty（适用场景）。
- 键盘激活、触摸目标以及可访问名称。

## 页面级验收

- 相同操作语义是否采用相同基础组件？
- 桌面右键菜单中的核心动作，是否也有非右键入口？
- Hover 下才出现的操作，键盘和触屏是否都能发现？

参见：[Actions & Inputs](actions-inputs.md) · [Navigation & Overlays](navigation-overlays.md) · [Feedback & States](feedback-states.md)。
