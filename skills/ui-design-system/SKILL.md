---
name: ui-design-system
description: 使用规范优先的跨平台 UI 设计系统，实现、审查或扩展覆盖桌面、移动、触控、键盘和响应式布局的产品界面。用于设计决策和 UI 实现指导，不是 React 组件库，也不提供像素级设计资产。
metadata:
  short-description: 跨平台 UI 设计与审查
---

# UI 设计系统

当 UI 任务需要统一 Pattern、Design Tokens、平台适配、无障碍检查或记录项目例外时，使用此 Skill。参考资料包含必须遵守的语义和无障碍规则，以及可以按项目适配的视觉基线；它不是可直接安装的组件库。

## 工作流

1. 确定任务模式：实现 UI、审查已有 UI，或扩展系统中的 Pattern、Token 和适配器。
2. 确定主要 Pattern、运行平台、可用容器空间和输入方式。不要把窄窗口等同于手机，也不要把触控输入等同于小布局。
3. 先识别项目已采用的设计系统、组件、Token 和已批准适配，再依据 [规范强度与优先级](references/design-system/06-governance/normative-levels.md) 处理冲突。项目视觉基线优先于本 Skill 的默认建议，但不能绕过安全、无障碍和平台强制约束。
4. 只读取当前任务和 Pattern 需要的参考资料，技术适配器按所选技术栈加载。
5. 实现或审查后，报告使用的 Pattern 和参考资料、复用的组件和 Token、验证的视口和输入条件、检查的状态，以及记录的例外。

## 参考资料路由

从 [设计系统索引](references/design-system/README.md) 开始，再按任务读取参考资料。交付时读取 [UI 验收清单](references/design-system/06-governance/review-checklist.md)。

| 任务 | 共享参考资料 | 按需参考资料 |
|---|---|---|
| 实现页面 | Principles、Tokens、Components、Responsive、Input Methods、Accessibility、Review Checklist | 目标 Pattern 的 `overview.md`、`desktop.md`、`mobile.md`；所选技术适配器 |
| 审查或审计 UI | Principles、Tokens、Responsive、Input Methods、Accessibility、Review Checklist | 目标 Pattern 和能说明问题的示例 |
| 扩展 Pattern 或 Token | 设计系统索引、相关 Principles、Tokens、例外和版本规则 | 受影响的 Pattern、平台文件、示例和适配器 |
| React/shadcn/Tailwind 实现 | 所选任务的共享参考资料 | React/shadcn 和 Tailwind 适配器 |

Pattern 位于 `references/design-system/04-patterns/<pattern>/`，示例位于 `07-examples/`。示例是结构参考，不是强制模板。

## 规范来源与项目接入

`references/design-system/` 是本 Skill 的共享基线，不替代项目已有设计系统。项目复用既有组件和 Token，只记录采用范围及适配差异，不复制第二份会独立漂移的规范。需要建立接入约定时参考 [AGENTS 示例](references/design-system/AGENTS.example.md)，不要机械覆盖项目规则。

## 规范强度

无障碍、语义行为、键盘可达、焦点处理和平台安全约束属于必须遵守的规则。尺寸、断点、密度和视觉值属于推荐基线；项目可以适配，但要记录原因、影响、所有者和复审条件。

## 完成报告

实现或审查时包含：

- 使用的 Pattern 以及共享、桌面、移动参考资料；
- 复用的组件和 Token，以及新增的语义值；
- 容器宽度、输入方式、主题/缩放和已验证状态；
- 无障碍、键盘和触控检查；
- 验证证据、环境、工具或截图/录屏，并说明未覆盖检查；
- 例外及其理由；没有例外时写“无”。
