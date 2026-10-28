---
name: project-skill-router
description: 根据任务选择 owner-skills 的主 Skill、辅助 Skill 和 audit/edit/publish 模式。用于不知道从哪个 Skill 开始、需要组合多个 Skill 或判断边界时；不执行具体代码或文档修改。
---

# 项目 Skill 路由

这是使用者项目中的入口 Skill。它只负责分类、选择和说明下一步，不替代被选中的 Skill，也不直接修改代码或文档。

## 工作流

1. 读取目标项目根及相关路径的 `AGENTS.md`，识别项目已有的约束、文档 owner、测试入口和发布规则。
2. 将请求归类为 `feature`、`bug`、`review`、`docs`、`ui`、`release`、`simplification` 或 `unknown`。
3. 判断执行模式：
   - `audit`：只读检查和报告；
   - `edit`：在用户请求范围内修改文件；
   - `publish`：准备 PR、升级指南或其他对外发布材料。
4. 选择一个主 Skill。只有存在直接影响时才添加辅助 Skill，不把整套 Skill 串行运行。
5. 检查被推荐的 Skill 是否已安装。缺失时报告 Skill 名称和安装建议，不假装已经调用。
6. 输出路由结果，等待用户确认或直接进入用户明确要求的下一步。

## 路由基线

完整任务类型、主 Skill、辅助 Skill 和不适用条件见 [路由目录](references/catalog.md)。目录只是默认路由；目标项目自己的规则和当前请求优先。

## 输出格式

```text
任务类型：<feature|bug|review|docs|ui|release|simplification|unknown>
模式：<audit|edit|publish>
主 Skill：<skill-name>
辅助 Skill：<skill-name 或 None>
未安装依赖：<skill-name 或 None>
理由：<基于请求和项目证据的一句话>
下一步：<明确的 Skill 调用或需要用户决定的事项>
```

## 边界

- 不因为“可能有帮助”就推荐全部 Skill。
- 不把辅助 Skill 当成主 Skill 的隐式依赖；每个调用都要有任务证据。
- 不将 `audit` 请求改写成 `edit`，不将 `edit` 请求误报为已发布。
- 不替用户决定未确认的架构取舍、发布版本或外部操作。
- 如果任务不适合本库，明确说明并给出最小的本地回退，而不是强行套用路由。
