# AI UI Development Contract — UI Design System v1.1.1

> 可选的项目 AI 契约模板。合入项目 `AGENTS.md` 后，用 `$ui-design-system` 作为唯一 UI 规范来源；不要复制本目录或维护第二套规范。

## 基础约定

- 若项目使用 React + TypeScript + shadcn/ui，优先复用对应 adapter；无论技术栈如何，设计决策都**以 Skill 规范为准**，不是以示例代码为准。
- 设计遵循 `$ui-design-system` 的优先级；不得绕过 Tokens 自行发明新数值。
- 在一个页面使用同一个 Pattern，不得为相同页面功能另外设计一套视觉和交互风格。

## 每次 UI 任务的基础阅读

调用 `$ui-design-system`，先读取设计系统索引、Design Tokens、Responsive、Input Methods、Accessibility、Normative Levels 和 Review Checklist；根据任务再读取 Components、目标 Pattern 的 `overview.md` 与适用的 `desktop.md` / `mobile.md`。React/shadcn/Tailwind 任务再读取对应 adapter。项目中不需要存在同名文件。

## 必须遵守

- 先写明页面属于何种 Pattern、有哪些导航和状态、使用哪些平台适配策略，再实现。
- 共性业务行为不随 Desktop/Mobile 改变；布局和可见操作入口可适配；窄窗口≠手机，触屏≠小窗口。
- 优先使用项目已有组件、shadcn/ui；不要无理由新建 Button、Dialog、Sheet、SettingsRow 等重复组件。
- 遵守语义颜色、字号/行高、密度、间距、圆角与 focus/empty/error/loading/disabled 状态。
- 除非记录例外，按 Normative Levels 区分 `MUST`、`SHOULD` 和 `MAY`；推荐数值不是平台硬性值。
- 危险操作必须有清晰标识与适当确认；不可只依靠悬停、右键或长按才能操作关键任务。
- 图片与视觉示例只是辅助，规范文本和可访问性优先。

## 完成任务时必须说明

- Pattern 与 Shared/Desktop/Mobile 文档：
- 复用的组件与 Tokens：
- 实际检查的容器宽度 / 输入方式：
- 已验证的键盘、触控、浅色/深色、状态：
- 验证证据（环境、工具或截图/录屏；未覆盖项写明原因）：
- 例外及原因（无例外写“无”；记录模板见 `$ui-design-system` 的 Exceptions & Versioning 参考）：
