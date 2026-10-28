---
name: skill-maintenance
description: 维护 owner-skills 仓库及其 Skill 库。用于新增、修改、拆分、翻译、结构验证、职责冲突审计和触发描述优化；行为评估与版本发布仅在任务需要时进行。
---

# Skill 仓库维护

保持每个 Skill 职责窄、入口清晰、references 可达、中文完整。通过结构检查发现确定性错误，通过实际使用反馈改进决策；不把测试目录或评估数量当作质量证明。

## 先读什么

读取根 README、CHANGELOG、LICENSE、受影响的 Skill、[结构和边界](references/structure-and-boundaries.md) 和 [验证](references/validation.md)。调整语言时读取 [术语与语言](references/terminology.md)；多文件改造可用 [变更计划模板](templates/skill-change-plan.md)。只有分析真实失败或明确评估效果时，才读取 [可选行为评估](references/eval-workflow.md)。

## 工作流

1. **确定意图和模式**：审计请求保持只读；明确要求修复时直接在授权范围修改；发布单独处理。先检查能力是否已由现有 Skill 覆盖。
2. **设计边界**：一个 Skill 一个主要职责。只添加确有用途的 references、templates、scripts、agents 或 assets；不为凑结构创建空目录或占位用例。
3. **编写入口**：description 区分触发场景和相邻职责；正文保留关键判断、安全边界、工作流和输出。支持目标项目既有规则，不把某个项目的约定提升为通用要求。
4. **渐进加载**：运行所需参考资料和模板从入口或索引可达，并说明何时读取。开发期评估材料不进入普通任务的必读路径；其他 Skill 不可用时提供最小本地回退。
5. **运行结构检查**：使用仓库验证命令检查 frontmatter、名称、链接、实际 JSON/YAML、模板和独立安装依赖；新增或修改脚本需实际运行并检查失败退出码。
6. **判断实际效果**：人工检查职责、触发、指令冲突和真实任务反馈。必要时复现具体失败并保存最小回归案例；不强制测试数量、逐字断言、benchmark 或 viewer。
7. **记录变更**：更新根 CHANGELOG，必要时同步 README 和分发授权。普通编辑只写未发布记录；只有用户明确要求发布时才确定版本、创建新 tag 或执行发布动作，不覆盖已有 tag。

## 按需资源

```text
SKILL.md
references/   templates/   scripts/   agents/   assets/
NOTICE        evals/（仅在真实回归或专项评估需要时）
```

除了入口，资源按用途选择，不执行固定目录配额。本仓库各 Skill 独立分发时保留 NOTICE 或必要的 LICENSE；参考目录允许导航 README，但不复制一套独立版本和发布历史。根 README、CHANGELOG 和 LICENSE 仍负责仓库元数据。

## 输出

报告职责和触发变化、受影响文件、实际验证及其局限、使用反馈和未完成事项。没有做行为评估就明确说明；不默认修改使用这些 Skill 的项目，也不把编辑请求当成发布授权。
