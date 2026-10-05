---
layout: default
title: "Horizon Summary: 2026-10-05 (ZH)"
date: 2026-10-05
lang: zh
---

> 从 114 条内容中筛选出 5 条重要资讯。

---

1. [Strata 声称 125B 的 Qwen3.8-Flash-Next 可在单张 RTX 4090 上以 100+ tokens/s 运行](#item-1) ⭐️ 8.0/10
2. [OpenAI 据悉洽谈租赁俄亥俄州 10 吉瓦数据中心](#item-2) ⭐️ 8.0/10
3. [推理支出 2026 年首超训练：“Token 工厂”崛起，AI 基础设施投资逻辑生变](#item-3) ⭐️ 7.0/10
4. [OpenAI 负责 AI 安全的员工离职，警告 AI 运营应像核电站一样管理](#item-4) ⭐️ 7.0/10
5. [白宫设立&quot;超级智能力量&quot;AI 特别工作组，要求 120 天内提交风险报告](#item-5) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Strata 声称 125B 的 Qwen3.8-Flash-Next 可在单张 RTX 4090 上以 100+ tokens/s 运行](https://github.com/Niko1221/Strata) ⭐️ 8.0/10

一个名为 Strata 的 GitHub 项目（github.com/Niko1221/Strata）声称能在单张消费级 RTX 4090 上运行 125B 参数的 Qwen3.8-Flash-Next 模型，速度约为每秒 100-124 个 token；一位评论者称自己在配备 128GB DDR5 和 Ryzen 7950X3D 的 4090 上独立复现出 124 tokens/s。该成绩依赖于极为激进的 4-bit 以下量化，而这正是多位评论者质疑的核心所在。 如果这些数字能够站得住脚，125B 级别的模型就可以在单张消费级显卡上本地部署，而无需租用数据中心级 GPU，这将显著降低本地大模型部署的成本与隐私门槛。同时，它也把「为了提升每秒 token 数究竟愿意牺牲多少输出质量」这一争论推向更尖锐的层面。 这一亮眼吞吐量来自于 4-bit 以下的量化，而在这个精度区间，权重精度损失可能明显损害推理与空间定位能力。一位独立测试者在两个推理栈上使用完全相同的 GGUF 与视觉适配器权重做坐标预测任务，结果 Strata 的中位误差为 154.8 像素，而 llama.cpp 为 46.5 像素，说明这些速度可能部分是靠牺牲准确度换来的。

hackernews · snehesht · 10月4日 12:51 · [社区讨论](https://news.ycombinator.com/item?id=49953495)

**背景**: 量化是指用更低的数值精度（例如用 4-bit 整数代替 16-bit 浮点数）存储模型权重，从而大幅降低显存占用并提升速度，代价是输出质量会有所损失。GGUF 是 llama.cpp 使用的流行单文件模型格式，而 llama.cpp 是目前最广泛使用的本地推理引擎，因此自然成为这类对比的基准。一个 125B 参数的模型即便在 4-bit 下通常也需要 60GB 以上显存，要塞进 RTX 4090 的 24GB 显存，就必须把精度压到明显低于 4-bit。tokens/s（每秒 token 数）是衡量生成速度的标准指标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sumguy.com/quantization-sweet-spot/">LLM Quantization : Q 4 _K_M Isn&#x27;t Always the... | SumGuy&#x27;s Ramblings</a></li>
<li><a href="https://www.minimum-code.com/glossary/llm-quantization">What is LLM Quantization | Minimum Code</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/discussions/4167">Performance of llama . cpp on Apple Silicon M-series · ggml-org...</a></li>

</ul>
</details>

**社区讨论**: 社区情绪褒贬不一：有用户表示该工具出人意料地好用，也有人对 4-bit 以下量化的质量以及围绕它的炒作持怀疑态度。批评者援引独立视觉基准测试，指出其误差远大于 llama.cpp；不少评论者转而推荐 llama.cpp、ds4 等成熟推理栈，或以约每小时 1 美元租用 RTX Pro 6000，凭借缓存实现每小时约 120 万输出 token、4000 万输入 token。

**标签**: `#llm-inference`, `#quantization`, `#local-llm-deployment`, `#gpu-optimization`, `#model-benchmarking`

---

<a id="item-2"></a>
## [OpenAI 据悉洽谈租赁俄亥俄州 10 吉瓦数据中心](https://news.google.com/rss/articles/CBMiSEFVX3lxTFBrdHpIekxCYlpaeVc0Y3pndTJtVFkwaVlDWDdYVnlfR2t5YW4tWnRrQXlpVU5kUWdrc3prSmtwQmJQZ3E3UWgxeA?oc=5) ⭐️ 8.0/10

据 The Information 援引两名直接知情人士的消息报道，OpenAI 正在洽谈租赁俄亥俄州一个拟建的 10 吉瓦数据中心园区。据称该交易可能涉及英伟达，建设费用或高达 5000 亿美元。 10 吉瓦的规模将使其成为 AI 领域有史以来最大的单一算力基础设施承诺之一，远超通常以数十到数百兆瓦计量的普通数据中心。这也表明前沿 AI 实验室的竞争正从模型能力转向对电力、土地和芯片等国家级电网规模资源的争夺。 该报道尚未得到证实，且来源于单一信源，其中 10 吉瓦指的是园区规划中的供电容量，而非已建成的设施。作为参照，国际能源署估计近年来全球所有数据中心用电约 415 太瓦时，约占全球用电量的 1.5%；高盛则指出，AI 驱动的新增数据中心需求中约 60% 需要新建发电容量，而新电厂上线可能需要 5 至 7 年。

rss · Google News - AI 前沿 · 10月4日 22:48

**背景**: 数据中心的容量通常以吉瓦为单位描述，指的是园区可调用的峰值电力功率，因为 AI 训练和推理需要 GPU 集群及其冷却系统持续消耗大量电力。作为参照，1 吉瓦大致相当于一座大型核反应堆的出力，因此 10 吉瓦已接近一座大城市的用电需求。OpenAI 此前已宣布与英伟达合作，后者将投资最高 1000 亿美元并共同建设至少 10 吉瓦的 AI 数据中心，首批 100 亿美元将随着第一个吉瓦数据中心建成而投入；因此此次俄亥俄州租赁传闻符合各大实验室提前数年锁定电力与硬件的整体趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.163.com/dy/article/KV2IU3JM0519D45U.html">OpenAI谈判租赁俄亥俄州 10 吉 瓦 数 据 中 心 预计建设费用达5000亿美元</a></li>
<li><a href="http://news.cnfol.com/guojicaijing/20250923/31665186.shtml">英伟达拟向OpenAI投资最高1000亿美元 并共建 10 吉 瓦 AI...</a></li>

</ul>
</details>

**标签**: `#AI compute`, `#data centers`, `#OpenAI`, `#infrastructure`, `#energy demand`

---

<a id="item-3"></a>
## [推理支出 2026 年首超训练：“Token 工厂”崛起，AI 基础设施投资逻辑生变](https://news.google.com/rss/articles/CBMiSEFVX3lxTFBvRE95cDRYaW5JQ2xZVEhpODctWTZGR2V6MkJIakdiYjJqUXZjYWFtaWlIWXQ1elJzN0tNUk5FRWU1UXc2ZWpqMA?oc=5) ⭐️ 7.0/10

财联社一篇深度报道指出，全球 AI 推理支出预计将在 2026 年首次超过训练支出，报道将这一转变归因于“Token 工厂”的崛起以及 AI 基础设施投资逻辑的变化。该标题将这一“交叉点”视为 AI 算力预算配置方式的结构性转折。 这一“交叉”之所以重要，是因为它改变了 AI 基础设施的根本建设目标：资本开支与芯片需求将从一次性的、以算力为核心的大规模训练集群，转向持续运行、以每 Token 成本（而非峰值 FLOPS）来衡量的推理集群。这会影响芯片厂商、云服务商、数据中心建设方，以及所有需要决定 AI 预算投向的企业。 由 NVIDIA 及其 CEO 黄仁勋推广的“Token 工厂”框架，把 AI 数据中心视为一条生产线，其核心指标是每瓦 Token 产出量和每百万 Token 成本；与受算力瓶颈约束的训练不同，推理负载通常更受内存带宽和延迟制约。需要说明的是，本条内容仅为 RSS 标题与链接，没有正文或社区讨论，因此该预测背后的具体数据无法从所提供来源中核实。

rss · Google News - AI 前沿 · 10月4日 14:59

**背景**: 训练是指通过处理海量数据集来构建或更新模型能力的过程，而推理则是让训练好的模型实际运行、回答查询并生成输出的阶段。传统上，训练占据了 AI 算力预算的绝大部分，因为它需要规模庞大且高度耦合的 GPU 集群；但推理要为每一次用户请求持续运行，其累计成本会随使用量增长。NVIDIA 把 AI 数据中心描述为“AI 工厂”，认为它们不断“处理 Token”，把 Token（模型读写文本等数据的基本单位）转化为该公司所称的 AI“货币”，即智能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/ai-tokens-explained/">What Are AI Tokens ? The Language and Currency... | NVIDIA Blog</a></li>
<li><a href="https://www.spheron.network/blog/token-factory-gpu-cloud-tokens-per-watt-guide/">Token Factory on GPU Cloud: Maximize Tokens per Watt for AI ...</a></li>
<li><a href="https://www.cloudflare.com/learning/ai/inference-vs-training/">AI inference vs . training : What is AI inference ?</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#inference`, `#training`, `#Token factory`, `#AI investment`

---

<a id="item-4"></a>
## [OpenAI 负责 AI 安全的员工离职，警告 AI 运营应像核电站一样管理](https://news.google.com/rss/articles/CBMimgNBVV95cUxQUURBWl9FcXltZFRXNm9PSl9MRkpVaTMyek9ZZThVUVlXMTM5MWhrQ2lSbmo1NnhDUVRkU3F5VTkzOW5tUV82ZWwxUExPX0pVeXhRUlJldlBYeW1MSHBGRVBId2lhZVY2NWZucWdrWGN2clVTYVNKWkh1M1d0MjRfQWVyeGtfSm9CQThYT19Xc0tyZzNOWU1YYVp3YlMzZXlOVlFlbDZORkN1T2N1a1NDVm5VMEV2bUFaRmhzM2M5dW8tTTdTSV9Fc0dUT05LUVB1VHVZbWFJcndTRlp2eDIzOFJxQ1hsVEU3S1NENUc2NFdoalNiUlpzVEZBNWZqczZwZk9lQlZXbk16cEpNQ2kwTGpRM0tJOTFpWmkwcHMxTk1KN0Qyc3M4SXZFNU5yeFFHU0llQnBpeGlLS0x6bGlZRXF1R0R1a2JudG1tdmh3d2NqemoyOHBlN2VHQTdvY1FISnIzeFpOR3lPY002b0o4dEZSOXBBT0ZxNXF6bHdVaVZyMzc0aGk0QnJHQnY3bmpZbGcwelZkZjQwdw?oc=5) ⭐️ 7.0/10

据报道，OpenAI 一名负责 AI 安全的员工已经离职，并在离职时警告称，AI 的运营应像核电站一样以同等的严格标准来管理，以避免灾难性后果。这一消息由中文媒体《星島頭條》报道，将该离职事件定性为一次 AI 安全与治理层面的警告，而非普通的人事变动。 OpenAI 安全团队核心人员接连高调离职，加剧了外界关于“商业压力是否正在超越前沿实验室安全投入”的争论，也为监管机构和政策制定者讨论 AI 风险与监管规则提供了具体论据。对于依赖前沿模型开展业务或开发的各方而言，“像核电站一样管理”这一类比意味着行业需要比现状严格得多的运营管控、监控机制与事故响应纪律。 目前可得的内容实质上只是一条标题加链接，因此离职员工的具体姓名、确切职位以及警告全文都无法从所给来源中独立核实；所谓“像核电站一样”更多是一种用于运营风险管理的比喻性标准，而非字面上的制度建议。报道也没有说明其所呼吁的具体安全做法，例如分阶段发布、独立审计或紧急关停权限等。

rss · Google News - EDF AI 部署工程 · 10月4日 01:33

**背景**: AI 安全是一门研究如何确保能力日益强大的 AI 系统不造成伤害的领域，其风险来源包括滥用、事故以及人类失去对系统的控制；在大型实验室里，这项工作涵盖研究、红队测试、发布前的门槛审查以及内部政策制定。核电站之所以常被用作这一争论中的参照，是因为它同时具备极高的潜在危害和高度受监管、冗余设计、独立监督的安全工程体系。近年来 OpenAI 已有多位专注安全与政策的知名员工离职，媒体和 AI 社群往往将此解读为其安全优先级与产品、商业节奏之间如何权衡的信号。

**标签**: `#AI safety`, `#OpenAI`, `#AI governance`, `#risk management`, `#regulation`

---

<a id="item-5"></a>
## [白宫设立&quot;超级智能力量&quot;AI 特别工作组，要求 120 天内提交风险报告](https://www.wsj.com/tech/ai/new-ai-task-force-to-report-on-risks-of-technology-after-public-and-industry-concerns-b6308bef) ⭐️ 7.0/10

白宫新设了一个名为&quot;超级智能力量&quot;（Super Intelligence Force，简称 SIF）的人工智能特别工作组，由国家情报总监 Jay Clayton 领导，他已向《华尔街日报》确认了这一任命。该工作组被要求在 120 天内评估人工智能带来的风险，并厘清联邦政府应承担何种责任；一名白宫高级官员称，这让 Clayton 实际上成为特朗普政府的&quot;AI 沙皇&quot;。 这是一个对决策有实际参考意义的行政信号：它把 AI 监管协调权集中到情报系统负责人手中，而非交给监管机构，从而强化了本届政府偏好自愿安全承诺、而非强制法规的立场。对于 AI 开发者、部署方、审计机构和合规团队而言，这意味着短期内安全治理更可能依赖外部审计与内部管控，而不是新的立法要求。 Clayton 将该任务的目标表述为确保美国&quot;继续在超级智能领域保持领先&quot;，并把美国人民的利益放在首位；政府支持的是一套自愿性框架，即企业加强内部安全监控、组建审查团队，并允许外部审计方评估其安全措施。值得注意的是，该工作组的产出是风险评估与建议，而非可强制执行的法规，其核心动因是保持对中国的竞争优势。

telegram · zaihuapd · 10月4日 02:37

**背景**: &quot;超级智能力量&quot;这一命名反映了特朗普总统偏好使用&quot;超级智能&quot;而非&quot;人工智能&quot;一词的说法。&quot;AI 沙皇&quot;这一称呼在美国政坛自 2024 年起被使用，当时 David Sacks 被任命为兼职 AI 顾问职位，绕开了参议院确认程序；而 Clayton 本身已是在任的国家情报总监，同样避免了新的确认之争。该工作组的成立紧随白宫与 OpenAI、Anthropic、Google、Meta、Nvidia 和 SpaceX 等企业高管的会面，科技巨头在会上同意了一套以内部监控和外部审计为核心、而非具有法律约束力的多层自愿安全框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.dw.com/en/trump-ai-czar-clayton-task-force/a-79537966">Trump taps Jay Clayton as AI czar for new task force</a></li>
<li><a href="https://www.straitstimes.com/world/united-states/us-ai-task-force-led-by-jay-clayton-to-report-on-technologys-risks-wsj">US AI task force to assess risks and report on super intelligence</a></li>
<li><a href="https://www.businesstoday.in/technology/artificial-intelligence/story/trumps-ai-push-tech-giants-agree-to-voluntary-safety-standards-as-expansion-grows-558724-2026-09-30">Trump’s AI push: Tech giants agree to voluntary safety standards...</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#AI governance`, `#regulation`, `#AI safety`, `#United States`

---