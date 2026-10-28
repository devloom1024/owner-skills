---
name: project-change-sync
description: 检查代码、配置、契约、生成器和设计变更是否同步到正确的当前事实、包 README、Agent Notes、规范、postmortem、指南、契约和升级记录。用于 PR、commit、worktree 和 retarget 后审计；默认只读，不自动改文档。
---

# 代码变更同步

把完整变更范围映射到 canonical owners，判断每条路径的文档同步状态。本 Skill 只分析和报告；后续明确要求修改时可由 `project-docs` 或项目自身编辑流程执行，设计状态按项目 ADR/决策规则处理，不依赖安装其他 Skill。

## 读取参考资料

按任务读取：

1. [范围预检](references/scope-preflight.md)；
2. [来源与所有权](references/ownership-mapping.md)；
3. [更新矩阵](references/update-matrix.md)，涉及规范或可复用缺陷时读取其中的专项检查。

涉及 Notes 位置、生命周期、替代关系或归档变更时，再读 [决策记录变更检查](references/note-transitions.md)。

## 工作流

1. **固定范围**：按范围预检验证 base/head 或 worktree 范围，收集完整 changed paths；比较基线变化时重新预检。
2. **读取路由**：读取任务/PR、根及变更路径的有效指令、当前事实所有者和相关验证入口。
3. **解析所有权**：记录配置映射 `configured`、项目显式声明 `declared` 或证据推断 `inferred`，附证据和置信度。配置与 AGENTS/当前 owner 冲突时报告冲突，不因存在 YAML 就视为权威。
4. **判断语义影响**：结合 diff、公开 API、消费者、配置 precedence、状态/失败/兼容性、生成关系、测试和任务描述。代码 diff 不是语义变化的唯一证据。
5. **检查设计收敛**：核实当前决策 owner，区分目标、采纳与交付，检查设计偏差及当前文档；历史、拒绝和未实现记录不作当前实现证据。
6. **检查适用门禁**：只检查项目已有且与本次影响相关的 freshness、类型、链接、双语、快照、契约或升级验证。使用只读检查或已有结果；会改写文件的生成命令不自动执行。区分 pass/fail/not-run，不适用项说明理由。
7. **生成报告**：按 [报告模板](templates/change-impact-report.md) 汇总路径结论、证据和缺口。涉及规范或可复用缺陷时，分开核实项目采纳依据与验证方式；必要时提出经验或规范候选及待满足条件，不创建记录或自动提升规范。

## 状态

- `covered`：确需同步的 owner/派生物已完成更新，适用检查已验证。
- `not-needed`：证据证明无需同步，例如公开契约、消费者行为和派生来源均未改变；列出支持判断的检查，而非把未更新等同于不需要。
- `missing`：已确认需要某项同步，但对应更新缺失；给出要求和缺口的直接证据。
- `review-required`：所有权、影响或验证存在实质不确定性，尚不能支持上述结论；说明待补证据。检查失败但已确认缺少更新时仍可标 `missing`，同时报告失败。

解析方式和同步状态是两条独立维度。缺少配置或使用推断并不自动降为 `review-required`；没有实质疑问且证据充分时可得出确定结论，不把推断升级成项目新规则。

## 项目差异

`docs-governance.yml` 是可选映射，不是运行前提。字段与解析方式见 [来源与所有权](references/ownership-mapping.md)，需要配置示例时参考 [项目映射模板](templates/docs-governance.yml)；仅采用项目真实存在的 owner 和 checks，不把模板占位路径或门禁当成正式规则。

## 安全边界

只读；不移动、删除、重写项目文件。不把设计记录当实现证据，不把 observed 规则提升为 adopted，不把命令未运行写成通过。
