# UI Design System v1.1 — Specification First

> **定位**：跨项目、跨设备的 UI **设计规范**，不是 React 组件库。  
> **适用**：React + TypeScript + shadcn/ui 优先，也可作为其他技术栈的设计依据。  
> **版本**：v1.1.1 · 2026-10-25 · 初版可用 / 迭代完善。

## 一句话原则

**统一 Pattern（信息与业务行为） → 分别规定 Desktop / Mobile 呈现（布局与输入） → 按 Design Tokens 落地 → 使用 Checklist 验收。**

## 使用边界

本目录是 `ui-design-system` Skill 的唯一参考资料。Skill 按任务从这里读取文档；不要把规范复制到产品仓库，也不要维护第二套 UI 规范。`AGENTS.example.md` 只是可选的项目 AI 契约，Skill 的任务路由和读取顺序见包根目录的 `SKILL.md`。

## 设计目标

1. **跨页面一致**：相同用途使用相同语义与页面模式；避免七八种 Settings。
2. **跨项目可复用**：规范不绑死 React API、路由、状态管理和品牌配色。
3. **跨端一致而不雷同**：信息架构和行为一致，布局与操作方式根据空间/输入适配。
4. **可交给 AI 执行**：优先规则、明确数值、Do/Don't、例外条件及验收项目。
5. **Specification First**：不维护独立 TSX 组件源码。技术实现仅在 `adapters/` 提供映射指导。

## 目录与阅读顺序

| 顺序 | 路径 | 解答的问题 |
|---|---|---|
| 1 | [01-principles](01-principles/design-philosophy.md) · [平台哲学](01-principles/platform-philosophy.md) | 我们为何这样设计？平台间什么必须一致、什么允许变化？ |
| 2 | [02-foundations](02-foundations/design-tokens.md) · [Typography](02-foundations/typography.md) · [Colors](02-foundations/colors.md) · [Spacing](02-foundations/spacing-layout.md) · [Radius](02-foundations/radius-elevation.md) · [Icons & Motion](02-foundations/icons-motion.md) | 字体、空间、圆角、颜色如何确定？ |
| 3 | [03-components](03-components/overview.md) | shadcn/ui 等基础组件应如何使用？ |
| 4 | [04-patterns](04-patterns/README.md) | Settings / List / Detail / Form / Navigation / Overlays 如何统一？ |
| 5 | [05-platforms](05-platforms/responsive.md) · [Desktop](05-platforms/desktop.md) · [Mobile](05-platforms/mobile.md) · [输入方式](05-platforms/input-methods.md) · [自适应导航](05-platforms/adaptive-navigation.md) | 窗口、输入方式、导航、移动端安全区如何适配？ |
| 6 | [06-governance](06-governance/review-checklist.md) · [Accessibility](06-governance/accessibility.md) · [Exceptions & Versioning](06-governance/exceptions-versioning.md) | 如何检查、处理例外、演进规范？ |
| 7 | [07-examples](07-examples/README.md) | 如何查看结构示例及正反例？ |
| 可选 | [adapters](adapters/react-shadcn.md) · [Tailwind Tokens](adapters/tailwind-tokens.md) | 如何映射到 React + shadcn/ui + Tailwind？ |
| 项目接入 | [AGENTS.example.md](AGENTS.example.md) | 如何约束 AI 编码工具？ |

## 页面模式导航

| 模式 | 统一规则 | 桌面端 | 移动端 | 示例 |
|---|---|---|---|---|
| Settings | [overview](04-patterns/settings/overview.md) | [desktop](04-patterns/settings/desktop.md) | [mobile](04-patterns/settings/mobile.md) | [example](07-examples/settings.md) |
| List | [overview](04-patterns/list/overview.md) | [desktop](04-patterns/list/desktop.md) | [mobile](04-patterns/list/mobile.md) | [example](07-examples/list.md) |
| Detail | [overview](04-patterns/detail/overview.md) | [desktop](04-patterns/detail/desktop.md) | [mobile](04-patterns/detail/mobile.md) | [example](07-examples/detail.md) |
| Form | [overview](04-patterns/form/overview.md) | [desktop](04-patterns/form/desktop.md) | [mobile](04-patterns/form/mobile.md) | [example](07-examples/form.md) |
| Navigation | [overview](04-patterns/navigation/overview.md) | [desktop](04-patterns/navigation/desktop.md) | [mobile](04-patterns/navigation/mobile.md) | [example](07-examples/navigation.md) |
| Overlays | [overview](04-patterns/overlays/overview.md) | [desktop](04-patterns/overlays/desktop.md) | [mobile](04-patterns/overlays/mobile.md) | [example](07-examples/overlays.md) |

## 规范优先级（解决冲突）

1. **可访问性与平台系统强制约束**（例如安全区域、键盘可达、系统权限）。
2. **本仓库全局基础规则**（Tokens、组件语义、反馈一致性）。
3. **对应 Pattern 的 `overview.md`**（功能结构与统一行为）。
4. **Pattern 的 Desktop 或 Mobile 文件**（具体呈现与交互）。
5. **项目级有记录的例外**（必须写明原因、范围、测试与到期复审）。

当窗口宽度、指针类型和 OS 平台发生冲突时，**不要把 `width < 600` 机械等同于“手机”**。布局参考容器可用空间；控件密度按输入方式和用户偏好；系统行为按操作系统。参见 [响应式原则](05-platforms/responsive.md)。

## 默认规范速查（本体系推荐基线，并非平台官方硬性值）

| 项目 | Compact / Desktop | Comfortable / Touch |
|---|---:|---:|
| 正文 | 14px / 行高 22px | 16px / 行高 24px |
| 辅助文字 | 12px / 18px | 14px / 20px |
| 页面标题 | 24px / 32px | 24px / 32px |
| 常规控件高度 | 36px（主动作 40px） | 44px（强调 48px） |
| 设置行最小高度 | 48px | 56px |
| 页面左右内边距 | 24–32px | 16px |
| 圆角：控件 / surface / overlay | 8 / 12 / 16px | 同一语义值 |
| 间距 | 4px 基础网格，语义档位 | 同一语义档位、可选择更舒适密度 |
| 设置内容最大宽度 | 720px | 填充容器减安全边距 |

## 使用方法

1. 通过 `$ui-design-system` 使用本 Skill，按任务路由读取参考文档。
2. 开发前阅读 [Tokens](02-foundations/design-tokens.md) + [组件规范](03-components/overview.md) + 目标 Pattern 的 `overview.md` 与适用平台文件。
3. 设计先描述 **Anatomy、状态、导航和适配**，再用已有 shadcn/ui 组件实现，不要为同一语义造第二种组件。
4. 完成后跑 [UI 验收清单](06-governance/review-checklist.md)；必要时按 [例外模板](06-governance/exceptions-versioning.md) 记录项目差异。

## 按任务读取

| 任务 | 先读 | 按需读取 |
|---|---|---|
| 实现页面 | Principles、Tokens、Components、Responsive、Input Methods、Accessibility、Review Checklist | 目标 Pattern 的 Shared/Desktop/Mobile；相关 adapter |
| Review / 审计 | Principles、Tokens、Responsive、Input Methods、Accessibility、Review Checklist | 目标 Pattern；必要时读取 examples |
| 扩展 Pattern 或 Token | README、相关 Principles、Tokens、Exceptions & Versioning | 受影响的 Pattern、平台规则、examples、adapters |

## v1.1 范围 / 非范围

**已包含**：六种核心页面/交互模式的 Shared + Desktop + Mobile 规范；主要 Tokens；组件使用约束；输入与响应式规则；文本结构示例；AI 接入规则。  
**暂不包含**：可直接运行的 React 页面库、Figma 组件资源、品牌色方案、自动化视觉回归工具、完整 i18n 设计资产。示例是**结构参考，不是像素级最终设计图**。

## 许可证

规范文档以 [CC BY 4.0](LICENSE) 授权。Skill 的分发、安装或再利用应保留来源与许可证声明。

## 参考来源与边界

- [Apple Human Interface Guidelines — Layout](https://developer.apple.com/design/human-interface-guidelines/layout)：平台适配、分组、视觉层级、安全区域。
- [Microsoft Fluent 2](https://fluent2.microsoft.design/)：桌面生产力 UI 设计理念与组件组织。
- [shadcn/ui — Theming](https://ui.shadcn.com/docs/theming)：语义主题 CSS 变量。
- [W3C WCAG 2.2 — Target Size (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum)：Web 指针目标最低要求及例外。

**说明**：本仓库表格中的字号、尺寸与断点是基于上述原则形成的项目默认推荐，不应误认为各平台官方规定。原生 iOS/Android 的 pt/dp/sp 和 Web CSS px 必须由目标平台适配，不做一比一套用。

[查看变更记录](CHANGELOG.md)
