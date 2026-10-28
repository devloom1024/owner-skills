---
name: skill-maintenance
description: 维护 owner-skills 仓库及其 Skill 库。用于新增、拆分、翻译、评估、验证、职责冲突审计、版本发布和描述触发优化；统一管理根 README、CHANGELOG、LICENSE 和 v1.0.0 之后的版本变化。
---

# Skill 仓库维护

保持每个 Skill 职责窄、入口清晰、references 可达、评估可验证、中文完整，并让根仓库统一管理目录、版本、变更和授权。

## 先读什么

读取根 README、CHANGELOG、LICENSE、现有 Skill、[结构和边界](references/structure-and-boundaries.md)、[验证](references/validation.md)、[评估流程](references/eval-workflow.md)、[变更计划模板](templates/skill-change-plan.md) 和 [评估场景](evals/evals.json)。

## 工作流

1. **确定意图**：说明新 Skill 能做什么、何时触发、输出什么、依赖什么；先检查是否属于现有 Skill。
2. **设计边界**：一个 Skill 一个主要职责；入口负责选择和路由，细节放 references，重复结构放 templates，机器场景放 evals，执行确定性重复任务才放 scripts；可选 `agents/` 和 `assets/` 必须列出用途。
3. **编写入口**：frontmatter description 要写触发场景；正文包含安全边界、工作流、参考路由、输出格式和验证。
4. **设计渐进加载**：每个 reference/template/eval 从入口可达，并说明何时读取；入口保持可加载但不能只剩摘要。
5. **建立评估**：每个 Skill 至少有正常、边界和失败/不确定场景；提供 `files` fixture、`expected_output` 和 `expectations`，必要时做 with-skill/without-skill 对照。
6. **运行验证**：quick_validate、JSON schema/解析、Python/脚本语法、Markdown 相对链接、frontmatter、中文检查、目录白名单和职责冲突检查。
7. **人工评估**：运行评估，保存 outputs、timing、grading、benchmark；需要时用 Skill Creator viewer 展示结果，根据反馈迭代。
8. **发布**：根 CHANGELOG 记录变化，确认根 LICENSE 范围，更新 README，使用 Git tag；不覆盖已有 tag。

## 允许的 Skill 目录

```text
SKILL.md
references/   templates/   scripts/   evals/   agents/   assets/
```

除 `SKILL.md` 外均为可选。Skill 内不创建 README、CHANGELOG 或 LICENSE；仓库元数据由根目录统一维护。

## v1.1.0 基线

v1.1.0 补齐 v1.0.0 的入口路由、文档所有权、设计生命周期、变更范围预检、真实审查维度、专项验证、评估场景和中文化要求；保留十个项目 Skill 与 UI 设计系统。

## 输出

报告 Skill 边界、文件变化、references 路由、评估场景和断言、验证命令、版本、兼容性、未完成事项以及是否需要人工评审。不默认修改使用这些 Skill 的项目。
