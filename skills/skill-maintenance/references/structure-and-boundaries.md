# 结构和边界

每个 Skill 只有一个主要职责：

- `SKILL.md`：触发、选择、工作流、安全边界、输出和验证；
- `references/`：需要按任务加载的规则和背景；
- `templates/`：输出骨架和必填字段；
- `scripts/`：确定性、重复、可测试的执行任务；
- `evals/`：正常、边界、失败/不确定场景和可验证 expectations；
- `agents/`：工具或客户端元数据；
- `assets/`：输出所需静态资产。

根 README、CHANGELOG 和 LICENSE 由仓库根目录统一维护。Skill 不复制项目事实、产品契约或其他 Skill 的完整规则。
