---
layout: default
title: "Horizon Summary: 2026-07-28 (ZH)"
date: 2026-07-28
lang: zh
---

> 从 179 条内容中筛选出 8 条重要资讯。

---

1. [月之暗面开源 Kimi K3：首个 2.8 万亿参数模型](#item-1) ⭐️ 10.0/10
2. [谷歌公布 Gemini 4，迄今最雄心勃勃的预训练项目](#item-2) ⭐️ 9.0/10
3. [vLLM v0.26.0 发布：新增 Inkling 模型系列和 DeepSeek-V4 优化](#item-3) ⭐️ 8.0/10
4. [Anthropic 阐明对开放权重模型的立场](#item-4) ⭐️ 8.0/10
5. [钢价暴跌，钢厂承压](#item-5) ⭐️ 8.0/10
6. [英伟达牵头成立开放 AI 安全联盟](#item-6) ⭐️ 8.0/10
7. [奥特曼和黄仁勋将与参议员会面讨论 AI 安全](#item-7) ⭐️ 7.0/10
8. [华盛顿因中国‘失控模型’陷入 AI 安全恐慌](#item-8) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [月之暗面开源 Kimi K3：首个 2.8 万亿参数模型](https://huggingface.co/moonshotai/Kimi-K3) ⭐️ 10.0/10

月之暗面在 Hugging Face 上正式发布了 Kimi K3 模型，这是全球首个开源的 2.8 万亿总参数（激活参数 104B）模型，支持 1 亿 token 的上下文窗口，并采用了 Kimi Delta Attention（KDA）、Attention Residuals（AttnRes）和 Stable LatentMoE 等全新架构。 此次发布将开源模型推向了 3T 参数级别，能够支持更高级的长上下文推理和多模态理解，同时其高效的架构有望降低大规模 AI 应用的部署成本。 该模型共有 896 个专家，每 token 激活 16 个，扩展效率相比 Kimi K2 提升约 2.5 倍，并支持 MXFP4 量化以减少内存占用。其许可证对大型“模型即服务”企业有额外限制，年收入超过 2000 万美元需要单独签订协议。

telegram · zaihuapd · 7月27日 15:15

**背景**: 此次发布基于月之暗面此前于 2025 年 7 月推出的 Kimi K2 模型，后者使用了修改版的 MIT 许可证。Kimi K3 引入了 Kimi Delta Attention——一种在 2025 年论文中阐述的高效线性注意力机制，并采用了 NVIDIA 提出的 LatentMoE 技术，该技术通过在低维潜在空间中计算来减少计算量。这些创新使得一个 2.8 万亿参数的模型能够比以前代际的模型更高效地训练和部署。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2510.26692">[2510.26692] Kimi Linear: An Expressive, Efficient Attention Architecture</a></li>
<li><a href="https://arxiv.org/abs/2601.18089">[2601.18089] LatentMoE: Toward Optimal Accuracy per FLOP and Parameter in Mixture of Experts</a></li>

</ul>
</details>

**社区讨论**: 社区对该模型的扩展效率和新型架构组件表示赞赏。Simon Willison 的分析指出了其许可证条款的严格性，偏离了标准的开源定义；而 teortaxesTex 的一则推文称赞了其大规模训练的稳定性，并认为如果投入更多算力，它可能会挑战其他前沿模型。

**标签**: `#AI`, `#open-source`, `#large language model`, `#MoE`, `#Kimi K3`

---

<a id="item-2"></a>
## [谷歌公布 Gemini 4，迄今最雄心勃勃的预训练项目](https://9to5google.com/2026/07/26/google-gemini-4-teases/) ⭐️ 9.0/10

谷歌 CEO Sundar Pichai 在 Alphabet 2026 年第二季度财报电话会上宣布，下一代大语言模型 Gemini 4 正在训练中，并将其描述为该公司迄今为止最具雄心的预训练项目。该模型预计于 2026 年底发布，很可能在 11 月或 12 月。 这一公告表明谷歌继续大力投资 AI 前沿研究，旨在保持与其他主要玩家的竞争力。Gemini 4 的发布可能带来 AI 能力的重大进步，尤其是在通用智能方面取得新突破。 Pichai 强调，谷歌将优先将算力分配给前沿 AGI 研发，以确保 Gemini 4 在发布时仍处于前沿。同时，Gemini 3.x Flash 系列将保持大约每月一次的迭代频率，重点提升智能编码等能力。

telegram · zaihuapd · 7月27日 04:06

**背景**: 预训练是构建大型语言模型的第一步且计算最密集的阶段，系统通过自监督学习从海量无标签数据中学习通用模式。人工通用智能 \(AGI\) 指的是一种假想的 AI 系统，能够在广泛任务中达到或超越人类认知能力。谷歌对 AGI 研究的关注表明其雄心是超越狭义 AI 能力，迈向更通用、更强大的模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/what-is-pre-training-and-its-objective/">What is Pre Training and its Objective - GeeksforGeeks</a></li>
<li><a href="https://en.wikipedia.org/wiki/Artificial_general_intelligence">Artificial general intelligence - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Gemini 4`, `#Google AI`, `#large language models`, `#AI frontier`, `#pre-training`

---

<a id="item-3"></a>
## [vLLM v0.26.0 发布：新增 Inkling 模型系列和 DeepSeek-V4 优化](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.0/10

vLLM v0.26.0 引入了 Inkling 开放权重模型系列的完整支持，包括基础建模、MTP=1 推测解码和 ModelOpt NVFP4 量化。同时为 DeepSeek-V4 在多种 GPU 平台上带来了显著的性能优化，新增用于生成模型的 fp32 lm\_head，以及按 KV 缓存组选择注意力后端的功能。 此次发布显著扩展了 vLLM 的模型支持和推理效率，使得部署 Inkling 等新兴模型以及跨硬件优化 DeepSeek-V4 变得更加容易。注意力灵活性和 KV 卸载改进使得生产级 AI 系统的推理更加高效可扩展。 Inkling 模型系列是 Thinking Machines Lab 的首个开放权重模型，其较小版本 Inkling-Small 拥有 120 亿活跃参数。DeepSeek-V4 的优化包括专用路由内核实现了 2.94%的端到端 TPOT 提升，以及 fused\_topk\_bias 内核加速 1.5-2 倍。

github · khluu · 7月27日 01:06

**背景**: vLLM 是一个高性能的大语言模型推理引擎，支持多种模型架构和量化方法。Inkling 模型系列专为广泛的推理任务设计，注重开放权重可用性。MTP（多令牌预测）是一种推测解码技术，每次前向传播预测多个令牌，以在不降低质量的情况下提高吞吐量。NVFP4 是 NVIDIA ModelOpt 的一种 4 位浮点量化方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our Open-Weights Model - Thinking Machines Lab</a></li>
<li><a href="https://nvidia.github.io/TensorRT-LLM/blogs/tech_blog/blog02_DeepSeek_R1_MTP_Implementation_and_Optimization.html">DeepSeek R 1 MTP Implementation and Optimization — TensorRT LLM</a></li>
<li><a href="https://docs.vllm.ai/projects/vllm-omni/en/latest/user_guide/quantization/modelopt/">ModelOpt - vLLM-Omni</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#AI deployment`, `#inference optimization`, `#LLM inference`, `#performance`

---

<a id="item-4"></a>
## [Anthropic 阐明对开放权重模型的立场](https://www.anthropic.com/news/position-open-weights-models) ⭐️ 8.0/10

Anthropic 发布声明，澄清其不主张全面禁止开放权重 AI 模型，但支持对足够强大的模型进行强制性安全测试。 这一立场可能影响全球 AI 监管讨论，因为 Anthropic 是一家领先的 AI 公司。它旨在平衡开放性与安全性，可能影响政府如何监管开源 AI。 Anthropic 强调，不具备危险能力的开放权重模型是公共利益，但具有关键风险的模型应接受测试。该公司还支持禁止向中国出售芯片和打击走私等措施。

hackernews · surprisetalk · 7月27日 22:03 · [社区讨论](https://news.ycombinator.com/item?id=49076057)

**背景**: 开放权重模型是指最终训练出的权重和偏置被公开发布的 AI 模型，任何人都可以下载、检查、修改并运行它们。它们促进了社区驱动的创新，但也引发了安全和滥用问题。Anthropic 的声明旨在解决这些问题，而不诉诸全面禁令。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/position-open-weights-models">Our position on open-weights models - Anthropic</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you&#x27;ve been told - Open Source Initiative</a></li>
<li><a href="https://cset.georgetown.edu/article/ai-safety-evaluations-an-explainer/">AI Safety Evaluations: An Explainer | Center for Security and Emerging Technology</a></li>

</ul>
</details>

**社区讨论**: 许多评论者表示怀疑，认为如果测试成本高昂或准入受限，强制性安全测试可能成为事实上的禁令。一些人指责 Anthropic 出于自身利益保护其封闭模型。

**标签**: `#AI governance`, `#open-weights`, `#safety testing`, `#Anthropic`, `#regulation`

---

<a id="item-5"></a>
## [钢价暴跌，钢厂承压](https://news.google.com/rss/articles/CBMidkFVX3lxTE1LRER1bUtWbk5RbDV0WW83S3dyT2lpRU5zTWtVSllIWjNsM0NsemN1cURkcmtLZ3gycGZzMmllUU9XQ0dMNEs1b2ZsNGRoaXVOREt2d0g4RHNubVpGV0thSjEzOTl3bUVTWEhEZEFwc1RlVmZUMFE?oc=5) ⭐️ 8.0/10

据新浪财经报道，钢材价格出现集体下跌，给钢厂带来了巨大的经营压力。 此次价格下跌表明钢铁市场需求疲软，可能导致钢厂减产、裁员和财务亏损，进而影响从原材料到建筑业的整个供应链。 文章指出，跌势涉及多种钢材产品，钢厂维持盈利越来越困难，如果趋势持续，一些钢厂可能面临停产。

rss · Google News - 钢材加工配送 · 7月27日 11:38

**背景**: 钢材价格是重要的经济指标，反映了建筑、制造和基础设施领域的需求。价格下跌通常表明供过于求或需求减少，而钢厂由于固定成本高，对价格下跌尤为敏感。

**标签**: `#steel processing`, `#steel distribution`, `#price drop`, `#market trend`, `#industry news`

---

<a id="item-6"></a>
## [英伟达牵头成立开放 AI 安全联盟](https://news.google.com/rss/articles/CBMimwFBVV95cUxNcWJRR0hGVnp6RHFJOXB4SXE3QkFfVjZ4eV9UU04wTlV2SE01UjhzRkZJTW1TeWFnSUZCRGtIYVppSVV0OVM4YWJvSlU2Vl94cERWZHYyTzdxTGZzbWswRlc4WXEtVXJUV29kUXZrQW1xZzI1Ulp2WWdmazNEb1hVZTBJQTN6V2x1c2ZpVGE4RE1VdlFnQlZIMVhaUQ?oc=5) ⭐️ 8.0/10

英伟达牵头成立了开放安全 AI 联盟，这是一个由 36 家公司组成的联盟，包括微软、SpaceX 等，旨在制定 AI 安全与防护的开放标准并共享相关工具。 这一举措代表了行业范围内标准化 AI 安全实践的重大努力，随着开放权重 AI 模型的广泛部署以及网络威胁的增加，这变得至关重要。 该联盟专注于为 AI 代理构建开放防御体系，包括身份验证、安全模型格式和多模型扫描。贡献包括 Hugging Face 的 Safetensors 格式，用于安全存储模型权重。

rss · Google News - EDF AI 部署工程 · 7月27日 09:32

**背景**: 开放安全 AI 联盟的成立是对近期 OpenAI 和 Hugging Face 网络攻击事件的回应，这些攻击暴露了 AI 基础设施的脆弱性。开源 AI 模型虽然强大，但也引入了远程代码执行和未授权访问等安全风险。该联盟旨在制定共享的安全标准和工具，以减轻整个行业的这些风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/open-secure-ai-alliance/">Industry Leaders Join Open Secure AI Alliance for AI Safety and Security | NVIDIA Blog</a></li>
<li><a href="https://coinpaper.com/33507/nvidia-launches-open-ai-safety-alliance-after-hugging-face-cyberattack">Nvidia Launches Open AI Safety Alliance After Hugging Face...</a></li>
<li><a href="https://www.pymnts.com/cybersecurity/2026/nvidia-forms-ai-safety-alliance-following-openai-cyberattack/">PYMNTS | Nvidia Forms AI Safety Alliance Following OpenAI ...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#Nvidia`, `#AI alliance`, `#open standards`

---

<a id="item-7"></a>
## [奥特曼和黄仁勋将与参议员会面讨论 AI 安全](https://news.google.com/rss/articles/CBMivgJBVV95cUxNOE1fbGpUTG5tWTZqWkx4WGRzQ3JHM0NiRWJmdDBpZmdyMDVoU0pWbndKYlFvVzlCdXBtR2pjUGxxQl9UZk1uZGlwdWVERi15NFVGZkZpUnhpN08xYm1ySk5zLXJGTEpEUGd3aFdUVjl1NnhQZmZ4Q0pJUnFVX3NEWHFBTUgwVFBQdU12LTFaa3VGdGVGY3hBRmdpcmsxTU5ZaXZGeXFCd0xrNU9yMUhkRDZOYlVoM1RGX2hrdVpJQkpNeFVBSjJkaGFxNG9zMDJwSGZzTHJrdXB5VVZhTDVZNTdhdnhiNnFSZERrQXRjbDkxUEdqeXdDdlJ5a1pCS2J2VkFyTDZwTFp4T0EyOHlRRERpLVdHWXpvOTdFWk1Lc0N6Qkh5QkRsUTI1VzRRb2h1bkNmSGM3ZUU5ZFMyNlE?oc=5) ⭐️ 7.0/10

OpenAI 首席执行官萨姆·奥特曼和英伟达首席执行官黄仁勋计划在国会山与民主党参议员会面，讨论持续存在的 AI 安全风险以及潜在的监管措施。 此次会面表明顶级 AI 行业领袖正直接与政策制定者接触，可能加速 AI 安全法规的制定，并影响美国 AI 治理的方向。 此次会面正值一系列 AI 安全事件及公众关注度上升之际；具体议程尚未披露，但议题可能包括偏见、虚假信息以及先进 AI 系统带来的生存风险。

rss · Google News - EDF AI 部署工程 · 7月27日 23:25

**背景**: 随着像 ChatGPT 和 GPT-4 这样的生成式 AI 模型展现出引发伦理和安全问题的能力，AI 安全已成为一个突出问题。美国政府正在探索监管框架，行业领袖被要求作证或与立法者会面。

**标签**: `#AI safety`, `#regulation`, `#Sam Altman`, `#Jensen Huang`, `#policy`

---

<a id="item-8"></a>
## [华盛顿因中国‘失控模型’陷入 AI 安全恐慌](https://news.google.com/rss/articles/CBMitgJBVV95cUxQM0JaYVdEMlRXU2ozV3M0eGVrdWhSZXJwYUZrVEQ5VnFobDJ5THo2WWpGTVBZY2RoVjNrOTZZWFY5N3NhNThRSk9CT2R1U0diZDYtekhIczJ2RU5KTGI4T0ZSU2RDeDJEcHN1TWY3V1gwR3k2ZVdCZFA0V2lPa3JRNnU4NkZXTHh3QTV4UmlNU3p2Y25DUW9hbE1saHM4WGNDYlRiU09mTE9iWk9fc0dNcnlEcGgxWThCRDZZbDJEdVRJRUliNktRSzRUd2VVT09PXzFZaEJEcmt2bUhYV0NGWnVvWk80U2NjSmdTWnRnN1AybmQ2QnVrMXAxLUZUOWxQQ1BJZ01oRXJ2ZVlfU2x5WnlxT0lyLVBGOHJSNVJMbndReXJ5RU55ZktFWGVFT2RrVTM5VThR?oc=5) ⭐️ 7.0/10

《华尔街日报》报道称，华盛顿方面正因中国开发失控 AI 模型引发的安全风险而日益恐慌。 这种恐慌可能导致更严格的 AI 监管和加剧的地缘政治紧张，影响全球 AI 合作与安全标准。 文章聚焦于对“失控”AI 模型的恐惧，这些模型可能造成灾难性危害，但缺乏来自中国的此类模型的具体技术证据。

rss · Google News - EDF AI 部署工程 · 7月27日 01:23

**背景**: 随着先进 AI 系统变得更加强大和不透明，AI 安全问题日益受到关注。“失控 AI”的概念指的是超出人类控制的 AI 系统，可能造成意外伤害。在美中竞争的背景下，政策制定者担心中国 AI 的快速发展可能导致不安全的部署。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sipi.bot/how-to/how-to-prevent-runaway-agents">How to Prevent Runaway AI Agents (2026 Guide) — sipi.bot</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#AI policy`, `#geopolitics`, `#China threat`, `#AI security`

---