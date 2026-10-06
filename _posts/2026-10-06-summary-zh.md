---
layout: default
title: "Horizon Summary: 2026-10-06 (ZH)"
date: 2026-10-06
lang: zh
---

> 从 140 条内容中筛选出 8 条重要资讯。

---

1. [vLLM v0.31.0 发布：DeepSeek-V4.1-Flash 内核、SM100 默认配置与权重预载守护进程](#item-1) ⭐️ 8.0/10
2. [Reflection 发布 Beam：501B 开放权重 MoE 模型](#item-2) ⭐️ 8.0/10
3. [高通获得华为 LogicFolding 芯片封装技术专利许可](#item-3) ⭐️ 8.0/10
4. [OpenAI 据悉洽谈租赁俄亥俄州 10 吉瓦数据中心](#item-4) ⭐️ 8.0/10
5. [10 月建筑钢材供需博弈加大 钢价承压运行](#item-5) ⭐️ 7.0/10
6. [中国钢材季报：供需双弱延续，库存结构出现分化](#item-6) ⭐️ 7.0/10
7. [LNG Canada 基蒂马特 330 亿加元扩建因采购中国钢材遭批评](#item-7) ⭐️ 7.0/10
8. [贝莱德与多家阿联酋基金洽谈参与 OpenAI 约 300 亿美元融资](#item-8) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [vLLM v0.31.0 发布：DeepSeek-V4.1-Flash 内核、SM100 默认配置与权重预载守护进程](https://github.com/vllm-project/vllm/releases/tag/v0.31.0) ⭐️ 8.0/10

vLLM 发布了 v0.31.0，该版本包含来自 307 位贡献者（其中 96 位是新贡献者）的 717 个提交，重点是 DeepSeek-V4.1-Flash 的性能优化：带 V4.1 NVFP4 压缩 KV 缓存的 FlashMLA mega attention 现已成为 SM100 上的默认实现，同时还加入了 DeepGEMM 稀疏 MQA logits，以及将 TP all-reduce、mHC 输入准备和 MoE finalize 融合在一起的解码器边界内核。该版本还引入了新的 \`vllm preload\` CLI，用于运行权重缓存守护进程，使量化后的权重在引擎重启之间常驻 GPU 显存；此外还包括 Model Runner V2 上的投机解码、MoonEP all2all 后端以及若干破坏性变更。 vLLM 是目前使用最广泛的开源大模型推理与服务引擎之一，因此这些吞吐、延迟和冷启动方面的改进会直接进入生产部署，尤其是对在 Nvidia SM100/SM103（Blackwell）硬件上运行 DeepSeek 级 MoE 模型的团队而言。\`vllm preload\` 守护进程和基于 CRIU 的引擎快照针对的是重启缓慢这一运维痛点，而破坏性变更（例如移除 \`tokenizer\_mode=&quot;slow&quot;\`、用 \`fp8\_per\_tensor\` 简写替代 \`quantization=&quot;fp8&quot;\`）则意味着运维人员升级前必须检查现有配置。 该版本包含多项值得关注的技术细节：在 SM100/SM103 上融合了逆 RoPE 与 MXFP8 量化的小批量 WO-A 内核、与序列并行 reduce-scatter 融合的 MXFP8 \`wo\_b\` GEMM、跨 TP rank 分片的 Engram \`wkv\`、为视觉塔引入的 encoder CUDA graphs，以及将滑动窗口 KV 排除在前缀缓存之外的 SWA 有界重放。基于 CRIU 的 \`vllm snapshot create/restore\` 功能仍属实验性质，且只能恢复已完全初始化的 TP1 引擎；新的 \`vllm preload\` 守护进程目前支持数据并行、MTP 草稿模型、\`/health\` 端点以及就绪等待。

github · khluu · 10月5日 06:44

**背景**: vLLM 是一个用于服务大语言模型的开源引擎，以 PagedAttention 风格的 KV 缓存管理和高吞吐的连续批处理著称。FlashMLA 是 DeepSeek 为其 MLA（多头潜在注意力）架构优化的注意力内核库，DeepGEMM 则是 DeepSeek 的统一高性能张量核心内核库，覆盖 FP8、FP4 和 BF16 的 GEMM 运算；本次发布将二者更深度地集成为 SM100 上的默认实现。“SM100/SM103”是 Nvidia Blackwell 数据中心 GPU 的流式多处理器架构代号，而 TP（张量并行）、EP（专家并行）、MoE（混合专家）和 MTP（多 token 预测）等术语则描述了高效运行超大模型所需的并行与解码策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/deepseek-ai/FlashMLA">GitHub - deepseek-ai/ FlashMLA : FlashMLA : Efficient Multi-head...</a></li>
<li><a href="https://github.com/deepseek-ai/DeepGEMM">GitHub - deepseek-ai/ DeepGEMM : DeepGEMM : clean and efficient...</a></li>

</ul>
</details>

**标签**: `#vllm`, `#llm-inference`, `#inference-optimization`, `#mlops`, `#model-serving`

---

<a id="item-2"></a>
## [Reflection 发布 Beam：501B 开放权重 MoE 模型](https://reflection.ai/blog/introducing-beam) ⭐️ 8.0/10

Reflection 正式发布 Beam，这是一个总参数量 5010 亿、激活参数量 230 亿的稀疏混合专家（MoE）开放权重模型，在 23.8 万亿经过筛选的高质量 token 上预训练，并进一步通过强化学习针对编程、推理和 agentic 工作负载进行调优。官方称 Beam 在同等规模的开源基础模型中达到或超过现有水平，该发布在 Hacker News 上引发热议（323 分、92 条评论）。 Beam 为开放权重阵营再添一个接近前沿规模的成员，让开发者和企业可以下载、自托管并微调 501B 级别的模型，而不必只依赖闭源 API。这也进一步加剧了开放权重领域的竞争——近期中国实验室在该赛道节奏领先，而独立第三方评测仍是目前最关键的缺口。 根据 Hacker News 评论者贴出的对比表，Beam 在 prefill 与 decode 阶段的激活参数均为 230 亿，而 DeepSeek V4.1 Flash 分别为 80 亿和 160 亿——不过后者据称带有 1960 亿 N-gram/PLE 参数，且预训练 token 量更大。值得注意的一处出入是：官方博客称预训练用了 23.8 万亿 token，而该评论者的表格写的是 28 万亿；此外官方用来支撑泛化能力的是一项数天前才出现的空间拼图测试（正确率 95.5%），因此独立评测结果仍有待公布。

hackernews · Philpax · 10月5日 19:16 · [社区讨论](https://news.ycombinator.com/item?id=49969183)

**背景**: 开放权重（open-weight）指模型训练完成后的权重被公开发布，任何人都可以下载、运行、检查或微调，但这并不代表训练数据、源代码或完整训练配方也一并公开。稀疏混合专家（MoE）架构在每个 token 上只激活一部分参数，因此即使总参数量非常庞大，推理成本依然可控——Beam 的 5010 亿总参数中每次前向计算只用到约 230 亿。它瞄准的 “agentic” 工作负载指的是 AI 系统能够接受一个目标、拆解成多个步骤、调用工具并在较少人工干预下完成任务，而不是只回答单个提问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mahaai.co.in/glossary/open-weight-model/">Open - Weight Model — Meaning &amp; Definition | Maha AI Glossary</a></li>
<li><a href="https://getmorefromai.com/glossary/agentic-ai">Agentic AI : Definition , Examples, and Why It Matters | GetMoreFromAI</a></li>
<li><a href="https://www.linkedin.com/posts/in-simple-terms-with-satish_what-is-an-open-weight-ai-model-open-weights-activity-7487542745708814336-8tqk">Open - Weight AI Models Explained | In Simple Terms with... | LinkedIn</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的讨论整体乐见更多开放权重模型出现，但分析相当犀利：有评论者专门列出 Beam 与 DeepSeek V4.1 Flash 在参数量与 token 量上的对比表；也有人认为 Beam“更大却仍不如更小的中国免费模型”，并担忧世界只剩中美两个模型来源的风险；还有人对官方用几天前才出现的拼图实验来论证泛化能力的做法提出质疑。

**标签**: `#open-weight-models`, `#mixture-of-experts`, `#llm`, `#ai-frontier`, `#agentic-ai`

---

<a id="item-3"></a>
## [高通获得华为 LogicFolding 芯片封装技术专利许可](https://www.bloomberg.com/news/articles/2026-10-05/qualcomm-licenses-patents-on-huawei-s-logicfolding-chip-tech) ⭐️ 8.0/10

华为与高通宣布达成一项为期多年、范围广泛的专利交叉许可协议，覆盖 5G、计算、人工智能和网络等领域；高通还同意获得华为 LogicFolding 芯片制造技术相关专利的许可，并将购买华为部分美国专利，交易尚待必要监管批准。华为表示，交易完成后其专利许可协议的累计预期合同价值预计超过 69 亿美元。 这标志着技术转移方向的显著反转：如今是中国企业向美国领先芯片厂商提供先进半导体封装知识产权，而非相反。这也凸显出先进封装（而不仅是光刻）已成为决定 AI 算力性能的关键战场，使华为在中美科技竞争中获得了商业筹码。 LogicFolding 并非传统的块级 3D 封装，而是一种粒度更细的方案，将逻辑电路分布到面对面键合的两层逻辑之上；据报道华为计划在 2026 年秋季推出采用该技术的麒麟芯片，并声称基于 Tau Scaling 的高端芯片到 2031 年前后可达相当于 1.4nm 节点的性能水平。该交易仍需获得监管批准，而且其与华为被列入美国实体清单的关系尚不明确。

hackernews · 0xedb · 10月5日 07:46 · [社区讨论](https://news.ycombinator.com/item?id=49961861)

**背景**: 先进封装通过把多个裸片或逻辑层堆叠成一颗芯片来提升性能，从而无需依赖晶体管微缩，这一路线在传统摩尔定律放缓后变得至关重要。华为将其封装路线命名为“Tau Scaling（涛定律）”，LogicFolding 是其芯片层面的实现方式——把两层逻辑面对面键合，使信号传输距离更短，据报道还能降低发热。华为自 2019 年起被列入美国实体清单，该清单通常限制美国企业向其出售技术，因此美国公司反过来向华为支付专利许可费属于罕见安排，而专利交叉许可规则似乎为此留出了空间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://insightsintegration.com/logic-folding-explained-huaweis-chip-packaging-breakthrough-that-could-redefine-the-ai-race/">Logic Folding Explained: Huawei&#x27;s Chip Packaging Breakthrough...</a></li>
<li><a href="https://www.kad8.com/hardware/huawei-tau-scaling-v2-explained-is-the-semiconductor-industry-entering-the-tau-era/">Huawei Tau Scaling V2 Explained: Is the Semiconductor Industry...</a></li>
<li><a href="https://locsic.com/thinking/3d-stacking-chip-evolution/">From CoWoS to Tau Scaling: 3D Stacked Chips , Technology ...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者主要关注两点：在华为处于实体清单的情况下，高通为何仍能达成此类交易这一法律难题，以及华为从美国芯片厂商处获得净许可收入这一象征性转变。也有人称赞 LogicFolding 的巧妙之处，指出层内信号路径更短带来的散热优势；同时不少人质疑此前 5G 主导权之争的讽刺意味，并好奇爱立信是否会作出回应。

**标签**: `#semiconductors`, `#huawei`, `#qualcomm`, `#geopolitics`, `#chip-packaging`

---

<a id="item-4"></a>
## [OpenAI 据悉洽谈租赁俄亥俄州 10 吉瓦数据中心](https://news.google.com/rss/articles/CBMiSEFVX3lxTFBrdHpIekxCYlpaeVc0Y3pndTJtVFkwaVlDWDdYVnlfR2t5YW4tWnRrQXlpVU5kUWdrc3prSmtwQmJQZ3E3UWgxeA?oc=5) ⭐️ 8.0/10

据财联社报道，OpenAI 正在洽谈租赁位于俄亥俄州的一座总容量达 10 吉瓦（GW）的数据中心园区。报道未披露开发方身份、具体选址、租赁金额与建设时间表，OpenAI 方面也尚未公开确认这一洽谈。 单一 10 吉瓦的租赁规模将远超目前已知的任何 AI 数据中心交易，意味着行业算力军备竞赛出现量级跃升，也把前沿模型的野心直接与电力采购和电网建设绑定在一起。这还会加剧外界对电力供应、居民电价与输电容量能否支撑这类园区的担忧，其影响将波及公用事业公司、芯片厂商以及其他 AI 实验室。 作为参照，10 吉瓦大致相当于十座大型核反应堆的出力，也是美国数据中心总用电需求中相当可观的一部分，因此这一规模的园区需要多年分期建设、重大电网接入审批，甚至可能需要自建发电设施。该消息目前属于单一信源的传闻，缺乏技术细节，因此这一数字、租赁结构，以及它代表的是已签约容量还是长期选择权，都应视为尚未证实。

rss · Google News - AI 前沿 · 10月5日 22:55

**背景**: 吉瓦是功率单位，1 吉瓦等于 1000 兆瓦；而 AI 训练集群以往通常只有数十兆瓦到一百多兆瓦，这正是 10 吉瓦这一数字格外引人注目的原因。俄亥俄州，尤其是哥伦布与纽奥尔巴尼一带，因土地便宜、税收优惠和电力基础设施不断扩充，已成为美国重要的数据中心聚集地，吸引了众多超大规模云厂商设厂。这一报道也契合当前的整体竞赛背景：OpenAI、微软、谷歌、亚马逊和 Meta 都在争抢用于 AI 训练的土地、电力与芯片，此前宣布的 Stargate 合资项目同样瞄准多吉瓦级的 AI 算力。

**标签**: `#AI compute`, `#data centers`, `#OpenAI`, `#infrastructure capex`, `#energy demand`

---

<a id="item-5"></a>
## [10 月建筑钢材供需博弈加大 钢价承压运行](https://news.google.com/rss/articles/CBMia0FVX3lxTFBqVUlXR0x0Zjd2eFN4YUN1OGpPQ011QjNueEtBTG1SY0N1MkEzYS16eU1qTDIxcXdveUo1T1pmMFp6SFh3RTkwVWMzVkJLZnVvNlBQZXdVSWt3M2oyeUZzTEZORnZLQXQ5QjlF?oc=5) ⭐️ 7.0/10

财富号发布的一篇市场评论预计，10 月份中国建筑钢材市场的供需博弈将有所加大，钢价将承压运行。该观点将 10 月定位为钢厂供给与下游采购之间分歧加剧的阶段，而非单边行情。 建筑钢材是中国房地产与基建活动的重要风向标，因此 10 月价格走弱的预期会直接影响贸易商、加工配送企业和下游施工方的采购节奏、合同定价与库存水平。对于采购和备货方而言，这一信号倾向于谨慎下单，而不是在预期价格下跌前加大库存。 该条目本质上只是一个方向性判断的标题式观点：文中没有给出产量、库存或价格的具体数据，因此只反映方向而非幅度。同时内容来自财富号这一自媒体内容平台，而非官方统计发布或交易所报告，应被视为市场评论，并需与硬数据相互印证。

rss · Google News - 钢材加工配送 · 10月5日 11:53

**背景**: 在中国，“建筑钢材”主要指螺纹钢和线材，其需求主要来自房地产施工和基础设施建设。其价格受钢厂产量、房地产与基建的下游需求、社会库存与厂内库存，以及限产、环保等政策因素共同影响。财富号是东方财富旗下的自媒体专栏平台，分析师和交易者会在上面发布市场观点。10 月通常是从秋季施工旺季向年底过渡的时段，天气、资金状况和政策预期都可能使需求快速变化。

**标签**: `#steel-prices`, `#construction-steel`, `#supply-demand`, `#steel-distribution`, `#china-market`

---

<a id="item-6"></a>
## [中国钢材季报：供需双弱延续，库存结构出现分化](https://news.google.com/rss/articles/CBMiXkFVX3lxTE9fN251TElncUlyQUwzd25Vd1F4YTdwOWFrTDRjanVUQmJRdnRiT3QxV2hWZ3p3UVRsZVczWFNCdlJOYWY0VkpFSXRlTE15eHc0SVpTVTlOTzFNWmpXbkE?oc=5) ⭐️ 7.0/10

中国金融数据平台同花顺发布的钢材季报显示，中国钢材市场供需两端继续双双走弱，同时不同市场环节的库存水平出现分化走势。这一标题表明，产量与消费同步收缩并未带来单一、统一的库存变化趋势。 钢材是建筑、基建、机械和制造业的核心原材料，因此供需持续双弱是观察中国工业活动与房地产行业状况的重要风向标。库存结构分化对钢贸商、分销商和下游加工企业尤为关键，因为它意味着库存风险和价格压力在产业链上分布不均，而非全面一致。 该条目仅为同花顺季报的标题，未附带正文、数据或统计方法，因此无法从来源确认具体的产量、消费量或库存量。关键的定性结论在于两点信号的叠加：供需双弱态势延续，以及库存呈现分化而非同步的变化格局。

rss · Google News - 钢材加工配送 · 10月5日 05:59

**背景**: 在中国钢铁行业中，“供需双弱”通常指钢厂减产或控制产量，同时下游消费（主要来自房地产建设、基建项目和制造业）也表现低迷的市场状态。“库存结构分化”一般指不同类别库存走势不一，例如钢厂库存与贸易商（社会）库存的差异，或螺纹钢、线材、热轧卷板等不同品种之间的差异。此类季报会汇总产量、表观消费量、库存和价格等数据，对行业供需平衡给出阶段性判断。同花顺是中国广泛使用的金融信息与行情数据平台，会发布此类市场综述。

**标签**: `#steel`, `#supply-demand`, `#inventory`, `#commodities`, `#steel-distribution`

---

<a id="item-7"></a>
## [LNG Canada 基蒂马特 330 亿加元扩建因采购中国钢材遭批评](https://news.google.com/rss/articles/CBMiXkFVX3lxTE1Ea3JBSk1Bbk0wcTdyWXpCN0Q1dXRfUlRIcC0wQUNlRmEzQzMzUUdYc2hMTjl0VzM2SjdNbTFBYS1YVk94eXREUzJPc01wcHJfckpaa0o1WjhwY2tXamc?oc=5) ⭐️ 7.0/10

LNG Canada 表示，由于加拿大本土供应商无法制造项目所需的部件，其位于不列颠哥伦比亚省基蒂马特、总投资 330 亿加元的 LNG 终端二期扩建工程将再次采购中国钢材。此举在渥太华推行“购买加拿大货”采购政策的背景下引发批评，不过该项目已为管道网络扩建设定了 70%的加拿大钢材目标。 这一事件凸显了加拿大推动本土采购与重型模块制造产能主要集中在亚洲这一现实之间的矛盾，同时也意味着一个重大能源基础设施项目将带来具体而大规模的钢材需求。此外，它还牵涉到加中之间围绕钢材等产品持续发酵的贸易争端，该争端已被提交至世界贸易组织。 据 CBC 报道，中国钢材主要用于大型预制模块，而非整个项目，LNG Canada 称加拿大供应商根本无法生产所需部件。扩建项目中的管道部分设定了 70%的加拿大钢材目标，因此不同工程范围的采购结构并不相同。

rss · Google News - 钢材加工配送 · 10月5日 16:26

**背景**: LNG Canada 是由壳牌牵头，并包含马来西亚国家石油公司、中国石油、三菱商事和韩国天然气公司的合资企业，正在不列颠哥伦比亚省基蒂马特建设一座液化天然气出口终端。LNG 出口终端需将天然气冷却至约零下 162 摄氏度使其液化，体积缩小约 600 倍，从而能够通过运输船运往亚洲市场。此类规模的项目通常由在低成本船厂和海外场地（常常是中国）制造的大型预制模块组装而成，再通过海运运抵工地，这也是钢材采购会成为政治敏感话题的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cbc.ca/news/politics/lng-expansion-chinese-steel-9.7366745">LNG Canada to use Chinese steel on $33B expansion project in...</a></li>
<li><a href="https://en.wikipedia.org/wiki/LNG_Canada">LNG Canada - Wikipedia</a></li>
<li><a href="https://www.hashtaginvesting.com/blog/lng-canadas-33b-expansion-will-use-chinese-steel-despite-ottawas-buy-canadian-push">LNG Canada ’s $33B Expansion Will Use Chinese Steel Despite...</a></li>

</ul>
</details>

**标签**: `#steel procurement`, `#supply chain`, `#LNG Canada`, `#trade policy`, `#energy infrastructure`

---

<a id="item-8"></a>
## [贝莱德与多家阿联酋基金洽谈参与 OpenAI 约 300 亿美元融资](https://news.google.com/rss/articles/CBMiZkFVX3lxTE5NYy1YSHJDUkc3MDJSNEthRlcxLUtXOURjWGllZDlFMVF2TGhVdjFTLXdYelBfR0hMaUVwcjRYWVZ3MUNVMHNlcWRHTDZMTm1LcndwdWkxdm85RXo3cEdqcEZJeEVEdw?oc=5) ⭐️ 7.0/10

据报道，贝莱德（BlackRock）以及多家阿联酋投资基金正在洽谈参与 OpenAI 最新一轮融资，该轮融资规模约为 300 亿美元。TradingView 的报道未披露具体条款、各家出资额度或最终承诺情况。 若消息属实，这将意味着全球最大的资产管理机构与海湾地区主权背景的资本直接站到了领先的前沿 AI 实验室背后，进一步印证 AI 算力与模型研发正越来越多地由机构资金和国家关联资本提供融资。这也是一个明确信号，说明大体量资本看好该领域的长期回报，同时加深了美国 AI 实验室与海湾基金之间的资金联系。 该报道仍停留在消息层面：约 300 亿美元的数字以及潜在参与者名单均来自未具名消息源，OpenAI、贝莱德和阿联酋相关基金都没有公开确认这一洽谈。如果最终以该规模完成，这轮融资将成为有史以来针对单一公司规模最大的私募融资之一。

rss · Google News - EDF AI 部署工程 · 10月5日 09:02

**背景**: OpenAI 是 ChatGPT 和 GPT 系列大语言模型的开发者，其昂贵的模型训练与算力需求历来依靠由微软等全球机构参与的超大规模私募融资来支撑。贝莱德是全球最大的资产管理公司，主要代表养老金和机构客户管理资金。阿联酋的多家机构（包括与阿布扎比相关的投资集团）一直在构建以 AI 为重点的投资组合，被视为该行业日益重要的资金来源。所谓“一轮融资”，是指公司在上市之前由私人投资者认购其股权的阶段。

**标签**: `#AI frontier`, `#OpenAI`, `#funding`, `#sovereign wealth funds`, `#capital markets`

---