# owner-skills

由 `devloom1024` 维护的中文 Codex Skill 仓库。

最近已发布版本：`1.2.0`；完整变化见 [变更日志](CHANGELOG.md)。

## Skill 目录

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

### Skill 仓库维护

- [`skill-maintenance`](skills/skill-maintenance/SKILL.md)：维护 Skill 内容、职责、结构验证和可选的使用反馈回归。

### 现有设计系统

- [`ui-design-system`](skills/ui-design-system/SKILL.md)：跨桌面、移动、触控、键盘和响应式布局的 UI 设计规范。

## 按任务选择

不要求每项开发工作依次运行整套 Skill。先选择主要职责，只有实际需要时才补充：

| 任务 | 主 Skill | 按需补充 |
|---|---|---|
| 初始化文档、更新单页、整理目录 | `project-docs` | 有新增长期取舍时用 `project-design-notes`；文案编辑用 `project-prose-standard` |
| 从实践或缺陷经验提炼、维护开发规范 | `project-docs` | 仅审计变更中的规范同步时用 `project-change-sync`；区分候选、项目采纳与验证证据 |
| 检查代码变化是否遗漏文档同步 | `project-change-sync` | 确认需要编辑后用 `project-docs` |
| 设计方案或维护 ADR | `project-design-notes` | 当前事实文档需要同步时用 `project-docs` |
| 明确请求将决策记录迁移到本库规范 | `project-docs` | 决策语义与替代关系用 `project-design-notes`；迁移差异审计用 `project-change-sync` |
| 审查 PR/commit/worktree | `project-code-review` | 有同步、测试可靠性或兼容性风险时才补相关 Skill |
| 诊断或修复 flaky test | `project-test-reliability` | 有外部契约变化时再检查同步和升级影响 |
| 生成 PR 描述或迁移指南 | `project-pr-description` / `project-upgrade-guide` | 只读取相关的设计、diff 和验证证据 |
| UI 实现或审查 | `ui-design-system` | 沿用项目现有设计系统；按技术栈读取 adapter |
| 简化项目或维护 Skill | `project-simplification` / `skill-maintenance` | 先区分审计、编辑和发布授权 |

可单独安装任何 Skill。辅助 Skill 不可用时，依据项目规则和当前入口完成必要检查，说明证据缺口，不要求为一次任务安装全套。

## 安装与发现

本仓库的 `skills/` 是源文件目录，不是仅 clone 后就会被 Codex 自动发现的位置。按 [Codex 官方 Skills 文档](https://developers.openai.com/codex/skills/)，项目级放在 `<project>/.agents/skills/`，用户级放在 `~/.agents/skills/`；也支持软链接的 Skill 文件夹。以下命令只提供安装示例，不会由本仓库自动执行。

### 项目级：复制一个 Skill

替换两个仓库路径并选定 Skill，在终端运行：

```bash
(
  set -eu
  OWNER_SKILLS=/absolute/path/to/owner-skills
  TARGET_PROJECT=/absolute/path/to/target-project
  SKILL=project-docs
  SOURCE="$OWNER_SKILLS/skills/$SKILL"
  DEST="$TARGET_PROJECT/.agents/skills/$SKILL"
  test -f "$SOURCE/SKILL.md"
  test -f "$SOURCE/NOTICE"
  test -d "$TARGET_PROJECT"
  if [ -e "$DEST" ] || [ -L "$DEST" ]; then
    printf 'Already exists: %s\n' "$DEST" >&2
    exit 1
  fi
  mkdir -p "$TARGET_PROJECT/.agents/skills"
  cp -R "$SOURCE" "$DEST"
)
```

保留整个 Skill 文件夹及其 NOTICE，不要只复制 `SKILL.md`。项目可将安装副本纳入版本控制，和项目规则一起审阅；有本地改动时不要直接覆盖。

### 用户级：链接本地源目录

适合维护者或跨项目个人使用；源仓库必须保持在原路径，后续源文件改动会立即影响所有使用该链接的项目。

```bash
(
  set -eu
  OWNER_SKILLS=/absolute/path/to/owner-skills
  SKILL=ui-design-system
  SOURCE="$OWNER_SKILLS/skills/$SKILL"
  DEST="$HOME/.agents/skills/$SKILL"
  test -f "$SOURCE/SKILL.md"
  if [ -e "$DEST" ] || [ -L "$DEST" ]; then
    printf 'Already exists: %s\n' "$DEST" >&2
    exit 1
  fi
  mkdir -p "$HOME/.agents/skills"
  ln -s "$SOURCE" "$DEST"
)
```

用户级也可以复制，项目级也可以软链接；团队可移植安装通常更适合复制。不要依赖同名 Skill 的覆盖顺序，先检查已有安装，避免同时维护多个同名副本。

### 选装、验证与更新

- 按任务选装：文档工作常用 `project-docs`，变更审查可加 `project-change-sync` 与 `project-code-review`；UI 只需 `ui-design-system`。分组只是推荐，不是依赖链。
- 安装后在目标项目的 Codex 中输入 `$` 选择 Skill；CLI/IDE 也可用 `/skills`。检查名称与实际来源，再用 `$project-docs` 等显式调用。没有出现时检查目录和软链接，必要时重启 Codex。
- 复制前确认源仓库的 tag/commit 和未提交变更；团队采用稳定版本时从已确认的 tag/commit 复制，并记录来源。软链接直接跟随工作区，不等于版本锁定。
- 更新时先比较本地适配与新版本，备份需要保留的内容后替换整个副本；仅覆盖同名文件会留下已删除的旧资源。不要自动覆盖用户修改，也不要移动已有 tag。
- 独立分发保留 NOTICE 中的署名、来源和许可链接；修改后标明本地变化。无需为每个 Skill 维护独立的 CHANGELOG。

## 使用规则

每个 Skill 只携带真正支持任务的流程、参考资料、模板、脚本和资产。仓库级说明、版本变化和授权由本文件、根 CHANGELOG 和 LICENSE 统一维护；参考目录的导航 README 与独立分发需要的 NOTICE/LICENSE 是合理例外。

目标项目已有的 AGENTS、决策语义、冻结约束、发布流程和设计系统优先于通用模板，不以示例替代项目有效规则。审计保持只读，明确编辑请求在授权范围内执行；创建 tag、发布或其他项目的修改不由修改 Skill 自动授权。

Skill 的说明、流程、理由和报告使用中文；稳定的 English controlled vocabulary 保留原样。Skill 名称、目录名、路径、命令、代码、API、协议字段、Pattern、Token、状态值和门禁名称不翻译。详细规则见 `skills/skill-maintenance/references/terminology.md`。

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
git diff --check
```

单独检查一个源目录或复制后的安装副本：

```bash
python3 scripts/validate_skills.py --skill /absolute/path/to/project/.agents/skills/ui-design-system
```

[校验脚本](scripts/validate_skills.py) 使用 PyYAML 与 Markdown 解析器检查：

- frontmatter、Skill 名称和非空描述；
- Markdown 中的本地文件链接，包括图片和引用式链接；忽略代码块、外部 URL 和锚点内容，不扫描行内代码里的示例路径；
- Skill 内实际 JSON/YAML 语法与 Python 脚本语法，不执行文档示例或生成命令；
- 默认 PR 模板四章节、升级指南文件头、分发所需 NOTICE 或 LICENSE；
- Skill 内本地链接和软链接是否越过其独立分发边界。

任何文件失败都会汇总并返回非零退出码，不会被最后一个成功项覆盖。它不检查外部链接可达性、模型效果、所有普通文本依赖或 UI 可访问性；references 路由与语义仍需人工审阅。需要时可补充运行 Skill Creator 的 `quick_validate.py`，不依赖其本机安装路径。

### 行为是否有效

结构有效不等于 Skill 有效；效果通过真实任务和反馈判断。本仓库不要求每个 Skill 建立 `evals/`，也不强制三类场景、固定断言或 benchmark。

未来遇到值得防止复发的真实失败，再保留最小输入和可观察预期；人工 fixture 与真实运行日志需区分，临时输出默认留在仓库外。详见 [可选行为评估](skills/skill-maintenance/references/eval-workflow.md)。不因为移除模板化 evals 而删除目标项目真正有价值的代码测试。

完整变更记录见 [CHANGELOG.md](CHANGELOG.md)，授权信息见 [LICENSE](LICENSE)。
