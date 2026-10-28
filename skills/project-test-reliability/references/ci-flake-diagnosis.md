# CI 不稳定诊断

## 诊断记录

- 失败概率、首次和最近日志：
- worker/job/process 拓扑：
- 共享资源和 owner：
- 原子分配和 readiness：
- 同步信号和 timeout budget：
- cleanup、退出和 quiescence：
- 平台差异：
- 最小复现和负例：
- 根因、修复方向和验证：

诊断-only 请求保持只读。优先修复资源所有权和同步缺陷，不用 sleep、重试或全局串行化掩盖问题。
