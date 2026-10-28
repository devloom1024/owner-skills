# 审查流程

## 1. 固定范围

验证 live base/exact head；项目有 `change-scope` 时先运行并保存输出。记录 changed paths、dirty layers、rename/delete/untracked、排除项和失败。retarget、merge 或 ref 改变后重跑。

## 2. 事实路由

先按路径读取根/祖先 AGENTS、架构地图、subsystem/package owner、设计记录、规范和测试入口，再读完整 diff。不要用局部 diff 或提交说明替代上下文。

## 3. 证据链

每个判断连接到：需求/设计、源码行、调用方/消费者、测试或 gate、实际命令结果。命令未运行、环境缺失、所有权推断和不确定语义都要显式报告。

## 4. 结论

先列有证据的问题和影响，再列开放问题、假设、未验证项和建议；无发现时明确说明。阻塞问题给出精确位置和可复现路径，未实际运行则注明。绿色 gate 只证明它覆盖的约束，不证明设计和语义正确。
