---
name: skill-maintenance
description: 维护 owner-skills 仓库及其 Skill 库。用于新增、拆分、翻译、评估、验证、版本发布和职责冲突审计；统一管理根 README、CHANGELOG、LICENSE 和 v1.0.0 之后的版本变化。
---

# Skill 仓库维护

保持每个 Skill 职责窄、入口清晰、引用有效、内容可验证，并让根仓库统一管理目录、版本、变更和授权。

## 工作流

1. 阅读根 README、CHANGELOG、LICENSE 和现有 Skill 目录。
2. 判断新增或修改是否属于已有 Skill，优先合并职责而不是复制。
3. 保持每个 Skill 只包含 `SKILL.md`、references、templates、scripts、evals 和必要资产。
4. 检查中文化、frontmatter、相对链接、目录白名单和评估用例。
5. 运行 Skill Creator 验证、JSON 解析、Markdown 链接和仓库级检查。
6. 在根 CHANGELOG 记录版本变化，使用 Git tag 发布仓库版本。
7. 先生成变更计划，再修改 Skill；不把项目专属事实写入通用 Skill。

## v1.0.0 基线

v1.0.0 包含项目文档、设计记录、代码同步、代码审查、文案、升级指南、测试可靠性、PR 描述、简化和 Skill 维护十个 Skill，以及现有 UI 设计系统。

## 输出

报告新增或修改的 Skill、职责边界、验证结果、评估场景、兼容性和未完成事项。默认不修改使用这些 Skill 的项目。
