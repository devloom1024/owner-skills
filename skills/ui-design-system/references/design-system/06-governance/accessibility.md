# Accessibility — 无障碍最低标准

## Web 端采用 WCAG 2.2 AA 为默认验收目标

- 普通文字一般目标 ≥4.5:1，对符合大文字定义的文字 ≥3:1；必要的控件状态/非文本图形一般 ≥3:1（存在规范例外，验收时核对条款）。
- Pointer target 依 WCAG 2.2 SC 2.5.8 的基本条件 ≥24×24 CSS px，或满足其列出的豁免/间距条件；本设计系统默认舒适触摸推荐 ≥44×44 CSS px。
- 全部功能可通过键盘使用；焦点可见，焦点顺序符合阅读与任务顺序，模态焦点合理进入与返回。
- 使用文字标签、可访问名称、错误说明、表单关联、状态反馈；颜色不能是唯一信息载体。
- 支持缩放与系统大字体，关键内容不被裁切；避免仅靠拖拽、多点触控或复杂手势。
- 尊重 `prefers-reduced-motion`；动画/弹层不造成必须等待的障碍。

## Pattern 验收最低场景

Settings：开关说明、错误回滚、关联 Label。  
List：表格表头、可见排序状态、分页/过滤状态。  
Detail：可达的返回路径、隐藏面板不丢失关键信息。  
Form：字段关联、错误聚焦、保存反馈。  
Navigation：当前层级、快捷键、响应式重排。  
Overlays：焦点约束/恢复、Escape/返回、关闭后状态。

## 注意

本规范不是完整 WCAG 审计报告；具体法定义务依部署地区与产品类型而异。参考 [WCAG 2.2](https://www.w3.org/TR/WCAG22/) 和 [Target Size (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum)。
