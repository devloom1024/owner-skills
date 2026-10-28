---
name: project-simplification
description: 发现项目中的重复事实、重复状态、过度抽象、无消费者接口、过期设计记录、重复生成路径和不必要复杂度。用于提出有证据的简化候选或评估另一分支的简化方案，不自动删除代码或文档。
---

# 项目简化

简化不是删除数量竞赛。候选必须证明维护义务减少，并说明能力、兼容性、失败语义和所有权变化。

## 先读什么

读取根/祖先 AGENTS、架构、相关 subsystem/package owner、active Agent Notes、规范、测试策略和 [证据清单](references/evidence-checklist.md)。使用 [候选报告](references/candidate-report.md) 和 [简化提案模板](templates/simplification-proposal.md) 输出。归档记录只作历史参考；新候选需要检查 supersession。

## 检查顺序

1. 固定 scope 和保护约束，识别用户明确保留的架构/兼容要求；
2. 搜索重复事实、状态、配置、适配层、接口、生成路径和文档 owner；
3. 追踪完整 producer → transformation → consumer → observable effect，不把声明、测试或零引用误当作无消费者证据；
4. 检查配置 precedence、manifest/loader、动态加载、已安装包、脚本和生成产物；
5. 检查 borrowed/owned 值、权限、持久化、取消、回调、资源清理和失败状态；
6. 评估依赖替换是否真正删除实现和专用测试，是否只是把复杂度移动到 glue；
7. 判断是删除概念、收窄公开行为、合并 owner、压缩表达还是证据不足；
8. 检查新候选是否替代已有设计记录，并按项目规则记录提案、替代和验证；
9. 输出带优先级、证据、能力损失、风险、迁移和验证的候选报告。

## 拒绝条件

如果候选破坏保留义务、只移动复杂度、依赖消费者证据不足、改变持久化/协议却没有迁移，或没有有意义的维护成本下降，则标记为拒绝或 review-required。

## 边界

默认只读。不直接删除代码、文档、测试、生成物或目录；实施需要明确授权和变更影响审查。
