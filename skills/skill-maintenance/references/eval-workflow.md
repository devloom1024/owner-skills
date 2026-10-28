# 评估流程

每个 Skill 至少准备三类场景：

1. 正常场景：验证主要工作流和预期输出；
2. 边界场景：缺少映射、混合职责、无变化或复杂跨平台条件；
3. 失败/不确定场景：命令失败、证据不足、冲突或未验证环境。

每条 eval 使用 `id`、`prompt`、`expected_output`、`files` 和 `expectations`。`expectations` 是可验证陈述，不用未定义的 `name` 字段替代。

改进既有 Skill 时保存旧版本作为 baseline；运行 with-skill 与 baseline；记录 outputs、timing、grading、benchmark 和反馈。必要时使用 Skill Creator 的 review viewer；先看定性结果，再依据 assertion pass rate、token、时间和失败模式修改入口或 references。
