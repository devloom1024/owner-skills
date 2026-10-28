---
name: project-test-reliability
description: 设计、审查和诊断会受 CI 并发、共享资源、时钟、进程、网络监听器、异步清理或跨平台影响的测试。用于 flaky CI、测试隔离、资源生命周期和回归证明；默认只读诊断，不用 sleep、重试或盲目串行化掩盖问题。
---

# 项目测试可靠性

检查测试是否在真实 CI 拓扑中隔离、同步并证明行为。它不替代项目测试层级或 push 命令选择。

## 先读什么

读取项目 testing policy、运行器配置、CI workflow、fixture owner、快照规则和 [CI 不稳定诊断](references/ci-flake-diagnosis.md)。

## 工作流

1. 建模同一文件、不同 worker、不同 gate process、不同 job/runner 的并发层；
2. 为每个端口、临时目录、数据库、socket、进程、环境变量、cwd、fake timers、mock、global fetch 和输出位置确定 owner、原子分配、readiness、清理和 quiescence 信号；
3. 使用 `listen(0)`、`mkdtemp`、唯一 namespace、exclusive creation 和依赖注入，避免先检查再占用；
4. 捕获全局状态的 absent/present 原态，立即注册恢复，在最小范围用 `try/finally`，必要时保留 afterEach fallback；
5. 用 readiness event、barrier、promise、状态转换和明确条件同步，不用固定 sleep；
6. 让 timeout 与 lane budget 匹配，setup/teardown 一起预算；
7. 停止后等待 child/server/worker/任务真正退出；`abort/close/kill` 未等待完成不算清理；
8. 用 invalid negative control、真实入口、外部状态和修复前失败证明回归；stress 不能替代确定性回归；
9. 检查 Windows/POSIX、权限、路径、环境名、文件句柄和时间精度；
10. 报告拓扑、证据、最小复现、根因、修复方向、命令和未验证环境。

## 拒绝掩盖 flaky 的修复

增加 timeout、重试、全局串行化、吞错、弱断言、归一化不稳定行为或加 sleep 不能作为根因修复；只有项目明确允许的外部 provider 瞬态重试例外可以保留。

## 评估

正常、边界和失败/不确定场景见 [evals/evals.json](evals/evals.json)，输入 fixture 位于 `evals/files/`。
