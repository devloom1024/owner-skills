# 范围预检

## PR 或 commit

1. 验证 base 和 exact head 都是预期 ref；
2. 项目有范围命令时优先运行，例如：

```bash
<project-change-scope-command> --base <verified-base> --head <verified-head>
```

3. 保存命令、输出、changed paths、dirty layers 和失败信息；
4. retarget、merge、force-push 或 base/head 变化后重新运行。

## Worktree

没有 PR ref 时分别列出：

- staged；
- unstaged；
- untracked；
- renamed；
- deleted；
- 忽略或排除的路径。

## 全量路径

不只读取 Markdown；源码、测试、配置、manifest、契约源、生成器、生成物、脚本、快照、双语文件和升级记录都进入范围判断。

显式包含 `.agents/notes/` 隐藏路径，移动时保留源/目标；归档的新增、移动、修改和删除仍在本次审查范围内，不与“不得作为当前事实证据”混淆。排除无关依赖、缓存和第三方代码时记录理由。

## 失败处理

范围命令失败、ref 不存在或工作树范围不明确时，继续只读收集可用证据，但结果不得为 `covered` 或 `not-needed`；报告 `review-required` 和未验证原因。
