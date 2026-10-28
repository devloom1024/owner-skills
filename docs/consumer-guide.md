# 使用者项目快速开始

`owner-skills` 是一个 Skill 分发仓库。使用者应把需要的 Skill 安装到自己的项目中，再从自己的项目目录启动 Agent；不需要把本仓库作为目标项目运行。

## 安装方式

### Codex Plugin

优先使用 Codex 的 Plugin 安装入口安装 `owner-skills`。Plugin 会分发仓库中的 Skill，并按仓库版本更新。

### 本地 checkout

维护者或需要可编辑副本时，可以从本地 checkout 安装：

```bash
python3 /path/to/owner-skills/scripts/install_skills.py \
  --target /path/to/your-project \
  --profile core
```

可用 profile：

- `core`：路由、文档、代码审查和变更同步；
- `quality`：测试可靠性、文案、简化和升级指南；
- `ui`：UI 设计系统；
- `full`：全部 Skill。

只安装指定 Skill：

```bash
python3 /path/to/owner-skills/scripts/install_skills.py \
  --target /path/to/your-project \
  --skill project-code-review \
  --skill project-change-sync
```

默认复制文件，团队项目建议使用复制以便锁定版本。维护本仓库时可以使用 `--mode link` 跟随本地源文件。

安装目标是使用者项目的 `.agents/skills/`，不会修改 `owner-skills` 源目录。

## 第一次使用

从使用者项目根目录启动 Agent，然后运行：

```text
$project-skill-router 我想审查当前分支相对 main 的变更
```

已知 Skill 时可以直接调用：

```text
$project-code-review 审查当前分支相对 main 的变更
```

如果新安装的 Skill 没有出现，重启宿主后运行诊断：

```bash
python3 /path/to/owner-skills/scripts/skill_doctor.py \
  --target /path/to/your-project
```

## 使用边界

- 每个任务先选一个主 Skill，只有存在直接影响时才补充辅助 Skill；
- `audit` 只读报告，`edit` 才修改文件，`publish` 才准备对外材料；
- 目标项目的 `AGENTS.md`、设计系统、冻结约束和发布规则优先于通用 Skill；
- 安装 Skill 不会自动迁移目标项目的文档、Notes 或决策记录；
- 需要更新时重新安装目标版本，不要覆盖使用者项目中的本地适配。

## 安装记录

本地安装器会在目标项目写入 `.agents/owner-skills.json`，记录版本、profile、安装模式和已安装 Skill。该文件可以帮助团队审查安装状态；是否提交由目标项目自己的规则决定。
