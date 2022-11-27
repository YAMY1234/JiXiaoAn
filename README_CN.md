<div align="right">
  語言:
  中文
  <a title="English" href="/README.md">英文</a>
</div>
[TOC]

# 简介

   物联网(IoT)技术的快速发展产生了大量的流量，其中通常包含正常生产或违规行为的产生的可能会损害物联网通信安全的各种问题，例如自动驾驶、工业物联网、智能家居等领域。收集这些流量可以检测通过物联网网络的入侵。尽管在注释物联网流量记录方面做了很大的努力，但标记记录的数量仍然非常少，增加了识别恶意攻击的难度。我们实现了一种基于异常的半监督深度学习方法(ESet)的入侵检测系统—济小安-物联网质性入侵检测系统。

   济小安致力于设计一款**质性**物联网入侵检测系统，及**高精确度、快速、鲁棒、轻量级**的基于半监督学习的入侵检测系统。它可以部署在[物联网平台](http://www.nlecloud.com/about)上，在云端层上训练模型且在检测层进行流量检测，兼具轻量和实用的特点。

   我们预设了半监督入侵检测框架的应用模型，由云端层、检测层和边缘层构成。由在完成边缘层的流量收集后，将在云端层将收集到的流量进行特征处理、模型训练等工作，并在检测层对流量进行异常检测。在强大的深度学习预测速度与准确度的支持下，能够对于物联网系统的入侵检测行为进行实时预测，并对使用者进行警报。

   在创新性上，我们设计了一个半监督的模型架构以用于实时应用半监督预测，充分利用未标记的网络流量数据来构建一个实时的NID系统，利用自主设计的可信度选择器模块，基于kitnet算法对恶性流量数据的敏感性，为伪标签的质量提供保证。我们提出了频域编码变换器，它实现了对提取的频域特征和字节编码特征的分析。

   在运行效果上，考虑到人工标记大量物联网记录困难的前提，仅一小部分物联网流量可以被标记，剩下的大部分是未标记的。本系统能够从少量标记的数据和大量未标记的数据中高效的学习：在IDS2017和IDS2018数据集上用小部分的标注数据（10％）取得了优异的性能（F1-score：99.48％）。在极端情况下，仅用1％的数据，F1值超过97％。我们同时关注模型鲁棒，对于目前针对ML/DL弱点的攻击，我们通过模拟敌手的行为进行不同类型的测试，PDR小于5%，表现了济小安的高鲁棒性。

   物联网因为其具有开放性、多源异构性、泛在性等特性，物联网的安全关系到个人、家庭、社会、乃至国家的安全。在商业价值上，根据Gartner网络安全行业产品结构比例分布，2019年，我国入侵检测/防御设备市场规模约为19亿元。因此，济小安-物联网质性入侵检测系统，因其具有高精确度、快速、鲁棒、轻量级的实用特性，在未来市场上具有较为广泛的应用场景。

   # 作品概述

      ##  背景

   物联网(IoT)技术的快速发展，促进了各种创新服务和应用的发展，如智能制造、智能医疗保健和智能交通。大量的物联网通信在各种物联网实体之间进行通信，传递信息，如交换机控制、智能设备管理、通信细节和设备维护细节，其中通常包含正常生产或违规行为的产生的可能会损害物联网通信安全的各种问题。

   物联网的通信网络系统主要用于将感知层获取的信息在网络中进行传递和处理。由于物联网涉及的网络多种多样，从感知层的无线、红外线等射频网络，通过无线接入网，例如窄带物联网络、无线局域网、蜂窝移动通信网、无线自组网等，经过互联网，到达物联网应用层平台，因此物联网面临的网络安全威胁更为复杂，具体有四方面安全隐患。

   无线数据传输链路具有脆弱性

   物联网的数据传输一般借助无线射频信号进行通信，无线网络固有的脆弱性使系统很容易受到各种形式的攻击。攻击者可以通过发射干扰信号使读写器无法接受正常电子标签内的数据，或者使基站无法正常工作，造成通信中断。 另外无线传输网络容易导致信号传输过程中难以得到有效防护，容易被攻击者劫持、窃听甚至篡改。

   传输网络易受到拒绝服务攻击

   由于物联网中节点数量庞大，且以集群方式存在，攻击者可以利用控制的节点向网络发送恶意数据包，发动拒绝服务攻击，造成网络拥塞、瘫痪、服务中断。

   非授权接入和访问网络

   用户非授权接入网络，非法使用网络资源，或对网络发起攻击；用户非授权访问网络，获取网络内部 数据，如用户信息、配置信息、路由信息等。

   通信网络运营商应急管控风险

   对于通信网络运营商来说传统的短信、数据、语音等通信功能管控主要依据单一设备、单一功能、单一用户进行。但物联网设备终端规模大，且不同业务的短信、数据等通信功能组合较多，若不能在网络侧通过地域、业务、用户等多维度实施通信功能批量应急管控，则无法应对海量终端被控引发的风险。

   ##  相关工作

   入侵检测系统（IDS）已被引入，以识别避开安全技术的入侵行为。入侵可以定义为任何类型的对信息系统造成损害的未经授权的活动。这意味着任何可能对信息机密性、完整性或可用性构成威胁的攻击都将被视为入侵。例如，使计算机服务对合法用户无响应的活动被视为入侵。IDS 是一种软件或硬件系统，用于识别计算机系统上的恶意行为，以便维护系统安全。IDS 的目标是识别传统防火墙无法识别的不同类型的恶意网络流量和计算机使用情况。这对于实现对损害计算机系统可用性、完整性或机密性的行为的高度保护至关重要。

   总体上来说，IDS 系统可以大致分为两类：基于签名的[入侵检测](https://so.csdn.net/so/search?q=入侵检测&spm=1001.2101.3001.7020)系统 (SIDS) 和基于异常的入侵检测系统 (AIDS)，以下分别介绍：

   基于签名的入侵检测系统 (SIDS)

   基于签名入侵检测系统 (SIDS) 是基于模式匹配技术来发现已知攻击，也被称为基于知识的检测或误用检测。在 SIDS 中，匹配方法用于查找先前的入侵。换言之，当入侵特征与特征数据库中已经存在的先前入侵的特征相匹配时，触发警报信号。对于 SIDS，检查主机的日志以查找先前被识别为恶意软件的命令或操作序列。 SIDS主要思想是建立一个入侵特征数据库，并将当前活动集与现有特征进行比较，如果发现匹配则发出警报。SIDS 通常对先前已知的入侵提供出色的检测精度。然而，SIDS 难以检测零日攻击，因为在提取和存储新攻击的签名之前，数据库中不存在匹配的签名。 SIDS 被用于许多常用工具，例如 Snort (Roesch, 1999) 和 NetSTAT (Vigna & Kemmerer, 1999)。 SIDS 的传统方法检查网络数据包并尝试与签名数据库进行匹配。但是这些技术无法识别跨越多个数据包的攻击。由于现代恶意软件更加复杂，可能有必要从多个数据包中提取签名信息。这需要 IDS 调用早期数据包的内容。关于为 SIDS 创建签名，通常有许多方法可以将签名创建为状态机 、正式语言字符串模式或语义条件。零日攻击的频率越来越高，这使得 SIDS 技术的有效性逐渐降低，因为任何此类攻击都不存在先前的签名。恶意软件的多态变体和不断增加的针对性攻击可能会进一步破坏这种传统范式的充分性。SIDS的大体结构如图1所示。

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=YTM1NTI0NzNmMTZmMGYzOTYwNmIyMDgxYzNhYWQ4ZGVfcUxXTjF3SWFxeGNTdEEyYzh1djZLeVI5ZU1EREY5Rm9fVG9rZW46Ym94Y25FY2paS1RQRm1zQ1ZGb0pGUm5EUm9nXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   图 1 SIDS架构图

   基于异常的入侵检测系统（AIDS）

   AIDS由于能够克服SIDS的局限性而引起了许多学者的关注。在AIDS中，计算机系统行为的正常模型是使用机器学习、基于统计或基于知识的方法创建的。观察到的行为与正常模型之间的任何显着偏差都被视为异常，可以解释为入侵。这组技术的假设是恶意行为不同于典型的用户行为。异常用户的与标准行为不同的行为被归类为入侵。AIDS的发展包括两个阶段：训练阶段和测试阶段。在训练阶段，正常流量配置文件用于学习正常行为模型，然后在测试阶段，使用新数据集建立系统泛化到以前未见过的入侵的能力。AIDS可以根据训练的方法分为许多类别，例如，基于统计的、基于知识的和基于机器学习的方法。 AIDS 的主要优点是能够识别零日攻击，因为识别异常用户活动不依赖于签名数据库。当被检查的行为与通常的行为不同时，AIDS会触发危险信号。SIDS 只能识别已知的入侵，而 AIDS 可以检测零日攻击。然而，AIDS 可能导致高误报率，因为异常可能只是新的正常活动，而不是真正的入侵。

   对于物联网网络来说，识别未知入侵的困难是一个特别的问题，因为物联网网络连接了大量具有不同计算资源、通信技术、电池容量、软件和操作系统的设备。这种异质性挑战了安全解决方案的部署，增加了攻击面，使物联网网络更容易受到新的和陌生的入侵[1]-[3]。传统的机器学习（ML）技术[8]已被证明可以有效地识别物联网流量中的重要模式，从而熟练地识别网络攻击[4]。然而，ML也被证明无法扩展到巨大的数据集（即具有一百多个特征的数百万条记录），并且在物联网节点极其分散的情况下，ML在检测入侵/网络攻击方面的表现也不尽人意[5]，[6]。另外，深度学习（DL）技术的不断改进激发了新的IDS，它能够很好地处理和处理所需的入侵/网络攻击、难度和复杂程度以及分布水平[7]。

   ML/DL等人工智能方法一直是在物联网[7]、[9]、[13]环境中开发可靠IDS的一个重要挑战。在这方面，目前检测物联网入侵的方法可以分为三个不同的方面。

   有监督的方法

   有监督的ML或DL方法通常使用有标记的物联网记录进行训练，以区分正常记录和其他攻击记录（即二进制分类），或从正常流量中区分不同的攻击类别（即多类分类）。传统的机器学习方法在物联网IDS上得到了应用。例如，Yang等人[28]利用k-近邻(kNNs)为大规模物联网数据开发了一个安全的IDS。也有使用深度学习的方法，例如Gao等人[12]分别使用LSTM和前馈神经网络(FNN)来检测入侵，并在集成架构中进行了实验。尽管监督方法在IDS中取得了较高精确度，但由于有标签物联网数据的缺乏，它们并没有得到普及[10]。此外，当数据在类之间不均匀分布时，它们的性能很差（类不平衡问题）。这促使我们使用半监督学习来开发高效的AIDS。

   无监督的方法

   数据或流量标签被称为无监督的IDS。这种方法不需要任何流量标签，因此具有成本效益，而且它们利用物联网流量样本的固有特征来区分不同的攻击。因此，它们能够可靠地识别出新的攻击。例如，Ergen和Kozat[14]利用了一个LSTM架构来处理物联网流量的序列，并生成一个固定长度的序列。然后，他们使用单类SVM和支持向量数据描述技术来计算最终的分类决策。Vu等人[11]开发了一个正则化版本的AE架构来学习输入流量的潜在表示，利用它来微调监督学习者的性能。然而，对于这些方法来说，虽然不需要对数据进行人工标注，但它们并没有给出非常可观的性能和稳定的结果。此外，它们没有监督方法的鲁棒性能，特别是在识别以前识别的攻击方面。其次，它们表现出较高的计算复杂度，这限制了它们在实时或资源限制的物联网应用[1]、[14]、[15]中的适用性。

   半监督的方法

   半监督方法使用有注释和未注释的样本来训练特定的分类器，特别是当有少量的标记样本可用时。许多这样的技术已经被开发用于检测物联网流量中的入侵，并已证明了良好的性能[15]，[16]。例如，Ravi和沙利尼[17]开发了一种半监督ML方法来检测网络攻击，通过集成监督神经网络和重复随机抽样的无监督数据聚类。Gao等人[18]通过集合学习提出了一种新的基于模糊性的半监督学习方法，在 "KDDTest+"和 "KDDTest-21 "数据集上实现了84.54%和71.29%的准确率。与监督方法相比，他们在识别先前识别的攻击方面的性能仍然很低。换句话说，他们需要更多的标记数据来提高其性能。Abdel-Basset等人使用了25%的标记数据，实现了98%的F1值。在我们的模型中，我们只使用了10%的标记数据，实现了99%的F1值。此外，模型的稳健性也很少受到关注。与现有方法相比，我们的方法提高了检测精度、标注数据的利用效率和模型的稳健性。

   ##  作品介绍

   物联网(IoT)技术的快速发展产生了大量的流量，其中通常包含正常生产或违规行为的产生的可能会损害物联网通信安全的各种问题，例如自动驾驶、工业物联网、智能家居等领域。收集这些流量可以检测通过物联网网络的入侵。尽管在注释物联网流量记录方面做了很大的努力，但标记记录的数量仍然非常少，增加了识别恶意攻击的难度。我们实现了一种基于异常的半监督深度学习方法(ESet)的入侵检测系统—济小安-物联网质性入侵检测系统。

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=Yjg1MmVmM2EyYjNiNmE1NDFjODU0MGQ3NDMzMWVmOGFfN1M3RmRzbFRUM3lXeFY4dzk2VmZ2bUdPd1J3Z1VsdHRfVG9rZW46Ym94Y25YdGpkaTM3RGdIcXVLTUtyWldWV1FmXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   图 2 物联网通信应用场景

   济小安致力于实现一个高精确度、快速、鲁棒、轻量级的基于异常的入侵检测系统。它可以部署在[物联网云平台](http://www.nlecloud.com/about)上，在云端层上训练模型且在检测层进行流量检测，兼具轻量和实用的特点。

   我们预设了半监督入侵检测框架的应用模型，由云端层、检测层和边缘层构成。由在完成边缘层的流量收集后，将在云端层将收集到的流量进行特征处理、模型训练等工作，并在检测层对接下来的流量进行异常检测。在强大的深度学习预测速度与准确度的支持下，能够对于物联网系统的入侵检测行为进行实时预测，并对使用者进行警报。

   在创新性上，我们设计了一个半监督的模型架构以用于实时应用半监督预测，充分利用未标记的网络流量数据来构建一个实时的NID系统，利用自主设计的可信度选择器模块，基于kitnet算法对恶性流量数据的敏感性，为伪标签的质量提供保证。我们提出了频域编码变换器，它实现了对提取的频域特征和字节编码特征的分析。

   在运行效果上，我们工作的亮点有两点。一是在人工标记大量物联网记录变得困难的前提下，只有一小部分物联网流量可以被标记，剩下的大部分可以是未标记的，济小安能够从少量标记的数据和大量未标记的数据中中高效的学习，在IDS2017和IDS2018数据集上用小部分的标注数据（10％）对NID取得了优异的性能（F1-score：99.48％）。在极端情况下，仅用1％的数据，F1值就超过97％。二是对模型鲁棒性的关注，对于目前针对ML/DL弱点的攻击，我们通过模拟敌手的行为进行不同类型的测试，PDR小于5%，表现了济小安的高鲁棒性。

   物联网因为其具有开放性、多源异构性、泛在性等特性，物联网的安全关系到个人、家庭、社会、乃至国家的安全。在商业价值上，根据Gartner网络安全行业产品结构比例分布，2019年，我国入侵检测/防御设备市场规模约为19亿元。因此，济小安-物联网质性入侵检测系统，这样一个高精确度、快速、鲁棒、轻量级的实用系统，我们相信，这一产品的未来发展，将有无限的可能！

   ##  本作品要解决的痛点问题

   相对于基于签名的入侵检测系统 (SIDS)的入侵信息的收集和更新困难，难以检测本地入侵和新的入侵行为，维护特征库的工作量巨大；基于异常的入侵检测系统（AIDS）能够检测新的入侵或从未发送的入侵；对操作系统的依赖性较小；可检测出属于滥用权限型的入侵。因此我们主要致力于对AIDS的研究，特别是关注人工智能技术在其中的应用。

   对于2.2中提到的ML/DL中的方法，我们已经分析了有监督、无监督、半监督方法目前所面临的问题，因此我们提出了基于频域编码变换器的半监督的ESet。ESet致力于实现一个高精确度、快速、鲁棒、轻量级的AIDS，旨在检测物联网网络产生的流量记录中的网络攻击，在训练过程中利用有标签和无标签的流量序列的优势。

   综上所属，我们主要解决的痛点问题包括以下方面：

   标签化数据短缺。由于物联网数据规模的快速和极度增加，很难获得最新的有标签的物联网流量数据集，特别是用于入侵/网络攻击检测。因此，从未标记的数据中学习已经成为物联网环境中一个重要的研究挑战。
     已标记数据的利用效率。人工标记大量物联网记录变得困难。然而，一小部分物联网流量可以被标记，剩下的大部分可以保持未标记的。我们使用了半监督的DL方法，非常适合这种情况，能够从少量标记的数据中有效的学习，达到了10%的有标记数据99%的F1值的精确率。
     模型的鲁棒性是大多数IDS忽略的问题。我们考虑了三种不同的攻击方式，使用白盒灰盒黑盒攻击模拟敌手的行为并抛弃了不切实际的假设对ESet进行攻击。从测试结果来看，反映了ESet的高鲁棒性。

   # 作品设计与实现

      ##  总体设计与功能介绍

   我们设计了济小安在现实世界物联网网络中的应用模型和功能。下图展示了济小安中半监督入侵检测框架的应用模型。

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=ODljM2Q5ODFkNjg5MDA4ZDZkNDFiNDY5MTlkMGYzNmZfOUFtRFRqZjhER3pzWWVZYXRScTlNQVh1NmxiTFhKWWdfVG9rZW46Ym94Y25RdEVETjB0Y2xpcW5Kc1ZKZTFkWEplXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   图 3 半监督入侵检测框架的应用模型

   物联网网络的结构主要由三层组成，即云端层、检测层和边缘层。

   云端层拥有高度和强大的计算资源；因此，模型训练的过程是在这一层进行的，因为训练需要获得大量的物联网跟踪数据。这样的大数据可以很容易地被汇总并存储在云端。此外，云端层还存储了模型配置、旧的预训练版本和其他与训练交易有关的设置。

   检测层通常由许多雾服务器/设备组成，使计算更接近物联网网络的边缘。在物联网网络中，检测层具有关键作用，因为它是发生入侵检测的地方。具体来说，每个检测节点由四个主要部分组成，即：1）流量聚合部分；2）流量准备部分；3）流量对策部分；和4）流量诊断。流量聚合组件负责捕捉和接收来自边缘物联网网络连接部分的物联网流量记录，然后将成批的样本传递给准备阶段。流量准备组件负责将收到的批次转换为标准格式，应用必要的数据清洗和规范化。之后，流量诊断组件被指定使用**济小安对准备好的物联网流量数据进行分类**， 而无需与云端后端进行任何通信，从而防止任何延迟。这个分类过程可以在二元类或多元类的情况下进行。一旦一个活动被确定为攻击，所提供的活动信息就会被转发到云端后端进行简要介绍。每个检测节点负责诊断物联网网络的相关区域。因此，所有的物联网流量记录都被在混杂模式下运行的相应雾化设备所捕获。例如，鉴于底层物联网网络的一个特定区域的流量发生了重大变化，如果这些变化是恶意的，即拒绝服务（DoS）事件，济小安将识别它们并传达对策组件。当改变是良性的，就必须将一些节点连接到另一个可访问的雾化设备上，以减轻它变成拥堵的情况。毕竟，反措施组件采取从济小安产生的决定，然后执行必要的预定的反措施模块，即警告、阻止和删除行动。在此之后，关于已确定的行动的信息被传输到云端，用于结果的日志组件。

   最后，边缘层由边缘节点和边缘设备（即笔记本电脑、智能手机、智能手表等）组成，通过路由和交换设备通过物联网网络进行通信，并同时与特定的雾服务器/节点连接，作为通往云端后端的计算桥梁。

   ##  设计方案

          ###   系统环境设计方案

   现在所有的云端的物联网平台和设备之间的通讯，本质上都是建构在TCP/IP协议之上的，只是对数据包的再封装而已，基于此我们可以是用Wifi，4G来实现设备和云平台的通讯。

   基于济小安预设的应用场景模型，我们设计了一个真实的物联网网络系统实例。同时将“济小安——物联网网络检测专家”内嵌入检测层节点中，具体网络拓扑结构如下所示。我们使用Windows 10 x86系统主机模拟了检测层节点，为了简化配置实例，在完成边缘层的流量收集后，按照我们的预测应用场景，接下来将在云端层进行模型训练、检测层预测，这里简化为使用云层训练好的模型，直接在检测层完成模型的预测。此架构是最简单的架构，设备就如同我们的手机，基于移动通讯来上网。

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=YjJjYTE5MDFjYWQzZTM5ZTc4OTRkNzk4NjZkNTYzYzVfdXNzR0xVRjV5Y1dsOUN0QlIyZEZIUlBmRFNLdlZ6bmtfVG9rZW46Ym94Y240eElXQjRSeG1zbWZidVh6aDBsOFFjXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   图 4 实例系统环境

   #### 设备硬件

   云层环境：

   英特尔公司Sky Lake-E,12多核处理器上建立实验环境，使用Ubuntu 18.04.6 LTS, 3.10.0-1062.9.1.el7.x86_64操作系统；我们还使用NVIDIA公司的GV104[GeForce GTX 1180]作为我们的GPU环境来加速我们的实验。加速我们的实验。

   检测层设备：

   Honor Magic Book 2019笔记本搭载Windows 10 x86系统

   边缘层设备：

   Honor20智能手机

   小米全面屏电视EA65

   荧石C6CN星光监控摄像头*2

   xiaomi watch S1智能手表

   #### 拓扑结构描述

   **主机服务器**：windows系统的电脑，并且将其设置为一个WIFI热点，然后让我们家中的设备都连接到这个WIFI上来,组成一个物联网，以此让所有设备的数据流量都通过该服务器，并在该服务其上部署济小安——物联网网络检测专家。

   **济小安——物联网网络检测专家**：检测系统会分析每一个设备的流量信息，一旦发现有到达一定阈值的恶意攻击流量到来就会通过电子邮件的方式发出警报，提醒相关工作人员注意检查网络环境，必要时断开相关设备的网络连接。

   **网络入侵拓扑结构示例**：以下是一个设想网络入侵的的拓扑图，一个黑客从外部接入或者突破连接到了内网，然后向摄像头1发送恶意网络数据，然后会由我们软件检测到，然后发送预警信息给相关的人员，然后由相关人员再去检测。

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=YzM5ZDZmOTY5ZTc3NjU1ODdlNzlmZTg0MzM3YjU4ZmFfU3dKRTY4d2p5T1RHYUMwc0duMmdUYVdZcWRFNVplT0NfVG9rZW46Ym94Y25UYnhDV01oNVFmNjEzczJ3YlJNZmhnXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   图 5 网络入侵报警示例

   ### 底层算法设计方案

      ####  方法概述

   物联网网络入侵检测(IoTNID)作为一种重要的主动安全防御技术，旨在实现对网络攻击事件的精确检测。近年来，许多有监督和无监督的方法已经被提出来用于IoTNID。然而，这些方法主要面临两个挑战。首先，绝大多数的网络流量数据是没有标记的，现有的方法不能有效地将这些未标记的数据与现有的已标记的网络流量数据相结合，以提高检测的准确性。其次，他们不能从不同层次的网络流量数据中学习特征，如数据包层次和流量层次，从而对网络流量特征有全面的了解。为了应对这些挑战，我们提出了一种基于双特征编码变换器的极端半监督模型(ESeT)，它仅仅使用极少量的标记数据，充分利用了未标记的网络流量数据来丰富提取的特征信息信息，并通过可信度选择器(Confidence Selector)来减少错误的伪标记的负面影响。此外，我们提出了一个多级特征表示学习模块(Multi-level Feature Extraction)，以学习流量级频域特征和数据包级字节编码特征。实验结果表明，我们的模型不仅在IDS2017和IDS2018数据集上以小比例的标注数据(10%)实现了对NID的出色表现 (F1分数: 99.48%)。

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=ZGQxZjAwYjJkMGJkYjhjOWQ3NWZhZDQwMGIwODFiZmRfUWpBME9nQXRTTlB3cGcyaEx3dWFKOUtsUHJrSTh5dmtfVG9rZW46Ym94Y25JMlpiSkgwSGZiWUo3TGdOd1RoRjVjXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   图 6 Eset总体架构

   上图展示了我们物联网网络系统的底层深度学习基础——ESeT，它由两个模块组成，即多级特征提取和半监督的双特征编码转化器。多级特征提取包括字节编码和频域特征提取，目的是提取网络工作流量的字节特征和频域特征。半监督式双特征编码变换器包含双特征编码变换器作为预测、可信度选择器和特征增强器的核心组件，它描述了半监督式的训练过程。由已标记和未标记的pcap数据包组成的原始输入数据被发送到多级特征提取模块。在提取之后，处理后的数据被提供给半监督训练模块进行预测。

   ####  多层次特征提取

   网络流量首先被过滤并分离成会话。然后将通过随机矢量字节编码和频域特征提取对过滤和分离的网络流量进行分析，提取字节特征和频域特征。

   1、随机矢量字节编码

   （1）匿名化。

   网络流量数据中的地址，包括MAC源地址和目的地址，以及IP源地址和目的地址可能会泄露流量数据的类别标签，我们使用匿名化处理这个问题，将所有MAC地址替换为00:00:00:00:00，所有IP地址替换为0.0.0.0。

   （2）数值编码

   在对数据包进行匿名处理后，我们以二进制格式读取数据包，并将其转换为范围为[0-255]的8位整数序列。

   （3）长度均匀

   我们确定;为数据包长度。对于每个数据包的数据，我们将其截断或将低于该长度的数据填充为0，以保证统一的长度。

   （4）随机矢量编码

   我们使用随机初始化向量的方法，用随机初始化的浮点向量来呈现原始字节，与一热编码相比，大大减少了空间占用。此外，由于每个数字单位都有一个值，而且数字具有实际意义，它为我们的半监督转化器的后续位置编码和双特征编码提供了一个基础。

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=MjliNTA5ODU5ZGVhODZmMzEzY2M2NTFlMGFjMWMxNGVfOTZLcHhkREFoaVdqUU5na0VGczNxU3J6MXR0aVVCSnJfVG9rZW46Ym94Y25UaVE1VmdKUnNDa3dIN3NOQkhxWUNXXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   图 7 随机矢量字节编码步骤

   2、频域特征提取与分析

   首先我们将所有数据包的每数据包特征表示为矩阵 S，其中 Sik定义为第 i个数据包的第 k个属性，

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=YjVlNDg4ZTU2N2NhODJkZTFjMmJkMzQ3MDNkYzg3NmZfSWJSb21USnp5SG5BMm1DZWNEQnFJY3d6RW85cU5tZ1dfVG9rZW46Ym94Y245bWhJZTlRdnJ2U2hxQlllVEZWUGRQXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   再将 S乘以一个编码向量 w进行线性变换，w的值则由自动参数选择模块实现，得到

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=M2E2OTZjNDU2Y2FiMjRmNzg1NmJhYjk5OTM0YmEwM2NfOHNiT3hTQjlUZmw4WHNnV3ByUFJ6VXhkbnpwd1hQdEJfVG9rZW46Ym94Y25ITGFndWVqS3g4RnE1bFFxRlFpRTljXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   接下来我们需要基于帧的离散傅里叶变换，先将数据包分割成帧，我们将帧的数量表示为Nf ，帧的长度为Wseg，表示为：

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=ZjEzMmM0ZGY3ODgzYmZmMzNlNzllYjhhOTcxMzU1NThfY0tjMFdsSmY3aGJFWFgyMGlTTTl2Q3AxcDhFRG5uVmFfVG9rZW46Ym94Y25hOHBoWkFaRzUybDJadDFMN0ZRY0lsXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   之后我们对每一帧执行离散傅里叶变换 (DFT)，我们可以得到每一帧的频率特征如下:  

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=NzZiYThmYmVlNDc0NmVlNGFlODI5YWY1MjExNzliOTVfZU9NZXFndG93QUx0Smw5cXlqazVaeldyUElvYnVrQ2dfVG9rZW46Ym94Y244MFJZdkdSN3RpUEx0bFg2bkJsVWtoXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   其中，Fik是第 i帧，频率为 2π(k − 1)/Wseg的频率分量。由于傅里叶变换后得到的是复数，不能作为机器学习算法的输入。使用坐标平面法，我们将复数转换为实数，并计算频域表示的模；为了使频域特征在数值上稳定，并防止机器学习训练中的浮点溢出，因此进行对数变换，最终得到如下图为示意的结果：

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=N2M3ZjI1NGJhMTUzOTJjYmM1ZmIwZTFmMzU2ZDRlMjRfYVI0NjE4cnlmVXZNcEZEY0MyNlJ2YnFHa2llMGxLRXZfVG9rZW46Ym94Y25mc1VPUlpNNmJvUU9lSE85d1BLdVRoXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=MmY5Y2ZkMmVjMTgxYjgzNmQwMDVmODI0Yzk2YjUzYzhfdlo0bldPSlc1SUxUdXB0bnFFMU5vSDFkdnV3TU01eG1fVG9rZW46Ym94Y25GTUVZTDVqdWJrM3NBcEFHQWRrWlhjXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   双特征编码变换器(DET)是我们半监督学习模型的核心组成部分。DET本身可以作为一个顶级的监督交通分类模型，在只有少量标记样本的半监督训练中取得了很高的性能。

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=ZDkzY2MyMDBkMjUzMjNhMzRmNzk2ZjA5YTJmMDcwNWVfR1ZlUmsxM3VvTDhGa2V0RVlwWXpsOW14V04xT2FBU21fVG9rZW46Ym94Y25UMDFCcE4wZ3JTOVNyUlFsaGZRc2ZnXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   图 8 多重特征融合编码Transformer

   DET的整体结构如图8所示。DET接收特征提取模块给出的字节编码结果，得到度量I，包含子度量，形状为，每个矩阵代表一个数据包的特征，其中表示用于字节编码的字节数，表示随机字节编码矢量的长度。将频域特征结果融合至Transformer模型。

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=NjI3MWE0ODFiNGY4N2RmNWVlNGE3MTQ4YjNmYTQ2M2ZfelFSemtNb3c2NE15UTB3ak5CWDFmcFZCWVlpREZITGxfVG9rZW46Ym94Y254R1Q4MEJ0SzNBWHhTMW1oSUFqMlJiXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   在位置编码之后，数据将与提取的频域特征一起在双特征编码中进行处理。 双特征编码首先获得频域特征提取的输出，并提取与这些数据包的频域特征相关的矩阵F，其大小为。编码向量V（长度为）被设计用来确定每个频域特征的学习权重，它将通过连续的模型训练自动生成和更新。获得数据包的频域特征值的过程入下列公式所示。

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=NWU5OWJiOWQzNGJkOTAxMjlmZmRmMDJiZDc0N2MxNTdfQjV4Mjh4dndDSXV5ZUxQTzVvSmFaUUdIR2ZtRU10dVdfVG9rZW46Ym94Y25FaGZia1ZaanNCbFIwYll0bTlON21wXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   其中，表示用于选择与DFT的输入数据包相对应的频域特征的0-1索引度量，表示第i数据包在第k属性上的频域特征，V表示编码向量，表示每个数据包的最终频域特征值。

   由于频域特征与字节特征表征在不同的维度，其反映的是该数据包在特定属性上基于流粒度的频域特征。本身不能够简单作为字节属性与原始字节编码特征进行横向拼接。我们在原始编码的基础上实现加权&残差连接操作，得到的结果作为频域特征编码的输出。这样既融入了基于流的频域特征，也保留了原始数据包未改变的字节特征。

   编码器由N个相同的层组成，其中有两个子层，分别代表多头自注意机制和全连接前馈网络层。在两个子层的周围实现了剩余连接，并进行了层的归一化。

   在N个相同的编码器之后，分类层被添加到输出中进行预测。分类层由一个线性子层和一个sortmax子层实现，它将类嵌入到类的数量中，作为最终分类结果的指标。

   ####  半监督训练架构

   模型训练视图

   我们将原始训练数据分为有标签的数据和无标签的数据，以模拟半监督的情况。我们使用等比例筛选法对数据进行抽样，以确保每一类未标记的样本与整个训练数据中的类别具有相同的比例。

   模型预训练

   首先，有标签和无标签的数据都被输入到多级特征提取模块。

    在FE之后，所有的数据样本（包括所有标记的数据和未标记的数据）都被用于可信度选择模块的kitnet训练，同时选择前50/%的标记数据样本对DET进行预训练，以确保它具备基本的流量异常检测能力。

   每一轮训练

   在每一轮中选择一定比例的样本，作为DET和kitnet网络的输入。DET预测分类结果，而kitnet则生成RMSE向量，表示恶性数据和良性数据之间差异的均方根误差。可信度选择器根据对RMSE值和预测结果的判断，筛选出可以作为伪标签原材料的数据。由可信度选择器模块筛选出的合格预测数据将与一定比例的标注样本混合，特征增强模块将可信度选择器的输出与部分标注样本数据进行融合，并进行特征增强。经过处理后，这些数据将作为伪标签数据样本，然后输入到转化器模型进行训练。到此为止，模型进入一个新的半训练回合。

   置信度选择器

   可信度选择器旨在筛选出具有高可信度的预测结果，并抛弃那些低可信度的结果。

   基于kitnet的置信度保障机制

   Kitnet算法的实现是利用与恶性率正相关的RMSE值从DET中过滤出预测结果。Kitnet是Kitsune [23]的轻量级核心算法，用于生成区分恶性流量和良性流量的差异化指标RMSE。虽然对预测来说不够准确，但在我们的实验中，RMSE值被证明是预测结果可靠性的一个很好的评价指标。由于只训练了少量的样本，DET本身并不足以做出精确的分类结果，可信度选择器有助于筛选出具有高可信度的预测结果，并抛弃那些低可信度的预测结果。新一轮的变压器学习的伪标签样本更加准确。

   筛选过滤原理

   在使用预先训练好的kitnet映射器生成RMSE后，可信度选择器会过滤掉RMSE值低于恶性RMSE限值的良性标注数据，以及RMSE值低于良性RMSE限值的恶性数据，良性RMSE限值和恶性RMSE限值都是自动参数，由每轮训练和历时学习。整个过程可以表示为。

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=ZjQwNzk5YTIyNzFiODY0OTFkZTFmNTVhMWNiM2FlZWNfY3JZMG93NEg5WFBMbkxWZ0lPdjNiaXY1d3JERDZpWFRfVG9rZW46Ym94Y25WUGRsYkdNbHl6bFYyQjNLczFWNEJiXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   其中，I表示每轮数据包的输入特征，RMSEs表示RMSE值的向量，、表示良性RMSE阈值和恶性RMSE阈值，mask象征选择高置信度数据的结果指数。

   特征增强模块

   为了保证模型在连续训练过程中不会因为不准确的伪标签而偏离原来的预测精度，我们在每轮伪标签生成中加入一定比例的标签样本。由于同一类型的攻击流量具有相似的频域特征，为了进一步增强特征以获得更好的训练效果，我们随机选择已标注流量数据的频域特征，并将其与原始标注样本中同一类别的预测流量数据的字节编码特征随机交换，生成新的数据样本。

   ### 系统功能设计

   本系统的主要功能是通过收集服务器网卡上流经的各个设备的数据包，然后将其传送给已经训练好的入侵检测模型，得到预测结果，并将其存放在对应的数据库中，之后将数据进行整理传送给前端页面，前端对每一个设备都维护一个表格以进行滚动展示，并且当检测到瞬时恶意攻击的数据包的比例到达一定阈值时，就发出警告。由此就可以实时监控整个物联网中的网络环境，保护各个设备的网络安全。并且经过实验测试，对于在每秒20000个数据包的高负载网络环境下，本系统也能够做到实时的检测分析。

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=ZDY1YWM1NWQ5YTgyYzM3MzBhOTJkNmIxZGNiMzJhYmVfSzdSMENpZERVVzBJUk50cDlxRHJ0a01FeTZwdHBCSUVfVG9rZW46Ym94Y241VzJVVmF2NVZSQk1HT1FOeGJTTVBkXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   图 9 系统功能总览

   ####  运行设计

   程序运行时首先需要选择要捕获的本地网卡，即用来作为热点的网卡。

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=YjM0ZDBlYzg0ZGE0MmM0YTdkNWM5YTg4OTA1NzMyMTlfVHZPaFRWbTBOZXZFaGc1eTFZRDVFOEQ5dTdxVXZpQ0JfVG9rZW46Ym94Y25uZ0V6dUdOY2NJWkc0N0NGaFVick1yXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   选择完成后，程序会扫描所有连接到这个网卡上的设备，然后由用户来选择要监控的设备，这里是全选：

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=ZjFjMmM1YTljNTU4M2Q0NjA1YzJiNTYxNTQwYTRlMDZfTlN5ODl1RHA3MGVxSDJyQWRGSkpra2dTYUh6VHJ6NTJfVG9rZW46Ym94Y25NWG5UT2NZVFVsdTlrS2xERFYwOHVlXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   确定后会进入到监控大屏：

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=NTllOTVjOTE4NTVhYjAyOTM4OWIxMjJiY2Y0OTE5MjJfU091MVc4ZkJ6bTh5ODNraE83Q2tzcVNWYlFUbERzaDZfVG9rZW46Ym94Y25oWEhCa2hsODFiZUt5Yk82bDdpaW1mXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   点击开始开始后程序开始运行。

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=ZWJiMTMyYTZhOTJiYzQ2NTJlNjU3OWQ1MGVhMzM5YmJfWFgySnV0cnVkNVBiRTMzOXNCUmlkbVJIWEdxT3BjV3FfVG9rZW46Ym94Y25FdE1rRmh5T3FhMnhhVmMyTDZMaHJoXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   若某一个设备的恶意包率到达了某一个阈值，就会弹窗警告，并且发送邮件和短信给事先设定的用户：

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=OTBkOTg4ZGUzYThmMDhmNTY3MDM4NDI4YjM4MmQzZjhfaFltWXVPRzlzUGhPcHptZVQ0cGRVOTRINE1ucFZFYlhfVG9rZW46Ym94Y25IZTlVQno2VGJOeGZYdnZCNk1hVkNlXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=MDg5Y2I3OTg3MWIyZDczYmY1Y2ExNDI3MjhiYjhlM2VfZzFWSlBFbGVRSXIwQXlwem1HMFQxdWhid0RZTUdXak5fVG9rZW46Ym94Y25BN2hDSG5PcW9wc3ZaV1hmQ3JIeGFkXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=YjIzOWVlYTcxMWUwNzc3ZWQ4ODU4MzQ1ZDA1MTU1YmFfbDEzQ2xCTXNvc1NwdFFMeW80TnNValJIdWhHTGpIejJfVG9rZW46Ym94Y24wRHJkYnJvTXhnaHBvT2ZiRjBpOHdnXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   ####  系统界面设计技术说明

   本程序使用Python进行开发，使用的Python版本为3.8.6，开发使用的工具是Pycharm，运行的平台为Windows10。

   **Pyqt5前端UI框架实系统现页面设计**。设计过程中秉承接口隔离原则，一个接口只干一件事，一个按钮只对应一个功能，保证了程序功能解耦，高聚合、低耦合。同时充分增加代码的复用性，展示不同设备的数据表都使用同一个类来进行设计、复用。

   **SMTP服务实现163邮箱邮件发送**。我们注册了专门的账号进行邮件发送至系统用户，以将威胁内容向用户进行及时告知。

   **Sqlite实现前后端分离与数据交互**。程序前端展示与后端网卡数据包捕获、预测等功能分离，数据传递通过Sqlite数据库来进行交互。

   **多线程技术保证前端和后端的并发执行**。由于同时要分析处理不同的IP对应的物联网设备的流量数据，以及兼顾系统前端展示与邮件发送，各部分功能需要通过多线程技术协调处理来保证程序的稳定运行。

   ####  Sqlite数据库说明

   本程序使用Sqlite数据，Sqlite是一个进程内的库，实现了自给自足的、无服务器的、零配置的、事务性的 SQL 数据库引擎。它是一个零配置的数据库，不需要安装或管理，不需要一个单独的服务器进程或操作的系统，容量大小也十分小，完全配置时小于 400KB，同时具有强大的兼容性，保证在在不同电脑上都能够稳定运行。

   在选择完需要监控的设备后，对每一个需要监控的设备程序都会去Sqlite中创建一个对应的数据库表，后续捕捉到的数据包在程序中解析完之后都会存入到对应的数据库表项中，数据库表的结构如下：

   | 数据表名:设备名 |                  |          |      |            |           |
   | --------------| ---------------| -------| ---| ---------| --------|
   | 字段名称        | 字段描述         | 数据类型 | 长度 | 是否允许空 | 备注      |
   | Index           | 数据包序号       | int      |      | N          | 主键,索引 |
   | Time            | 数据包捕获时间   | int      | 50   | N          |           |
   | SourceAddr      | 数据包源地址     | varchar  | 18   | N          |           |
   | DestAddr        | 数据包目标地址   | varchar  | 18   | N          |           |
   | Length          | 数据包长度       | int      |      | N          |           |
   | Type            | 数据包类型       | varchar  | 50   | N          |           |
   | IsBad           | 是否恶意         | int      |      | N          |           |
   | AllData         | 数据包逐字节信息 | text     |      | N          |           |

   ##  评估指标

   济小安致力于实现一个高精确度、快速、鲁棒、轻量级的AIDS。因此我们设立了如下的评价指标来评估济小安的性能，并在之后的测试部分详细给出济小安的真实表现。

   准确度：衡量预测的样本占总样本的比例 恶性流量占总样本的比例：

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=ZjU2ZTZkY2YzN2FkMzA4NDZjYTQzMGJmMTk5MGVkZDVfclZzeHBiNXJLMXFYQXc5ckp4R2J6b2l2V1Y0SE1ScmJfVG9rZW46Ym94Y25QeHVGejVKWURpdU94OTh0elVKbnd0XzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   精度：衡量真阳性样品在所有预测阳性样品中的比例。所有预测的阳性样本的比例：

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=YTc5Yzg1MTVhMzBkZmY3NzU5MzFiMGEyMTExOTRjNjVfWVJSUU5wZ3FqZUVreGtRZlZwdzdvTkt3TlV3T1R4R21fVG9rZW46Ym94Y25rRExrbDVYSzFYMkh2cHVPNEc2UHVlXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   召回率：衡量所有阳性样本的比例 的所有阳性样本中，实际预测为阳性的比例：

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=ZWM0NWY4MGQzYjEyNWVlZjA4MTQzZjI3Zjc0M2VmYzZfYmRGckNrb0I4Y1FsVndDVldwMlhPYXE1c3VDVXF0c2pfVG9rZW46Ym94Y25tekJYZEJ5VWlxbnRzS0xLVWg5R0xiXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   F1分数。作为PRC和RCL的加权平均值的衡量标准，它是对绩效结果的综合反应。RCL的加权平均数，它是对性能结果的综合反应，数值越接近1，说明性能结果越好。值越接近于1，性能结果越好：

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=ODY4MjEyMWUzMWUxNDNlY2JiMGM1NzcyZTc4M2U4NTlfODBJcHF4OEc4a044ZXpaQWt2TUZ2Tm1sV09yVHVCZ1JfVG9rZW46Ym94Y243ZWdpQjFwY2J5bkNuNURJcXZWU2pnXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   单位数据包训练时间。表征对于数据样本训练的时常。为了达到实时训练同时节省算力资源的目的，该值应当尽量小：

   单位数据包预测时间。表征对于数据样本预测的时长。为了尽可能减少实时预测过程当中出现的时间损耗，该值应当尽量小：

   ##  数据集

   IDS2017和IDS2018展示了加拿大网络安全研究所的Sharafaldin等人[19]最近的IDS数据集，称为CIC-IDS，其中包含最传统的攻击类别，以及广泛用于入侵检测实验的未经改变的现实世界良性流量。

   Mawilab数据集来自MAWI档案[20]中记录的WIDE MAWI千兆骨干网（2022年1月1日至10日期间）。由于它已经用成熟的标签方法进行了持续的更新，它包含了更广泛的最新攻击类型，并有精细的分类结果。在我们的实验中，我们选择了2022年1月1日至10日的数据作为模型对不同攻击结果的对比实验验证。

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=NjI2NGM2MGNkZTA1NmQ1MmE2MDVlMDA3N2I3NjYxYzRfanZLNWhMbEtPc0NyaUZBSFpRSE1NZGFHVWpnbFdtY3pfVG9rZW46Ym94Y24wa0lGSUNCVE00ZEczT3dXVHVYREpZXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   表 1 IDS2017,IDS2018数据集详细信息

   我们使用的数据是原始的PCAP数据包流量，在wireshark中具体的数据样例展示见图 4。

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=YTRlZTFiOTIwYjA5ZGM4NDYyYmYxODJhM2EzOTAxMmZfQ2E5ZFFZTXc5T2VrY0Q4U0RTaFUzWjZhN1dxejlycFRfVG9rZW46Ym94Y251Yk5nOFRnb0I1Qk9ZTTNUVlJQOTdlXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   图 10 wireshark中数据包展示

   单个数据包样例展示见图5。

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=NGQ0MWViYjU3MWQwNWJiYWQ1M2VhNzkzZjFmMTc5OTNfNHBJTjhZSVRJbVpFRjE3YmlCU09yUlJkUjJiRjJEcUxfVG9rZW46Ym94Y25NdG00MVgyblVXQ01wSFU2bk5Hd2pmXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   图 11 wireshark中单个数据包展示

   # 作品测试与分析

      ##  入侵检测算法实验测试

   为了验证该模型的可行性，我们使用最新的IDS数据集IDS2017和IDS2018进行实验。IDS2017和IDS2018展示了加拿大网络安全研究所的Sharafaldin等人[27]的最新NoTNID数据集，该数据集包含广泛的物联网网络的攻击类别，以及广泛用于物联网网络入侵检测实验的未经改变的现实世界良性流量。

   详细的数据集信息见下表：

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=ODA2YTVmZDcyYWI4YTg5ODA2NzMwZjA2NTQzZTNhNjlfdDZ3NFhBazhrUmNvZ0prN0ZncDBidW0xcVpMR0RvT3NfVG9rZW46Ym94Y256TG1wMzJCeExzZVNvejAxcmptZjBkXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   表 2 数据集详细信息

   ### 实验环境

   我们在英特尔公司Sky Lake-E,12多核处理器上构建实验环境，使用Ubuntu 18.04.6 LTS, 3.10.0-1062.9.1.el7.x86/64操作系统；我们还使用NVIDIA公司GV104[GeForce GTX 1180]作为我们的GPU环境来加速实验。

   ### 比较实验及结果

   该实验将我们的模型与最新的有监督、半监督和无监督模型在IDS2017和IDS2018数据集上的表现进行比较。

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=N2U4OTVjOTFiOWFjZWZjNjRiYjFhYWMyNDYzMzQxNzhfUjE2WU1LRUEyNlEwOE5YSHR2N3FFSXFubkNabVJYSVlfVG9rZW46Ym94Y25KQ0xQSG1jaE44c2NucnRUaDFaUUZlXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

​    

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=NDc1NGI3MGQ2Nzk5NWEyZjYxN2MwOWNlZDllYzY4NTlfaHhmdVMwUFRrV1RBYlJxS0FYRTJUSjV1R3hGUmgyeGlfVG9rZW46Ym94Y25HTnc0RG82OUhHWkRQME9KOVhXTGliXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   图表 1 对比实验结果

   为了保证实验结果的公平性，所有的监督学习模型都只用标注的数据进行训练，而半监督和无监督模型则用所有的标注和无标注数据进行训练。左图比较和分析了现有性能最好的模型与10％的标记训练数据。右图显示了ESeT在不同比例的标记训练样本中的性能结果。1％，5％，10％，和20％。

   在所有的半监督和监督与非监督学习模型算法中，所提出的模型在所有指标上都有很好的表现结果。在极端情况下，仅用1％的数据，F1值就超过97％。这足以证明所提出的模型在不同比例的训练数据下都有出色的性能结果。

   ##  消融实验

   为了进一步验证模型在更多样、更丰富的攻击类型下的性能，我们在mawilab数据集中选择了2022年1月1日至10日的所有流量数据进行对比实验，该数据集共包括43种攻击类型，攻击流量分布与预测结果显示如下图所示：

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=YjE4ZDBhZjE4ZDI3NzEzOWJmNWJmYzAzYjU5ZmNjOWFfTHhJQ0F3eHByMTlEYmtPaXJZb1RDRFhSS0lmbG5oUDNfVG9rZW46Ym94Y253dXd1dkNnT1hxYjNzR1o5VWIwUzVkXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   图表 2 mwilab数据集攻击类型汇总

   与之前的描述一致，我们还使用10％的标记样本比例的数据来训练模型，并在43个mawilab数据集中对不同的攻击类型的性能结果进行比较。

   我们在整个mawilab数据集上的表现也达到了很高的性能，F1值达到99.7％。从表中，我们可以发现，济小安-物联网质性入侵检测系统对大多数攻击都能达到99%或更高的预测准确率。

   ##  鲁棒性实验

   除了关注模型的性能指标（F1，准确率，召回率等），我们还评估了模型对对抗性攻击的鲁棒性。下面，我们评估了在mawilab数据集下模型的鲁棒性通过模拟两种攻击方式：基于梯度的攻击（白盒）和实用性质的攻击（灰盒、黑盒）。

   基于梯度的攻击

   我们的特征提取分为字节编码和频域编码。由于特征的离散性和非数字意义的性质，字节编码可以抵抗基于梯度的攻击。对于频域编码，它的鲁棒性在本实验中使用类似于FGSM[22]的方法进行了评估。

   于频域编码后的特征向量在一次训练中向梯度的反方向前进  距离，可以表示为：

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=NDBmMGRjMGUwZWY2NTlmMDQzNmY3YmUxNDJkYzk4MDJfdUtvbUZXcjhwNTFESTdUckNxaURPVVBMWEpWZTVsUzFfVG9rZW46Ym94Y25kZVpyNXIwOHprVk9UaEtQdGk2U2loXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   。其中

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=NDEzYzZlNzY0OTdiMDgyZjk4ZjRkMzYwM2NkMmUzM2ZfM1QwU01OWkNETjBrSUx0MHBqSTVucVRVb1lGWFhsdDZfVG9rZW46Ym94Y25yQ1hpUXBNNTlIY2NrelllZzE5b1ZmXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   表示为梯度的方向，是扰动规模。这种方法可以定义为增加小的扰动规模，导致模型结果发生大的变化。我们在mawilab上做了一组测试，将设置为不同的值，发现这种扰动对模型结果几乎没有影响，如表3。

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=YWQwODY4MzNmYzlmNDVkMDkyMjRkZjgyYWMzMmM2OTBfOU9tMkxFeklzVkIzOHFNMkg2dnQyTWRvT01iWUxnakhfVG9rZW46Ym94Y25uaEc5OUtQQnQ2bnBtNzl2WVJNTmdYXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   表 3 不同对模型鲁棒性的影响

   实用性质的攻击

   我们关注[21]中的两种方法：实用性质的灰盒攻击(PGA)和黑盒攻击（PBA）。[21]基于GAN-PSO的方法生成规避特征，在限定的开销下自动改变原始恶意流量，并且不影响其功能。该算法结合了GAN和PSO的方法来完成逃避攻击，具体可分为以下两个步骤：

   1.对抗性特征生成：我们假设攻击者想要启动一些活动，这将引发一系列的恶意流量。首先，攻击者需要在其控制的网络中收集一些良性流量。然r后，通过代理提取器将两种流量提取到特征中，并输入到我们的GAN模型中。在训练阶段之后，生成器能够产生对抗性的特征。

   2.恶意流量突变：在生成对抗性特性后，我们使用带有预定义操作符的PSO来自动突变恶意流量。蜂群中的每个粒子代表一个由突变流量的元信息组成的向量。该群在其特征与对抗性特征最相似的临时最佳粒子的引导下，迭代搜索交通空间。最后，经过多次迭代，选择出最佳粒子。

   除了传统的指标（F1，准确率，召回率，精度）之外，[21]中引入了新的指标（MMR和PDR）来衡量攻击的效果。攻击效果和鲁棒性的关系是攻击效果越好，鲁棒性越差。

   可解释性指标(MMR)可以明确显示攻击过程中潜伏空间中的特征变化，反映了突变过程中恶意特征与对抗特征的接近程度。

   恶意概率下降率（PDR）用于测量目标分类器输出的恶意概率的下降率。PDR的值越高，代表攻击的效果越好，模型的鲁棒性越差。

   PGA和PBA抛弃了不切实际的假设，而选择了更实际的攻击。简而言之，在PBA中，攻击者对目标NIDS中使用的特征的了解非常有限，甚至是一无所知，PGA和PBA的唯一区别是，攻击者了解我们的特征提取器。

   PBA：一个对目标系统没有任何了解的攻击者只能通过使用其他特征来模拟提取器。假设他使用模型Kitsune[23](一个比较成熟的IDS)作为目标NIDS，并获得对抗性流量并将其输入我们的模型。表4中的结果显示，虽然这些修改后的流量对Kisune实现了效果较好的攻击(PDR=23.00%)，但对我们的模型(ESet)却不敏感(PDR=2.10%)。

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=MTRjNTI2Y2Y0MjUxYTQ5ZWI2MDJmZWM1MmNiZDIxNWRfTkE5NmxSODl2c1dncHdZc2NqRUppYXJjME5lRllkSFJfVG9rZW46Ym94Y255YzR0c01lTmhRMUh1dk1NbDBlTWVjXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   表 4 基于kisune的PBA对ESet的影响

   PGA：我们使用频域编码作为特征提取器来分析不同攻击成本（l_c, l_t）对模型鲁棒性的影响。第一个开销用l_c表示，是精心制作的数据包数量与原始数据包的比率。第二个开销用l_t表示，是变异流量与原始流量的耗时率。我们使用较低的l_c= 0. 2,l_t = 2和较高的预算l_c = 0.5, l_t = 5），结果如表5所示。结果表明，无论是高成本(PDR=5.25%)还是低成本(PDR=3.44%)，PGA对ESet攻击的影响都是有限的。

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=ZDZlODhlOGVlMzRlNTRmMGY5ODNmMjJiM2FkYjBkMDdfVE1mWkxBdlpXVXZNN3VCU2JuVWFjM0Y0VkJBRk1XQkFfVG9rZW46Ym94Y25UMHpsaVpZT0FId1BFQzZPUE85TURmXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   表 5 不同攻击代价对我们模型的影响

   综上所述，这些结果证明了ESet的鲁棒性。特别是，我们的模型对敌手攻击代价表现不敏感。

   ##  压力测试实验

   本实验的压力测试主要是为了检测我们系统在多设备、高并发的网络环境下，能否顺利地运行。主要的压力来源在于系统能否及时捕获所有网卡中的数据包以及模型的预测能否及时完成，数据能否及时写入到数据库中，还有前端展示的页面更新能否跟上网路环境中的数据包产生速度。最终采取的评测指标是从数据发送到前端页面展示所耗费的时间。

   **测试场景**

   本次压力测试中使用3台电脑连接同一服务器，关闭这3台电脑的其他可能产生数据包的软件，使用xcap软件进行发包并控制发包的速率大小。然后记录下发包完成时的时间戳和服务器这边展示完时候的时间戳，统计从电脑发包到服务器这边展示所耗费的时间。

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=NzQzM2FhMjIyNmY0OWQ3MDA2ZmQ5ZmM4OTdkOTQwNjhfMnpzRFdRM3ZqZFN1NVhBY0c5MUJJcHFjMWVvVFVteTZfVG9rZW46Ym94Y25xNXJ0UkhnaUdTOTh0RE5PS2hnSUpiXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   图 12 压力测试场景

   **测试结果**

   | 发包速(100Kb/s) | 响应时间(ms) |
   | --------------| -----------|
   | 1               | 50           |
   | 10              | 50           |
   | 100             | 63           |
   | 300             | 183          |
   | 500             | 472          |
   | 800             | 841          |
   | 1000            | 1598         |
   | 3000            | 3721         |
   | 5000            | 8154         |

   ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=NzhjYjIwYjZiYWJmYTIxYmUwMTQ0NTE3MjYyZGRiNDhfa1hRcUIwS2F3ZTRVS01KNmhnak1xSG1uTHpBckU3RGlfVG9rZW46Ym94Y25GYWtmMnFjU2tzak1jcDdIV2Nxcm1iXzE2Njk1Njk5NjM6MTY2OTU3MzU2M19WNA)

   表 6 压力测试结果

   **测试结果分析**

   测试结果发现在小于50000Kb/s的速率下，系统的响应都十分迅速，不超过500ms，但是随着发包速率的增大，系统会表现得不稳定，平均响应时间大幅延长，在超过300000Kb /s的速率后，系统就会变得极度卡顿，难以正常运行。经过定点排查发现原因主要在于前端对于表格的更新，因为每次更新时都要向表格的最上方插入一行，然后再填入数据，而频繁地更新表格插入数据对于前端的展示是一个很大的压力点，同时数据库的读写也是一个较为耗时的部分。

   而对于一般非工业级设备如家庭电器、无人驾驶车辆，其每秒产生的数据总量一般在10000Kb/s，最大峰值在50000Kb/s，而这都在我们系统的可承受范围之内，而这也就说明了我们系统的性能对于非工业级的物联网的安全监控是足够的。

   # 创新性说明

   济小安-物联网质性入侵检测系统的落脚点是物联网网络中的安全问题，这是一个非常实际、紧迫解决的问题点。物联网安全比互联网安全更重要，影响更大，物联网是与物理世界打交道的，无论是自动驾驶、智能电网还是桥梁检测、灾害监测，一旦出现问题甚至可能会涉及生命财产的损失。

   济小安致力于实现一个高精确度、快速、鲁棒、轻量级的基于异常的入侵检测系统。它可以部署在物联网云平台上，在云端层上训练模型且在检测层进行流量检测，兼具轻量和实用的特点。

   我们充分利用了已标记和未标记的网络流量数据的特征，并通过可信度选择器来减少错误的伪标记的负面影响。此外，我们提出了一个多级特征表示学习模块，既学习流量级频域特征，又学习数据包级字节编码特征。

   由于大多数数据过时且不可靠、缺乏多样性、数据量过少，不能涵盖已知攻击，我们使用了IDS2017、IDS2018来自真实世界的攻击数据集，包含良性和最新的常见攻击，覆盖率广且能够反映当前的趋势。

   我们主要的工作有：

   我们设计了基于三层架构的物联网入侵检测系统——云端层、检测层、边缘层。在强大的深度学习预测速度与准确度的支持下，能够对于物联网系统的入侵检测行为进行实时预测，并对使用者进行警报。
     我们设计了一个半监督的模型架构以用于实时应用半监督预测，充分利用未标记的网络流量数据来构建一个实时的NID系统，利用自主设计的可信度选择器模块，基于kitnet算法对恶性流量数据的敏感性，为伪标签的质量提供保证。我们提出了频域编码变换器，它实现了对提取的频域特征和字节编码特征的分析。
     我们在三个数据集上进行了实验，即IDS2017、IDS2018和mawilab，包括对比实验、消融实验、鲁棒性实验等，结果显示我们的模型表现良好，既有高准确率，又有高鲁棒性。

   我们工作的**亮点**有两点。一是在人工标记大量物联网记录变得困难的前提下，只有一小部分物联网流量可以被标记，剩下的大部分可以是未标记的，济小安能够从少量标记的数据和大量未标记的数据中中高效的学习，达到了10%的有标记数据99%的F1值的精确率。在极端情况下，仅用1％的数据，F1值就超过97％。二是对模型鲁棒性的关注，对于目前针对ML/DL弱点的攻击，我们通过模拟敌手的行为进行不同类型的测试，PDR小于5%，验证了济小安的高鲁棒性。

   # 总结

      ##  作品小结

   物联网因为其具有开放性、多源异构性、泛在性等特性，物联网的安全关系到个人、家庭、社会、乃至国家的安全。济小安致力于实现一个高精确度、快速、鲁棒、轻量级的基于异常的入侵检测系统。它可以部署在[物联网云平台](http://www.nlecloud.com/about)上，在云端层上训练模型且在检测层进行流量检测，兼具轻量和实用的特点。

   我们预设了半监督入侵检测框架的应用模型，由云端层、检测层和边缘层构成。由在完成边缘层的流量收集后，将在云端层将收集到的流量进行特征处理、模型训练等工作，并在检测层对接下来的流量进行异常检测。在强大的深度学习预测速度与准确度的支持下，能够对于物联网系统的入侵检测行为进行实时预测，并对使用者进行警报。

   在实现方法上，我们设计了一个半监督的模型架构以用于实时应用半监督预测，充分利用未标记的网络流量数据来构建一个实时的NID系统，利用自主设计的可信度选择器模块，基于kitnet算法对恶性流量数据的敏感性，为伪标签的质量提供保证。我们提出了频域编码变换器，它实现了对提取的频域特征和字节编码特征的分析。

   在运行效果上，我们在人工标记大量物联网记录变得困难的前提下，只有一小部分物联网流量可以被标记，剩下的大部分可以是未标记的，济小安能够从少量标记的数据和大量未标记的数据中中高效的学习，在IDS2017和IDS2018数据集上用小部分的标注数据（10％）对NID取得了优异的性能（F1-score：99.48％）。在极端情况下，仅用1％的数据，F1值就超过97％。于此同时，对于目前针对ML/DL弱点的攻击，我们通过模拟敌手的行为进行不同类型的测试，PDR小于5%，表现了高鲁棒性。

   ##  商业价值

   随着“互联网+”时代的到来，物联网发展迅猛，正在逐渐渗透到生活的各个领域之中， 物联网设备规模呈现爆发性增长趋势，万物互联时代正在到来，物联网安全的重要地位也在物联网快速的发展中愈加凸显。物联网根据业务形态可分为：工业控制物联网、车载物联网、智能家居物联网等三个部分，且不同的业务形态又对于安全具有不同的业务需求。 

   然而，在物联网技术高速发展的同时，隐私安全却是值得思考的问题。根据惠普安全研究院调查的10个最流行的物联网智能设备后发现几乎所有设备都存在高危漏洞，一些关键数据如下：

   80%的IOT设备存在隐私泄露或滥用风险；

   80%的IOT设备允许使用弱密码；

   70%的IOT设备与互联网或局域网的通讯没有加密；

   60%的IOT设备的web 界面存在安全漏洞；

   60%的IOT设备下载软件更新时没有使用加密；

   物联网在给我们带来便利的同时，物联网的设备、网络、应用等也在面临着严峻的安全威胁，例如：

   2015年，两名网络安全专家通过中间人攻击的方式，对高速公路上的吉普车实现了远程控制（例如，控制空调、收音机、挡风玻璃刮水器和制动器等）。这次袭击展示了中间人攻击的危害性，也导致厂商召回了140万辆汽车。“水滴直播”、“海康威视”事件中的摄像头遭到入侵而被偷窥；美国制造零日漏洞病毒，利用 “震网”攻入伊朗核电站，破坏伊朗核实施计划等；2015年，英国的网络供应商Talk Talk遭受几个网络安全漏洞的攻击，导致未经加密存储的客户数据暴露在云端。黑客能够轻松访问和窃取数百万客户的信用卡和银行详细信息。

   从IDS/IPS (入侵检测/防御) 市场中的份额来看，硬件占了IDS/IPS的主要部分，比例约为45%，其次是基于托管的IDS/ISP，市场份额约为31%，基于网络的软件占市场份额的24%。随着市场的发展，基于网络的IDS/IPS软件增长速度越来越快。根据Gartner网络安全行业产品结构比例分布，2019年，我国入侵检测/防御设备市场规模约为19亿元。物联网因为其具有开放性、多源异构性、泛在性等特性，物联网的安全关系到个人、家庭、社会、乃至国家的安全，种种安全威胁的出现，也不断地证实着物联网网络入侵检测系统的必要性。

   ##  作品展望

   济小安-物联网质性入侵检测系统是一款准确而迅速的物联网入侵检测系统，拥有强大的半监督训练模型支持，能够在精准而快速的对于入侵行为进行物联网网络入侵行为进行预测；在不断地完善中，我们将从以下方面对济小安-物联网质性入侵检测系统的功能进行改进：

   在安全防御上，济小安-物联网质性入侵检测系统能够准确地定位到物联网入侵流量、入侵点位、入侵时间和流量类型同时对齐进行精确的预报和跟踪。但是在总体的防御策略上采用较为单一的“中断连接”的方式对于受攻击的设备物联网连接进行处理，没有考虑到不同设备正在进行的实际活动。在响应策略上，入侵检测系统分为两种模式——主动响应和被动相应。前者对于搜集到的不正常情况只发出告警通知，不试图降低所造成的破坏，也不对攻击者反击；后者则可能对被攻击系统实施控制，阻断或减轻攻击影响。我们将综合不同的相应策略。我们将综合考虑不同设备的运行状态，以便在保存设备正常运行参数的同时对于恶意流量来源进行阻断，尽量不影响设备运行状态的情况下将风向讲到最低。

   在架构部署上，“云端层”和“检测层”之间的数据交互，包括与训练模型的传输、训练数据、检测数据包的传输等。由于时间和硬件条件的原因，在本模型的设计当中并没有很好的对于这一部分传输进行保护，如果攻击者在这一传输过程当中对于模型发起攻击将会带来较为严重的后果。在后续的改进当中，我们将搭建内网保护机制，建立“云端层”和“检测层”之间绝对安全的数据传输，来保证整个物联网检测系统的可靠性。

   在应用领域上，济小安网络安全专家设计的物联网安全检测系统适用于大型的企业级网络架构与小型的家用智能架构。但并不是每一个家用网络都能够支持云端设备的高强度算力的服务器。因此在后续设计当中我们协商那个能够将云服务器单独抽离出来，将众多的物联网安全网络相互交织的更大一个层级的系统。使得训练数据能够更好的独立于检测模块，的在服务器集群上进行，从而能够及你不减少硬件消耗的情况下不改变整体的模型性能。

   # 参考文献

   M. Stoyanova, Y. Nikoloudakis, S. Panagiotakis, E. Pallis, and E. K. Markakis, "A survey on the Internet of Things (IoT) forensics: Challenges, approaches, and open issues," IEEE Commun. Surveys Tuts., vol. 22, no. 2, pp. 1191–1221, 2nd Quart., 2020, doi: 10.1109/COMST.2019.2962586.

   M. M. Hassan, S. Huda, S. Sharmeen, J. Abawajy, and G. Fortino, "An adaptive trust boundary protection for IIoT networks using deep-learning feature-extraction-based semisupervised model,” IEEE Trans. Ind. Informat., vol. 17, no. 4, pp. 2860–2870, Apr. 2021, doi: 10.1109/TII.2020.3015026. 

   M. Saharkhizan, A. Azmoodeh, A. Dehghantanha, K.-K. R. Choo, and R. M. Parizi, "An ensemble of deep recurrent neural networks for detecting IoT cyber attacks using network traffic," IEEE Internet Things J., vol. 7, no. 9, pp. 8852–8859, Sep. 2020, doi: 10.1109/JIOT.2020.2996425.

   M. A. Al-Garadi, A. Mohamed, A. K. Al-Ali, X. Du, I. Ali, and M. Guizani, “A survey of machine and deep learning methods for Internet of Things (IoT) security,” IEEE Commun. Surveys Tuts., vol. 22, no. 3, pp. 1646–1685, 3rd Quart., 2020, doi: 10.1109/COMST.2020.2988293

   L. Li, J. Yan, H. Wang, and Y. Jin, “Anomaly detection of time series with smoothness-inducing sequential variational auto-encoder,” IEEE Trans. Neural Netw. Learn. Syst., early access, Apr. 13, 2020, doi: 10.1109/TNNLS.2020.2980749.

   J. Wu, Z. Zhao, C. Sun, R. Yan, and X. Chen, “Fault-attention generative probabilistic adversarial autoencoder for machine anomaly detection,” IEEE Trans. Ind. Informat., vol. 16, no. 12, pp. 7479–7488, Dec. 2020, doi: 10.1109/TII.2020.2976752.

   X. Wang, Y. Han, V. C. M. Leung, D. Niyato, X. Yan, and X. Chen, “Convergence of edge computing and deep learning: A comprehensive survey,” IEEE Commun. Surveys Tuts., vol. 22, no. 2, pp. 869–904, 2nd Quart., 2020, doi: 10.1109/COMST.2020.2970550.

   M. Shafiq, Z. Tian, A. K. Bashir, X. Du, and M. Guizani, “CorrAUC: A malicious bot-IoT traffic detection method in IoT network using machine-learning techniques,” IEEE Internet Things J., vol. 8, no. 5, pp. 3242–3254, Mar. 2021, doi: 10.1109/JIOT.2020.3002255.

   S. Gamage and J. Samarabandu, “Deep learning methods in network intrusion detection: A survey and an objective comparison,” J. Netw. Comput. Appl., vol. 169, Nov. 2020, Art. no. 102767.

   Y. Cheng, Y. Xu, H. Zhong, and Y. Liu, “Leveraging semisupervised hierarchical stacking temporal convolutional network for anomaly detection in IoT communication,” IEEE Internet Things J., vol. 8, no. 1, pp. 144–155, Jan. 2021, doi: 10.1109/JIOT.2020.3000771.

   L. Vu, V. L. Cao, Q. U. Nguyen, D. N. Nguyen, D. T. Hoang, and E. Dutkiewicz, “Learning latent representation for IoT anomaly detection,” IEEE Trans. Cybern., early access, Sep. 18, 2020, doi: 10.1109/TCYB.2020.3013416

   J. Gao et al., “Omni SCADA intrusion detection using deep learning algorithms,” IEEE Internet Things J., vol. 8, no. 2, pp. 951–961, Jan. 2021, doi: 10.1109/JIOT.2020.3009180.

   L. Xiao, X. Wan, X. Lu, Y. Zhang, and D. Wu, “IoT security techniques based on machine learning: How do IoT devices use AI to enhance security?” IEEE Signal Process. Mag., vol. 35, no. 5, pp. 41–49, Sep. 2018.

   T. Ergen and S. S. Kozat, “Unsupervised anomaly detection with LSTM neural networks,” IEEE Trans. Neural Netw. Learn. Syst., vol. 31, no. 8, pp. 3127–3141, Aug. 2020, doi: 10.1109/TNNLS.2019.2935975.

   J. Wang, C. Jiang, H. Zhang, Y. Ren, K.-C. Chen, and L. Hanzo, “Thirty years of machine learning: The road to Pareto-optimal wireless networks,” IEEE Commun. Surveys Tuts., vol. 22, no. 3, pp. 1472–1514, 3rd Quart., 2020, doi: 10.1109/COMST.2020.2965856.

   F. Hussain, R. Hussain, S. A. Hassan, and E. Hossain, “Machine learning in IoT security: Current solutions and future challenges,” IEEE Commun. Surveys Tuts., vol. 22, no. 3, pp. 1686–1721, 3rd Quart., 2020, doi: 10.1109/COMST.2020.2986444.

   N. Ravi and S. M. Shalinie, “Semisupervised-learning-based security to detect and mitigate intrusions in IoT network,” IEEE Internet Things J., vol. 7, no. 11, pp. 11041–11052, Nov. 2020, doi: 10.1109/JIOT.2020.2993410.

   Ying Gao, Yu Liu, Yaqia Jin, Juequan Chen, and Hongrui Wu. 2018. A Novel Semi-Supervised Learning Approach for Network Intrusion Detection on Cloud-Based Robotic System. IEEE Access 6 (2018), 50927–50938. https://doi.org/10.1109/ACCESS.2018.2868171

   G Karatas, O Demir, O K Sahingoz, Increasing the Performance of Machine Learning-Based IDSs on an Imbalanced and Up-to-Date Dataset[J], IEEE Access 8 (2020) 32150–32162.

   WIDE. Accessed January 202MAWI Working Group Traffic Archive. http://mawi.wide.ad.jp/mawi/.

   Dongqi Han, Zhiliang Wang, Ying Zhong, Wenqi Chen, Jiahai Yang, Shuqiang Lu, Xingang Shi, and Xia Yin. 202Evaluating and Improving Adversarial Robustness of Machine Learning-Based Network Intrusion Detectors. IEEE Journal on Selected Areas in Communications 39, 8 (2021), 2632–2647. https://doi.org/10.1109/JSAC.2021.3087242

   Md Ashraful Alam Milton. 2018. Evaluation of Momentum Diverse Input Iterative Fast Gradient Sign Method (M-DI2-FGSM) Based Attack Method on MCS 2018 Adversarial Attacks on Black Box Face Recognition System. https://doi.org/10.

   48550/ARXIV.1806.08970

   Mirsky, Yisroel & Doitshman, Tomer & Elovici, Yuval & Shabtai, Asaf. (2018). Kitsune: An Ensemble of Autoencoders for Online Network Intrusion Detection. 