# Radius & Elevation — 形状和层次

## 圆角 Token

| Token | 值 | 典型用途 |
|---|---:|---|
| `radius.xs` | 4px | 微型标签、简短状态容器 |
| `radius.control` | 8px | Button、Input、Select |
| `radius.surface` | 12px | Card、设置分组容器 |
| `radius.overlay` | 16px | Dialog、Sheet 可见内面板 |
| `radius.pill` | 9999px | 标签与胶囊按钮，头像独立圆形 |

## 层次顺序

基础页面背景（canvas）→ 内容表面（surface）→ 浮层（overlay）；优先利用背景层次和适度边框，**阴影不是卡片必需属性**。暗色模式可利用细边界、明度区分层次，避免强烈高斯阴影。

## Elevation 与层级

- 使用 `elevation.surface`、`elevation.overlay`、`elevation.modal` 表达语义层级，不在业务页面散落自定义阴影。
- 使用 `z.layer.base` → `sticky` → `overlay` → `modal` → `toast` 的顺序；具体数值由项目实现，但层级关系必须稳定。
- 深色主题可用边界和表面明度替代阴影；阴影强度不能成为唯一的层级信息。

## 规则

- 方形大面积主工作区可以保持直角；不要求把所有边界都卡片化。
- 同类卡片圆角一致，同级同语义共享边框/阴影；内层嵌套可减少额外圆角。
- 不在同一视野同时出现 6、9、12、14、18px 五种卡片圆角。
- 弹窗形态变化不改变层级语义、关闭策略和危险按钮规范。

## 验收

抽查一页中控件/卡片/弹窗的圆角来源；检查浅色与深色状态的层次以及嵌套边框数量。
