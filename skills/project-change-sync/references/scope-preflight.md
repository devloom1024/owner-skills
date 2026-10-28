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

不要把“当前有 Markdown 改动”当作完整范围。源码、配置、测试、生成器、快照和契约都必须进入范围判断。

## 失败处理

范围命令失败、ref 不存在或工作树范围不明确时，继续只读收集可用证据，但结果不得为 `covered` 或 `not-needed`；报告 `review-required` 和未验证原因。
