---
layout: default
title: "Horizon Summary: 2026-09-17 (ZH)"
date: 2026-09-17
lang: zh
---

> 从 243 条内容中筛选出 8 条重要资讯。

---

1. [Nvidia 宣布支持用 Rust 原生编写 GPU 程序](#item-1) ⭐️ 8.0/10
2. [4B 模型宣称查询计划比 Postgres 快 81%，引发质疑](#item-2) ⭐️ 7.0/10
3. [小米发布 MiMo 实时强化学习后训练仪表盘](#item-3) ⭐️ 7.0/10
4. [Mistral 与 Mozilla 为 Firefox 带来私密多语言 AI](#item-4) ⭐️ 7.0/10
5. [唐山钢坯上涨 20 元，钢价或震荡偏强](#item-5) ⭐️ 7.0/10
6. [香港五年规划：逾半公营房屋采用 MiC 建筑，公屋轮候时间降至四年以下](#item-6) ⭐️ 7.0/10
7. [摩根大通：开源冲击与 AI 安全均非威胁，半导体设备将成新瓶颈](#item-7) ⭐️ 7.0/10
8. [OpenAI、Anthropic 与谷歌 DeepMind 开始合作研究 AI 安全措施](#item-8) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Nvidia 宣布支持用 Rust 原生编写 GPU 程序](https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/) ⭐️ 8.0/10

Nvidia 在官方开发者博客上发布了名为“CUDA Rust”的方案，提供两条不同的技术路线，让开发者可以用 Rust 而非 C++ 或 CUDA C 来编写 GPU 内核。其中一条路线面向 SIMT 风格内核并直接编译为 PTX，另一条则支持在稳定版 Rust 中进行基于 tile 的 GPU 编程。 厂商官方支持大幅提升了 Rust 在 GPU 计算领域的合法性与可信度，有望把内存安全保障引入长期以来用易出错的 C++ 编写的内核代码。这可能加速 Rust 在 AI 与 HPC 场景中的采用，但同时也进一步强化了 CUDA 生态对单一厂商的依赖。 两条路线差异明显：一条依赖自定义的 rustc codegen 后端，通过 Pliron IR 框架和 LLVM 把 SIMT 风格内核下沉为 PTX；另一条则借助 CUDA Tile IR 的 JIT 编译，由编译器负责线程映射与内存布局，并且可在稳定版 Rust 上运行。历史上最大的障碍是 LLVM 的 PTX 后端在面对许多常见 Rust 操作时会生成非法 PTX，这正是社区转而开发专用工具链的原因。

hackernews · nonmaskable · 9月16日 11:15 · [社区讨论](https://news.ycombinator.com/item?id=49724881)

**背景**: CUDA 是 Nvidia 专有的通用 GPU 计算工具链，而“内核（kernel）”指的是由程序员编写、在数千个 GPU 线程上并行执行的函数。长期以来编写这些内核都依赖 CUDA C/C++，而 Rust 的编译期所有权与借用检查机制有望消除困扰内核代码的整类内存与并发错误。此前 Rust-CUDA 项目和 rust-gpu（将 Rust 编译为 SPIR-V）等社区努力曾试图填补这一空白，但都缺乏 Nvidia 的官方支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Rust-GPU/Rust-CUDA">GitHub - Rust-GPU/rust-cuda: Ecosystem of libraries and tools ... Introducing CUDA Rust: Two Tracks for Writing GPU Kernels Getting Started - The Rust CUDA Guide - GitHub Pages Rust for GPU Programming: wgpu and rust-gpu Complete Guide ... GPU programming in Rust : r/rust - Reddit</a></li>
<li><a href="https://modal.com/gpu-glossary/device-software/kernel">What is a CUDA Kernel ? | GPU Glossary</a></li>
<li><a href="https://rust-gpu.github.io/">Rust GPU</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍看好 Rust 在内核编程中的安全优势，多人称 CUDA C++ 使用体验痛苦，并指出它与 Hugging Face 的 Candle 推理库天然契合。最强烈的反对意见来自一位开发者，他反感 CUDA 的专有锁定，更青睐 Metal、OpenCL、Triton 这类将内核分离编写的方式；也有人对文章疑似由大模型撰写出以及大模型削弱学习 Rust 动力表示担忧。

**标签**: `#Rust`, `#CUDA`, `#GPU programming`, `#Nvidia`, `#AI/ML`

---

<a id="item-2"></a>
## [4B 模型宣称查询计划比 Postgres 快 81%，引发质疑](https://rohanbansal.com/qorl) ⭐️ 7.0/10

博客作者在 rohanbansal.com/qorl 上训练了一个 4B 参数的语言模型，用于生成查询计划，并宣称在小型内存数据集上比 Postgres 快 81%。这一结论引发了社区对其基准测试真实性和统计严谨性的详细质疑。 这是将小型（4B）语言模型应用于查询规划这一数据库核心功能的一次真正新颖的尝试，而该领域长期由确定性的、基于代价的启发式方法主导。如果结论稳健，这种方法可能重塑优化器的构建方式；但由于评测存在争议，它目前更像是一个有争议的概念验证，而非已证实的 Postgres 替代方案。 评测在一个 8 GB 的内存只读数据集上进行，shared\_buffers 被限制为其中一小部分，查询在测量前已预热，除主键外没有任何二级索引，也没有扩展统计信息。这些限制严重削弱了其在真实 OLTP 规模下优于 Postgres 启发式方法的说法，而 LLM 规划器的非确定性本质也带来了可靠性和可观测性方面的隐忧。

hackernews · polyphilz · 9月16日 18:50 · [社区讨论](https://news.ycombinator.com/item?id=49731285)

**背景**: 查询优化器是数据库中负责通过比较各种可能的执行计划来决定最高效执行 SQL 查询方式的组件。Postgres 使用的是确定性的、基于代价的规划器，它会依据对数据的统计知识选出最优计划——这也正是不准确或缺失的统计信息往往成为慢查询根因的原因。近期诸如 LLM-QO 和 SEFRQO 等研究探索了利用大语言模型生成提示或计划来引导经典优化器，而要做好这类工作的基准测试，需要谨慎控制缓存预热和 shared\_buffers 等设置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Query_optimization">Query optimization - Wikipedia</a></li>
<li><a href="https://www.aha.io/engineering/articles/optimizing-with-the-postgresql-deterministic-query-planner">Optimizing with the PostgreSQL deterministic query planner</a></li>
<li><a href="https://www.tangramvision.com/blog/how-to-benchmark-postgresql-queries-well">Tangram Vision Blog | Hands-on with PostgreSQL Authorization, Part 2.5: How To Benchmark PostgreSQL Queries Well</a></li>

</ul>
</details>

**社区讨论**: 讨论明显带有批判性且技术含量很高。评论者指出这种内存中、已预热、只读的设置容易过拟合，并指出评测缺少二级索引和扩展统计信息，同时数据存在强相关列（例如电影数据中国别与年份的关联），还警告非确定性的 LLM 规划器会带来运维隐患——工程师将不得不“反复重跑 LLM 直到得到更快的查询”。另一些人则认为查询规划是数学和算法密集型的工作，AlphaGo 式的学习型启发式方法会比通用 LLM 更合适。

**标签**: `#LLM-for-databases`, `#query-optimization`, `#Postgres`, `#AI-deployment-reliability`, `#benchmarking-methodology`

---

<a id="item-3"></a>
## [小米发布 MiMo 实时强化学习后训练仪表盘](https://mimo.xiaomi.com/rl/) ⭐️ 7.0/10

小米在其官网 mimo.xiaomi.com/rl/ 上线了一个实时仪表盘，公开呈现 MiMo 模型后训练（强化学习）过程的进展，该消息在 Hacker News 上获得 229 分和 58 条评论。这个页面展示的是正在进行的训练状态，而不是一次正式发布或静态技术报告。 前沿模型实验室通常对后训练配方和奖励曲线严格保密，因此公开展示实时训练进展，能让外界直接判断一个中国开源权重模型的迭代速度以及强化学习带来的增益。这也直接触及价格性能之争：开发者反馈 MiMo 的每美元编码质量已经能与 Anthropic 的模型相抗衡。 仪表盘本身并未提供深入的技术细节，具体数字主要来自评论区：有用户引用 MiMo-v2.5-Pro 在 DeepSWE 1.1 上得分 19%，而 Fable 为 70%、Kimi K3 为 69%、Astra 为 74%（均为最大推理投入）；另有用户提到该模型偶尔会陷入幻觉循环，但通过中断再继续即可解决。

hackernews · krackers · 9月16日 20:09 · [社区讨论](https://news.ycombinator.com/item?id=49732270)

**背景**: 后训练是预训练之后的阶段，通过监督微调以及随后的偏好优化或强化学习，把基础模型变成可用、对齐的系统，模型的实际能力大多在这一阶段形成。开源权重模型会公开训练好的参数，DeepSeek、阿里 Qwen、月之暗面等中国团队多采用这一路线，而美国主流实验室则普遍保持闭源。MiMo 是小米的大模型系列，其 V2.5-Pro 的定价约为每百万输入 token 1 美元、每百万输出 token 3 美元。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mimo.xiaomi.com/">mimo . xiaomi .com</a></li>
<li><a href="https://en.wikipedia.org/wiki/Post-training_of_large_language_models">Post-training of large language models</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open-weight_model">Open-weight model</a></li>

</ul>
</details>

**社区讨论**: 整体情绪偏正面：joelwallis 表示 MiMo-V2.5 已承担他大部分的软件工程工作，成本&quot;低得难以置信&quot;，质量接近去年底到今年初的 Anthropic 模型；passive 把 2.5-pro 比作一位能力强但对项目不熟悉的健忘资深工程师。ricardobeat 给出了对比性的 DeepSWE 分数，其他模型明显更高；krm01 追问其他厂商有什么理由不公开这类信息；dr\_dshiv 则调侃开源 AI 的进展速度&quot;像在看一颗定时炸弹&quot;。

**标签**: `#llm-training`, `#reinforcement-learning`, `#open-weight-models`, `#model-evaluation`, `#ai-compute`

---

<a id="item-4"></a>
## [Mistral 与 Mozilla 为 Firefox 带来私密多语言 AI](https://mistral.ai/news/mistral-x-mozilla/) ⭐️ 7.0/10

Mistral AI 与 Mozilla 宣布合作，将 Mistral 的模型集成进 Firefox，实现跨标签页的上下文感知搜索、页面摘要和记忆检索，并支持多语言。该功能同时提供本地（设备端）推理与云端推理两种路径，其中云端模式需要用户明确同意。 这是欧洲挑战者模型厂商较早的一次浏览器层级 AI 集成，使 Firefox 直接对标 Chrome 内置的 Gemini Nano。它可能影响数亿用户接触 AI 浏览的方式，并为本地与云端推理之间隐私取舍的告知方式树立先例。 本地路径依赖在浏览器内运行的小型设备端模型（例如通过 WebGPU），云端路径则把数据发送到 Mistral 的服务器，争议正集中于此。批评者认为官方宣传页面没有清楚区分这两种模式，也没有明确把云端推理表述为“同意上传浏览历史”的选项。

hackernews · vertigoruntime · 9月16日 08:08 · [社区讨论](https://news.ycombinator.com/item?id=49723408)

**背景**: 设备端（本地）推理指 AI 模型完全在用户自己的硬件上运行，数据不离开设备；云端推理则把请求发送到远程服务器，算力更强但需要信任服务方。得益于 WebGPU 以及 WebLLM 等引擎，浏览器内运行大模型已经变得可行，模型无需安装即可在客户端执行。此举也契合 Mozilla 长期坚持的隐私优先定位，同时是 Mozilla 与法国 AI 实验室 Mistral 在由美国主导的 AI 格局中提供“欧洲替代方案”的一步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.runlocalai.co/compare/local-vs-cloud">Local vs cloud inference — privacy, latency, lock-in, cost</a></li>
<li><a href="https://www.everydev.ai/tools/webllm">WebLLM - In - Browser LLM Inference Engine | EveryDev.ai</a></li>
<li><a href="https://nhimg.org/glossary/on-device-inference/">What Is On - device inference ? Definition &amp; Examples</a></li>

</ul>
</details>

**社区讨论**: 评论分歧明显：一种高赞观点认为这本是完全本地小模型推理的理想场景，并指责 Mozilla 在缺乏坦诚说明的情况下把上传私密浏览历史“正常化”。也有人看好它对非英语文档的私密多语言检索，建议在浏览器内内置一个微型模型把自然语言查询转成高级搜索语句，还有人指出即便是主打隐私的云端方案，用户仍需对 Mozilla 及其合作方报以无法自行验证的信任。

**标签**: `#AI`, `#Mozilla Firefox`, `#Privacy`, `#On-device Inference`, `#LLM Deployment`

---

<a id="item-5"></a>
## [唐山钢坯上涨 20 元，钢价或震荡偏强](https://news.google.com/rss/articles/CBMiaEFVX3lxTE45UXlhd3pVRmEyR0VlUEZXNGUtcE1rcms1R0d4Q1lYWnpmMHZSMFNYa0dYSjhLVGJVbnFGUTQzR0ZmenR5dFl5TWxUamdqZ0Ntb3puMGs0RW9MNnBIRHI4WWtTbVMtclZI?oc=5) ⭐️ 7.0/10

我的钢铁（Mysteel）发布的每日钢市报告显示，唐山钢坯价格上调 20 元/吨，钢材价格预计将震荡偏强运行。 唐山钢坯是中国钢材需求与定价的重要先行指标，上涨 20 元反映市场情绪转强，将直接影响钢材加工企业、贸易商以及下游建筑采购方的成本与拿货节奏。 该内容属于例行每日行情快评，并未附带数据表格；20 元的涨幅相对温和，而 Mysteel 此前的周度调研显示唐山钢坯价格每周波动剧烈、常出现快速反转，因此“震荡偏强”更偏向方向性判断而非确定预测。

rss · Google News - 钢材加工配送 · 9月16日 09:57

**背景**: 唐山位于中国北方的河北省，是全国最大的钢铁产区，其钢坯价格被广泛视为全国钢市情绪的风向标。钢坯属于半成品连铸坯（方形或矩形钢坯），需要经过进一步轧制加工，才能成为螺纹钢、线材、型钢等建筑与制造业用成品钢材。我的钢铁（Mysteel）是中国主要的大宗商品价格与数据服务机构，其每日钢市快评被贸易商和钢厂广泛参考。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Steel_billet">Steel billet</a></li>
<li><a href="https://www.steelprices.com/news/china-tangshan-billet-prices-trend-downwards/267">China Tangshan billet prices trend downwards</a></li>
<li><a href="https://www.kallanish.com/en/prices/details/tangshan-billet/">Billet / Tangshan Ex-Works CNY/t - Kallanish</a></li>

</ul>
</details>

**标签**: `#steel prices`, `#steel distribution`, `#Tangshan billet`, `#commodity markets`, `#construction materials`

---

<a id="item-6"></a>
## [香港五年规划：逾半公营房屋采用 MiC 建筑，公屋轮候时间降至四年以下](https://news.google.com/rss/articles/CBMiuwNBVV95cUxNd19VVXgxRUtNbm11M3JPUFFYX0JmQlg2NFpJdkpzNENUNV91aXZ4cm8xODdtaEdoM1R0dUlTYmdlZURMUldPZmZwYTJMc0lGaE91OVRPbEVjUzF4NU9zcDlrbC1hZ2JwWEVCNXo5eTA2aldQd2hWbW1WZUJSRk9YMFNYNTFLMW5FUWYwRnZ3U0xKbGJKeEUtUWUwNFNnMjZ5Qk94a01lUnVZa1AwN1ZkWUJlRWxoaGo2SnhndHgtbm5jdTBMNTZFWUtsWkVwVFNCdm00dk92ajVBbHdlcHJfX29wNkIydXhUWmJoZlZyY3MyYjRGZGxoOHB3dU5HMlRSOF9ZWlM1UVNNcVZmSGRtdjVVTE4xZnpZYVY2VFNoS3NpcTFaaDhxdUhzbllFdDJFOEQxZXJsdmxsYUE3U3p4N3RMRGd2ZktkQjJteWxoQlpmWjRlWXhOYnBySGU4Y01TZGFXWm14bXRjcmp6aFo0ajhXQkpVLUEyUENMRVVKWHM5LWR4QlBsblJmZnhoaXRrWUdlR3lhdW10cktyWG5ERm1yZDhhTWxNVHIwa1FxUkVqZzM3Q2pOZTR0SQ?oc=5) ⭐️ 7.0/10

香港最新的五年规划提出，超过一半的公营房屋将以「组装合成」建筑法（MiC）建造，并预计规划期内公屋平均轮候时间将由约四年降至四年以下。该政策信号由《香港 01》报道，把工业化建造的强制要求与可量化的房屋供应目标直接挂钩。 这对建造业供应链是一个具有决策价值的需求信号：政府承诺 MiC 占公营房屋多数工程量，意味着模块工厂、承建商、物流与吊装能力将获得多年期的订单储备。其社会意义同样重大，因为公屋轮候时间是香港最受关注的民生指标之一，而推动行业转向场外制造也有助于缓解长期存在的熟练建筑工人短缺问题。 该报道并未给出技术参数，例如模块类型、楼层数、合约金额或交付时间表，因此实务上真正的疑问在于 MiC 工厂产能、熟练安装工人与工地物流能否同步扩张以承接这一要求。MiC 模块通常在受控的工厂环境中预制，再运至现场吊装组装，对施工排序与重型吊装能力要求很高，而非依赖传统的湿作业工种。

rss · Google News - 工业化建造与智能空间 · 9月16日 04:47

**背景**: 「组装合成」建筑法（MiC）是一种把整个房间或建筑单元在场外工厂预制为独立模块，再运至现场堆叠并连接的建造方式。它属于工业化建造大趋势的一部分，即把预制、标准化与自动化等制造业原则引入长期在生产力上落后于一般制造业的建筑业。香港近年已在公营房屋试点、检疫及医院设施和其他政府项目中采用 MiC，主要目的是加快交付速度并减少对稀缺现场工人的依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.promat.com/en-hk/construction/hong-kong/modular-integrated-construction/">Modular Integrated Construction - Promat Hong Kong</a></li>
<li><a href="https://en.wikipedia.org/wiki/Industrialization_of_construction">Industrialization of construction - Wikipedia</a></li>
<li><a href="https://www.gharpedia.com/blog/modular-integrated-construction-evolution/">Modular Integrated Construction : Building the Future</a></li>

</ul>
</details>

**标签**: `#MiC`, `#industrialized construction`, `#Hong Kong housing policy`, `#public housing`, `#construction demand`

---

<a id="item-7"></a>
## [摩根大通：开源冲击与 AI 安全均非威胁，半导体设备将成新瓶颈](https://news.google.com/rss/articles/CBMiU0FVX3lxTE92QW55blNNLTZYWm11Wmx1ZFYzbEVEdkJad0JVWlBXY193MFRtM2Fyakw2NXFtQ292XzREZUstcnpGM2hScUtsYzVka2FSMFo3VXRz?oc=5) ⭐️ 7.0/10

摩根大通分析师 Gokul Hariharan 等人在 9 月 16 日发布的亚洲科技策略报告中，逐一回应了市场近期的三大疑虑——开源大模型崛起、AI 安全监管呼声升温、以及超大规模云厂商自由现金流转负——并得出结论：算力需求的基本面并未动摇。该行认为未来两年 AI 资本开支周期仍将延续、仍有增长空间，而半导体设备将在 2027 年前后取代芯片本身，成为整条供应链最关键的瓶颈。 这是卖方机构对“廉价开源模型与监管风险将戳破 AI 基础设施泡沫”这一叙事的明确反驳，同时也给投资者提供了一个具体的供应链信号：稀缺性和价值可能从 GPU 转向建设晶圆厂与产能所需的资本设备。若该判断成立，半导体设备厂商、其零部件供应商以及设备交付周期，将成为决定 AI 算力实际落地速度的关键限制因素。 报告将 AI 安全监管视为短期扰动而非结构性威胁，并认为开源模型可能压低单位 token 成本，但不会削减总算力需求。其最具体的判断是下一个约束出现的时间点——半导体设备将在 2027 年前后成为最关键瓶颈——这意味决定 AI 建设节奏的将是产能扩张计划，而不是芯片设计。

rss · Google News - EDF AI 部署工程 · 9月16日 03:13

**背景**: AI 资本开支指的是微软、谷歌、亚马逊、Meta 等超大规模云厂商在数据中心与基础设施上的巨额投入，它带动了 GPU 及整个 AI 供应链的需求。所谓“开源冲击”，是指市场担心免费或低成本的开源权重模型会冲击昂贵闭源 AI 的商业逻辑，从而减少对算力的需求。半导体设备则指建设与扩产晶圆厂所需的光刻、刻蚀、薄膜沉积等工具；当需求增速超过设备供给能力时，设备厂商就会成为整个产业的卡点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.qq.com/rain/a/20260916A06UMT00">摩根大通：“开源冲击”、“AI安全”都不是问题，未来两年资本开支仍有空...</a></li>
<li><a href="https://news.smm.cn/news/104117885">摩根大通：未来两年资本开支仍有空间 半导体设备将成“新瓶颈”</a></li>
<li><a href="https://www.toutiao.com/article/7685972475926889010/">摩根大通：“开源冲击”、“AI安全”都不是问题，未来两年资本开支仍有空...</a></li>

</ul>
</details>

**标签**: `#AI capex`, `#semiconductor equipment`, `#AI compute`, `#supply chain`, `#JPMorgan`

---

<a id="item-8"></a>
## [OpenAI、Anthropic 与谷歌 DeepMind 开始合作研究 AI 安全措施](https://news.google.com/rss/articles/CBMiWEFVX3lxTE1aU2w0MHp3UHNHZWE3LThlcW5CZFp2SUZ0bkJOaTFVeFVidDZzY0tXSncwUzFFWExyc3dsOHhWZFp1azNMRkpDekEzUHJxc1BPcHBBUURybVY?oc=5) ⭐️ 7.0/10

据白鲸出海等媒体报道，OpenAI、Anthropic 与谷歌 DeepMind 这三大前沿 AI 实验室据称已开始就 AI 安全措施展开合作研究。相关报道还提到，OpenAI 同期正在洽谈新一轮融资，估值可能高达 1.2 万亿美元。 这三家实验室过去长期激烈竞争，其安全工作（例如扩展策略与负责任扩展框架）大多各自独立发布，因此任何联合行动都意味着前沿领域正在向共享行业规范靠拢。若合作能产出共同的安全标准，将影响整个 AI 生态中模型部署、评估乃至监管的走向。 目前该消息仍停留在标题层面：没有披露具体工作组名称、研究范围、时间表或联合技术框架，因此无法判断这是正式的共同研究、共同原则声明，还是在模型评估方面的协调。报道中提到的 OpenAI 1.2 万亿美元估值融资洽谈，属于与安全议题并列出现的另一条财务消息。

rss · Google News - EDF AI 部署工程 · 9月16日 02:15

**背景**: AI 安全（AI Safety）是一个较大的问题域，关注的是如何确保 AI 系统不造成危害；而 AI 对齐（AI Alignment）则是更具体的研究目标，即让模型行为符合人类意图与价值观，通常被描述为“前向对齐”（构建行为良好的系统）与“后向对齐”（评估并纠正它们）构成的循环。AI 治理（AI Governance）则指引导这些系统如何被构建与部署的规则、机构与激励机制。长期以来，前沿实验室更多依靠自愿的、单方面的承诺来推进这些工作，而非联合项目；由于最有能力的模型掌握在少数几家大实验室手中，它们之间的合作被普遍视为任何真正约束前沿的安全标准得以成立的前提。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://swarma.org/?p=48540">北大发表 AI Alignment 综述：确保 AI ...</a></li>
<li><a href="https://hub.baai.ac.cn/view/35378">北大发表 AI Alignment 综述：确保 AI ...</a></li>
<li><a href="https://www.secrss.com/articles/65179">AI Safety 与 AI Security：探索共同点和差异</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#AI governance`, `#OpenAI`, `#Anthropic`, `#Google DeepMind`

---