---
layout: default
title: "Horizon Summary: 2026-10-01 (ZH)"
date: 2026-10-01
lang: zh
---

> 从 200 条内容中筛选出 7 条重要资讯。

---

1. [谷歌发布 Gemini 4 Argon，主打智能体编程的前沿模型](#item-1) ⭐️ 9.0/10
2. [DeepSeek 开源华为昇腾基础组件，对标其英伟达平台栈](#item-2) ⭐️ 8.0/10
3. [Cloudflare 宣布计划成为公共证书颁发机构](#item-3) ⭐️ 8.0/10
4. [Kimi K3 接入 OpenAI Codex 企业通道，中国开源模型首入其付费结算体系](#item-4) ⭐️ 8.0/10
5. [Mysteel 对比近五年国庆节前后钢价走势规律](#item-5) ⭐️ 7.0/10
6. [Mysteel 午报：钢价局部上涨，黑色期货普涨](#item-6) ⭐️ 7.0/10
7. [英伟达、谷歌、Meta 等六家公司签署白宫 AI 安全自愿协议](#item-7) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [谷歌发布 Gemini 4 Argon，主打智能体编程的前沿模型](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) ⭐️ 9.0/10

谷歌发布了新前沿模型 Gemini 4 Argon，官方称其在智能体编程、推理和多模态能力上实现跃升，尤其强调能够持续完成长时间、多步骤的任务。该消息在 Hacker News 上获得 971 分和 662 条评论，但谷歌表示仍在收集早期测试者反馈并迭代安全护栏，之后才会向开发者、企业和消费者全面开放。 谷歌的旗舰前沿模型发布进一步加剧了 AI 领域的多厂商竞争，各大实验室几乎以月为周期互相超越，同时也把智能体编程从代码补全式辅助推向项目级的真实工程自动化。社区反应显示，讨论焦点正从单纯的基准分数转向能力、算力与市场权力在超大规模云厂商、新兴云服务商和 ASIC 之间的分布格局。 谷歌称 Argon 在编程、推理和多模态方面的能力使其适用于各类企业工作流，并表示 Argon 智能体已在谷歌内部用于将 C/C++ 代码库迁移到 Rust。第三方评测机构 Artificial Analysis 将 Gemini 4 Argon（High）评为智能水平领先且价格合理的模型之一，但该模型尚未正式开放，因而招致“先发布后交付”的批评。

hackernews · bradleyg223 · 9月30日 20:04 · [社区讨论](https://news.ycombinator.com/item?id=49913571)

**背景**: 前沿模型（frontier model）指最先进的一类通用 AI 系统，通常是在海量数据上以极高算力训练出来的大语言模型，因此只有少数资金雄厚的实验室能够研发。智能体编程（agentic coding）指在项目层面而非文件层面工作的 AI 系统：给定一个目标后，智能体会读取配置文件、追踪依赖、运行并调试代码，并进行多轮迭代。谷歌的 Gemini 系列正是其旗舰模型家族，与 OpenAI、Anthropic 等公司的模型直接竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/">Introducing Gemini 4 Argon</a></li>
<li><a href="https://artificialanalysis.ai/models/gemini-4-argon">Gemini 4 Argon (high) - Intelligence, Performance... | Artificial Analysis</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agentic_coding">Agentic coding</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了令人印象深刻的一手体验，其中有人称某个 Gemini 模型自动将 GDB 附加到 GPU 驱动上，逆向分析了内核队列的 ioctl 接口，并编写 LD\_PRELOAD C 垫片，让 ROCm 版 llama.cpp 在 Strix Halo 机器上跑通。不少人对 Dario Amodei 提出的 AI“集中化”赢家通吃理论表示反对，认为 AI 能力正分散于超大规模云厂商、新兴云服务商和 ASIC 之间，并建议开发者保持模型与供应商可替换，让智能真正成为商品。也有人批评谷歌习惯提前很久发布模型，并指出 Argon 智能体将谷歌自家 C/C++ 代码迁移到 Rust，证明了 Rust 路线优于此前的 Carbon、Swift 等方案。

**标签**: `#AI frontier`, `#LLM`, `#Google Gemini`, `#AI agents`, `#model release`

---

<a id="item-2"></a>
## [DeepSeek 开源华为昇腾基础组件，对标其英伟达平台栈](https://mp.weixin.qq.com/s/X41mKH4Ds-VXUAnK6M8Eww) ⭐️ 8.0/10

DeepSeek 开源了一套面向华为昇腾平台的基础组件，涵盖 TileLang 高级语言编译工具、计算库以及分布式通信库，与其现有的英伟达平台组件一一对应。此次发布包括 DeepGEMM Ascend、DeepEP Ascend、TileKernels、FlashMLA 和 DeepSelect，DeepSeek 称这些组件在多项测试中性能接近硬件上限，并正与华为推进昇腾 950 的 128 卡超节点方案。 通过把核心训练与推理基础设施从基于 CUDA 的 GPU 迁移到华为昇腾 NPU，DeepSeek 为中国国产 AI 加速器生态提供了一套相对成熟的软件栈，有望降低大模型工作负载对英伟达硬件与软件锁定的依赖。如果性能宣称属实，这将增强昇腾在 AI 算力供应链中的地位，并为其他模型开发者提供一条可规模化部署混合专家（MoE）模型的可行路径。 DeepGEMM Ascend 是一个采用 MIT 许可证的算子库，在面向昇腾 NPU 的同时保持了原 DeepGEMM 的 API 形态，支持 BF16、FP8、FP4 GEMM 以及 MQA logits；DeepEP Ascend 则提供专家并行（EP）的 all-to-all dispatch 与 combine 原语，支持 FP8 dispatch 和延迟 epilogue，服务于 MoE 负载。需要注意的是，该公告本身非常简短，且标注日期为 2026 年 9 月 30 日，相对常见发布节奏显得像是未来日期，因此具体性能数字与昇腾 950 的 128 卡超节点计划应视为厂商宣称，有待独立验证。

telegram · zaihuapd · 9月30日 03:09

**背景**: 华为昇腾 NPU 是中国最主要的国产 GPU 替代方案，但其软件生态长期落后于英伟达的 CUDA 体系，这也是移植成熟库意义重大的原因。TileLang 是一种基于 TVM 编译器基础设施、语法接近 Python 的领域特定语言，让开发者无需手工调优底层代码即可编写 GEMM、FlashAttention 等高性能算子。DeepGEMM 是 DeepSeek 的高性能矩阵乘法库，DeepEP 则是其专注于专家并行（即混合专家模型使用的 all-to-all 令牌路由）的通信库，昇腾版本的目标是在华为硬件上复现这些接口。“超节点”指紧耦合的多 NPU 系统，这里指昇腾 950 世代的 128 卡配置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/deepseek-ai/DeepGEMM-Ascend">GitHub - deepseek-ai/ DeepGEMM - Ascend : DeepGEMM - Ascend ...</a></li>
<li><a href="https://github.com/deepseek-ai/DeepEP-Ascend">GitHub - deepseek-ai/DeepEP-Ascend: A high-performance ...</a></li>
<li><a href="https://github.com/tile-ai/tilelang">GitHub - tile-ai/tilelang: Domain-specific language designed ...</a></li>

</ul>
</details>

**标签**: `#AI compute`, `#Huawei Ascend`, `#DeepSeek`, `#open source`, `#inference optimization`

---

<a id="item-3"></a>
## [Cloudflare 宣布计划成为公共证书颁发机构](https://blog.cloudflare.com/cloudflare-certificate-authority/) ⭐️ 8.0/10

Cloudflare 宣布计划成为公共证书颁发机构，已申请加入 Chrome、Apple、Microsoft 和 Mozilla 的根证书计划，并与 GlobalSign 签署协议以收购一个被广泛信任的根证书。该公司目前尚未开始签发证书，并表示新 CA 将优先支持 ACME 自动签发与续期，目标是在 2027 年第一季度签发生产级默克尔树证书（MTC），以服务后量子互联网。 作为一家重要的互联网基础设施厂商，Cloudflare 进军公共 CA 市场可能打破长期以来由少数商业 CA 主导的集中格局，同时它也有动力推动整个网络的自动化与后量子就绪。由于其证书将默认被 Chrome、Apple、Microsoft 和 Mozilla 的信任库接受，这一举措几乎会影响所有提供 HTTPS 服务的网站。 Cloudflare 并非只依赖自建的新根证书，而是从 GlobalSign 收购一个已受信任的根证书，以缩短被各大浏览器广泛信任的时间；同时计划将 ACME 作为主要的签发和续期方式。默克尔树证书计划仍依赖于一份 IETF 草案，该草案以证书透明度（Certificate Transparency）的方式将证书日志整合进证书本身，用以抵消短生命周期证书与体积庞大的后量子签名带来的开销。

telegram · zaihuapd · 9月30日 06:26

**背景**: 证书颁发机构（CA）负责签发 TLS 证书，让浏览器能够验证网站身份，而根证书则是 X.509 信任链顶端自签名的信任锚点。Google、Apple、Microsoft 和 Mozilla 等浏览器与操作系统厂商各自运营根证书计划，决定哪些根证书默认受信任，因此被这些计划接纳是任何新公共 CA 的前提条件。ACME 协议已被标准化为 RFC 8555，最初为 Let&\#x27;s Encrypt 设计，用于通过 HTTPS 自动化完成证书的签发与续期。默克尔树证书是一种被提议的 X.509 替代格式，旨在让后量子认证变得实用，因为后量子签名算法生成的证书体积远大于当今的算法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/">draft-ietf-plants-merkle-tree-certs-06 - Merkle Tree Certificates</a></li>
<li><a href="https://en.wikipedia.org/wiki/ACME_protocol">ACME protocol</a></li>
<li><a href="https://en.wikipedia.org/wiki/Root_certificate">Root certificate - Wikipedia</a></li>

</ul>
</details>

**标签**: `#PKI`, `#TLS certificates`, `#Cloudflare`, `#post-quantum cryptography`, `#ACME`, `#internet infrastructure`

---

<a id="item-4"></a>
## [Kimi K3 接入 OpenAI Codex 企业通道，中国开源模型首入其付费结算体系](https://36kr.com/newsflashes/4005691489112198) ⭐️ 8.0/10

美国 AI 基础设施公司 Baseten 宣布，企业用户现在可以在 OpenAI 的编程工具 Codex 中使用 Kimi K3，相关调用费用直接计入企业已有的 OpenAI 采购承诺额度，无需走新的供应商接入或采购流程。这使 Kimi K3 成为首个进入 OpenAI 企业付费采购体系的中国开源模型。 这标志着企业 AI 供应链的一次明显变化：采购方可以在不新增供应商、合同或预算科目的情况下使用中国开源模型，因为费用通过既有的 OpenAI 采购额度结算。这降低了非美国前沿模型的采用门槛，也让企业在出于成本或能力考虑更换模型后端时，仍能保持采购集中管理。 Kimi K3 是月之暗面（Moonshot AI）的开源权重模型，拥有 2.8 万亿参数、100 万 token 上下文窗口和原生视觉能力，面向长周期编程与知识工作；Baseten 提供推理托管，并通过兼容 OpenAI 的 API 暴露模型。该消息来自 36kr 的单条快讯，因此结算安排的具体商业条款（如分成比例或费率加价）尚未披露。

telegram · zaihuapd · 9月30日 11:23

**背景**: 月之暗面的 Kimi 系列是开源权重大模型，可通过网页、API 以及 Kimi Code 命令行代理访问，其中 2026 年 7 月发布的 Kimi K3 是迄今规模最大的开源权重模型。OpenAI 的 Codex 是开发者使用的编程代理/工具，而大型企业通常通过预付费或年度采购承诺购买 OpenAI 服务，这些额度需在规定周期内消耗完。Baseten 这类推理平台利用自有 GPU 资源托管第三方模型，并通过兼容 OpenAI 的接口对外提供服务，这正是 Kimi K3 能够被接入既有 OpenAI 企业结算关系的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_%28AI%29">Kimi (AI) - Wikipedia</a></li>
<li><a href="https://www.kimi.ai/ai-models/kimi-k3">Kimi K3: 2.8T Open Model for Coding &amp; Knowledge Work</a></li>
<li><a href="https://docs.baseten.co/overview">Baseten overview - Baseten</a></li>

</ul>
</details>

**标签**: `#AI frontier`, `#enterprise AI procurement`, `#Kimi K3`, `#OpenAI Codex`, `#China AI models`

---

<a id="item-5"></a>
## [Mysteel 对比近五年国庆节前后钢价走势规律](https://news.google.com/rss/articles/CBMiigFBVV95cUxPRFFIazYwN2lqa29aMkR5Mk9YVUdHUjVZRTk5THpxNk8tRWFyNHVjVnhFRUZmVHlMRjFwejJmNHBDNm9xUkhvZjl3MEpNWmxicWJZQ3pCSC1aem83cVJoUzV1WjNfYjRRYlBzc0oyVmdTTjdEMGpmWi1pbFpIWm56bFBfUGh1bkV6V3c?oc=5) ⭐️ 7.0/10

中国领先的钢铁市场数据服务商 Mysteel 发布了一份分析报告，对比了近五年国庆节前后钢价的走势，以梳理其中反复出现的季节性规律。该文由新浪财经转载，总结了钢价在十一假期前以及假期后数周的典型表现。 季节性价格规律对钢铁贸易商、加工企业和分销商具有直接的实操价值，因为他们必须在长假前后安排采购节奏、库存积累和定价决策，而国庆假期会打断生产、物流与交易。了解钢价在节前和节后历史上是涨是跌，有助于这些企业更好地管理风险、开展合同谈判。 该分析属于回溯性的统计梳理，而非对某一具体价格点位的预测，其结论仅基于五年数据，样本窗口较短，未必能覆盖所有市场情形。此外，季节性趋势也可能被宏观政策变化、钢厂产量以及建筑与制造业需求的变化所打破。

rss · Google News - 钢材加工配送 · 9月30日 07:21

**背景**: 中国的国庆假期从 10 月 1 日开始，为期一周，期间许多工厂、建筑工地和物流环节会放缓或暂停，从而暂时压低钢材消费与交易活跃度。Mysteel 是中国被广泛引用的商品市场研究机构，其价格指数和库存数据常被国内钢铁行业用作基准。中国钢价受季节性需求周期、钢厂生产排期、库存水平以及政府政策等多重因素影响，因此贸易商常研究假期前后的价格规律以寻找线索。

**标签**: `#steel prices`, `#steel processing &amp; distribution`, `#market analysis`, `#seasonal trends`, `#China commodities`

---

<a id="item-6"></a>
## [Mysteel 午报：钢价局部上涨，黑色期货普涨](https://news.google.com/rss/articles/CBMiigFBVV95cUxPUjBhYkVUV184OEk3LTJjSUMwNUowMnIydnJnQ1RkOXU1QUN3SGdMdWFyNlZ5Nm9QemplQkN2eVEwQ1hpRlByamdEN2ZEeVNtMDJ2WnlmQjhLNkpQbW5RVFl2eWtZX0ZkeUdDdy1IbGNNN200M2hqLUVMbTZoaGpxcmRINndqSXd0VXc?oc=5) ⭐️ 7.0/10

Mysteel 发布的午间市场报告（经新浪财经转载）指出，钢材现货价格在部分区域市场出现上涨，同时黑色系期货普遍走高。该条目属于例行性的日内行情快照，而非深度分析文章，可获取的摘要中并未给出具体价格点位或涨跌幅。 黑色系期货往往领先于钢材现货价格，因此期货普涨叠加现货局部上调，可能预示短期内钢价存在上行压力，直接影响钢铁加工企业、贸易商与分销商的采购成本、利润空间和库存决策。对需要管理钢材敞口的主体而言，这是一项具体的短期定价参考，而非长期趋势指引。 该报告是每日的、以价格水平为导向的行情更新，缺乏分析深度，且可获取的正文内容未包含各合约报价或分区域明细。对技术型读者而言，应将其仅视为方向性信号——文中所描述的“普涨”（黑色期货）与“局部”（现货）的措辞差异，意味着这是一轮由期货带动的行情，尚未在现货市场得到充分确认。

rss · Google News - 钢材加工配送 · 9月30日 05:34

**背景**: Mysteel（我的钢铁网）是中国领先的大宗商品定价与数据服务机构之一，发布钢铁、金属、能源和农产品市场的价格、新闻与分析。在中国市场语境中，“黑色期货”指在上海期货交易所（SHFE）、大连商品交易所等境内交易所上市的铁系品种，包括螺纹钢、热轧卷板、铁矿石、焦炭和焦煤等。这些合约为中国钢铁供应链提供了主要的发现价格与套期保值场所，因此期货的每日波动会受到加工企业和贸易商的高度关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mysteel.net/">China Steel &amp; Commodities Price and Data Service| Mysteel</a></li>
<li><a href="https://www.shfe.com.cn/eng/">Shanghai Futures Exchange</a></li>
<li><a href="https://www.triland.com/media/qpoliue1/expert_guide_ferrous_derivatives_on_lme.pdf">FERROUS</a></li>

</ul>
</details>

**标签**: `#steel-processing`, `#steel-distribution`, `#commodity-prices`, `#ferrous-futures`, `#market-signal`

---

<a id="item-7"></a>
## [英伟达、谷歌、Meta 等六家公司签署白宫 AI 安全自愿协议](https://news.google.com/rss/articles/CBMiowFBVV95cUxQLTQ2V0h3M2ZSekdDeEJUc3BxQTZtYlZIbTZEbDBiLW1XcGo2V2I1eTFKYlZLSHNrNklWeTNtVXdpMlVlMXUyVDlaSzRBeTc2a3pydGtiLTczV0J4OGlURDBRQ3BLaG94YVdsSlE2SzVDRFpwNnRTSndCTWRhVWk1TG1DdkRnMnZxeGFJblVOS2RpYWxxdFFOVnRIbDZWamNBNTBN?oc=5) ⭐️ 7.0/10

9 月 29 日，美国总统特朗普与谷歌、Anthropic、Meta、OpenAI、xAI 和英伟达六家公司的负责人共同签署了一份一页篇幅的人工智能协议，并将文件发布在 Truth Social 上，称其具有“道义约束力”。该协议要求这六家公司为其 AI 系统建立四层内部控制与监督机制。 尽管这些承诺是自愿性质而非法律强制，但该协议为前沿模型开发者在审计、监督和监控自家系统方面树立了一个公开的治理基准，可能影响整个行业的合规规范、模型发布方式以及对安全评估的预期。它同时强化了美国偏向行业自我监管、而非强制部署前测试的政策取向，这一取向将影响各国监管机构、企业级 AI 使用方以及供应商。 协议要求建立四层控制机制：由外部审计机构对 AI 管控系统进行独立评估、设立董事会独立委员会实施监督，并在模型训练和部署期间围绕网络安全以及生物和化学威胁，监测 AI 的能力与对齐情况，确保各项措施按预期运行。由于文件仅有一页且明确不具法律约束力，其中并未规定执行机制、处罚措施或独立核查要求。

rss · Google News - EDF AI 部署工程 · 9月30日 11:32

**背景**: 人工智能对齐是指引导 AI 系统的行为，使其符合设计者的意图和价值观，通常通过监督微调、基于人类反馈的强化学习等技术来实现。此次协议呼应了拜登政府时期主要 AI 公司做出的自愿安全承诺，当时这些企业同意对系统进行安全测试并报告安全事件。有报道指出，当前白宫倾向于让企业自愿参与而非强制进行模型测试，这份协议因此成为美国 AI 治理整体转向放松监管的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cn.nytimes.com/usa/20260930/ai-trump-meta-microsoft-openai/">特朗普要求人工智能巨头 自 我监管 - 纽约时报中文网</a></li>
<li><a href="https://zh.wikipedia.org/wiki/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E5%AF%B9%E9%BD%90">人工智能对齐 - 维基百科，自由的百科全书</a></li>
<li><a href="https://www.aitntnews.com/newDetail.html?newId=25144">Bloomberg 独家： 白 宫 AI ...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#AI regulation`, `#policy`, `#AI governance`, `#industry news`

---