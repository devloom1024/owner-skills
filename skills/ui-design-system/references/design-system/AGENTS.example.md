# AI UI Development Contract — UI Design System

> 可选的项目 AI 契约模板。仅合并适用条款，保留项目已有设计系统与指令；记录采用的 Skill tag/commit，不复制一套独立规范。

## 基础约定

- 若项目使用 React + TypeScript + shadcn/ui，按实际组件版本读取对应 adapter；其他技术栈沿用已有实现，不为使用此 Skill 引入 shadcn/ui。
- 采用 `$ui-design-system` 的规范优先级：强制约束优先，项目已采用的系统和批准适配先于 Skill 默认建议；复用现有 Tokens，不散落无依据的数值。
- 在一个页面使用同一个 Pattern，不得为相同页面功能另外设计一套视觉和交互风格。

## 每次 UI 任务的基础阅读

调用 `$ui-design-system`，先读取设计系统索引、Design Token、Responsive、输入方式、Accessibility、规范强度 和 UI 验收清单；根据任务再读取 Components、目标 Pattern 的 `overview.md` 与适用的 `desktop.md` / `mobile.md`。React/shadcn/Tailwind 任务再读取对应 adapter。项目中不需要存在同名文件。

## 必须遵守

- 先写明页面属于何种 Pattern、有哪些导航和状态、使用哪些平台适配策略，再实现。
- 共性业务行为不随 桌面端/移动端 改变；布局和可见操作入口可适配；窄窗口≠手机，触屏≠小窗口。
- 优先使用项目已有组件；已使用 shadcn/ui 时复用对应实现，不无理由新建 Button、Dialog、Sheet、SettingsRow 等重复组件。
- 遵守语义颜色、字号/行高、密度、间距、圆角与 focus/empty/error/loading/disabled 状态。
- 按规范强度区分 `MUST`、`SHOULD` 和 `MAY`；推荐数值可适配，例外不能取消安全或无障碍要求。
- 危险操作必须有清晰标识与适当确认；不可只依靠悬停、右键或长按才能操作关键任务。
- 图片与视觉示例只是辅助，规范文本和可访问性优先。

## 完成任务时必须说明

- Pattern 与 Shared/桌面端/移动端 文档：
- 复用的组件与 Tokens：
- 实际检查的容器宽度 / 输入方式：
- 已验证的键盘、触控、浅色/深色、状态：
- 验证证据（环境、工具或截图/录屏；未覆盖项写明原因）：
- 例外及原因（无例外写“无”；记录模板见 `$ui-design-system` 的 例外 & Versioning 参考）：
