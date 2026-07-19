# 老板行业日报

每天北京时间 07:00，GitHub Actions 会生成中文行业日报，并同时保留三种查看方式：

- GitHub 仓库：`老板行业日报/YYYY/MM/YYYY-MM-DD.md` 和同名 `.html`
- GitHub Pages：继续使用现有 Horizon 日报网站，并提供独立早报页面
- 本地：同步到 `D:\Obsidian\老板行业日报`，双击 `.html` 可在浏览器中阅读

日报按四条业务主线筛选：钢材加工配送、工业化建造与智能空间（MiC/MiMEP）、AI 前沿、EDF AI 前沿部署工程（模型部署、RAG、MLOps/LLMOps、推理优化、评测、可观测性、安全和成本）。

## 本地同步

运行：

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "D:\Obsidian\Horizon\scripts\sync-boss-digest.ps1"
```

脚本只会把公开 GitHub 仓库中的 `老板行业日报`（Markdown 和 HTML）复制到 `D:\Obsidian\老板行业日报`，不会删除目标文件夹中的其他文件。

Windows 计划任务建议每天 07:30 运行，并启用“错过计划后尽快启动”。计划任务由本机创建，不需要额外 GitHub 密钥。
