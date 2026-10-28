---
name: project-docs
description: 建立、整理、审计和验证项目文档体系。用于 docs 目录、AGENTS.md、架构地图、子系统参考、包 README、指南、规范、Agent Notes、postmortem 和契约索引的设计与维护。无论用户说“整理文档”“检查文档是否合理”还是“让代码文档同步”，都先使用此 Skill；默认只读规划，不自动修改项目文档。
---

# 项目文档

负责文档的职责、放置、当前事实、导航和验证。设计理由交给 `project-design-notes`，代码变化影响交给 `project-change-sync`，变更正确性审查交给 `project-code-review`。

## 先读什么

1. 根目录和变更路径祖先的 `AGENTS.md`；
2. [文档模型](references/document-model.md)；
3. [指令层级](references/instruction-hierarchy.md)；
4. [事实验证](references/fact-check.md)；
5. 项目自身的 `docs/AGENTS.md`、文档索引和验证脚本。

## 工作流

1. 固定范围：新项目、已有项目审计、单页更新、目录重组或迁移。
2. 识别读者、文档主要职责和事实所有者；一份文档只拥有一个主要职责。
3. 先读事实来源：源码、配置、测试、生成器、包 manifest 和当前决策记录。
4. 选择文档位置：入口、架构地图、当前子系统、包 README、规范、Agent Note、postmortem、指南或契约索引。
5. 当前事实只写已经有证据的行为；目标行为放入 `project-design-notes` 管理的 `proposed` 记录。
6. 更新文档入口、索引、本地链接、生成器说明和验证命令。
7. 记录来源、置信度、未验证命令和仍需人工决定的语义。
8. 修改前生成逐文件计划和备份 manifest；迁移按批次执行并逐批验证。

## 目录职责

- `architecture.md`：系统组合、主要运行路径、扩展点和阅读路线。
- `subsystems/`：一个主题的当前类型、语义、实现边界、源码位置、状态和验证；不替代高层架构地图。
- 包 README：包配置、公开接口、限制、扩展点、用户/模型可见行为和包级验证。
- `standards/` 或项目等价目录：规范性规则、理由和验证证据。
- `agent-notes/`：持久化设计理由和决策生命周期。
- `postmortem/`：事故故事、证据、因果链和预防；只有项目定义了其他 Lessons 层时才使用该名称。
- `guides/` 或 cookbook：面向结果的有序操作步骤。
- `contracts/`：真实机器可读契约的源、生成器、产物和语义所有者索引。
- 生成参考：由源代码和生成器拥有，禁止手工编辑生成区域。

## 文档更新

代码变化影响职责、接口、状态、失败、兼容性、配置、生成区域、公开文案或操作流程时，在同一变更中更新对应所有者，或记录 `not-needed` / `review-required` 的证据。先更新事实源，再更新派生文档。

## 输出

使用 [报告格式](references/report-format.md)；至少包含范围、目录职责、有效 AGENTS.md、事实所有者、证据、验证结果、未决事项和迁移批次。

## 评估

正常、边界和失败/不确定场景见 [evals/evals.json](evals/evals.json)，输入 fixture 位于 `evals/files/`。
