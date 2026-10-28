# Colors — 语义颜色与状态

## 颜色层级

| Token | 语义 | 对应 shadcn/ui 可参考映射 |
|---|---|---|
| `color.bg.canvas` | 最外层页面背景 | `background` |
| `color.bg.surface` | 面板和卡片表面 | `card`、部分 `popover` |
| `color.bg.muted` | 次要区域、hover 表面 | `muted`、`accent` |
| `color.text.primary` | 正文及主要标题 | `foreground` |
| `color.text.secondary` | 注释、时间、描述 | `muted-foreground` |
| `color.border.default` | 边界与分隔线 | `border` |
| `color.action.primary` | 主操作 | `primary` |
| `color.action.on-primary` | 主操作上的文字 | `primary-foreground` |
| `color.state.success` | 成功、已完成、同步完成 | `success`（项目主题变量） |
| `color.state.warning` | 风险提示、待处理、部分完成 | `warning`（项目主题变量） |
| `color.state.info` | 中性提示、进行中、同步状态 | `info`（项目主题变量） |
| `color.state.danger` | 危险操作与错误 | `destructive` |
| `color.focus.ring` | 键盘焦点轮廓 | `ring` |

## 设计规则

- 尽量保留灰阶与一个主要强调色；强调色用于交互与状态，不用来给普通卡片增加视觉噪音。
- 只通过语义调整主题，不在组件级重复写亮/暗两套具体颜色。
- 同一状态的颜色、文字、图标至少两者协同；不允许只靠红色或绿色解释结果。
- 一般正文目标达到 WCAG AA 正常文字 4.5:1；较大字体 3:1，非文本必要图形/控件状态也优先 3:1（具体适用条件以 WCAG 规范为准）。
- 选中、Hover、Active、Focus、Disabled 必须可区分；Focus 不应被 Hover 背景取代。
- 深色主题不仅是颜色反转；阴影、边界、表面层级应重新核对。

## 应该 / 不应该

✅ “危险删除”用 destructive token + 明确动词。  
❌ 用品牌蓝色表示普通选中，又在另一个页面用同蓝色表示错误。  
✅ 空白/加载/错误状态使用同一语义配色。  
❌ 低对比度灰字承载账户余额、错误信息或必须操作。

## 验收

Light/Dark 下抽检正文/辅助/按钮/链接/错误/Focus/禁用，检查对比度和可辨识性；禁用状态信息也应通过上下文让用户理解其原因。
