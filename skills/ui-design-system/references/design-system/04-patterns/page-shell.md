# Page Shell — 页面通用骨架

## 结构

1. **Navigation Context**：从哪里来、当前位置（由 App Shell 或 Pattern 提供）。
2. **Page Header**：唯一主要标题、摘要/状态、主操作；高度随内容变化。
3. **Page Tools**：搜索、筛选、排序、页内 Tab 等（按需）。
4. **Main Content**：页面主 Pattern；尽量只有一条明确滚动主线。
5. **Supplementary Content**：可选 inspector、帮助信息；窄空间优先折叠。
6. **Feedback Layer**：加载、错误、Toast、Modal；与主体的层级相符。

## 规则

- 页面边距仅由 Page Container 控制，Pattern 不重复管理最外层留白。
- 主操作的位置应在同一类页面中保持稳定；不要一页右上角、一页卡片底、一页悬浮角落。
- 固定标题栏或固定底部动作条不得遮挡滚动内容；留足有效底部 inset。
- 页面主体的阅读顺序应匹配 DOM/键盘导航顺序；视觉重新排列也不能破坏可访问性。
- 长页面默认单一主滚动区；两个独立滚动列必须有明确工作流理由。

## 参考尺寸

桌面端 Page Padding 24px（宽屏可 32px）；移动端 Content Padding 16px + Safe Area；设置阅读宽 720px，表单阅读宽 640px。来自 [Foundations](../02-foundations/design-tokens.md)。

## 验收

缩窄窗口、打开软键盘、放大 200% 字体、增加长状态提示，确认 Page Header / Main / Actions 都仍可访问。
