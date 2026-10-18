---
layout: default
title: "Horizon Summary: 2026-10-18 (ZH)"
date: 2026-10-18
lang: zh
---

> 从 165 条内容中筛选出 6 条重要资讯。

---

1. [DeepSeek 发布 V4.1-Flash-1017，开放权重并提升编码基准成绩](#item-1) ⭐️ 9.0/10
2. [OpenCode Console 遭入侵，约 1.4% 用户的 AI API 密钥外泄](#item-2) ⭐️ 7.0/10
3. [唐山钢坯亏损 200 元，钢价涨跌空间预计有限](#item-3) ⭐️ 7.0/10
4. [微软拟投入 1750 亿美元，Jefferies 称 Azure 或借算力紧缺提价](#item-4) ⭐️ 7.0/10
5. [商务部、科技部拟将人工智能、生物医药、光伏技术增列出口管制目录](#item-5) ⭐️ 7.0/10
6. [Anthropic 力推 AI 安全法案：以 50 人死伤、10 亿美元损失为叫停门槛](#item-6) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [DeepSeek 发布 V4.1-Flash-1017，开放权重并提升编码基准成绩](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) ⭐️ 9.0/10

DeepSeek 于 2026 年 10 月 17 日发布 DeepSeek-V4.1-Flash-1017，同日在官网、移动应用和开发者 API 上线该检查点，并以 MIT 许可证公开模型权重。此次更新宣称在推理、编码、智能体任务和视觉任务上相较 V4.1-Flash 有大幅提升，DeepSWE v1.1 Pass@1 得分达到 77.0，同时 DeepSeek 将其 Search 与 Fetch API 开放给所有开发者，而不再仅限内部使用。 一个接近前沿水平且开放许可的模型直接投入生产，在价格与可及性两方面对闭源实验室形成压力，配套的 API 开放也降低了开发者构建检索增强与智能体应用的门槛。由于 DeepSeek 的发布往往会重塑人们对开放权重模型的预期，这些基准成绩被解读为对 OpenAI、Anthropic 等领先闭源模型的直接挑战。 名称中的“1017”是发布日期编码，延续了 DeepSeek 以日期标记小幅更新的习惯，而非推出全新一代模型；官方自称这是“次要更新”（minor update）却带来“实质性改进”（substantial improvements），这一措辞被评论区读者调侃。其宣称的优势主要体现在基准测试上：DeepSeek 称在 11 项编码基准中有 10 项超过 Sol 5.6，但 Sol 6.1 才是当前最新版本，因此对比对象并非最强基线。

hackernews · theykk · 10月17日 08:21 · [社区讨论](https://news.ycombinator.com/item?id=50129045)

**背景**: DeepSeek 是一家以开放权重方式发布模型而闻名的中国 AI 实验室，开放权重意味着任何人都可以下载并自行运行模型，而不必只通过付费 API 访问。“Flash”指其更轻量、更快速的档位，面向高吞吐的生产场景；V4.1-Flash-1017 这类后缀式版本号则表示对既有模型系列的增量刷新。搜索结果中链接的 OpenRouter 是一个模型市场，用统一 API 聚合了来自不同厂商的数百个模型，很多开发者会通过它来试用该检查点。DeepSWE 这类基准衡量的是模型解决真实软件工程任务的能力，Pass@1 表示第一次尝试即成功的比例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.datastudios.org/post/deepseek-v4-1-flash-1017-open-weights-coding-benchmarks-api-pricing">DeepSeek V4.1 Flash 1017: Open Weights, Benchmarks and API ...</a></li>
<li><a href="https://tech-insider.org/deepseek-v4-1-flash-1017-deepswe-search-api-2026/">DeepSeek V4.1-Flash-1017 Hits 77.0 on DeepSWE [2026]</a></li>
<li><a href="https://openrouter.ai/about">About - The Unified Interface For LLMs | OpenRouter</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论总体积极但观点分化：不少评论者认为 DeepSeek 在实际使用中“感觉”更好，原因是每秒 token 数高、首 token 延迟（TTFT）低，并且思维链可见、不会被莫名其妙的内容审核拦截。也有人对基准宣传持保留态度——一位开发者实测代码审查任务时发现，DeepSeek 花了约 20 分钟才找出一个相关的 P1 问题，而 GPT 5.6 Sol 用 5 分 30 秒找出两个相关问题、GPT 6.1 Sol 用 4 分 30 秒找出三个；另有评论者以此说明多元、多厂商的模型生态为何重要。

**标签**: `#DeepSeek`, `#LLM release`, `#AI frontier`, `#model benchmarks`, `#inference performance`

---

<a id="item-2"></a>
## [OpenCode Console 遭入侵，约 1.4% 用户的 AI API 密钥外泄](https://twitter.com/opencode/status/2111516673953935833) ⭐️ 7.0/10

OpenCode 确认其“OpenCode Console”服务（一个类似 OpenRouter 的模型网关）遭到入侵，约 1.4% 的 Console 用户所存储的 OpenAI、Anthropic 和 Google API 密钥被泄露，受影响账户已收到邮件通知。Anthropic 已撤销部分托管在 Console 上的受影响 Claude 密钥，官方表示目前尚无法确认这些密钥是否被恶意使用。 集中式 AI 网关同时替众多用户保管等同于明文的服务商凭证，因此一次入侵就可能波及 OpenAI、Anthropic 和 Google 账户，这是团队将 AI 接入生产环境时典型的供应链集中风险。该事件明确提醒人们：在设计 AI 服务的威胁模型时，不仅要考虑模型厂商本身，还必须把第三方密钥托管方纳入考量。 此次泄露仅限于 Console 服务，不影响开源 OpenCode 编程智能体的使用者，但团队因未清晰区分二者而受到批评。OpenCode 建议受影响用户在各厂商后台吊销并重新签发密钥、检查 10 月 17 日以来的用量并设置支出上限；评论者则主张每个密钥系统都应提供 \`invalidate\_api\_key\` 端点，让泄露的凭证能够被集中作废，而不是让每个用户各自处理。

hackernews · pranshuchittora · 10月17日 18:01 · [社区讨论](https://news.ycombinator.com/item?id=50133401)

**背景**: OpenCode 是一个开源的 AI 编程智能体，属于命令行风格的工具，开发者将其指向某个模型服务商来编写和修改代码。OpenCode Console 则是一个独立且使用范围小得多的托管服务，扮演模型网关的角色：用户把 OpenAI、Anthropic 或 Google 的 API 密钥存放在其中，Console 便可把请求路由到多个服务商，原理类似 OpenRouter。由于这些密钥等于对付费 API 的可计费访问权限，泄露的凭证在被轮换之前可能被用于产生高额推理费用，这也是 Anthropic 等厂商能够单方面吊销密钥的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opencode.ai/">OpenCode | The open source AI coding agent</a></li>
<li><a href="https://opencode.ai/docs/providers/">Using any LLM provider in OpenCode .</a></li>
<li><a href="https://oneuptime.com/blog/post/2026-02-20-api-key-management-best-practices/view">API Key Management Best Practices for Secure Services</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者首先致力于澄清事件范围，强调“OpenCode Console”并非 OpenCode 编程智能体，混乱的命名让人误以为影响面远大于实际。另一些人呼吁建立标准的 \`invalidate\_api\_key\` 端点，避免泄露后陷入与时间赛跑的被动局面；还有人对自己存放在后端服务器上的 API 密钥感到不安，担心存在供应链攻击风险。发帖人还提到该帖被 OpenCode 的支持者举报，暗示披露过程存在摩擦。

**标签**: `#security-incident`, `#api-key-management`, `#ai-infrastructure`, `#credential-leak`, `#supply-chain-risk`

---

<a id="item-3"></a>
## [唐山钢坯亏损 200 元，钢价涨跌空间预计有限](https://news.google.com/rss/articles/CBMiaEFVX3lxTE5ObV9aQ2VkSThhM2dQbFFFYUtETVJMb0Z1WmE0bnJTaG1sSmVweWZUVjQ3RlJtMzFnSXVZWndEQmZURzlESWFpQkhWajd2Z3ZILXRUMnVLd0E2Zl9Gc0c4R05wOVpoQkx6?oc=5) ⭐️ 7.0/10

我的钢铁发布的每日钢市快讯显示，唐山地区钢坯生产企业的吨钢亏损约为 200 元，并判断短期内钢价上涨和下跌的空间都不大。 唐山是中国最大的钢铁生产城市，当地钢坯环节出现亏损，对整个螺纹钢及长材产业链是一个预警信号：若亏损持续，钢厂通常会减产，进而反向影响铁矿石、焦炭和废钢的需求，以及钢材贸易商与分销商的定价。 该内容属于每日钢市短讯而非完整分析，因此未给出唐山钢坯的具体报价、评估的准确日期，也未说明这 200 元亏损是按完全成本还是现金成本口径计算；而“涨跌空间不大”的判断意味着市场预期价格将维持窄幅震荡，而非明显反弹。

rss · Google News - 钢材加工配送 · 10月17日 04:16

**背景**: 钢坯是一种半成品：铁水或废钢经连铸成方形或矩形坯料，属于炼钢的第二阶段产品，之后还需再轧制成螺纹钢、线材等成品。河北唐山是中国钢铁工业的核心产区，2025 年其粗钢产量约占全国总产量的 11.4%。钢厂利润通常以产品售价与铁矿石、焦煤、废钢等原料成本之间的价差来衡量，因此像“吨钢亏损 200 元”这样的具体数字被视为观察行业景气度的重要指标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.montriam.com/en-gb/insights/what-is-steel-billet">What Is Steel Billet ? - Montriam</a></li>
<li><a href="https://baike.baidu.com/en/item/Tangshan+Steel+Industry/6700678">Tangshan Steel Industry_Baiduwiki - 百度百科</a></li>
<li><a href="https://www.spglobal.com/commodity-insights/en/pricing-benchmarks/our-methodology/subscriber-notes/070317-platts-analytics-updates-china-steel-mill-margins">SUBSCRIBER NOTE: Platts Analytics updates China Steel Mill Margins</a></li>

</ul>
</details>

**标签**: `#steel market`, `#billet pricing`, `#margins`, `#China steel`, `#steel distribution`

---

<a id="item-4"></a>
## [微软拟投入 1750 亿美元，Jefferies 称 Azure 或借算力紧缺提价](https://news.google.com/rss/articles/CBMivgFBVV95cUxOb1VrRHgzNnAybDNwbTF5Z082cUcybkgzQVJLUjdYRUNhbVpvWk8wUzBHRUpNUC1ObzlOWEhSZ2RhY3FHU3Q3WkZJc08waUxsb2Ezb0FnWmlkTDRMQ0pGSlpPSl9EQmFiem85R3RlM3lzemhGdnJnbTFnWV85VndCSXRGYkM5REtYVnNlOXR0QUhMTjZ4SHpHWk5QSFBXemRlTURvU2tLam1ENGlqSC1pZXBQcGROSmUwMjBWMUNn?oc=5) ⭐️ 7.0/10

有报道称微软正准备投入约 1750 亿美元用于 AI 相关投资，同时 Jefferies 认为 AI 算力供需失衡可能让 Azure 得以继续提高价格。这一消息出现的背景是市场正担忧 AI 资本开支过热。 如果算力持续紧缺，微软等超大规模云厂商就能在 AI 负载上获得定价权，从而把云计算的讨论焦点从“资本开支是否合理”转向“谁能拿到回报”。这会直接影响采购 Azure AI 容量的企业、与之竞争的云厂商，以及判断 AI 建设能否回本的投资者。 1750 亿美元这一数字来自标题层面的报道，并未披露其在数据中心、芯片和模型研发之间的具体分配，而 Jefferies 的定价权判断属于分析师观点，并非微软已确认的提价计划。Azure 若涨价，将叠加在 Azure OpenAI 等按用量计费的服务之上，而客户本就对 token 成本十分敏感。

rss · Google News - AI 前沿 · 10月17日 10:50

**背景**: 超大规模云厂商通过采购 GPU、土地和数据中心电力来建设 AI 算力，这类支出记为资本开支（capex）。近期 AI 需求已超过供给，分析人士指出，在供给受限的市场中，定价权会流向掌握先进芯片、电力、数据中心空间等稀缺资源的一方。Azure 还转售 OpenAI 模型并提供微软自研的 Phi 系列模型，因此基础设施与模型调用都会向客户计费。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://am.jpmorgan.com/us/en/asset-management/adv/insights/market-insights/market-updates/on-the-minds-of-investors/is-ai-running-out-of-compute/">Is AI running out of compute? | J.P. Morgan Asset Management</a></li>
<li><a href="https://www.techtimes.com/articles/322868/20260803/street-got-cloud-capex-wrong-morgan-stanleys-14t-math-after-hyperscaler-earnings.htm">Street Got Cloud Capex Wrong: Morgan Stanley&#x27;s $1.4T Math After...</a></li>
<li><a href="https://aipricing.org/brands/microsoft">Microsoft AI Pricing 2026 | Azure OpenAI, Phi &amp; Models</a></li>

</ul>
</details>

**标签**: `#AI compute`, `#Microsoft Azure`, `#cloud capex`, `#AI infrastructure`, `#pricing power`

---

<a id="item-5"></a>
## [商务部、科技部拟将人工智能、生物医药、光伏技术增列出口管制目录](https://news.google.com/rss/articles/CBMickFVX3lxTFBxSkFkMHk4UElBUlluNWxTUkNMT1BHM3JKeVdBNnFxVUktVUxUNk5JdTRQeDZQdTRISkJGTkNFVTdKQ282YTl3Y0p2MjV0aExuNEdWVlpvdGxsZXkzVjNEeW5Tb09kdS1mTUZxeDA2UkMxdw?oc=5) ⭐️ 7.0/10

中国商务部与科技部公布了《中国禁止出口限制出口技术目录》的修订草案，拟新增人工智能、生物医药和光伏等领域的相关技术条目，据报道涉及约 40 项技术。该草案目前处于公开征求意见阶段，之后才会定稿并正式生效。 出口管制目录的调整是一项直接的法律杠杆：相关技术一旦被列入，向境外转移该技术——无论是通过许可授权、合资、海外研发中心还是人员流动——都可能需要政府许可，甚至被完全禁止。将人工智能和生物医药纳入其中，表明北京正在构建应对美国半导体与人工智能出口限制的对等工具，这将提高在中国设有工程团队或供应链的跨国企业的合规与供应商风险。 该目录分为两部分：一部分是任何情况下都禁止出口的较短清单，另一部分是出口需获商务部许可的限制类技术清单；草案尚未明确说明哪些具体的人工智能技术（例如模型架构、训练方法或数据处理诀窍）归入哪一档。由于报道只有标题、未披露具体范围与时间表，企业应关注最终文本和征求意见期，而非公告本身。

rss · Google News - AI 前沿 · 10月17日 09:52

**背景**: 中国对技术出口的管制采用目录清单制度，而非单一的综合立法，列出被禁止出境或需许可才能向境外转移的各类技术诀窍。该目录始于 2001 年，此后不定期修订，最显著的两次是 2008 年和 2020 年，历史上主要集中在稀土加工、中医药和农业育种等领域。将某项技术列入目录与管制实体货物在法律上是两回事：前者针对的是技术诀窍的转移——通过文件、专利、技术服务或人员流动——而非硬件发货。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cset.georgetown.edu/publication/china-export-control-catalog-july-2025/">Chinese Catalogue of Technologies Prohibited or Restricted from ...</a></li>
<li><a href="https://www.chinajusticeobserver.com/a/what-technologies-are-prohibited-or-restricted-from-import-or-export-in-china">What Technologies Are Prohibited or ... - China Justice Observer</a></li>
<li><a href="https://www.registrationchina.com/articles/china-revised-export-technologies/">China revised the Catalogue Technologies Prohibited or Restricted ...</a></li>

</ul>
</details>

**标签**: `#export-controls`, `#AI-policy`, `#China-regulation`, `#supply-chain`, `#tech-governance`

---

<a id="item-6"></a>
## [Anthropic 力推 AI 安全法案：以 50 人死伤、10 亿美元损失为叫停门槛](https://news.google.com/rss/articles/CBMiV0FVX3lxTE5sSUMyTzJQRVNfUTRyMWpBS3k2VHZMZVNjQ2lKa3ItbEpNWVBieTNZZ0RZNjJkUGFad0tWN3ZCbTBvaFVCZi10Rmxtdy1janh2QzhsbUk3QQ?oc=5) ⭐️ 7.0/10

据报道，Anthropic 起草了一份保密的 AI 安全法案并已向美国国会议员推介：一旦某起事件造成超过 10 亿美元损失，或导致超过 50 人死亡或重伤，政府便可暂停或下架相关 AI 模型。低于该门槛时，法案不赋予联邦政府采取行动的依据，且任何模型暂停都需获得法院批准。 这一举动的重要信号在于：一家头部前沿实验室正主动参与塑造 AI 监管，而不仅是被动应对；而明确的数字门槛也为立法者提供了“灾难性风险”法定阈值的范本。由于该法案既授权召回模型，又明确限制门槛以下的联邦权力，它将直接影响在美国运营的 AI 实验室的合规义务、部署工程与竞争定位。 据报道，该草案设置了两条并列触发条件——损失超过 10 亿美元，或超过 50 人死亡或重伤——并要求政府在暂停模型前取得法院批准，这实际上为联邦干预设定了上限并使其程序化。该文本被描述为在国会内部传阅的保密草案，因此在正式提出前门槛数值仍可能调整。

rss · Google News - EDF AI 部署工程 · 10月17日 00:42

**背景**: 随着前沿模型能力增强，要求出台 AI 安全立法的呼声不断上升，但现有规则大多聚焦于事件报告而非关停权限。例如欧盟《人工智能法案》第 73 条要求高风险系统的提供者在 15 天内向国家主管机构报告严重事件，但并未设定以金额或伤亡人数为基准的模型下架触发条件。美国目前没有与之对应的、具有约束力的跨行业制度，因此一部界定政府何时可以叫停模型的法律将是一种全新机制。Claude 系列模型的开发商 Anthropic 一直以“重视安全”自我定位，这份草案正是试图把自己偏好的机制写入法律。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tech-insider.org/anthropic-ai-safety-bill-lawmakers-2026/">Anthropic Pitches $1B AI Safety Bill to Lawmakers</a></li>
<li><a href="https://interestingengineering.com/ai-robotics/anthropic-confidential-congress-draft-bill">Anthropic&#x27;s confidential bill limits federal power to halt models</a></li>
<li><a href="https://shattered.io/anthropic-ai-safety-bill-congress-2026/">Anthropic Pitches Congress a $1B AI Safety Bill - shattered.io</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#AI safety`, `#Anthropic`, `#AI governance`, `#model risk`

---