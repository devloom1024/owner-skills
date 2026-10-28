# owner-skills

由 `devloom1024` 维护的中文 Agent Skills 仓库。

最近已发布版本：`1.2.0`；完整变化见 [变更日志](CHANGELOG.md)。

## Skill 目录

### 工作流入口

- [`project-workflow`](skills/project-workflow/SKILL.md)：创建和执行固定的 Feature 与 Bug 研发工作流，选择 Matt 或 Superpowers 作为流程提供者。

### 设计与文档

- [`project-docs`](skills/project-docs/SKILL.md)：初始化、整理、审计和验证项目文档，维护开发规范的来源、采纳与验证依据。
- [`project-design-notes`](skills/project-design-notes/SKILL.md)：在 `.agents/notes/` 统一管理 MVP 提案、架构决策（ADR）、替代关系和归档。
- [`project-change-sync`](skills/project-change-sync/SKILL.md)：检查代码变化是否同步到正确的文档所有者和验证门禁。
- [`project-prose-standard`](skills/project-prose-standard/SKILL.md)：审查文档、注释、JSDoc、提示词和诊断文案。

### 开发与审查

- [`project-code-review`](skills/project-code-review/SKILL.md)：根据目标、设计、代码、文档、测试和门禁审查变更。
- [`project-test-reliability`](skills/project-test-reliability/SKILL.md)：诊断测试隔离、并发、异步清理、平台差异和 CI 不稳定。
- [`project-pr-description`](skills/project-pr-description/SKILL.md)：根据变更证据生成和维护 PR 描述。
- [`project-upgrade-guide`](skills/project-upgrade-guide/SKILL.md)：为外部可见破坏性变化生成升级指南。
- [`project-simplification`](skills/project-simplification/SKILL.md)：发现重复、过度设计和可删除的维护义务。

### 现有设计系统

- [`ui-design-system`](skills/ui-design-system/SKILL.md)：跨桌面、移动、触控、键盘和响应式布局的 UI 设计规范。

## 使用者项目快速开始

本仓库是 Skill 的源代码和分发入口。使用者应把需要的 Skill 安装到自己的项目中，再从那个项目启动 Agent；本仓库本身不作为使用者项目的运行目录。

### Codex Plugin

优先使用 Codex 的 Plugin 安装入口安装 `owner-skills`。安装后从使用者项目根目录启动 Codex，宿主会发现插件中的 Skill。

### 本地 checkout

维护者或需要可编辑副本时，可以使用本仓库提供的安装器：

```bash
python3 /path/to/owner-skills/scripts/install_skills.py \
  --target /path/to/your-project \
  --profile core
```

可用 profile：

- `core`：工作流、文档、代码审查和变更同步；
- `quality`：测试可靠性、文案、简化和升级指南；
- `ui`：UI 设计系统；
- `full`：全部 Skill。

也可以只安装指定 Skill：

```bash
python3 /path/to/owner-skills/scripts/install_skills.py \
  --target /path/to/your-project \
  --skill project-code-review \
  --skill project-change-sync
```

默认复制文件以便锁定版本。维护本仓库时可以使用 `--mode link` 跟随本地源文件。安装目标是使用者项目的 `.agents/skills/`，不会修改本仓库的源目录。

更完整的安装、更新和排障说明见 [使用者项目快速开始](docs/consumer-guide.md)。

## 工作流与 Skill

工作流表达端到端的研发过程，Skill 表达其中的阶段能力。当前正式工作流包括 Feature 开发、Bug 修复、项目简化审计和发布材料准备；简单的局部任务可以直接调用专项 Skill。

### Feature 开发

```text
requirements-clarification
  -> project-design-notes（可选）
  -> implementation + test
  -> verification
  -> project-code-review
```

### Bug 修复

```text
bug-diagnosis
  -> project-design-notes（可选）
  -> regression test + fix
  -> verification
  -> project-code-review
```

### 项目简化

```text
project-simplification
```

这是独立的只读维护工作流，不自动删除代码或文档。

### 发布材料

```text
project-upgrade-guide（存在外部兼容性变化时）
  -> project-pr-description
```

工作流提供者在创建项目工作流时二选一：Matt 或 Superpowers。`to-spec`、`to-tickets`、`writing-plans` 和 `implement-spec` 暂不属于核心流程。

工作流阶段按变更影响条件激活辅助 Skill：

| 任务 | 主 Skill | 按需补充 |
|---|---|---|
| 新特性开发 | `project-workflow` | 按 provider 激活需求澄清、TDD、验证和 `project-code-review` |
| Bug 修复 | `project-workflow` | 按 provider 激活诊断、回归测试、验证和 `project-code-review` |
| 初始化文档、更新单页、整理目录 | `project-docs` | 有新增长期取舍时用 `project-design-notes`；文案编辑用 `project-prose-standard` |
| 从实践或缺陷经验提炼、维护开发规范 | `project-docs` | 仅审计变更中的规范同步时用 `project-change-sync`；区分候选、项目采纳与验证证据 |
| 检查代码变化是否遗漏文档同步 | `project-change-sync` | 确认需要编辑后用 `project-docs` |
| 设计方案或维护 ADR | `project-design-notes` | 当前事实文档需要同步时用 `project-docs` |
| 明确请求将决策记录迁移到本库规范 | `project-docs` | 决策语义与替代关系用 `project-design-notes`；迁移差异审计用 `project-change-sync` |
| 审查 PR/commit/worktree | `project-code-review` | 有同步、测试可靠性或兼容性风险时才补相关 Skill |
| 诊断或修复 flaky test | `project-test-reliability` | 有外部契约变化时再检查同步和升级影响 |
| 生成 PR 描述或迁移指南 | `project-pr-description` / `project-upgrade-guide` | 只读取相关的设计、diff 和验证证据 |
| UI 实现或审查 | `ui-design-system` | 沿用项目现有设计系统；按技术栈读取 adapter |
| 简化项目 | `project-simplification` | 先区分审计和编辑授权 |

## 使用

首次创建工作流时，在使用者项目中显式调用：

```text
$project-workflow create
```

工作流创建完成后运行 Feature 或 Bug：

```text
$project-workflow run feature
$project-workflow run bug
$project-workflow run simplification
$project-workflow run publish
```

如果项目没有 `.agents/workflow.yaml`，`project-workflow` 会停止并提示先创建。创建后的工作流定义不会自动修改；缺少依赖 Skill 时只报告安装建议，不自动更换流程提供者。

使用者项目中的完整路线见 [使用者项目工作流](docs/workflows.md)。

检查安装是否生效：

```bash
python3 /path/to/owner-skills/scripts/skill_doctor.py \
  --target /path/to/your-project
```

如果宿主没有显示新安装的 Skill，重启宿主后再检查。更新 Skill 时重新安装目标版本，不要覆盖使用者项目自己的 `AGENTS.md`、文档、Notes 或本地适配。

## 使用规则

每个 Skill 只携带真正支持任务的流程、参考资料、模板、脚本和资产。仓库级说明、版本变化和授权由本文件、根 CHANGELOG 和 LICENSE 统一维护；参考目录的导航 README 与独立分发需要的 NOTICE/LICENSE 是合理例外。

目标项目已有的 AGENTS、决策语义、冻结约束、发布流程和设计系统优先于通用模板，不以示例替代项目有效规则。审计保持只读，明确编辑请求在授权范围内执行；创建 tag、发布或其他项目的修改不由修改 Skill 自动授权。

Skill 的说明、流程、理由和报告使用中文；稳定的 English controlled vocabulary 保留原样。Skill 名称、目录名、路径、命令、代码、API、协议字段、Pattern、Token、状态值和门禁名称不翻译。

### 决策记录约定

项目根下 `.agents/notes/` 是唯一活跃决策记录根，架构类 Agent Notes 承担 ADR 职责。这是本库约定，不是所有工具的强制目录标准。当前事实由 `docs/` 和包 README 拥有，长期理由由 Notes 拥有，以链接关联，不双写正文。

职责与状态见 [文档模型](skills/project-docs/references/document-model.md)，日常组织见 [目录组织](skills/project-design-notes/references/organization.md)，只读审计见 [决策记录变更检查](skills/project-change-sync/references/note-transitions.md)。仅在用户明确请求迁移时加载 [决策记录迁移](skills/project-docs/references/notes-migration.md)；这是一次性任务，不随安装、初始化或日常维护启动。

## 验证与使用反馈

### 结构校验

维护者使用 Python 3.10+，在仓库根目录运行。依赖仅用于维护，不是 Skill 运行依赖；虚拟环境放在仓库外，避免产生需要提交或忽略的文件。

```bash
python3 -m venv /absolute/path/outside-repo/owner-skills-venv
source /absolute/path/outside-repo/owner-skills-venv/bin/activate
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_skills.py
python3 scripts/validate_workflow.py skills/project-workflow/templates/workflow.yaml
python3 scripts/test_consumer_install.py
git diff --check
```

单独检查一个 Skill 目录：

```bash
python3 scripts/validate_skills.py --skill /absolute/path/to/skill-directory
```

[校验脚本](scripts/validate_skills.py) 使用 PyYAML 与 Markdown 解析器检查：

- frontmatter、Skill 名称和非空描述；
- Markdown 中的本地文件链接，包括图片和引用式链接；忽略代码块、外部 URL 和锚点内容，不扫描行内代码里的示例路径；
- Skill 内实际 JSON/YAML 语法与 Python 脚本语法，不执行文档示例或生成命令；
- 默认 PR 模板四章节、升级指南文件头、分发所需 NOTICE 或 LICENSE；
- Plugin manifest、profiles 和 Skill metadata 的结构与引用一致性；
- Skill 内本地链接和软链接是否越过其独立分发边界。

任何文件失败都会汇总并返回非零退出码，不会被最后一个成功项覆盖。它不检查外部链接可达性、模型效果、所有普通文本依赖或 UI 可访问性；references 路由与语义仍需人工审阅。需要时可补充运行 Skill Creator 的 `quick_validate.py`，不依赖其本机安装路径。

项目工作流定义的语义校验使用单独的 [工作流校验脚本](scripts/validate_workflow.py)：

```bash
python3 scripts/validate_workflow.py /absolute/path/to/.agents/workflow.yaml
```

### 行为是否有效

结构有效不等于 Skill 有效；效果通过真实任务和反馈判断。本仓库不要求每个 Skill 建立 `evals/`，也不强制三类场景、固定断言或 benchmark。

未来遇到值得防止复发的真实失败，再保留最小输入和可观察预期；人工 fixture 与真实运行日志需区分，临时输出默认留在仓库外。不因为移除模板化 evals 而删除目标项目真正有价值的代码测试。

完整变更记录见 [CHANGELOG.md](CHANGELOG.md)，授权信息见 [LICENSE](LICENSE)。
