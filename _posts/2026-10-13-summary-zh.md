---
layout: default
title: "Horizon Summary: 2026-10-13 (ZH)"
date: 2026-10-13
lang: zh
---

> 从 189 条内容中筛选出 7 条重要资讯。

---

1. [黑客通过 Danfoss 控制器远程触发欧洲超市冷柜除霜](#item-1) ⭐️ 8.0/10
2. [Meta 发布 Muse Wonder 模型，基准可信度与隐私问题引热议](#item-2) ⭐️ 8.0/10
3. [Python 3.15 发布，带来 PEP 810 显式惰性导入](#item-3) ⭐️ 8.0/10
4. [芝商所拟于 10 月推出两项 AI 算力期货合约](#item-4) ⭐️ 8.0/10
5. [Mysteel 黑色金属例会：本周钢价或偏弱运行为主](#item-5) ⭐️ 7.0/10
6. [螺纹钢期货上涨，钢价反弹力度或有限](#item-6) ⭐️ 7.0/10
7. [中国 AI 基础设施独角兽无问芯穹完成 23 亿元 C 轮融资](#item-7) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [黑客通过 Danfoss 控制器远程触发欧洲超市冷柜除霜](https://www.tomshardware.com/tech-industry/cyber-security/unprecedented-cyberattack-cripples-supermarket-fridges-across-europe-as-hackers-activate-automatic-defrosting-delivery-and-store-prices-also-impacted-by-incident) ⭐️ 8.0/10

攻击者远程操纵了欧洲多家超市连锁的 Danfoss 制冷控制器，其中法国连锁超市 Intermarché 受影响最明显，约 150 家门店被攻击，冷柜被强制进入自动除霜模式、制冷被关闭，据报温度一度升至 50°C，导致冷冻和冷藏商品损毁。Danfoss 证实被劫持的控制器大多是运行过时固件的老旧设备，该事件还波及了配送和门店定价。 这是一起罕见的大规模、真实发生的 OT/IoT 网络攻击，造成了实实在在的商业损失，说明如今连超市楼宇和零售基础设施——而不只是工厂或电网——都已成为可行的攻击目标。它凸显了老旧工业控制器暴露在互联网上所带来的系统性风险，这类暴露往往源于远程诊断需求和订阅制联网模式，而这一模式在零售、物流和冷链运营商中反复出现。 疑似被利用的设备包括 Danfoss SM800（2021 年终止支持）和 SC355（2016 年终止支持）等控制器，Claroty 的 Team82 研究团队曾发表题为《Freeze the Controller, Defrost the Food》的研究，披露了 Danfoss 制冷控制器中的漏洞。由于这些控制器可被远程访问，攻击者能够把正常运行逻辑反转：系统不再冷冻保鲜，而是强行加热除霜，影响进一步传导至配送计划和货架价格。

hackernews · Zeekaas · 10月12日 12:16 · [社区讨论](https://news.ycombinator.com/item?id=50055304)

**背景**: 商用制冷控制器负责调节压缩机、风扇以及周期性除霜流程，使展示冷柜保持在安全的食品温度范围内；自动除霜本是正常的维护流程，但如果被持续触发或在错误时机触发，就会完全背离设备的用途。现代控制器越来越多地接入网络，以便运营商跨门店监控能效、避免为简单操作派工程师上门——这种便利也把它们接入了互联网。由于超市制冷业务利润率很低，老旧控制器通常只在损坏时才更换，而不会按安全周期更新，导致已终止支持的设备长期在线运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybernews.com/security/danfoss-refrigeration-hack-france-supermarkets/">Refrigeration Cyberattack Hits French Supermarkets | Cybernews</a></li>
<li><a href="https://www.msn.com/en-us/technology/cybersecurity/danfoss-says-hacked-controllers-behind-50c-french-supermarket-fridges-ran-old-firmware/ar-AA2e6nkW">Danfoss says hacked controllers behind 50C French ... - MSN</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论者总体对运营商表示同情而非苛责，他们指出肇事者很可能是 Danfoss SM800、SC355 这类已有 15 至 20 年历史的控制器，而已知 CVE 之所以未修补，就是因为&quot;没有利润空间&quot;，根本挤不出预算做安全审查或设备更新。不少人对&quot;冷柜为什么非要联网&quot;这种条件反射式的质疑提出反驳，举例说医院和实验室的设备如今必须付费订阅并联网才能运行，并引用 Danfoss 把联网包装成效率卖点的宣传文案。还有人猜测此事可能与 2026 年 8 月美军基地冷柜疑似遭篡改的事件有关，怀疑是同一团伙、模仿者，还是彼此无关。

**标签**: `#cybersecurity`, `#OT/IoT-security`, `#supply-chain`, `#retail-operations`, `#legacy-systems`

---

<a id="item-2"></a>
## [Meta 发布 Muse Wonder 模型，基准可信度与隐私问题引热议](https://research.meta.ai/blog/muse-wonder) ⭐️ 8.0/10

Meta 在其研究博客（research.meta.ai/blog/muse-wonder）上发布了新的前沿 AI 模型 Muse Wonder，该帖在 Hacker News 上迅速获得 550 分和 303 条评论。发布后数小时内，用户就开始自行评测：在图像转 HTML 任务上将 Muse Wonder 与 Anthropic 的 Opus 5.5 对比，并与更早的 Muse Spark 1.2、Muse 1.3 等版本做比较。 Muse Wonder 为这个日益被少数几家实验室主导的领域增添了又一个有分量的前沿模型；有评论者认为这是好事，因为它降低了由单一公司为强大 AI 制定规则的风险。与此同时，这次发布也让外界重新审视厂商自报的基准测试成绩，以及伴随这类发布而来的开发者平台安全实践。 评论者对公布的基准成绩能否转化为实际能力表示怀疑：一项图像转 HTML 测试显示，Muse Wonder 的表现更接近 Sonnet 或 Haiku 而非 Opus 5.5，测试者怀疑其视觉模块是短板。另有用户报告称，用一个仅用于 Quest 的旧 Meta 账号登录 dev.meta.ai 时，登录授权界面中出现了与其毫无关系的其他人的资料和邮箱，而其账号设置无法访问、无法注销。

hackernews · meetpateltech · 10月12日 16:48 · [社区讨论](https://news.ycombinator.com/item?id=50059115)

**背景**: Muse 是 Meta 旗下一系列 AI 产品的品牌名：既包括一个号称不只是回答问题、而是真正替人做事的个人智能体，也包括图像生成模型，以及面向长时间智能体与编程工作流的多模态推理模型 Muse Spark 系列。OpenRouter 上列出的 Muse Spark 1.3 提供 1,048,576 token 的上下文窗口，定价为每百万输入 token 1.25 美元、每百万输出 token 4.25 美元。这类前沿模型发布时通常附带厂商自报的基准分数，而开发者习惯用一些颇为古怪的提示词来非正式地检验它们——用 SVG 画鹈鹕就是社区由来已久的传统——并与竞品模型做直接对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/">Introducing Muse : The World’s First Personal AI Agent Built for Everyone</a></li>
<li><a href="https://openrouter.ai/meta/muse-spark-1.3">Muse Spark 1.3 - API Pricing &amp; Benchmarks | OpenRouter</a></li>
<li><a href="https://fliki.ai/models/image/meta-muse">Meta Muse AI Image Generator - Muse Image by Meta | Fliki</a></li>

</ul>
</details>

**社区讨论**: 讨论情绪褒贬不一。一派从竞争角度欢迎 Meta 入局，认为前沿有三四家实验室并存，可以避免出现赢家通吃、直奔递归自我改进的竞赛；另一派则对实测结果公开表示失望，认为其表现不及宣传的基准成绩，与 Opus 5.5 相比明显逊色。还有一条讨论聚焦于 dev.meta.ai 被指存在的隐私缺陷：登录过程中出现了陌生人的资料和邮箱，不少读者认为这一问题比任何基准差距都更严重。

**标签**: `#AI models`, `#Meta`, `#multimodal`, `#privacy/security`, `#LLM benchmarking`

---

<a id="item-3"></a>
## [Python 3.15 发布，带来 PEP 810 显式惰性导入](https://simonwillison.net/2026/Oct/12/python-3-15/) ⭐️ 8.0/10

Python 3.15 正式发布，同时公布了由 3.14 和 3.15 发布经理 Hugo van Kemenade 整理的官方《What&\#x27;s new in Python 3.15》指南。Simon Willison 重点介绍了 PEP 810 显式惰性导入（写法为“lazy import json”）以及 PEP 798 推导式中的解包语法；作为需要兼容所有受支持 Python 版本的开源维护者，他还表示自己终于可以告别 Python 3.10，开始使用 Python 3.11 的新特性。 惰性导入直击 Python 长期存在的启动开销痛点，对 CLI 工具和插件生态尤其重要——例如 Willison 的 LLM，仅仅安装一个依赖 sentence\_transformers 这类重型库的插件，就可能让每次调用命令多花几秒钟。与此同时，Python 3.10 退出支持窗口，迫使整个打包与库生态把最低版本基线提升到 3.11，这对几乎每一个 Python 项目都具有决策意义。 PEP 810 采用显式、可选择加入的方式：lazy 关键字只标记某一条具体的 import 语句，惰性作用范围是局部的，不会级联影响到依赖模块——这是对 PEP 690 全局隐式惰性导入的有意对照，后者在 2022 年因过于复杂和难以预测而被指导委员会否决。PEP 798 由 Adam Hartz 和 Erik Demaine 提出，扩展了早在 Python 3.5 就已落地的 PEP 448 解包语法，使 \[\*sublist for sublist in lists\] 和 \{\*\*d for d in dicts\} 这样的写法成为可能。

rss · Simon Willison · 10月12日 18:15

**背景**: Python 是全球使用最广泛的编程语言之一，遵循可预期的年度发布节奏，因此每个新版本都会伴随一份新的《What&\#x27;s New》文档，并自动改变哪些旧版本仍在支持范围内。新语言特性通过 PEP（Python 增强提案）这一正式文档流程提出和设计，在被 CPython 接纳之前需要先经过讨论与审核。通常情况下，import 语句会立刻查找并执行目标模块，如果该模块或其依赖很重，即使后续根本没用到导入的名字，这段开销也会在启动时被付出——这正是惰性导入要解决的问题。Simon Willison 是知名的 Python 开发者，著有 Datasette 和 LLM 命令行工具等，他撰写的版本发布解读被广泛阅读，常被视为判断新 Python 版本重点的风向标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://peps.python.org/pep-0810/">PEP 810 – Explicit lazy imports | peps.python.org</a></li>
<li><a href="https://socket.dev/blog/pep-810-proposes-explicit-lazy-imports-for-python-3-15">PEP 810 Proposes Explicit Lazy Imports for Python 3.15 - Soc...</a></li>
<li><a href="https://realpython.com/python315-lazy-imports/">Python 3.15 Preview: Lazy Imports</a></li>

</ul>
</details>

**标签**: `#Python`, `#Programming Languages`, `#PEP 810`, `#Lazy Imports`, `#Open Source Releases`

---

<a id="item-4"></a>
## [芝商所拟于 10 月推出两项 AI 算力期货合约](https://news.google.com/rss/articles/CBMiSEFVX3lxTE5ZOFgzYjZ3M2txMVFhLXRxU1R3Nkpad0ZRYUN3aC1raG1iMWZmN2V6SzAycUhaYWo1LTRUUUwxWVM3aVhBVFhmVQ?oc=5) ⭐️ 8.0/10

芝商所集团正式宣布计划于 10 月推出两项与 AI 算力相关的期货合约，据报将与算力数据提供商 Silicon Data 合作，目标上线日期为 10 月 5 日。与此同时，美国商品期货交易委员会（CFTC）表示拟就 AI 算力期货公开征求意见，芝商所与洲际交易所（ICE）均在推进相关产品。 这标志着 AI 算力开始金融化：GPU 与推理算力从单纯的运营成本，转变为可交易、可对冲的资产类别。若这些合约形成足够流动性，拥有庞大 AI 基础设施预算的企业就能对冲算力价格波动，而公开的远期曲线也可能成为整条 AI 产业链在预算与投资决策上的参考基准。 这些产品挂钩 Silicon Data 的算力价格基准，而 CFTC 启动公开征求意见程序说明合约仍处于监管审查阶段，能否如期上市尚无保证。合约规模、结算方式（现金结算还是实物 GPU 时长交割）以及参考指数编制方法等关键规格尚未公开，因此在成交量形成之前，其实际对冲效果仍待验证。

rss · Google News - AI 前沿 · 10月12日 08:20

**背景**: AI 算力指的是用于训练和运行模型的 GPU 处理能力，如今已成为 AI 公司最主要的成本项——行业分析显示，目前约 80%的 AI GPU 支出流向推理而非训练。由于算力在竞争性市场中租用或采购，价格波动明显，每 token 成本会随 GPU 型号、利用率与闲置容量而剧烈变化。期货是交易所标准化合约，允许买卖双方提前锁定未来某一时点的价格，石油、粮食与利率市场早已采用这一机制；把它套用到算力上，就相当于为 AI 算力建立了一个正式的价格发现市场。

**标签**: `#AI compute`, `#futures markets`, `#CME Group`, `#AI economics`, `#compute pricing`

---

<a id="item-5"></a>
## [Mysteel 黑色金属例会：本周钢价或偏弱运行为主](https://news.google.com/rss/articles/CBMiaEFVX3lxTE95V2JmQk82WlIzVGlROXl2emM2RG93MkYzLUtQSU1Bblk3SGNrWUVsVzVsWENORnZKNlBiemlYTkh2V3I4ZFpqRmdJTDVQY3pyU2JmZkx5TTNfMU9hcFRTRUUyWGF6aHNS?oc=5) ⭐️ 7.0/10

Mysteel（我的钢铁）发布了本周黑色金属例会观点，核心结论是本周期钢材价格预计以偏弱运行为主。该内容给出的只是短期方向性判断，并未在可见摘要中披露具体数据支撑。 Mysteel 的周度观点是中国钢铁产业链广受关注的定价参考，偏弱的短期展望会直接影响贸易商的补库节奏、加工企业的报价策略以及下游用户的采购时点选择。这一判断也与国内钢材需求情绪偏弱的整体格局相呼应，并会进一步传导至铁矿石、焦煤价格以及建筑和制造业的成本预期。 该内容信息量非常有限：仅有方向性标题，没有库存水平、钢厂产量或利润数据，也没有给出判断依据，因此更适合作为情绪指标而非量化预测来使用。此外，其表述为“偏弱为主”而非明显看空，意味着市场预期的是温和走弱而非大幅下跌。

rss · Google News - 钢材加工配送 · 10月12日 10:33

**背景**: Mysteel（我的钢铁）是中国黑色金属领域最受关注的大宗商品信息机构之一，其覆盖范围包括螺纹钢、热轧卷板等钢材品种以及铁矿石、焦煤、焦炭、废钢等原料。其每周例会纪要汇总市场对供需和库存的看法，为参与者提供短期价格方向参考。中国是全球最大的钢铁生产国和消费国，因此国内钢价情绪是全球大宗商品交易商、钢厂以及建筑和制造业下游企业的重要参考变量。

**标签**: `#steel prices`, `#ferrous metals`, `#steel distribution`, `#market outlook`, `#China commodities`

---

<a id="item-6"></a>
## [螺纹钢期货上涨，钢价反弹力度或有限](https://news.google.com/rss/articles/CBMiakFVX3lxTFB5MUFwNWI2MnNKaXowdHlnWjFiZmRwOVd2akZnS1FfUDFiTDJPUTROWUszaDl6SXRoUy1WUjVwQVVCLTRSeHJTM1Z5LTRmc1k2UzBfSmwzaW5QakFtcjBNbVE3aEhkWUJoLVE?oc=5) ⭐️ 7.0/10

我的钢铁网发布市场快讯称，螺纹钢期货价格出现上涨，但钢价反弹力度可能有限。该标题表明期货市场情绪有所改善，但现货价格涨幅可能受到抑制。 这一信号对钢材加工商、贸易商和建筑企业都很重要，因为螺纹钢是基础设施和房地产项目的关键投入品。反弹力度有限意味着利润率压力可能持续，从而影响整个钢铁供应链的采购和库存策略。 该快讯未提供详细分析或具体价格水平，但提及了上海期货交易所（SHFE）的螺纹钢期货，其主力合约是中国建筑钢材的基准。快讯暗示，尽管期货价格可能有所上涨，但疲软的季节性需求和谨慎情绪可能阻止现货价格持续上涨。

rss · Google News - 钢材加工配送 · 10月12日 03:50

**背景**: 螺纹钢是一种带肋钢筋，广泛用于建筑混凝土加固。其在上海期货交易所（SHFE）的期货合约被视为中国钢材需求的风向标，需求主要受房地产和基础设施活动驱动。2025 年初，惠誉评级指出，2024 年第四季度中国钢材和水泥价格有所反弹，但由于冬季和春节假期建筑活动减少，不确定性依然存在，2025 年第一季度产量和利润率仍将承压。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lechang.gvyun.com/rebar/">螺纹钢期货行情_钢材期货实时报价_建材市场交易图表_汇率网</a></li>

</ul>
</details>

**标签**: `#steel processing`, `#rebar futures`, `#steel prices`, `#commodity markets`, `#supply chain`

---

<a id="item-7"></a>
## [中国 AI 基础设施独角兽无问芯穹完成 23 亿元 C 轮融资](https://news.google.com/rss/articles/CBMiT0FVX3lxTE9WLXdPTGJfanh2YUNCbUc5a0pyMFJhRU82N2JkS0taY0xISWRQUmlpZV9OUGdXWjVYREVKLVJ2Z3hEaDVzTDAtQ1hEZ21waGM?oc=5) ⭐️ 7.0/10

总部位于上海的 AI 基础设施创业公司无问芯穹（Infinigence AI）宣布完成 23 亿元人民币（约合 3.2 亿美元）的 C 轮融资，累计融资额由此达到 43 亿元人民币。公司表示，这一数字刷新了国内 AI 基础设施领域的融资纪录。 这轮融资的规模是一个明确的资本市场信号：在先进 GPU 供应受限的背景下，投资人依然把算力与调度这一层，而非仅仅是模型层，视为中国 AI 技术栈的核心战场。与此同时，这也加剧了无问芯穹与百度百舸、阿里等云厂商自研异构计算平台之间的竞争。 无问芯穹的核心叙事是“M×N”技术范式，即用软硬协同与多元异构算力把 M 种模型与 N 种芯片连接起来，使其在云端与端侧均可运行。需要注意的是，该消息本身仅为标题式报道，并未披露本轮投资方名单、公司估值，也没有给出支撑“刷新纪录”这一说法的具体技术指标。

rss · Google News - EDF AI 部署工程 · 10月12日 12:04

**背景**: AI 基础设施（AI Infra）指的是位于 AI 模型与底层硬件之间的软件层，涵盖训练框架、推理引擎、GPU 虚拟化与算力调度等，常被形容为“基础设施之下的基础设施”，因为整个 AI 技术栈都依赖它运转。由于美国出口管制限制了中国企业获取英伟达高端加速卡，国内公司不得不在国产与进口芯片混合的集群上跑任务，这使得异构计算调度与多芯片适配成为商业上至关重要的能力。无问芯穹的定位正是充当这一抽象层，让任意模型都能在任意可用芯片上高效运行，从而避免客户被单一硬件厂商锁定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.infinigence-ai.com/">无问芯穹_Infinigence-AI_通用人工智能基础设施服务商</a></li>
<li><a href="https://www.infinigence-ai.com/about-us.html">公司介绍_无问芯穹_AGI基础设施服务商</a></li>
<li><a href="https://jimmysong.io/zh/blog/why-i-join-dynamia-ai-native-infra/">加入 Dynamia 密瓜 智 能 后的第一个月：为 什 么 AI Native Infra 值得投入</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#Funding`, `#AI Compute`, `#China Tech`, `#Industry Signal`

---