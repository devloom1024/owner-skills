# 验证

## 确定性结构检查

在 owner-skills 仓库根目录运行 `python3 scripts/validate_skills.py`，依赖安装与检查范围以根 README 为准。检查：

- `SKILL.md` frontmatter 存在，`name` 与目录一致，`description` 非空；
- Markdown 本地文件链接存在，Skill 内链接不依赖仓库根或兄弟 Skill；
- 实际 JSON/YAML 文件可解析，文档 frontmatter 位于文件开头；
- PR 默认模板章节、升级指南 frontmatter 等已声明的模板约束一致；
- 一个 Skill 失败时整次命令返回非零退出码，而不是被后续成功覆盖。

只安装单个 Skill 的目标项目不必安装这个维护脚本。维护者可选用 Skill Creator 的 `quick_validate.py` 做补充检查；新增脚本需验证实际成功和失败路径，不能只通过语法检查。

不强制 evals 数量、目录白名单、固定措辞或输出字数；不运行目标项目中可能改写文件的生成器。示例命令与代码块不是可执行授权。

## 人工检查与实际使用

- 触发描述和职责是否清晰，是否与相邻 Skill 抢占任务；
- 必要 references/templates 是否可路由，是否保留项目已有约定；
- 审计是否保持只读，明确要求修复时是否能完成编辑；
- 可选资源是否有真实用途，独立安装是否保留许可和署名；
- README、CHANGELOG、实际差异和未发布状态是否准确；
- 真实任务是否得到正确结果，而不只是输出了预期标题。

验证失败时报告精确路径和修复建议。结构检查不证明 Skill 的判断有效，行为评估也不必成为每次修改的门禁。
