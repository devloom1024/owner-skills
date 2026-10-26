# AI UI Development Contract — UI Design System v1.1

> 可选的项目集成模板。仅在将本目录 vendored 到项目 `docs/design-system/` 后合入项目 `AGENTS.md`；若使用已安装的 `ui-design-system` Skill，请以 Skill 的 `SKILL.md` 路由为准。

## 基础约定

- 项目优先采用 React + TypeScript + shadcn/ui，但设计决策**以文档为准**，不是以示例代码为准。
- 设计遵循 `docs/design-system/README.md` 的优先级（vendored 模式）；不得绕过 Tokens 自行发明新数值。
- 在一个页面使用同一个 Pattern，不得为相同页面功能另外设计一套视觉和交互风格。

## 每次 UI 任务的基础阅读

1. `docs/design-system/README.md`
2. `docs/design-system/02-foundations/design-tokens.md`
3. `docs/design-system/05-platforms/responsive.md` 和 `input-methods.md`
4. `docs/design-system/06-governance/accessibility.md`
5. `docs/design-system/06-governance/review-checklist.md`

根据任务再读取 `03-components/overview.md`、目标 Pattern 的 `overview.md` 与适用的 `desktop.md` / `mobile.md`；React/shadcn/Tailwind 任务再读取 `adapters/`。

## 必须遵守

- 先写明页面属于何种 Pattern、有哪些导航和状态、使用哪些平台适配策略，再实现。
- 共性业务行为不随 Desktop/Mobile 改变；布局和可见操作入口可适配；窄窗口≠手机，触屏≠小窗口。
- 优先使用项目已有组件、shadcn/ui；不要无理由新建 Button、Dialog、Sheet、SettingsRow 等重复组件。
- 遵守语义颜色、字号/行高、密度、间距、圆角与 focus/empty/error/loading/disabled 状态。
- 危险操作必须有清晰标识与适当确认；不可只依靠悬停、右键或长按才能操作关键任务。
- 图片与视觉示例只是辅助，规范文本和可访问性优先。

## 完成任务时必须说明

- Pattern 与 Shared/Desktop/Mobile 文档：
- 复用的组件与 Tokens：
- 实际检查的容器宽度 / 输入方式：
- 已验证的键盘、触控、浅色/深色、状态：
- 例外及原因（无例外写“无”；记录模板见 `docs/design-system/06-governance/exceptions-versioning.md`）：
