# Skills 验证与使用说明

核查日期：2026-10-05。项目内共 13 个 Skills。

## 本次解决

- 已安装 `fde-readout`，来源 `likamrat/skills`，锁定提交 `3a43ec8baad311ed79429477e9b3730eb3af8595`。与现有 `fde-engagement` 使用同一提交版本，包含模板、参考文档、许可证与脚本。
- `fde-engagement`：项目内 TMPDIR 环境下，`node scripts/test-package.mjs` 退出码 0。输出：`Local package checks passed: 24 behavior evals and 12/10 declared trigger fixtures.` 数字是仓库内的案例与触发声明数量，不是已完成模型行为评测的数量。
- `fde-readout`：同样设置 TMPDIR 后，`node scripts/test-package.mjs --static-only` 退出码 0。输出：`FDE readout package checks passed: 6 evals and 72 files.` 包含 HTML 渲染/浏览器测试与结构检查；Windows 原生 PowerPoint 自动化不在本次验收范围。
- Node.js 当前为 v22.16.0；本机有 Google Chrome，可用于独立测试浏览器。

## 已定位的测试路径问题

首次使用系统 TMPDIR 运行 `fde-engagement` 测试失败：`--output must stay inside the current workspace`，随后 manifest.json 不存在。测试将输出放在 macOS 系统临时路径，脚本以工作目录为输出边界。将 TMPDIR 设为项目内目录后同一套测试通过；没有放宽安全检查或修改上游验证器。

后续复检入口：

```sh
/Volumes/EXTERNAL/FDE/scripts/verify-fde-skills.sh
```

入口创建独立的项目内临时目录，设置 TMPDIR，运行两个包的检查，退出时清理自己创建的目录。Windows PowerPoint 原生渲染由 `--static-only` 跳过，不能将这个结果写成 PowerPoint 实际可用。

## 连接器与使用路径

当前 FDE 项目未发现 MCP 配置文件。Skill 中的 `~~knowledge base`、`~~ITSM` 是能力占位符，不代表已经连接。

当前会话暴露了 Gmail 和 Google Drive 工具；工具暴露不证明账户认证成功，也不证明 FDE 会话有相同权限。本次没有选择客户资料源，没有访问邮箱/网盘或测试客户数据，也没有配置账户。

`proposal-builder` 明确支持不依赖连接器的使用路径；`runbook` 的知识库/ITSM 是可选能力。默认可使用本地文件、上传或粘贴材料完成整理；报价缺少费率依据时保留待确认项，不能编造价格。需要从邮箱/网盘取资料时先指定具体来源与范围，再做只读认证与访问测试。财务接口、知识库发布、付款与对外发送均须相应具体授权。

## PowerPoint 平台限制

`fde-readout` 的 HTML 规划、渲染和验证脚本已通过本地检查。自带的可编辑 PowerPoint 协调器依赖 Windows、PowerShell 和 PowerPoint COM；macOS 不能直接运行这条流程。标准路径 `/Applications/Microsoft PowerPoint.app` 未发现应用，其他位置及授权状态 UNKNOWN。

本机先用 HTML 和 Markdown 输出即可。若明确要求可编辑 PPTX，可单独评估已有演示稿工具并验证实际输出；不能把已有工具说明当作此 Skill 原生 PowerPoint 流程已验收。此次未购买 Office、未安装转换器或新增依赖。

## 验证边界

安装、结构和本地脚本测试已经验收；未做真实客户案例评测、FDE 会话自动触发评测、连接器认证验收、Windows PowerPoint 渲染验收或对外发布。其他无脚本的 Skills 仍按任务读取与使用，不存在必须统一运行的安装测试。
