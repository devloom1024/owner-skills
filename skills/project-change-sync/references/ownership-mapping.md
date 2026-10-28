# 来源与所有权

## 通用解析顺序

1. 项目根和变更路径祖先的 `AGENTS.md`；
2. 架构地图：系统组合、循环、扩展点和高层运行路径；
3. subsystem：类型、语义、实现边界和生成 API；
4. 包 README：配置、公开接口、限制、扩展点和消费者体验；
5. Agent Note：持久化设计理由和替代方案；
6. postmortem/incident：事故因果链和预防；
7. standards/defensive patterns：审查规则及其门禁；
8. contract source/generator：机器可读契约及派生物；
9. guides/upgrade guides：面向用户或维护者的操作和迁移。

项目可以用不同目录名表达同一职责，必须以内容和 AGENTS 路由判断，不能只按文件名判断。

## 配置映射

支持以下 owner 字段：`architecture`、`subsystem`、`package_readme`、`agent_note`、`postmortem`、`standard`、`generated`、`i18n`、`contract`、`guide`、`upgrade_guide` 和 `gates`。

每个映射记录 `configured` 或 `inferred`、证据路径、置信度和验证命令。推断映射只能产生 `review-required`，不能自动成为正式规则。

## 项目适配

若项目有 `docs/AGENTS.md`、文档索引、生成器 manifest、双语协议或专用 gates，先采用项目规则；通用矩阵只补足未定义的部分。
