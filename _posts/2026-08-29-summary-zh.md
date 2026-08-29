---
layout: default
title: "Horizon Summary: 2026-08-29 (ZH)"
date: 2026-08-29
lang: zh
---

> 从 206 条内容中筛选出 13 条重要资讯。

---

1. [Triton 3.8.0 发布：新增聚合类型与后端改进](#item-1) ⭐️ 9.0/10
2. [Htmx 4.0.0 发布：新功能与兼容性改进](#item-2) ⭐️ 9.0/10
3. [英伟达据称 129 亿美元收购 Hugging Face，加码 AI 中间层](#item-3) ⭐️ 9.0/10
4. [Anthropic 锁定 450 亿美元算力订单，为 IPO 蓄力](#item-4) ⭐️ 9.0/10
5. [美法官裁定五角大楼封杀 Anthropic 违法，永久解除禁令](#item-5) ⭐️ 8.0/10
6. [腾讯混元 Hy4 Preview 发布：770B 参数开源模型，支持 1M 上下文](#item-6) ⭐️ 8.0/10
7. [钢企盈利能力分化加剧 规模扩张模式开始转向](#item-7) ⭐️ 7.0/10
8. [每日钢市：钢坯涨 30 元，三家钢厂提价，钢价或趋强](#item-8) ⭐️ 7.0/10
9. [成本推涨，建筑钢材价格或继续偏强](#item-9) ⭐️ 7.0/10
10. [钢材供需双弱，螺纹钢反弹空间受限](#item-10) ⭐️ 7.0/10
11. [城市更新，把预制房推上风口](#item-11) ⭐️ 7.0/10
12. [广发证券维持中国建筑国际“买入”评级，看好 MiC 及北部都会区](#item-12) ⭐️ 7.0/10
13. [Claude 以每小时 4 美元训练自己，胜过每小时 150 美元的人类研究员](#item-13) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Triton 3.8.0 发布：新增聚合类型与后端改进](https://github.com/triton-lang/triton/releases/tag/v3.8.0) ⭐️ 9.0/10

Triton 3.8.0 已发布，将 @triton.aggregate 和 @gluon.aggregate 设为公开 API，并为 tl.topk 新增了 descending 参数。此版本还包含针对 NVIDIA 与 AMD/HIP 的后端增强，例如通用 multi-CTA 支持和 TMA store waits。 Triton 是 AI/ML 基础设施中广泛使用的 GPU 内核语言，因此此版本会影响构建高性能内核的开发者。新增的聚合类型简化了内核参数传递，而 multi-CTA 改进则有助于在现代加速器上扩展工作负载。 该版本新增了自动调优监听器、确定性的依赖缓存键，并修复了 tl.fdiv 中的 IEEE 舍入以及解释器中的 NaN 处理。它还更新了固定的 LLVM 版本，以修复 GFX950 和 SLP-vectorizer 问题，并且包含一些破坏性变更。

github · warrendeng · 8月28日 18:25

**背景**: Triton 是一种嵌入 Python 的语言和编译器，用于对 GPU 编程，通常用于为深度学习框架编写自定义内核。Gluon 是 Triton 的低层 GPU 编程模型，可为内核实现提供更多控制。Proton 是 Triton 自带的性能分析工具，用于分析内核性能。聚合类型允许用户定义结构化数据类型（类似于 struct），使参数传递更清晰。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://triton-lang.org/main/gluon/index.html">Gluon Overview — Triton documentation</a></li>
<li><a href="https://deepwiki.com/facebookexperimental/triton/12-proton-profiler">Proton Profiler | facebookexperimental/triton | DeepWiki</a></li>
<li><a href="https://github.com/triton-lang/triton/issues/8781">[Frontend] OOP + aggregate in triton/gluon · Issue #8781 · triton-lang/triton</a></li>

</ul>
</details>

**标签**: `#triton`, `#gpu`, `#compiler`, `#ai`, `#release`

---

<a id="item-2"></a>
## [Htmx 4.0.0 发布：新功能与兼容性改进](https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released) ⭐️ 9.0/10

Htmx 4.0.0 于 2026 年 8 月 28 日发布，带来新的功能和兼容性改进。这次大版本更新包含了如 &\#x27;hx-alpine-compat&\#x27; 等新增特性，旨在解决 htmx 与 Alpine.js 之间的集成问题。 这一大版本发布显示了超媒体驱动开发作为 JavaScript 重度单页应用之外的一种替代方案的持续活力。它通过提供用服务器渲染的 HTML 构建交互式 UI 的新工具，影响着 Web 开发者，而随之而来的讨论也凸显了人们对更简单架构方法的兴趣日益浓厚。 htmx 是一个小巧、无依赖、可扩展的库，让开发者可以直接在 HTML 中使用现代浏览器特性，而无需编写大量自定义 JavaScript。新版本包含诸如 &\#x27;hx-alpine-compat&\#x27; 的兼容性改进，同时保持其以服务器驱动的 UI 更新为核心的理念。早期用户报告称，该更新在诸如 Go、htmx 和 SQLite 这类简单服务器渲染技术栈上表现良好。

hackernews · rmsaksida · 8月28日 13:28 · [社区讨论](https://news.ycombinator.com/item?id=49478178)

**背景**: htmx 是一个 JavaScript 库，作为 intercooler.js 的改进版本而创建，其 1.0 版本于 2020 年 11 月发布。它允许开发者直接在 HTML 中访问现代浏览器特性，例如发起 AJAX 请求、触发 CSS 过渡和更新页面部分，而无需编写大量客户端脚本。这种方法建立在超媒体概念之上，超媒体是超文本的扩展，包含图形、音频、视频和链接，万维网就是超媒体的典型例子。超媒体驱动开发倡导服务器生成 HTML 片段和更简单、更传统的 Web 架构，与单页应用形成对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Htmx">htmx - Wikipedia</a></li>
<li><a href="https://www.sitepoint.com/htmx-introduction/">An Introduction to htmx , the HTML-focused Dynamic UI... — SitePoint</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hypermedia">Hypermedia - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体热烈，许多人称赞 htmx 是对复杂前端的一种清新、简单的替代。有一位用户分享了他在 Go 和 SQLite 项目中使用 htmx 的乐趣，而一位 .NET/Angular 开发者的相反观点指出，htmx 可能会迫使开发者回到在后端混合表现层与业务逻辑的做法。其他人则将其与 Alpine.js 和 alpine-ajax 等替代方案进行比较，也有人指出 htmx 的流行源于对不必要的前端复杂性的反感。

**标签**: `#htmx`, `#web-development`, `#hypermedia`, `#javascript`, `#release`

---

<a id="item-3"></a>
## [英伟达据称 129 亿美元收购 Hugging Face，加码 AI 中间层](https://news.google.com/rss/articles/CBMiSEFVX3lxTE1SMjhaaVhOSVVSTFd5Z2tCbEZ2OXJvaGU0aDJ1MVdieEtyUGQ3WloxOFpaYVNoRHlqTzJNdElfSkVSeFQxZ085eg?oc=5) ⭐️ 9.0/10

据财联社报道，英伟达据称将以 129 亿美元收购 Hugging Face，以强化其在 AI 中间层和全链条 AI 生态中的布局。该交易尚未得到两家公司官方确认。 若交易完成，这将成为规模最大的 AI 基础设施并购案之一，使英伟达掌控最流行的开源 AI 模型与数据集分享平台。此举可能将模型分发与英伟达的硬件和软件栈更紧密绑定，重塑 AI 开发领域的竞争格局。 据称，Hugging Face 年收入约 1.5 亿美元，129 亿美元的估值对应较高倍数。该交易尚未确认，条款仍可能变化；所谓“AI 中间层”是指位于基础模型与终端应用之间的软件层。

rss · Google News - AI 前沿 · 8月28日 07:12

**背景**: Hugging Face 常被称为“AI 界的 GitHub”，因为它托管了数十万个开源模型、数据集和 AI 应用，是开发者的核心枢纽。其 Transformers 库被广泛用于自然语言处理。AI 中间件是位于 AI 模型与应用程序之间的横向软件层，负责编排数据流与通信，帮助企业将 AI 试点扩展为生产级应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hugging_Face">Hugging Face - Wikipedia</a></li>
<li><a href="https://www.buildaiq.com/articles//learn-ai/ai-industry-ecosystem/hugging-face-explained-the-platform-powering-open-source-ai">Hugging Face Explained: The Platform Powering Open-Source AI ...</a></li>
<li><a href="https://www.vmware.com/topics/ai-middleware">What is AI middleware? | VMware</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#Hugging Face`, `#acquisition`, `#AI ecosystem`, `#M&amp;A`

---

<a id="item-4"></a>
## [Anthropic 锁定 450 亿美元算力订单，为 IPO 蓄力](https://news.google.com/rss/articles/CBMif0FVX3lxTFBYQ0tNSkxIMVdHSDhHUEUwWHd4R0ZBLXluTXJIWThudl9NcTItYUR3b3p5MXJsYUo3cU1nTUFvbWdXUGUwdnh3N1B6WnIwdjFhUEtoMU9lNVNHT1F4alN1OFhoQkxSQkowb1Zzc3RZSGpMVlZmbXFXc0hlRWxnYjg?oc=5) ⭐️ 9.0/10

Anthropic 已敲定一笔价值 450 亿美元的算力订单，以扩充其 AI 算力储备，据报道该公司正准备首次公开募股（IPO）。财联社的报道称，在冲刺 IPO 之际，Anthropic 据悉豪掷 450 亿美元锁定 AI 算力。 这笔巨额订单标志着 AI 基础设施投资显著升级，将重塑数据中心、GPU 和能源的需求格局。同时表明，Anthropic 正在为可能的公开上市做准备，以积极与 OpenAI 等竞争对手展开较量。 该订单价值 450 亿美元，但已披露的摘要中未提及具体供应商、芯片类型或交付时间表。财联社的报道强调，这笔投入出现在“冲刺 IPO 之际”，暗示这是一种在上市前锁定算力产能的战略举措。

rss · Google News - AI 前沿 · 8月28日 04:44

**背景**: Anthropic 是一家人工智能安全与研究公司，以其 Claude 大语言模型闻名，是 OpenAI GPT 系列的主要竞争对手。AI 算力指训练和运行前沿模型所需的专用硬件和数据中心容量。随着 AI 模型规模不断扩大，领先实验室纷纷签署数十亿美元级的协议，以确保获得稀缺的 GPU 供应。由于没有可用的网络搜索结果，目前无法核实该报道的更多细节。

**标签**: `#AI`, `#Anthropic`, `#compute infrastructure`, `#data centers`, `#AI compute`

---

<a id="item-5"></a>
## [美法官裁定五角大楼封杀 Anthropic 违法，永久解除禁令](https://news.google.com/rss/articles/CBMiU0FVX3lxTE9RUjkwdENKaU5acmk3UFZ2cE9mWksyWjVveFNEbWIyX2VoZUJuWFZmWk1tUVdSMnphVlR2MEg2Mml2UmdEcG5TRGVCU1loMmFXcEw4?oc=5) ⭐️ 8.0/10

美国一名法官裁定，五角大楼对 AI 公司 Anthropic 实施的制裁违法，并永久解除该封禁。据华尔街见闻和 Newswav 报道，这一裁决标志着美国国防部在法律上受挫。 这是少数针对美国政府限制领先 AI 公司的重大司法裁决之一，对 AI 政策及前沿实验室监管具有直接影响。该案可能改变国防部与 AI 开发者的合作方式，并影响未来以国家安全为由的政府措施。 根据相关报道，该裁决永久撤销了五角大楼对 Anthropic 的制裁行动。但现有摘要未提供法院、法官、法律理由以及制裁具体范围等细节。

rss · Google News - EDF AI 部署工程 · 8月28日 07:41

**背景**: Anthropic 是一家 AI 安全与研究公司，由前 OpenAI 成员于 2021 年创立，包括 CEO 达里奥·阿莫迪（Dario Amodei）和总裁丹妮拉·阿莫迪（Daniela Amodei）。该公司专注于构建可靠、可解释、可操控的 AI 系统，如 Claude 系列模型。由于前沿 AI 具有军民两用能力并可能引发国家安全担忧，相关企业正越来越多地受到政府审查，制裁或封禁即属此类措施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/">Home \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#Anthropic`, `#legal`, `#regulation`, `#AI frontier`

---

<a id="item-6"></a>
## [腾讯混元 Hy4 Preview 发布：770B 参数开源模型，支持 1M 上下文](https://news.google.com/rss/articles/CBMiqAFBVV95cUxPUWpjUjZiYXE3eFdfT0J5OVlwekUtT0QtSlppa1ZLUzRXUFJXZFBHUnpYcDZKT3F5d1dOcjV4eU9qdDBTa3RFMjZ6dGRFQU9XM0duYkVDWXhHUXJpbG9LQVlUa2lVNGk3Y0cxaXU1aHNfbTRzbENZWEhrcEVtQ1hpNGFPRGlyU3NONEROVDZEVHRkdmMzdjlXRkxGWEJvWklNQVgtNHlIcnY?oc=5) ⭐️ 8.0/10

2026 年 8 月 28 日，腾讯发布了迄今最强的开源模型 Hy4 Preview，拥有 770B 总参数、49B 活跃参数和 1M token 上下文窗口。在 203 个工程任务的盲评中，它以 2.99 分略胜 GLM-5.3（2.92）与 Kimi K3（2.94）。 此次发布标志着开源 AI 的一个重要里程碑——一家中国领先科技公司以庞大的稀疏模型追赶顶级专有系统，推动技术前沿。1M 上下文窗口使其能够胜任长周期软件工程和科学研究等任务，可能重塑开源权重模型的竞争格局。 Hy4 Preview 采用混合专家（MoE）架构，总参数为 770B 但每个 token 仅激活 49B 参数，在规模与效率间取得平衡。API 定价为每百万输入 tokens 0.834 美元、每百万输出 tokens 2.501 美元，模型已上线腾讯云、GitHub、HuggingFace、ModelScope、AtomGit 和 OpenRouter 等平台。

rss · Google News - EDF AI 部署工程 · 8月28日 15:26

**背景**: Hy4 Preview 是腾讯开发的大语言模型，采用混合专家（MoE）架构，每个 token 只激活部分参数，从而在不按比例增加计算成本的前提下扩大模型规模。上下文窗口指模型一次能处理的最大输入文本量；1M tokens 非常庞大，使模型能够处理长文档、代码库及多步推理任务。这类开源模型降低了开发者和研究者的门槛，但在某些基准上仍常落后于闭源模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Context_window">Context window - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2507.11181">[2507.11181] Mixture of Experts in Large Language Models A Closer Look into Mixture-of-Experts in Large Language Models Mixture of Experts Explained - Hugging Face Applying Mixture of Experts in LLM Architectures | NVIDIA ... A Closer Look into Mixture-of-Experts in Large Language Models Understanding Mixture of Experts (MoE): The Architecture ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#large language model`, `#open-source`, `#Tencent`, `#Hunyuan`

---

<a id="item-7"></a>
## [钢企盈利能力分化加剧 规模扩张模式开始转向](https://news.google.com/rss/articles/CBMigAFBVV95cUxPeU9LbU12NklSbUhjaEVkakFvdlJGTGJabUhLYWhyNUp0TW5hdWtsaFJpTmFvUFBpNVJFNy0ybldmQjUzRGRTdmxaLUFhNmVwTW5DRDNtclJVeGhxU0EtWmllRmp1YjIyX3FrYllVa3d3NUZFTURRLXFfOG9hTHZ4bg?oc=5) ⭐️ 7.0/10

新华财经调查报道称，中国钢企之间的盈利能力差距正在扩大，行业开始摆脱传统的规模扩张模式。该报道由新浪财经转载，凸显了正在进行的结构性转变。 此事意义重大，因为它标志着中国最重要的基础工业之一正在发生战略转向，将影响投资决策、供应格局以及下游钢铁加工和流通环节。随着盈利能力出现分化，弱势企业可能面临整合或退出，而强势企业可能引领行业向效率和更高附加值产品转型。 该报道隶属于新华财经调查系列，由新浪财经转载。虽然标题中未提供具体企业或指标细节，但调查聚焦于盈利钢企与亏损钢企之间日益加剧的分化，以及行业对单纯产能扩张的重新审视。

rss · Google News - 钢材加工配送 · 8月29日 02:28

**背景**: 中国钢铁行业长期以来依靠大规模产能扩张来实现增长，这导致了产能过剩和激烈的价格竞争。钢企还面临铁矿石等原材料价格波动，以及建筑和制造业需求变化带来的挑战。随着盈利能力分化加剧，企业越来越需要依靠成本控制、产品质量和运营效率来竞争，而非单纯追求产量。报道所指的规模扩张模式转向，反映出行业正在向更可持续、更注重价值的方向发展。

**标签**: `#steel industry`, `#profitability`, `#industry trend`, `#steel processing`, `#business strategy`

---

<a id="item-8"></a>
## [每日钢市：钢坯涨 30 元，三家钢厂提价，钢价或趋强](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE8wTFFFSktsUHFrRi0yaXZ4UlFZNGxPUC1Zc2tjMWdPWk5zX242MDYzVnNBOUMwa1ZZSEV5VkJheXN2ZkZkVzRQclVBcFlFZms1d0I5c0pfUjNxaEZuWkdEWmRVelRGY00?oc=5) ⭐️ 7.0/10

据 Mysteel 每日钢市报告，钢坯价格上涨 30 元，同时有 3 家钢厂宣布上调出厂价，显示钢价短期内可能趋强运行。 这些价格信号显示中国钢铁市场情绪回暖，可能影响下游建筑和制造成本，并对整个供应链的贸易和库存策略产生连锁影响。 报告给出了两个具体指标：钢坯价格上涨 30 元以及 3 家钢厂提价，均指向行情可能上行。Mysteel 是中国领先的大宗商品数据信息服务商，其每日市场简报受到行业参与者的广泛关注。

rss · Google News - 钢材加工配送 · 8月28日 10:03

**背景**: 钢坯是用于生产螺纹钢、线材等成品钢材的半成品，其价格是观察钢铁市场短期情绪的重要指标。在中国，Mysteel 等平台的每日市场报告帮助贸易商和钢厂快速判断供需和价格走向，尤其是在原材料成本波动时期。

**标签**: `#steel`, `#price`, `#market`, `#steel mills`, `#China`

---

<a id="item-9"></a>
## [成本推涨，建筑钢材价格或继续偏强](https://news.google.com/rss/articles/CBMibEFVX3lxTE84U2NvN1NlU21WbDF2WnNVWWJmSWJfaVFwOGszUUJmQnBzY1dJMThvZ1ZjdEtKcmZFSW1WU3pJYVRrQUMtbVNVWEp1TW9fRHFCQjFrOHkxcnM2UkZlQjZ0SHpCdmFUX1hQQ3QwaA?oc=5) ⭐️ 7.0/10

网易手机新闻的一篇报道指出，受成本上涨推动，建筑钢材价格可能继续保持偏强态势或继续上行。文章聚焦于中国建筑钢材市场的近期价格走势。 建筑钢材是基础设施和房地产的关键材料，其价格变动会影响建筑预算和整个钢材市场情绪。如果成本推动的上涨持续，下游买家和建筑企业可能面临更高的材料成本。 文章未给出具体价格水平或成本数字，但强调成本压力是预期偏强的主要推动因素。该预测基于当前生产和原材料成本状况，可能属于短期展望。

rss · Google News - 钢材加工配送 · 8月29日 01:56

**背景**: 建筑钢材（如螺纹钢）广泛应用于建筑和基础设施项目。其价格受铁矿石、焦煤等原材料成本、能源价格以及建筑行业需求的影响。当生产成本上升时，生产商往往将成本转嫁给买家，导致市场价格上涨。这篇报道反映的是中国钢材市场的常见动态。

**标签**: `#steel`, `#construction steel`, `#pricing`, `#cost push`, `#market forecast`

---

<a id="item-10"></a>
## [钢材供需双弱，螺纹钢反弹空间受限](https://news.google.com/rss/articles/CBMijAFBVV95cUxNVEQ1VnJQNzI2c3VNbGwxcU1sSldVaG1pVHNKay1XVG5SZmttZXAxZnVMQldUU0dPMnV4M0JBQjRMVVEyajhzYmM1QjhhN2xTeC1JNHpSczlEUzBQOFRVSEJrRjVPSE42MXZKSUR6dG84U0gxMWlMNEllTzdRRFFSVmV0WHE3TXNoQW4yaA?oc=5) ⭐️ 7.0/10

新浪财经报道称，中国钢材市场继续维持“供需双弱”格局，螺纹钢价格上方的反弹空间受到限制。该报道仅为简短短标题，未附详细数据。 这意味着钢厂和贸易商面临的钢价及利润压力仍在持续。由于螺纹钢是建筑领域的关键材料，供需双弱格局反映出下游需求疲软，影响行业库存与交易决策。 该报道是新浪财经的一条简短短标题，表明钢材产量与下游消费均不旺盛。在此情况下，螺纹钢价格短期内的反弹空间预计有限。

rss · Google News - 钢材加工配送 · 8月28日 05:49

**背景**: 螺纹钢是建筑领域常用的钢材品种。“供需双弱”指供给端和需求端同时偏弱、甚至收缩的状态，常见于环保限产、房地产活动低迷或季节性因素影响。在中国钢材市场分析中，市场通常关注钢厂产量与下游需求的平衡，上期所等期货价格常被作为关键价格信号。

**标签**: `#steel`, `#rebar`, `#supply-demand`, `#price outlook`, `#China`

---

<a id="item-11"></a>
## [城市更新，把预制房推上风口](https://news.google.com/rss/articles/CBMigwFBVV95cUxOY1lWV3Mta0M4WVM5Z1NEc2IyQ1VYRnN2a3NHOU83SE1nclNVSlJObkZiS3NJbkFSelF6dlJncUFJS0hKUm4tOEJNa2dnVnZlZTF4SE0xdkZWUmhXMGlIdGJBcWk4ejRwME5iZGp4V3RaeXVjbElHY1AxLVRTaDhrTVJnNA?oc=5) ⭐️ 7.0/10

据新浪财经报道，中国的城市更新行动正在把预制房（又称模块化建筑）推上风口。文章指出，城市更新项目带来的需求增长正成为预制房产业的关键驱动力。 这一趋势标志着中国建筑业正朝着工业化和绿色建筑方向发生重大转变，有助于减少建筑垃圾并缩短工期。同时，它为预制房供应链上的制造商和供应商，以及关注政策驱动型需求的投资者创造了机遇。 目前仅提供标题和一句话摘要，因此没有包含具体数据和案例。该报道来自中国可信的财经新闻来源新浪财经，标签涉及预制房、城市更新、工业化建造、政策和需求。

rss · Google News - 工业化建造与智能空间 · 8月29日 03:50

**背景**: 预制房又称模块化建筑，其核心逻辑是将建筑拆解为独立模块，在工厂完成制造，再运到施工现场拼装成型，而不是在工地一砖一瓦地建造。城市更新项目，如旧城区和棚户区的改造，需要高效的施工方式来减少干扰并加快进度。中国政府一直将装配式建筑作为绿色建筑和建筑工业化政策的一部分加以推广，新冠疫情期间火神山医院的快速建成也展示了该技术的潜力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://m.voc.com.cn/xhn/news/202607/33147260.html">侃财邦｜“ 预 制 房 ”海外走红，这个万亿赛道湘企“抢跑”</a></li>
<li><a href="https://www.ahjzu.edu.cn/jsxh/2020/0316/c12883a141731/page.htm">火神山医院的背后：浅谈 装 配 式 建 筑 的发展</a></li>

</ul>
</details>

**标签**: `#prefabricated housing`, `#urban renewal`, `#industrialized construction`, `#policy`, `#demand`

---

<a id="item-12"></a>
## [广发证券维持中国建筑国际“买入”评级，看好 MiC 及北部都会区](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBrMHFzcTZPT0F5RnFxMVVkaE1seHJFZ0M0SlZyV3NZV1h4QkUyUWRyQm5zNmY5ZEhRYXBWNjhIbjVnbkdCeF9BVnNlbUkxd1FRanI0?oc=5) ⭐️ 7.0/10

广发证券维持对中国建筑国际的“买入”评级，指出北部都会区建设和模块化集成建筑（MiC）业务将成为新的增长点。此次为重申评级而非上调，表明分析师的看法保持连贯。 该评级显示出机构对北部都会区大型项目所带动香港建造需求的信心，并将 MiC 视为高效快速建造的战略性方法。对关注中国建筑国际及整个模块化建造板块的投资者来说，这是一个重要的信号。 该报告来自广发证券分析师，通过 Moomoo 的“研报掘金”栏目发布。中国建筑国际是香港主要承建商之一，报告明确将北部都会区及 MiC 业务列为未来增长的催化剂。

rss · Google News - 工业化建造与智能空间 · 8月28日 08:07

**背景**: MiC（模块化集成建筑）是一种创新的建造方式，将建筑工序由工地转移至工厂：独立模块在受控的工厂环境中完成装修、固定装置和配件，再运到现场进行组装。北部都会区是香港新界北部一个大型规划区域，旨在打造一个与内地更紧密连接的综合性生活与经济区域。鉴于北部都会区庞大的房屋及基建需求，MiC 被广泛视为加快交付和应对劳工短缺的关键技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mic.cic.hk/en/AboutMiC">CIC MiC | What is MiC and MiMEP - Construction Industry Council</a></li>
<li><a href="https://en.wikipedia.org/wiki/Northern_Metropolis">Northern Metropolis - Wikipedia</a></li>

</ul>
</details>

**标签**: `#MiC`, `#Industrialized Construction`, `#China State Construction International`, `#Northern Metropolis`, `#Equity Research`

---

<a id="item-13"></a>
## [Claude 以每小时 4 美元训练自己，胜过每小时 150 美元的人类研究员](https://news.google.com/rss/articles/CBMiiAFBVV95cUxPV2VhVFNKUkJnRnY3LVBnMjNGR0RhRmo4bDlaMzk3Yko4Y2xYNzE3Vkt4ZEwybkVPbWhFSGVGNW0tb3BCTkFEb3g4ajhadmNDVWxnRE5OaDJCT0xyV2lVemxIQ3JQZ0UwdHRPazBwQVZqRE9RZjM4N0ZDM19OUFJUODAzV0FEa2NV?oc=5) ⭐️ 7.0/10

据搜狐网报道，Anthropic 的 Claude AI 被用来以每小时 4 美元的成本训练另一个 Claude 模型，其成果超过了每小时 150 美元的人类研究员。 这凸显了 AI 驱动研究大幅降低成本、加速进步的潜力，可能推动递归自我改进的实现，并重新定义人类研究员在 AI 研发中的角色。 该报道缺乏技术细节，比如涉及哪些 Claude 模型、具体任务和评估指标。这一说法似乎来自单一实验的轶事或基准，而非经过同行评审的研究。

rss · Google News - EDF AI 部署工程 · 8月29日 02:37

**背景**: Claude 是 Anthropic 开发的一系列大语言模型，以其基于宪法的训练方法著称。递归自我改进（RSI）是一种假设性过程，AI 系统通过增强自身能力，可能引发智能爆炸。用 AI 训练 AI 是朝这个方向迈出的一步，但当前研究表明，开放式的 RSI 仍受到接地性要求、崩溃动态和算力限制的制约。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_%28AI%29">Claude (AI) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement - Wikipedia</a></li>
<li><a href="https://www.technologyreview.com/2026/08/18/1142188/ai-recursive-self-improvement/">AI’s recursive self-improvement might not come so quickly ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Claude`, `#AI self-improvement`, `#Anthropic`, `#AI research`

---