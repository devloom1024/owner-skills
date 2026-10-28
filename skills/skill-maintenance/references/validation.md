# 验证

## 单 Skill

- frontmatter `name` 与目录和 eval `skill_name` 一致；
- `quick_validate.py` 通过；
- SKILL.md 中的相对链接全部存在；
- references、templates、evals 从入口可路由；
- JSON 解析和 expectations 字段有效；
- Python/脚本语法有效；
- 中文人类可读内容完整，机器字段/路径/状态值可保留英文。

## 仓库

- 根 README、CHANGELOG、LICENSE 存在且版本一致；
- 每个 Skill 仅使用允许目录；
- 无 Skill 内 README/CHANGELOG/LICENSE；
- 所有 Skill 的职责和触发描述不重复；
- Git diff、tag 和工作区状态清晰；
- eval fixture、grading、benchmark 和 viewer 结果按项目要求保存或明确未运行。

验证失败时报告精确路径和修复建议，不用绿色结构检查替代语义审查。
