# Design Tokens — 核心规范数值来源

## Token 设计规则

- 使用**语义名称**定义用途（如 `color.text.secondary`），不要按当前色值命名（如 `gray500`）。
- 本目录定义**规范层 Token**；项目里可映射到 shadcn `foreground`/`muted-foreground`/`border` 等现有变量。
- 数值按 `base → semantic → component state` 三层；组件规格引用语义，而不是重复硬编码。
- 允许 light/dark、compact/comfortable 设不同数值，但语义名称保持相同。
- 新建 Token 必须说明适用范围、现有替代为何不足、影响范围；不得为一个页面新增匿名值。
- 未明确标为 `MUST` 的数值按 `SHOULD` 处理；规则强度定义见 [规范强度](../06-governance/normative-levels.md)。

## 规范层 Token 总表（建议值）

| Token | 规范值 | 用途 |
|---|---|---|
| `space.1/2/3/4/5/6/8/10/12/16` | 4/8/12/16/20/24/32/40/48/64 px | 空间基准 |
| `radius.xs/control/surface/overlay/pill` | 4/8/12/16/9999 px | 形状语义 |
| `type.page-title` | 24/32, 600 | 页面头 |
| `type.section-title` | 16/24, 600（触控 17/26） | 分组标题 |
| `type.body` | 14/22, 400（触控 16/24） | 正文 |
| `type.label` | 14/20, 500（触控 16/24） | 输入项、按钮、行名称 |
| `type.caption` | 12/18, 400（触控 14/20） | 次要信息 |
| `type.micro` | 11/16, 500（触控 12/18） | 小徽标，仅非关键信息 |
| `size.control.default` | 36px（触控 44px） | 常规控件高度 |
| `size.control.prominent` | 40px（触控 48px） | 主操作 |
| `size.row.settings.min` | 48px（触控 56px） | 设置行最小高度 |
| `size.row.list` | Compact 约 44–52px，随内容增长 | 数据列表/表格行高 |
| `size.icon.visual` | 桌面端 16–20px；Touch 20–24px | 图标视觉尺寸（不等于触摸目标） |
| `layout.padding.page` | 24px（宽屏可 32；紧凑 16） | 页面边距 |
| `layout.width.settings` | 720px | 设置主内容最大宽 |
| `layout.width.form` | 640px | 常规表单主内容最大宽 |
| `layout.width.readable` | 720px | 长文本阅读宽度 |
| `layout.width.detail` | 880px（长篇正文局部 720px） | 详情页主列最大宽 |
| `focus.ring.width` | 2px | `:focus-visible` 轮廓宽度 |
| `focus.ring.offset` | 2px | 焦点轮廓与控件边界的间距 |
| `elevation.surface/overlay/modal` | subtle / raised / modal | 表面、浮层、模态的语义层级；具体阴影随主题映射 |
| `z.layer.base/sticky/overlay/modal/toast` | ordered layers | 层级顺序；项目实现不得让低层级覆盖高层级 |
| `inset.safe.inline/block` | 见 [安全区合并规则](spacing-layout.md) | 普通页面合并安全区；固定动作容器单独判断，避免重复计算 |
| `motion.fast/normal/slow` | 120 / 200 / 280 ms | 动效等级（减少动画时关闭非必要动作） |

字体 `字号/行高, 字重` 详见 [Typography](typography.md)；其余细则见 [Colors](colors.md)、[Spacing & Layout](spacing-layout.md)、[Radius & Elevation](radius-elevation.md)、[Icons & Motion](icons-motion.md)。**此表与分项文档冲突时，以分项文档详细场景限定为准；若数值发生变更，必须同步此总表。**

## 颜色语义，不在规范中锁定品牌 Hex

`color.bg.canvas`、`color.bg.surface`、`color.text.primary`、`color.text.secondary`、`color.border.default`、`color.action.primary`、`color.state.success`、`color.state.warning`、`color.state.info`、`color.state.danger`、`color.focus.ring` 等。各主题必须具备足够对比度，详见 [Colors](colors.md)。

## Exceptions / 例外机制

项目已有 Token 与批准适配优先于本表建议值；新的密度或品牌差异按 [例外机制](../06-governance/exceptions-versioning.md) 记录依据，并验证受影响状态。不能牺牲可访问性。

## 验收

- 单一语义是否只对应一个 Token（含各密度变体）？
- 是否出现无记录的 `13px`、`17px margin`、自定义圆角、散落 Hex？
- Light/Dark 与桌面/触控的 Token 映射是否完整？
