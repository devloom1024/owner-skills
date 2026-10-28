# UI 设计系统 — 规范优先

> **定位**：跨项目、跨设备的 UI **设计规范**，不是 React 组件库。  
> **适用**：优先支持 React + TypeScript + shadcn/ui，也可以作为其他技术栈的设计依据。
> **采用版本**：记录实际安装的 owner-skills tag 或 commit；本目录不另行维护版本号。

## 一句话原则

**统一 Pattern（信息与业务行为）→ 分别规定桌面和移动呈现（布局与输入）→ 按 Design Token 落地 → 使用清单验收。**

## 使用边界

本目录维护 `ui-design-system` 的共享参考基线；项目已有设计系统和已批准的适配优先，不复制第二套规范。AI 按任务读取相关资料，接入方式见 [Skill 入口](../../SKILL.md) 和 [AGENTS 示例](AGENTS.example.md)。

## 设计目标

1. **跨页面一致**：相同用途使用相同语义与页面模式。
2. **跨项目复用**：规范不绑定 React API、路由、状态管理和品牌配色。
3. **跨端一致而不雷同**：信息架构和行为一致，布局和操作方式根据空间与输入适配。
4. **可交给 AI 执行**：优先规则、明确数值、正反例、例外条件和验收项目。
5. **规范优先**：不维护独立 TSX 组件源码；技术实现只在 `adapters/` 提供映射指导。

## 目录与阅读顺序

| 顺序 | 路径 | 解答的问题 |
|---|---|---|
| 1 | `01-principles` | 我们为何这样设计？平台间什么必须一致、什么允许变化？ |
| 2 | `02-foundations` | 字体、空间、圆角、颜色如何确定？ |
| 3 | `03-components` | 基础组件应该如何使用？ |
| 4 | `04-patterns` | Settings、List、Detail、Form、Navigation、Overlays 如何统一？ |
| 5 | `05-platforms` | 窗口、输入方式、导航和移动端安全区如何适配？ |
| 6 | `06-governance` | 如何检查、处理例外和演进规范？ |
| 7 | `07-examples` | 如何查看结构示例及正反例？ |
| 可选 | `adapters` | 如何映射到 React、shadcn/ui 和 Tailwind？ |
| 项目接入 | `AGENTS.example.md` | 如何约束 AI 编码工具？ |

规范强度与 `MUST`、`SHOULD`、`MAY` 的解释见 [规范强度](06-governance/normative-levels.md)。

## 页面模式

Settings、List、Detail、Form、Navigation 和 Overlays 都使用共享的 `overview.md`，并按需要读取桌面和移动文件。

## 规范优先级

以 [规范强度与优先级](06-governance/normative-levels.md) 为准。不要把本 Skill 的默认视觉数值置于项目已采用的设计系统和批准适配之上，也不要用例外绕过安全或无障碍要求。

窗口宽度、指针类型和操作系统发生差异时，根据可用容器空间、输入方式和平台行为分别判断，不使用单一宽度阈值代替平台分析。

## 使用方法

1. 通过 `$ui-design-system` 使用本 Skill，按任务路由读取资料。
2. 开发前阅读 Tokens、Components 和目标 Pattern 的适用文件。
3. 先描述 结构、状态、导航和适配，再使用已有组件实现。
4. 完成后运行 UI 验收清单；项目差异使用例外模板记录。

## 版本和授权

版本和变更由 [owner-skills 仓库](https://github.com/devloom1024/owner-skills) 统一管理，已发布版本见 [Releases](https://github.com/devloom1024/owner-skills/releases)。独立安装保留 Skill 内的 [NOTICE](../../NOTICE)，包含署名、来源和 CC BY 4.0 许可链接；这些引用不依赖仓库根目录。

## 参考来源

本规范参考 Apple Human Interface Guidelines、Microsoft Fluent 2、shadcn/ui Theming 和 WCAG 2.2。表格中的尺寸是项目推荐基线，不是平台官方硬性值；目标平台需要进行适配。
