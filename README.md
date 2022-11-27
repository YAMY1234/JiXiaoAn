<div align="right">
  Language:
  🇺🇸
  <a title="Chinese" href="/README_CN.md">🇨🇳</a>
</div>


1. 1. # Introduction

      The rapid development of Internet of Things (IoT) technology has generated a large amount of Traffic, which usually contains various problems arising from normal production or violations that may compromise the security of IoT communications, such as autonomous driving, industrial IoT, smart home, etc. Collecting these Traffic can detect intrusions through IoT networks. Despite great efforts in annotating IoT Traffic records, the number of flagged records is still very small, increasing the difficulty of identifying malicious attacks. We implement a Semi-Supervised Deep Learning Method (ESet) -based Intrusion Detection System for the Internet of Things.

      Ji Xiaoan is committed to designing a **qualitative** IoT intrusion detection system, and **high precision, fast, robust, lightweight** semi-supervised learning based intrusion detection system. It can be deployed on the [IoT platform ](http://www.nlecloud.com/about), training models on the cloud layer and performing Traffic detection at the detection layer, which is lightweight and practical.

      We preset the application model of the semi-supervised intrusion detection framework, which consists of a cloud layer, a detection layer and an edge layer. After collecting Traffic at the edge layer, the collected Traffic will be subjected to feature processing and Model Training in the cloud layer, and anomaly detection of Traffic at the detection layer. With the support of powerful Deep learning prediction speed and accuracy, it can predict the intrusion detection behavior of the IoT system in real time and alert users.

      In terms of innovation, we design a semi-supervised model architecture for real-time application of semi-supervised prediction, make full use of unlabeled network Traffic data to construct a real-time NID system, and use the self-designed trustworthiness selector module to provide quality assurance for pseudo-labels based on the sensitivity of kitnet Algorithm to malignant Traffic data. We propose a frequency domain coding converter, which realizes the analysis of extracted frequency domain features and byte coding features.

      In terms of operation effect, considering the difficulty of manually labeling a large number of IoT records, only a small part of the IoT traffic can be labeled, and most of the rest are unlabeled. The system can efficiently learn from a small amount of labeled data and a large amount of unlabeled data: Excellent performance (F1 score: 99.48%) was achieved with a small part of labeled data (10%) on the IDS2017 and IDS2018 datasets. In extreme cases, only 1% of the data was used, and the F1 value exceeded 97%. For the current attacks against ML /DL weaknesses, we conduct different types of tests by simulating the behavior of the adversary, PDR less than 5%, showing the high robustness of Ji Xiaoan.

      Because of its openness, multi-source heterogeneity, ubiquity and other characteristics, the security of the Internet of Things is related to the security of individuals, families, society, and even the country. In terms of commercial value, according to the proportion distribution of Gartner cyber security industry product structure, in 2019, the market size of intrusion detection/defense equipment in China is about 1.9 billion yuan. Therefore, the Ji Xiao'an-Internet of Things qualitative intrusion detection system has a wide range of application scenarios in the future market because of its high precision, fast, robust and lightweight practical characteristics.

      1. # Work overview

         - 1. ##  Background

      The rapid development of Internet of Things (IoT) technology has facilitated the development of various innovative services and applications, such as smart manufacturing, smart healthcare, and smart transportation. A large number of IoT communications communicate between various IoT entities, passing information such as swtich control, smart Facility Management, communication details, and equipment maintenance details, which often contain various issues arising from normal production or violations that may compromise the security of IoT communications.

      The communication network system of the Internet of Things is mainly used for transmitting and processing the information obtained by the sensing layer in the network. Due to the variety of networks involved in the Internet of Things, from wireless, infrared and other radio frequency networks in the sensing layer, through wireless access networks, such as narrowband IoT networks, wireless local area networks, cellular mobile communication networks, wireless ad hoc networks, etc., through the Internet to reach the IoT application layer platform, the cyber security threats faced by the Internet of Things are more complex, with four specific security risks.

      1. Wireless data transmission links are vulnerable

      The data transmission of the Internet of Things generally uses wireless radio frequency signals to communicate. The inherent vulnerability of wireless networks makes the system vulnerable to various forms of attacks. Attackers can make the reader unable to accept the data in the normal electronic tag by emitting interference signals, or make the base station unable to work properly, causing communication interruptions. In addition, wireless transmission networks can easily lead to difficult protection during signal transmission, and are easily hijacked, eavesdropped or even tampered with by attackers.

      1. Transmission networks vulnerable to Distributed Denial-of-service

      Due to the large number of nodes in the Internet of Things and the existence of clusters, attackers can use the controlled nodes to send malicious data packets to the network and launch Distributed Dial-of-service, causing network congestion, paralysis, and service interruption.

      1. Unauthorized access and network access

      User unauthorized access to the network, illegal use of network resources, or attack the network; user unauthorized access to the network, access to internal network data, such as user information, configuration information, routing information.

      1. Communication network operator emergency management and control risks

      - For communication network operators, the traditional management and control of communication functions such as SMS, data, and voice is mainly based on a single device, a single function, and a single user. However, the end point of IoT devices is large in scale, and there are many combinations of communication functions such as SMS and data in different services. If mass emergency management and control of communication functions cannot be implemented on the network side through multiple dimensions such as geography, business, and users, it will be impossible to cope with the risks caused by massive end point charges.

      - - 1. ##  related work

      Intrusion detection systems (IDS) have been introduced to identify intrusions that evade security technologies. An intrusion can be defined as any type of unauthorized activity that causes damage to an information system. This means that any attack that may pose a threat to the confidentiality, integrity or availability of information will be considered an intrusion. For example, an activity that makes a computer service unresponsive to legitimate users is considered an intrusion. IDS is a software or hardware system used to identify malicious behavior on a computer system in order to maintain system security. The goal of IDS is to identify different types of malicious network traffic and computer usage that traditional firewalls cannot. This is critical to achieving a high level of protection against behavior that compromises the availability, integrity, or confidentiality of computer systems.

      In general, IDS systems can be roughly divided into two categories: signature-based [intrusion detection ](https://so.csdn.net/so/search?q=入侵检测&spm=1001.2101.3001.7020)systems (SIDS) and anomaly-based intrusion detection systems (AIDS).

      1. Signature-Based Intrusion Detection System (SIDS)

      Signature-based intrusion detection systems (SIDS) are based on pattern matching techniques to discover known attacks, also known as knowledge-based detection or misuse detection. In SIDS, matching methods are used to find previous intrusions. In other words, an alarm signal is triggered when intrusion features match the features of a previous intrusion that is already present in the feature database. For SIDS, the logs of the host are checked for commands or sequences of operations that were previously identified as malicious software. The main idea of SIDS is to build a database of intrusion features and compare the current active set with existing features. If a match is found, an alert is issued. SIDS generally provide excellent detection accuracy against previously known intrusions. However, SIDS has difficulty detecting zero-day attacks because there are no matching signatures in the database until the signatures of the new attack are extracted and stored. SIDS is used in many common tools such as Snort (Roesch, 1999) and NetSTAT (Vigna & Kemmerer, 1999). Traditional methods of SIDS examine network data packets and try to match with the signature database. But these techniques fail to identify attacks that span multiple data packets. Since modern malicious software is more complex, it may be necessary to extract signature information from multiple data packets. This requires IDS to call the contents of earlier data packets. Regarding creating a signature for SIDS, there are usually many ways to create the signature as a Finite-State Machine, formal language string pattern, or semantic condition. The increasing frequency of zero-day attacks makes the SIDS technique gradually less effective as no previous signature exists for any such attack. Polymorphic variants of malicious software and increasing targeted attacks may further undermine the adequacy of this traditional paradigm. The general structure of SIDS is shown in Figure 1.

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTM0OTJlYzU1N2I0NDk4ZGY5MTliNzVlYTg4M2Q1NzBfY2lzQkcwMGRrd00zdkgyVTgzUkZyeHl2RXA3MjJQN3dfVG9rZW46Ym94Y25FY2paS1RQRm1zQ1ZGb0pGUm5EUm9nXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      Figure 1 SIDS architecture diagram

      1. Anomaly-Based Intrusion Detection System (AIDS)

      AIDS has attracted the attention of many scholars due to its ability to overcome the limitations of SIDS. In AIDS, normal models of computer system behavior are created using Machine Learning, statistical-based or knowledge-based methods. Any significant deviation between the observed behavior and the normal model is considered an anomaly and can be interpreted as an intrusion. The assumption of this group of techniques is that malicious behavior differs from typical user behavior. Behavior of abnormal users that differs from standard behavior is classified as an intrusion. The development of AIDS consists of two phases: a training phase and a testing phase. During the training phase, the normal traffic profile is used to learn the normal behavior model, and then during the testing phase, using the new dataset, the ability of the system to generalize to previously unseen intrusions is established. AIDS can be divided into many categories according to the method trained, for example, statistical-based, knowledge-based, and machine learning-based methods. The main advantage of AIDS is the ability to identify zero-day attacks, as identifying anomalous user activity does not rely on a signature database. AIDS triggers red flags when the checked behavior is different from the usual behavior. SIDS can only identify known intrusions, while AIDS can detect zero-day attacks. However, AIDS can lead to a high rate of false positives, as the anomaly may just be new normal activity, not a real invasion.

      The difficulty in identifying unknown intrusions is a particular problem for IoT networks, which connect a large number of devices with different computing resources, communication technologies, battery capacities, software, and operating systems. This heterogeneity challenges the deployment of security solutions, with the addition of Attack Surface, making IoT networks more vulnerable to new and unfamiliar intrusions [1] - [3]. Traditional Machine Learning (ML) techniques [8] have been shown to be effective in identifying important patterns in IoT Traffic, resulting in proficient identification of cyber attacks [4]. However, ML also proved unable to scale to huge datasets (i.e. millions of records with over a hundred features), and with IoT nodes extremely dispersed, ML performance in detecting intrusions/cyber attacks is also unsatisfactory [5], [6]. In addition, the continuous improvement of Deep learning (DL) techniques has inspired new IDS, which is able to handle and handle the required intrusions/cyber attacks well, with the level of difficulty and complexity, and distribution [7].

      Artificial intelligence methods such as ML /DL have been an important challenge in developing reliable IDS in IoT [7], [9], [13] environments. In this regard, current methods for detecting IoT intrusions can be divided into three distinct aspects.

      1. supervised approach

      Supervised ML or DL methods are typically trained using labeled IoT records to distinguish between normal records and other attack records (i.e., binary classification), or to distinguish different attack classes from normal traffic (i.e., multi-class classification). Traditional Machine Learning methods have been applied on IoT IDS. For example, Yang et al. [28] utilized k-nearest neighbors (kNNs) to develop a secure IDS for large-scale IoT data. There are also methods using Deep learning, such as Gao et al. [12] using LSTM and feedforward neural network (FNN) to detect intrusions, respectively, and experimented in integrated architectures. Although supervised methods achieve high precision in IDS, they have not gained popularity due to the lack of labeled IoT data [10]. Furthermore, they perform poorly when the data is not evenly distributed among classes (class imbalance problem). This motivates us to use semi-supervised learning to develop efficient AIDS.

      1. unsupervised method

      Data or Traffic tags are referred to as unsupervised IDS. This method does not require any Traffic tags, so it is cost-effective, and they utilize the inherent characteristics of IoT Traffic samples to distinguish different attacks. Therefore, they are able to reliably identify new attacks. For example, Ergen and Kozat [14] utilized a LSTM architecture to process a sequence of IoT Traffic and generate a fixed-length sequence. They then used single-class SVM and support vector data description techniques to compute the final classification decision. Vu et al. [11] developed a regularized version of the AE architecture to learn latent representations of input traffic, leveraging it to fine-tune the performance of supervised learners. However, for these methods, while manual annotation of the data is not required, they do not give very impressive performance and stable results. Furthermore, they do not have the robustness of supervised methods, especially in identifying previously identified attacks. Second, they exhibit high computational complexity, which limits their applicability in real-time or resource-constrained IoT applications [1], [14], [15].

      1. Semi-supervised approach

      - Semi-supervised methods use both annotated and unannotated samples to train a particular classifier, especially when a small number of labeled samples are available. Many such techniques have been developed to detect intrusions in IoT Traffic and have demonstrated good performance [15], [16]. For example, Ravi and Shalini [17] developed a semi-supervised ML method to detect network attacks by integrating supervised neural networks and repeated random sampling of unsupervised data. Gao et al. [18] proposed a new ambiguity-based semi-supervised learning method via ensemble learning, achieving 84.54% and 71.29% accuracy on the "KDDTest +" and "KDDTest-21" datasets. Their performance in identifying previously identified attacks remains low compared to supervised methods. In other words, they need more labeled data to improve their performance. Abdel-Basset et al., using 25% labeled data, achieved 98% F1 value. In our model, we achieved 99% F1 value using only 10% labeled data. In addition, the robustness of the model has received little attention. Compared with existing methods, our method improves detection accuracy, utilization efficiency of labeled data, and model robustness.

      - - 1. ##  Introduction

      The rapid development of Internet of Things (IoT) technology has generated a large amount of Traffic, which usually contains various problems arising from normal production or violations that may compromise the security of IoT communications, such as autonomous driving, industrial IoT, smart home, etc. Collecting these Traffic can detect intrusions through IoT networks. Despite great efforts in annotating IoT Traffic records, the number of flagged records is still very small, increasing the difficulty of identifying malicious attacks. We implement a Semi-Supervised Deep Learning Method (ESet) -based Intrusion Detection System for the Internet of Things.

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTg3ZGMzNzM4YzI0NzZjOWYxNmQwODU2YTQzMjQzM2VfcUxWdmNlSDU5cGQxQUYydnR2RlJHZWFkbWhlbzhmeHBfVG9rZW46Ym94Y25YdGpkaTM3RGdIcXVLTUtyWldWV1FmXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      Figure 2 IoT communication application scenario

      Ji Xiaoan is committed to realizing a high precision, fast, robust and lightweight anomaly-based intrusion detection system. It can be deployed on the [Internet of Things Cloud Computing Platform ](http://www.nlecloud.com/about), training models on the cloud layer and performing Traffic detection on the detection layer, which is both lightweight and practical.

      We preset the application model of the semi-supervised intrusion detection framework, which consists of a cloud layer, a detection layer and an edge layer. After collecting Traffic at the edge layer, the collected Traffic will be subjected to feature processing and Model Training in the cloud layer, and anomaly detection will be performed on the subsequent Traffic at the detection layer. With the support of powerful Deep learning prediction speed and accuracy, it can predict the intrusion detection behavior of the IoT system in real time and alert users.

      In terms of innovation, we design a semi-supervised model architecture for real-time application of semi-supervised prediction, make full use of unlabeled network Traffic data to construct a real-time NID system, and use the self-designed trustworthiness selector module to provide quality assurance for pseudo-labels based on the sensitivity of kitnet Algorithm to malignant Traffic data. We propose a frequency domain coding converter, which realizes the analysis of extracted frequency domain features and byte coding features.

      In terms of operation effect, there are two highlights of our work. First, under the premise that it becomes difficult to manually label a large number of IoT records, only a small part of the IoT Traffic can be labeled, and most of the rest can be unlabeled. Ji Xiaoan can efficiently learn from a small amount of labeled data and a large amount of unlabeled data. He achieved excellent performance against NIDs with a small part of labeled data (10%) on the IDS2017 and IDS2018 datasets (F1 score: 99.48%). In extreme cases, only 1% of the data is used, and the F1 value exceeds 97%. For the current attacks against ML /DL weaknesses, we conduct different types of tests by simulating the behavior of the opponent, PDR less than 5%, showing the high robustness of Ji Xiaoan.

      - Because of its openness, multi-source heterogeneity, ubiquity and other characteristics, the security of the Internet of Things is related to the security of individuals, families, society, and even the country. In terms of commercial value, according to the proportional distribution of Gartner cyber security industry product structure, in 2019, the market size of my country's intrusion detection/defense equipment is about 1.9 billion yuan. Therefore, Ji Xiaoan-IoT qualitative intrusion detection system, such a high precision, fast, robust and lightweight practical system, we believe that the future development of this product will have unlimited possibilities!

      - - 1. ##  The painpoint to be solved in this work

      Compared with the signature-based intrusion detection system (SIDS), it is difficult to collect and update intrusion information, it is difficult to detect local intrusion and new intrusion behavior, and the workload of maintaining the feature library is huge; the anomaly-based intrusion detection system (AIDS) can detect new intrusion or never-sent intrusion; it has less dependence on the operating system; it can detect intrusion of abuse of authority. Therefore, we mainly devote ourselves to the research of AIDS, especially focusing on the application of artificial intelligence technology in it.

      For the methods in ML /DL mentioned in 2.2, we have analyzed the current problems faced by supervised, unsupervised and semi-supervised methods, so we propose a semi-supervised ESet based on frequency domain coding converter. ESet is committed to implementing a high precision, fast, robust and lightweight AIDS, aiming to detect network attacks in Traffic records generated by IoT networks, taking advantage of labeled and unlabeled Traffic sequences during training.

      - To sum up, the painpoints we mainly solve include the following aspects:

      - - There is a shortage of labeled data. Due to the rapid and extreme increase in the size of IoT data, it is difficult to obtain up-to-date labeled IoT Traffic datasets, especially for intrusion/cyber attack detection. Therefore, learning from unlabeled data has become an important research challenge in the IoT environment.
        - Utilization efficiency of tagged data. It becomes difficult to manually tag a large number of IoT records. However, a small fraction of IoT traffic can be tagged, and most of the rest can remain untagged. We use a semi-supervised DL method, which is ideal for this situation and can effectively learn from a small amount of tagged data, achieving an accuracy of 10% of the tagged data and 99% of the F1 value.
        - The robustness of the model is an issue that most IDS ignore. We consider three different attack methods, using white-box-gray-box-Black box attack to simulate the behavior of the adversary and discarding unrealistic assumptions to attack ESet. From the test results, it reflects the high robustness of ESet.

      1. # Work design and realization

         - 1. ##  Overall design and function introduction

      We design the application model and functions of Ji Xiaoan in the real-world IoT network. The figure below shows the application model of Ji Xiaoan's medium and semi-supervised intrusion detection framework.

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=OGRiN2FjMDZhZjJjYmZkYmVlYmVlMzBhOWI5ZjExZTdfU0o0Y0hNeWdYQ1dKYVVZbTBJbUJaNEVvb0RuZmVrNjVfVG9rZW46Ym94Y25RdEVETjB0Y2xpcW5Kc1ZKZTFkWEplXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      Figure 3 Application model of semi-supervised intrusion detection framework

      The structure of the Internet of Things network is mainly composed of three layers, namely the cloud layer, the detection layer and the edge layer.

      The cloud layer holds high and powerful computing resources; therefore, the Model Training process takes place at this layer, as the training requires obtaining a large amount of IoT tracking data. Such Big data can be easily aggregated and stored in the cloud. In addition, the cloud layer stores the model configuration, old pre-trained versions, and other settings related to the training transaction.

      The detection layer usually consists of many fog servers/devices, bringing the computation closer to the edge of an IoT network. In an IoT network, the detection layer has a critical role as it is where intrusion detection occurs. Specifically, each detection node consists of four main parts, namely: 1) Traffic Aggregation part; 2) Traffic Preparation part; 3) Traffic Countermeasures part; and 4) Traffic Diagnosis. The Traffic Aggregation component is responsible for capturing and receiving IoT Traffic records from the IoT network connection part at the edge, and then passing batches of samples to the preparation phase. The Traffic Aggregation component is responsible for converting the received batches to a standard format, applying the necessary Data Cleaning and normalization. After that, the Traffic Diagnostic component is designated to use **to classify the prepared IoT Traffic data** , without any communication with the cloud backend, thus preventing any Motion to Photo Latency. This classification process can be carried out in the case of binary or multi-class. Once an activity is identified as an attack, the provided activity information is forwarded to the cloud backend for brief introduction. Each detection node is responsible for diagnosing the relevant area of the IoT network. Therefore, all IoT Traffic records are captured by the corresponding atomized device operating in promiscuous mode. For example, given that there have been significant changes in Traffic in a particular area of the underlying IoT network, if these changes are malicious, i.e. Denial of Service (DoS) events, Ji Xiaoan will identify them and communicate the countermeasures component. When the change is benign, some nodes must be connected to another accessible atomization device to mitigate the situation in which it becomes congested. After all, the countermeasure component takes the decisions generated from Ji Xiaoan and then executes the necessary predetermined countermeasure modules, namely warning, blocking, and deleting actions. After this, information about the identified actions is transmitted to the cloud for use in the logging component of the results.

      - Finally, the edge layer consists of edge nodes and edge devices (i.e. laptops, smartphones, smartwatches, etc.) that communicate through the IoT network through routing and switching devices, and are simultaneously connected to specific fog servers/nodes as a computational bridge to the back end of the cloud.

      - - 1. ##  design scheme

             1. ###   System Environmental Design

      Now all the communication between cloud IoT platforms and devices is essentially built on TCP/IP protocols, just re-encapsulation of data packets, based on which we can use Wifi, 4G to achieve communication between devices and Cloud Computing Platform.

      Based on the preset application scenario model of Ji Xiaoan, we design a real IoT network system instance. At the same time, "Ji Xiaoan-IoT network inspection expert" is embedded in the detection layer nodes. The specific network topology structure is shown below. We use the Windows 10 x86 system host to simulate the detection layer nodes. In order to simplify the configuration of the instance, after completing the traffic collection at the edge layer, according to our predicted application scenario, the next step is to perform Model Training and detection layer prediction in the cloud layer. Here it is simplified to use the cloud-trained model to directly complete the prediction of the model at the detection layer. This architecture is the simplest architecture, the device is like our mobile phone, based on mobile communication to access the Internet.

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=NmI1Mzg1Y2I5OGNkMmE2MzI3ZGEzNjMxNmRhNDkzMzFfemVXWXNLcVNyQ1d6VTdUOXRJYmRBN0JheU9ESkszY2NfVG9rZW46Ym94Y240eElXQjRSeG1zbWZidVh6aDBsOFFjXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      Figure 4 Example system environment

      1. #### Equipment Hardware

      Cloud environment:

      Intel Sky Lake-E, 12 multicore processor built on the experimental environment, using Ubuntu 18.04.6 LTS, 3.10.0-1062.9.1.el x86_64 operating system; we also use NVIDIA company's GV104 [GeForce GTX 1180] as our GPU environment to accelerate our experiments.

      Detection layer equipment:

      Honor Magic Book 2019 laptop with Windows 10 x86 system

      Edge layer devices:

      Honor20 smartphone

      Xiaomi full screen TV EA65

      Fluorite C6CN Starlight Surveillance Camera * 2

      Xiaomi watch S1 smart watch

      1. #### Description of topology

      **host server** : Windows system computer, and set it as a WIFI hotspot, and then let our home devices are connected to the WIFI up, the formation of an Internet of Things, so that all devices of data Traffic through the server, and in the service on which the deployment of Ji Xiaoan - Internet of Things network detection experts.

      **Ji Xiaoan - Internet of Things network detection expert** : Detection system will analyze the Traffic information of each device, once found to have reached a certain threshold of malicious attacks Traffic arrival will send an alert by e-mail, remind the relevant staff to pay attention to check the network environment, if necessary, disconnect the network connection of related equipment.

      **Network intrusion topology example** The following is an imaginary network intrusion topology diagram, a hacker from the outside access or breakthrough connected to the network, and then send malicious network data to the camera 1, and then detected by our software, and then send early warning information to the relevant personnel, and then by the relevant personnel to detect.

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=YTkxMTFjYWVjYmQ0ODQzMGQ3YTFmMDIxM2FjNDU3NmJfQkpWQ1dCOXlGZzM1Z2wxQUdwelVkcHNWUlRydkIxNmNfVG9rZW46Ym94Y25UYnhDV01oNVFmNjEzczJ3YlJNZmhnXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      Figure 5 Example of network intrusion alarm

      1. ### Underlying Algorithm Design Scheme

         - 1. ####  Methodological overview

      Internet of Things Network Intrusion Detection (IoTNID), as an important active security defense technology, aims to achieve accurate detection of network attack events. In recent years, many supervised and unsupervised methods have been proposed for IoTNID. However, these methods mainly face two challenges. First, the vast majority of network traffic data is unlabeled, and existing methods cannot effectively combine these unlabeled data with existing tagged network traffic data to improve the accuracy of detection. Secondly, they cannot learn features from different layers of network Traffic data, such as data packet hierarchy and Traffic hierarchy, so as to have a comprehensive understanding of network Traffic characteristics. To address these challenges, we propose an extreme semi-supervised model (ESeT) based on a dual-feature coding converter, which uses only a very small amount of labeled data, makes full use of unlabeled network Traffic data to enrich the extracted feature information and reduces the negative impact of false pseudo-labels through a confidence selector. Furthermore, we propose a Multi-level Feature Extraction to learn Traffic-level frequency-domain features and data packet-level byte-coding features. Experimental results show that our model achieves excellent performance on NIDs not only on IDS2017 and IDS2018 datasets with a small percentage of labeled data (10%) (F1 score: 99.48%).

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=NmQ0OGU0MjE1Yzg2ZDE0Y2YzNmIyNDRkNGE4MjYyNzhfclJoSmUyY2lkOFhRUFhtRDZWd0xtYUFpQVVnMWh3TXFfVG9rZW46Ym94Y25JMlpiSkgwSGZiWUo3TGdOd1RoRjVjXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      Figure 6 Eset overall architecture

      - The figure above shows the underlying Deep learning foundation of our IoT network system - ESeT, which consists of two modules, namely multi-level feature extraction and semi-supervised bi-feature coding converter. Multi-level feature extraction includes byte encoding and frequency domain feature extraction, with the purpose of extracting byte features and frequency domain features of network working Traffic. The semi-supervised bi-feature coding converter includes the bi-feature coding converter as the core components of prediction, confidence selector and feature enhancer, and it describes the semi-supervised training process. The raw input data consisting of labeled and unlabeled pcap data packets is sent to the multi-level feature extraction module. After extraction, the processed data is provided to the semi-supervised training module for prediction.

      - - 1. ####  Multi-level feature extraction

      Traffic is first filtered and separated into sessions. Then, the filtered and separated network traffic is analyzed by random Vector byte encoding and frequency domain feature extraction, and byte features and frequency domain features are extracted.

      \1. Random Vector byte encoding

      (1) anonymization.

      Addresses in network traffic data, including MAC source and destination addresses, as well as IP source and destination addresses can reveal the class labels of traffic data, we use anonymization to deal with this problem, replacing all MAC addresses with 00:00:00:00 and all IP addresses with 0.0.0.0.

      (2) Numerical coding

      After anonymizing the data packet, we read the data packet in binary format and convert it to a sequence of 8-bit integers in the range [0-255].

      (3) Uniform length

      We determine; as the data packet length. For the data of each data packet, we truncate it or fill the data below this length with 0 to guarantee a uniform length.

      (4) Random Vector encoding

      We use the method of randomly initializing vectors to render the raw bytes with randomly initialized floating-point vectors, which greatly reduces the space footprint compared with one-hot encoding. In addition, since every numeric unit has a value and the numbers have practical significance, it provides a basis for the subsequent positional encoding and bi-feature encoding of our semi-supervised converter.

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=NmE0YTY0ODZlMDgyNmNiZDkxNTYwM2Y2NDY3YzVhNDVfOTZNZFF4NFBCdE1jUE5QdnpXVkFGcDU3N2txSEtreUdfVG9rZW46Ym94Y25UaVE1VmdKUnNDa3dIN3NOQkhxWUNXXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      Figure 7 Random Vector byte encoding steps

      \2. Frequency domain feature extraction and analysis

      First we denote each data packet feature of all data packets as a matrix S, where Sik is defined as the kth attribute of the ith data packet,

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=MjZjOWY4MzI0NTBmMWVlYzM2ZTY0Yjk4OWVkYzBkM2JfejNnWDFCcDQwbU1jVlJrMHQyUGZyNWZPaWtzZ3UzY2NfVG9rZW46Ym94Y245bWhJZTlRdnJ2U2hxQlllVEZWUGRQXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      Then multiply S by a coding vector w for linear transformation, and the value of w is realized by the automatic parameter selection module, resulting in

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=NTk2M2EyNzFkNTY0YzcwNDQwY2I2M2U4NjZiOTJmMDRfZ2xkRGJMNVBVMjZ5UWVOZ2pnc29MaFg0bzZROGVsaTNfVG9rZW46Ym94Y25ITGFndWVqS3g4RnE1bFFxRlFpRTljXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      Next we need a frame-based discrete Fourier transform, first split the data packet into frames, we denote the number of frames as Nf, and the length of the frame as Wseg, denoted as:

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=NGU5ZGIwNmNjZmFjNDFhMmJmMzIzNDA5NjU2Nzg5YTdfbFc5NXpxUTNMdXJRekxNUFowNWZYQ3d5ek0yZGt6NlFfVG9rZW46Ym94Y25hOHBoWkFaRzUybDJadDFMN0ZRY0lsXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      After we perform a discrete Fourier transform (DFT) on each frame, we can get the frequency characteristics of each frame as follows:

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=OGIyNzVkOTM3MDA1M2Y5ODEyN2VmZWNhNjUyODQzNDZfOXBEVzlnNlNXcUNFVURNWWJpbjZIN1RITmFpQjlnQnRfVG9rZW46Ym94Y244MFJZdkdSN3RpUEx0bFg2bkJsVWtoXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      Fik is the frequency component of frame i with frequency 2π (k − 1)/Wseg. Since the obtained Fourier transform is a complex number, it cannot be used as an input to the Machine Learning Algorithm. Using the coordinate plane method, we convert the complex numbers to real numbers and compute the modulus expressed in the frequency domain. In order to make the frequency domain features numerically stable and prevent floating point overflow in Machine Learning training, we perform the logarithmic transformation to obtain the result as shown in the figure below:

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=NWIyM2JkNTA2YjRlN2E2MWQyOGE2YTU3Yzk3ZTU4MTFfVldMeGlTY3puV2Nndzl2MU1VSHpOMmNqZWI2dEd0WE1fVG9rZW46Ym94Y25mc1VPUlpNNmJvUU9lSE85d1BLdVRoXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=YmRjNDY1NjYyZTNhM2YyZjE0OWZiMmE5NTcyN2YyMWFfZk9BNVNvZk5yUm5kbHEyWWVPQ0tzYldod0dqSkpyMFBfVG9rZW46Ym94Y25GTUVZTDVqdWJrM3NBcEFHQWRrWlhjXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      The two-feature coding converter (DET) is a core component of our semi-supervised learning model. DET itself can be used as a top-level supervised traffic classification model, achieving high performance in semi-supervised training with only a few labeled samples.

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=OWI0NTJlN2U4NTkxNjdjN2ZkYmMwNGFlZWUwMWI1ZjFfNGNqR3VZVk0xRnZVdUlpbXZOdzV6THZMejFPM2ZrNnFfVG9rZW46Ym94Y25UMDFCcE4wZ3JTOVNyUlFsaGZRc2ZnXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      Figure 8 Multiple Feature Fusion Coding Transformer

      The overall structure of the DET is shown in Figure 8. DET receive the byte encoding result given by the feature extraction module to obtain metric I, including sub-metrics, of shape. Each matrix represents the feature of a data packet, where it represents the number of bytes used for byte encoding and the length of the random byte-encoded Vector. The frequency domain feature results are fused into the Transformer model.

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=YzQ1NzgyOTdmMDdlMmYzOTIyZjY1M2E5Y2Q3OTc5NTBfZU8wT0pzTUNlSjB5TGVoRWY2R0JzZUpjU3BicjB0VkhfVG9rZW46Ym94Y254R1Q4MEJ0SzNBWHhTMW1oSUFqMlJiXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      After position encoding, the data will be processed together with the extracted frequency domain features in a two-feature encoding. The two-feature encoding first obtains the output of frequency domain feature extraction and extracts a matrix F related to the frequency domain features of these data packets, which has a size of. The coding vector V (length is) is designed to determine the learning weights for each frequency domain feature, which will be automatically generated and updated through continuous Model Training. The process of obtaining the frequency domain feature values of the data packets is shown in the following formula.

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=YzNmYmYwNWUwYmU1NDY0OGJlZmRjOWFiYzhiNjQzZTBfemY1M1AyY2ZLUmNOQmE3NDBqMzFFaXUycFUzeUxoMEtfVG9rZW46Ym94Y25FaGZia1ZaanNCbFIwYll0bTlON21wXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      Wherein, for selecting the input data packet of the DFT corresponding to the frequency domain feature index metric 0-1, represents the frequency domain feature of the i-th data packet on the k-th attribute, V represents the coding vector, represents the final frequency domain feature value of each data packet.

      Since the frequency domain features and byte features are represented in different dimensions, they reflect the frequency domain features of the data packet based on the flow granularity on specific attributes. It cannot simply be used as byte attributes to laterally splice the original byte coding features. We implement the weighted & residual join operation on the basis of the original encoding, and the obtained result is used as the output of the frequency domain feature encoding. In this way, the stream-based frequency domain features are incorporated and the unaltered byte features of the original data source packet are retained.

      The encoder is composed of N identical layers with two sub-layers, which represent the multi-head self-attention mechanism and the fully connected feedforward network layer respectively.

      - After N identical encoders, a classification layer is added to the output to make predictions. The classification layer is implemented by a linear sublayer and a sortmax sublayer, which embeds the classes into the number of classes as an indicator of the final classification result.

      - - 1. ####  Semi-supervised training architecture

      1. Model Training View

      We split the raw training data into labeled and unlabeled data to simulate a semi-supervised situation. We sample the data using the proportional screening method to ensure that each class of unlabeled samples has the same proportions as the classes in the overall training data.

      1. model pre-training

      First, both labeled and unlabeled data are input to a multi-level feature extraction module.

      After FE, all data samples (including all labeled and unlabeled data) are used for kitnet training of the trustworthiness selection module, and the first 50/% labeled data samples are selected to pre-train the DET to ensure that it has basic traffic anomaly detection capabilities.

      1. each round of training

      In each round, a certain proportion of samples are selected as the input to the DET and kitnet networks. DET predict the classification result, while kitnet generates an RMSE vector representing the root mean square error of the difference between malignant data and benign data. Based on the judgment of RMSE values and prediction results, the trustworthiness selector filters out data that can be used as raw materials for pseudo-labels. The qualified prediction data screened out by the trustworthiness selector module will be mixed with a certain proportion of labeled samples, and the feature enhancement module fuses the output of the trustworthiness selector with some labeled sample data, and performs feature enhancement. After processing, these data will be used as pseudo-labeled data samples, and then input to the converter model for training. At this point, the model enters a new half-training round.

      1. Confidence Level Selector

      The confidence selector is designed to filter out predictions with high confidence and discard those with low confidence.

      1. Confidence Level Guarantee Mechanism Based on Kitnet

      The implementation of Kitnet Algorithm is to filter the prediction results from the DET by utilizing the RMSE values positively correlated with the malignancy rate. Kitnet is a lightweight core algorithm of Kitsune [23], which is used to generate a differentiated indicator RMSE that distinguishes malignant Traffic from benign Traffic. Although not accurate enough for prediction, in our experiments, the RMSE value proved to be a good evaluation indicator of the reliability of prediction results. Since only a small number of samples are trained, DET itself is not enough to make accurate classification results, the credibility selector helps to filter out the prediction results with high confidence and discard those with low confidence. The pseudo-label samples of the new round of transformer learning are more accurate.

      1. Filtration principle

      After generating RMSE using the pre-trained kitnet mapper, the trustworthiness selector filters out benign labeled data whose RMSE value is lower than the malignant RMSE limit, and malignant data whose RMSE value is lower than the benign RMSE limit. Both benign and malignant RMSE limits are automatic parameters that are learned by each round of training and duration. The whole process can be expressed as:

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=MDg4NGRiZDJmODhiYjNhODYyNjYxZTViNDkxMTRiZjBfN2RWMzlacXl3M1Q1SkszcHZoZzJldFZBUGMzZFdmVHBfVG9rZW46Ym94Y25WUGRsYkdNbHl6bFYyQjNLczFWNEJiXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      Wherein, I represents the input feature of each round of data packet, RMSEs represents a vector of RMSE values,, represents a benign RMSE threshold and a malignant RMSE threshold, the mask indicates the result of selecting a high Confidence Level data index.

      1. Feature enhancement module

      In order to ensure that the model will not deviate from the original prediction accuracy due to inaccurate pseudo-labels during continuous training, we add a certain proportion of label samples to each round of pseudo-label generation. Since the same type of attack Traffic has similar frequency domain features, in order to further enhance the features for better training effect, we randomly select the frequency domain features of the labeled Traffic data, and randomly exchange them with the byte-encoded features of the predicted Traffic data of the same class in the original labeled samples to generate new data samples.

      1. ### System function design

      The main function of this system is to collect the data packet of each device flowing through the server network interface card, and then transmit it to the already trained intrusion detection model to obtain the prediction result, and store it in the corresponding database, then organize the data and transmit it to the front end page, the front end maintains a table for each device for rolling display, and when the proportion of data packets that detect instantaneous malicious attacks reaches a certain threshold, issue a warning. As a result, it can monitor the entire network environment in the Internet of Things in real time and protect the cyber security of each device. And after experimental tests, the system can also do real-time detection and analysis under the high-load network environment of 20,000 data packets per second.

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=MzcwMjhmNWI5YTYyNjEzNTVmZmU5NTRhZWMwYTk0NjRfczNBQkh4Y1E2VnA3VUJ3QUF1WURDNDFNY0k0OFRpYjdfVG9rZW46Ym94Y241VzJVVmF2NVZSQk1HT1FOeGJTTVBkXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      - Figure 9 Overview of system functions

      - - 1. ####  operation design

      When the program runs, you first need to select the local network interface card to be captured, that is, the network interface card used as the hotspot.

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTMxODczYTMxMTA4OTdiNDc3ZjNkZjA0OTljNGM2MGFfdWNOSTFocGxDejRTUTBPdlZkZTZQQ3p2dG5LVlZEQXpfVG9rZW46Ym94Y25uZ0V6dUdOY2NJWkc0N0NGaFVick1yXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      After the selection is complete, the program will scan all devices connected to this network interface card, and then the user will select the device to monitor, here is select all:

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=MTM4NTg2MmY2NjMwMTU4MmU5MjdkM2NhN2M4ODJhZjhfdllwUVFBRWdRVk83eE9Nc0hPTmRUNldqVmpHeXJKWWtfVG9rZW46Ym94Y25NWG5UT2NZVFVsdTlrS2xERFYwOHVlXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      After confirming, you will enter the monitoring screen:

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=NTY4MWQxNDg2NmQ4NDNjYTMwZmZmZjhmNzQwYTRmNzdfanlOdWg0cWdNUE9nU1VhcFRHYXNGMGlFTjJmUmpWM3dfVG9rZW46Ym94Y25oWEhCa2hsODFiZUt5Yk82bDdpaW1mXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      Click Start Start and the program starts running.

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTliMmM4N2FhMTE1N2FjMmI3ZGZmOWM2ZGMxZDgwMjZfdGZyMzBxSGlDODlPeWFraXNieUkzNldpeUZ1VkRvdDhfVG9rZW46Ym94Y25FdE1rRmh5T3FhMnhhVmMyTDZMaHJoXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      If the malicious packet rate of a certain device reaches a certain threshold, a pop-up warning will be sent, and emails and text messages will be sent to the pre-set user:

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=MzU5NmIzOWQ0MDRjMDgyMWVkNzUzNjY5ZjU2YjEwMDlfWW51Qnl3SEZrMXFUQnUwMERaTVN5VUl4ZjBRNGthaVNfVG9rZW46Ym94Y25IZTlVQno2VGJOeGZYdnZCNk1hVkNlXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=MjY0ZjBiMDJjZjk1Y2YwY2JlMTQxNDUxZGZiMDE0NTJfZzQ2UnVxOFZMWUFzSTFOeDZsd2MxWHFkZ0FXdFY1MDVfVG9rZW46Ym94Y25BN2hDSG5PcW9wc3ZaV1hmQ3JIeGFkXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=M2FiNjYzODIyZDQyNmNlNTNkNWUyMzNhOTM1MzJiYWFfeGIwQXBzMEVsb2RNRlZyeFpmRHB1TGdId1dNRHM5M01fVG9rZW46Ym94Y24wRHJkYnJvTXhnaHBvT2ZiRjBpOHdnXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      - - 1. ####  System interface design technical description

      This program is developed using Python, the Python version used is 3.8.6, the development tool is Pycharm, and the running platform is Windows10.

      **Pyqt5 front-end UI framework implements system realization page design** . The design process adheres to the Interface Segregation Principle, an interface only does one thing, and a button only corresponds to one function, which ensures the decoupling of program functions, high Aggregation and low coupling. At the same time, it fully increases the code to reuse, showing that the data table of different devices uses the same class to design and to reuse.

      **SMTP service to achieve 163 mailbox mail sent** . We registered a special account to send emails to system users, in order to promptly inform users of the threat content.

      **Sqlite realizes front-end separation and data interaction** . Program front-end display is separated from back-end network card data packet capture, prediction and other functions, and data transmission interacts through Sqlite database.

      - **Multi-threading technology ensures concurrent execution of front-end and back-end** Since it is necessary to analyze and process the Traffic data of different IP corresponding IoT devices at the same time, as well as take into account the front-end display and mail sending of the system, each part of the function needs to be coordinated by multi-threading technology to ensure the stable operation of the program.

      - - 1. ####  Sqlite database description

      This program uses Sqlite data. Sqlite is an in-process library that implements a self-sufficient, serverless, zero-configuration, transactional SQL database engine. It is a zero-configuration database that does not require installation or management, does not require a separate server process or operating system, and has a very small capacity, less than 400KB when fully configured. At the same time, it has strong compatibility to ensure stable operation on different computers.

      After selecting the device to be monitored, each device program to be monitored will go to Sqlite to create a corresponding data database & table, and the subsequent captured data packets will be stored in the corresponding data database & table item after parsing in the program. The structure of the data database & table is as follows:

      | Data table name: device name |                                      |           |        |            |                    |
      | ---------------------------- | ------------------------------------ | --------- | ------ | ---------- | ------------------ |
      | field _ id                   | description                          | datatypes | Length | is _ empty | Remarks            |
      | Index                        | Data packet sequence number          | int       |        | N          | Primary key, index |
      | Time                         | Data packet capture time             | int       | 50     | N          |                    |
      | SourceAddr                   | Data packet source address           | varchar   | 18     | N          |                    |
      | DestAddr                     | Data packet destination address      | varchar   | 18     | N          |                    |
      | Length                       | Data packet length                   | int       |        | N          |                    |
      | Type                         | Data packet type                     | varchar   | 50     | N          |                    |
      | IsBad                        | is malicious                         | int       |        | N          |                    |
      | AllData                      | Data packet byte by byte information | text      |        | N          |                    |

      - - 1. ##  evaluation indicators

      Ji Xiaoan is committed to achieving a high precision, fast, robust and lightweight AIDS. Therefore, we set up the following evaluation indicators to evaluate the performance of Ji Xiaoan, and give the real performance of Ji Xiaoan in detail in the subsequent test part.

      1. Accuracy: measures the proportion of predicted samples to total samples, and the proportion of malignant Traffic to total samples:

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=NDI2ZTJjNzVjM2U2NDJkMmY3MWVmMzY5MDU5NmJiMThfdU85UnNUeDRsMnNtYkQzdThVSUp6Q3Mya1pkdGtQQ1ZfVG9rZW46Ym94Y25QeHVGejVKWURpdU94OTh0elVKbnd0XzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      1. Accuracy: A measure of the proportion of true positive samples among all predicted positive samples. Proportion of all predicted positive samples:

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=YTg2NzA4MDNkNWY4NjhmNDBhMzczNTAwZDFjZDEwYjRfNVZZZXdCSVhTT215TklVUm9kUkZCVjFwaU02ZEFKS1NfVG9rZW46Ym94Y25rRExrbDVYSzFYMkh2cHVPNEc2UHVlXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      1. Match rate: A measure of the proportion of all positive samples, the proportion of all positive samples that are actually predicted to be positive:

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=YTI4MTIyNDRhM2JkYmY3NTU4MDllMTlhOTk5ZjliY2VfZXNWdVB1dlFXbDRSNExMT3l0dTlNVXl6bUVrS1BuNklfVG9rZW46Ym94Y25tekJYZEJ5VWlxbnRzS0xLVWg5R0xiXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      1. F1 score. As a measure of the weighted average of the PRC and RCL, it is a composite response to the performance result. The weighted average of the RCL, it is a composite response to the performance result. The closer the value is to 1, the better the performance result. The closer the value is to 1, the better the performance result:

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=M2Q5N2JmOTkxODMyM2IzZmE0NzFiMDUwOWU3YWQxZDNfRGxwVlo1cndidVhaZTlabmQyRk05Y0hRWHJwWlg0aThfVG9rZW46Ym94Y243ZWdpQjFwY2J5bkNuNURJcXZWU2pnXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      1. Unit data packet training time. Represents the training duration for data samples. In order to achieve real-time training and save computing resources, this value should be as small as possible:

      1. Unit data packet prediction time. Characterizes the duration of the prediction for the data sample. In order to minimize the time loss in the real-time prediction process, this value should be as small as possible:

      - - 1. ##  dataset

      IDS2017 and IDS2018 showcase the recent IDS dataset by Sharafaldin et al. [19] of the Canadian Cyber Security Institute, called CIC-IDS, which contains the most traditional attack categories, as well as unaltered real-world benign traffic widely used in intrusion detection experiments.

      The Mawilab dataset is derived from the WIDE MAWI gigabit backbone (during January 1-10, 2022) documented in the MAWI archive [20]. As it has been continuously updated with mature labeling methods, it incorporates a wider range of recent attack types and has fine-grained classification results. For our experiments, we select the data from January 1-10, 2022 as the model's comparative experimental validation of different attack results.The Mawilab dataset is derived from the WIDE MAWI gigabit backbone (during January 1-10, 2022) documented in the MAWI archive [20]. As it has been continuously updated with mature labeling methods, it incorporates a wider range of the latest attack types and has fine-grained classification results. In our experiments, we

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=ZDRkMWEzYmNmNmFiOGUxYzlmZTU3YTg3MzdiNDEzOGRfT1RCTUhWWlF6TTFIMmRaeGtVTE5tdVQ4WTZ4SGVVWk9fVG9rZW46Ym94Y24wa0lGSUNCVE00ZEczT3dXVHVYREpZXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      Table 1 IDS2017, IDS2018 dataset details

      The data we use is the original PCAP data packet Traffic, and the specific data sample in wireshark is shown in Figure 4.

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTE0YzJiZGVhMjVmMWVkOTVhZWY0Nzc0MWVhNDgxZDZfUHVmbjQweGpSU2VSQVBMTGxxcW5kSUhKSmRqYTh6QVNfVG9rZW46Ym94Y251Yk5nOFRnb0I1Qk9ZTTNUVlJQOTdlXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      Figure 10 Data packet display in wireshark

      An example of a single data packet is shown in Figure 5.

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=ZGQxMDViYWI1MDc1MTgxZmUzYTkyZjc0ODdiZDg2Y2RfRng5b2FTNGpsMzR1TXdYWnBCamJ3OGdaSHBoZnp0cXRfVG9rZW46Ym94Y25NdG00MVgyblVXQ01wSFU2bk5Hd2pmXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      Figure 11 Display of a single data packet in wireshark

      1. # Work Testing and Analysis

         - 1. ##  Experiment Test of Intrusion Detection Algorithm

      To validate the feasibility of the model, we conduct experiments using the latest IDS datasets IDS2017 and IDS2018. IDS2017 and IDS2018 present the latest NoTNID dataset from Sharafaldin et al. [27] of the Canadian cyber security Institute, which contains attack categories for a wide range of IoT networks, as well as unaltered real-world benign traffic widely used in IoT network intrusion detection experiments.

      Detailed dataset information is shown in the table below:

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=MGU5ZjI2YTg5ZWVmYTQ4MDY1MTliOTBjOTU5N2U2NjdfY0tKaVhhOFhaU1ZFS0pHelV5QVZtMGpoUDZtd3d1RU1fVG9rZW46Ym94Y256TG1wMzJCeExzZVNvejAxcmptZjBkXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      Table 2 Dataset Details

      1. ### experimental environment

      We built our experimental environment on an Intel Sky Lake-E, 12 multi-core processor using Ubuntu 18.04.6 LTS, 3.10.0-1062.9.1.el 7.x86/64 operating system; we also used NVIDIA GV104 [GeForce GTX 1180] as our GPU environment to accelerate our experiments.

      1. ### Comparative experiments and results

      This experiment compares the performance of our model with the latest supervised, semi-supervised and unsupervised models on the IDS2017 and IDS2018 datasets.

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=NTUxYjA2YmE2ZGUwMmI5MTc4NmE5NzQxZDEyMzM1Y2NfTnc2cU9TUTBVTE5VNnp2M1Q5bERYSDBKOXhLSENicWpfVG9rZW46Ym94Y25KQ0xQSG1jaE44c2NucnRUaDFaUUZlXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

       

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=YjJjZjY1M2YyZjY3ZjBjNjY1ZDA0MTc0ODNhZjgwZmJfRW1wZjY5Z2Y0SDF6dWs1UGl4Q0ZLZFgxUWdnN1BOT1lfVG9rZW46Ym94Y25HTnc0RG82OUhHWkRQME9KOVhXTGliXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      Figure 1 Comparison of experimental results

      In order to ensure fairness of experimental results, all supervised learning models are trained with only labeled data, while semi-supervised and unsupervised models are trained with all labeled and unlabeled data. The left figure compares and analyzes the best existing model with 10% of labeled training data. The right figure shows the performance results of ESeT in different proportions of labeled training samples. 1%, 5%, 10%, and 20%.

      - In all the semi-supervised and supervised vs. unsupervised learning model Algorithms, the proposed model achieves good performance results on all metrics. In the extreme case, the F1 value exceeds 97% using only 1% of the data. This is sufficient to demonstrate that the proposed model achieves excellent performance results under different proportions of the training data.In this case, the proposed algorithm achieves excellent performance results on all metrics.

      - - 1. ##  Ablation experiment

      In order to further verify the performance of the model under more diverse and rich attack types, we selected all Traffic data from January 1 to 10, 2022 in the mawilab dataset for comparison experiments. The dataset includes a total of 43 attack types. The attack traffic distribution and prediction results are shown in the figure below:

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=NTU5OTcwZmQxMjIyOTZjMWY1OWFjZGFmOGJiNDMwYmRfSU1qeUIxaElySDFhcm9HMmR3dWJMYThhZEYzNXZyUGVfVG9rZW46Ym94Y253dXd1dkNnT1hxYjNzR1o5VWIwUzVkXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      Figure 2 Summary of attack types on the mwilab dataset

      Consistent with the previous description, we also trained the model on a 10% scale of labeled samples and compared performance results for different attack types across 43 mawilab datasets.

      - Our performance on the entire mawilab dataset also achieves a high performance, with an F1 value of 99.7%. From the table, we can find that the QIIS can achieve a prediction accuracy of 99% or higher for most attacks.

      - - 1. ##  robustness test

      In addition to focusing on the performance metrics of the model (F1, accuracy, Match rate, etc.), we also evaluate the robustness of the model against adversarial attacks. Below, we evaluate the robustness of the model under the mawilab dataset by simulating two attack modes: layer-based attacks (white box) and attacks of practical nature (gray box, Black box).

      1. Layer-based attacks

      Our feature extraction is divided into byte encoding and frequency domain encoding. Due to the discreteness nature of features and the nature of non-numerical meaning, byte encoding is resistant to layer-based attacks. For frequency domain encoding, its robustness is evaluated in this experiment using an approach similar to FGSM [22].

      The eigenvectors encoded in the frequency domain advance in the opposite direction of the layer in one training, and the distance can be expressed as:

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=NWQzMWY5OTZiMmI2NjE2ZTg5MWQxMGQyNjRkMjA0ZWJfdHVKSUpCNVZCcXdBT09HeVVBMjN5OUg1TFpBUFh1YnhfVG9rZW46Ym94Y25kZVpyNXIwOHprVk9UaEtQdGk2U2loXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      Which

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=MmEzMjhjZDQwMzI4MzQyY2YwZjIxY2IwOGQwYzkxMThfd2pmcEtrNUVMdHg4SUJXblhhM2RON0JqcmJSS2NadGNfVG9rZW46Ym94Y25yQ1hpUXBNNTlIY2NrelllZzE5b1ZmXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      This method can be defined as increasing the small perturbation scale, resulting in large changes in the model results. We did a set of tests on mawilab, which will be set to different values, and found that this perturbation has little effect on the model results, as shown in Table 3.

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=N2MxMDY1ZDUzOGRkZTE4Njc5MDMxNTAyY2Y5YWRjMTRfaDJsNnpYV1BOaUdIV0lzRnNTT0w3MmZVenNUOE12cVpfVG9rZW46Ym94Y25uaEc5OUtQQnQ2bnBtNzl2WVJNTmdYXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      Table 3 Effects of differences on model robustness

      1. Attacks of a practical nature

      We focus on two methods in [21]: utility gray box attack (PGA) and Black box attack (PBA). [21] The GAN-PSO-based algorithm generates evasion features that automatically change the original malicious traffic under limited overhead without affecting its functionality. The algorithm combines GAN and PSO methods to complete evasion attacks, which can be divided into the following two steps:

      Adversarial Feature Generation: We assume that the attacker wants to start some activity, which will trigger a series of malicious traffic. First, the attacker needs to collect some benign traffic in the network he controls. Then, the two types of traffic are extracted into features through a proxy extractor and fed into our GAN model. After the training phase, the generator is able to generate adversarial features.

      \2. Malicious Traffic Mutation: After generating the adversarial characteristics, we automatically mutate the malicious Traffic using a PSO with predefined operators. Each particle in the swarm represents a vector consisting of meta-information of the mutant Traffic. The swarm iteratively searches the traffic space, guided by a temporary best particle whose characteristics most resemble those of the adversarial one. Finally, after many iterations, the best particle is selected.

      In addition to the traditional metrics (F1, Accuracy, Match Rate, Precision), [21] introduced new metrics (MMR and PDR) to measure the effectiveness of the attack. The relationship between attack effectiveness and robustness is that the better the attack, the worse the robustness.

      The interpretability index (MMR) can clearly show the feature changes in the latency space during the attack, reflecting the proximity of malicious features and adversarial features in the mutation process.

      Malicious probability drop rate (PDR) is used to measure the decline rate of malicious probability output by the target classifier. The higher the value of the PDR, the better the attack effect and the worse the robustness of the model.

      PGA and PBA discard unrealistic assumptions in favor of more practical attacks. In short, in PBA, the attacker has very limited or no knowledge of the features used in the target NIDS, PGA the only difference between PBA and PBA is that the attacker knows our feature extractor.

      PBA: An attacker without any knowledge of the target system can only simulate the extractor by using other features. Suppose he uses the model Kitsune [23] (a relatively mature IDS) as the target NIDS and obtains adversarial Traffic and inputs it into our model. The results in Table 4 show that although these modified Traffic achieve a good attack against Kisune (PDR = 23.00%), it is not sensitive to our model (ESet) (PDR = 2.10%).

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=OGYzNjhiNDk2YjllZGVjY2FkZGEzNmQ1NTA1OWNkYzBfbjdmbHYwWENkZVZMQmZZcnNNNnZ1MVNnWUF3ZWxSSUVfVG9rZW46Ym94Y255YzR0c01lTmhRMUh1dk1NbDBlTWVjXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      Table 4 Impact of kisune-based PBA on ESet

      PGA: We used frequency domain coding as a feature extractor to analyze the impact of different attack costs (l_c, l_t) on the robustness of the model. The first overhead, expressed in l_c, is the ratio of the number of crafted data packets to the original data source packets. The second overhead, expressed in l_t, is the time-consuming rate of mutated traffic vs. original traffic. We used lower l_c = 0.2, l_t = 2 and higher budget l_c = 0.5, l_t = 5) and the results are shown in Table 5. The results show that whether it is high cost (PDR = 5.25%) or low cost (PDR = 3.44%), the impact of PGA on ESet attacks is limited.

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=NWFhNzExNjE2MmNmMGEyMDkzNjJlNjcwNmRlNzUyOWZfRDJEbnNGV1Y1bmhOUGlISHFBTm1laWE4QjJFVzdpbUhfVG9rZW46Ym94Y25UMHpsaVpZT0FId1BFQzZPUE85TURmXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      Table 5 Impact of different attack costs on our model

      - Taken together, these results demonstrate the robustness of ESet. In particular, our model is insensitive to adversary attack costs.

      - - 1. ##  Stress Testing Experiment

      The stress testing of this experiment is mainly to check whether our system can run smoothly in a multi-device and high concurrent network environment. The main source of pressure lies in whether the system can capture the data packet in all network interface cards in time, whether the model prediction can be completed in time, whether the data can be written to the database in time, and whether the page update displayed by the front end can keep up with the data packet generation speed in the network environment. The final evaluation indicator is the time it takes to send the data to the front end page display.

      **Test Scenarios**

      This Stress Testing uses 3 computers to connect to the same server, close other software that may generate data packets on these 3 computers, use xcap software to perform code packet of the released version and control the rate size of the code packet of the released version. Then record the timestamp when the code packet of the released version is completed and the timestamp when it is displayed on the server side, and count the time it takes to display the code packet of the released version from the computer to the server side.

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=MWNjMTJiM2M1Y2NmZjJmYTkyZTQxNTRiNGZjN2ZiZDlfRTAyamFIZkxpQlY1cHNzVW5lTllmMHJyRUw4aTNFWVdfVG9rZW46Ym94Y25xNXJ0UkhnaUdTOTh0RE5PS2hnSUpiXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      Figure 12 Stress Testing Scenario

      **Test results**

      | Speed of the released version of the code packet of the code packet (100Kb/s) | Response time (ms) |
      | ------------------------------------------------------------ | ------------------ |
      | 1                                                            | 50                 |
      | 10                                                           | 50                 |
      | 100                                                          | 63                 |
      | 300                                                          | 183                |
      | 500                                                          | 472                |
      | 800                                                          | 841                |
      | 1000                                                         | 1598               |
      | 3000                                                         | 3721               |
      | 5000                                                         | 8154               |

      ![img](https://p0mv60127x.feishu.cn/space/api/box/stream/download/asynccode/?code=NzdkMTdkNTE2MjI4OTNjZDE5NzlmYzI1Njc4YzE5ZmRfbjdUTGxqMmtGUExPQVV3QVl3S1BVZ0tFS0YyY2Y3NFJfVG9rZW46Ym94Y25GYWtmMnFjU2tzak1jcDdIV2Nxcm1iXzE2Njk1NzA3Njc6MTY2OTU3NDM2N19WNA)

      Table 6 Stress Testing Results

      **Test result analysis**

      The test results found that at a rate of less than 50000Kb/s, the response of the system is very fast, not more than 500ms, but with the increase of the rate of the code packet of the released version, the system will behave unstable, the average response time is greatly extended, and after the rate of more than 300000Kb /s, the system will become extremely stuck and difficult to operate normally. After fixed-point troubleshooting found that the main reason is that the front end for the update of the table, because each update to insert a row to the top of the table, and then fill in the data, and frequently update the table to insert data for the front end of the display is a big pressure point, while reading and writing the database is also a more time-consuming part.

      For general non-industrial equipment such as home appliances, driverless vehicles, the total amount of data generated per second is generally 10000Kb/s, the maximum peak is 50000Kb/s, and this is within the tolerance of our system, which also shows that the performance of our system is sufficient for non-industrial IoT security monitoring.

      1. # innovative description

      The foothold of the qualitative intrusion detection system of the Internet of Things is the security problem in the Internet of Things network, which is a very practical and urgent problem to solve. The security of the Internet of Things is more important and influential than the security of the Internet. The Internet of Things deals with the physical world, whether it is automatic driving, smart grid, bridge detection or disaster monitoring. Once a problem occurs, it may even involve the loss of life and property.

      Ji Xiaoan is committed to implementing a high precision, fast, robust and lightweight anomaly-based intrusion detection system. It can be deployed on the Internet of Things Cloud Computing Platform, train models on the cloud layer and perform Traffic detection at the detection layer, which is lightweight and practical.

      We make full use of the features of labeled and unlabeled network Traffic data and reduce the negative effects of false pseudo-labels through a trustworthiness selector. In addition, we propose a multi-level feature representation learning module that learns both Traffic-level frequency-domain features and data packet-level byte-coding features.

      Since most of the data is outdated and unreliable, lacks diversity, and is too small to cover known attacks, we used IDS2017, IDS2018, a real-world attack dataset that includes both benign and up-to-date common attacks, with broad coverage that reflects current trends.

      - Our main tasks are:

      - - We design an IoT intrusion detection system based on a three-tier architecture - cloud layer, detection layer, and edge layer. With the support of powerful Deep learning prediction speed and accuracy, it can predict the intrusion detection behavior of the IoT system in real time and alert users.
        - We design a semi-supervised model architecture for real-time application of semi-supervised prediction, make full use of unlabeled network Traffic data to construct a real-time NID system, and use a self-designed trustworthiness selector module to provide quality assurance for pseudo-labels based on the sensitivity of kitnet Algorithm to malignant Traffic data. We propose a frequency-domain coding converter, which implements the analysis of extracted frequency-domain features and byte-encoded features.
        - We conducted experiments on three datasets, namely IDS2017, IDS2018 and mawilab, including comparative experiments, ablation experiments, robustness experiments, etc. The results show that our model performs well, with both high accuracy and high robustness.

      Highlights of our work **Highlights** There are two points. First, under the premise that it becomes difficult to manually label a large number of IoT records, only a small part of IoT traffic can be labeled, and most of the rest can be unlabeled. Ji Xiaoan was able to efficiently learn from a small amount of labeled data and a large amount of unlabeled data, achieving an accuracy rate of 99% of the F1 value of 10% of the labeled data. In extreme cases, using only 1% of the data, the F1 value exceeds 97%. For the current attacks against ML /DL weaknesses, we conduct different types of tests by simulating the behavior of the adversary, PDR less than 5%, which verifies the high robustness of Ji Xiaoan.

      1. # Summary

         - 1. ##  Summary of works

      Because of its openness, multi-source heterogeneity, ubiquity and other characteristics, the security of the Internet of Things is related to the security of individuals, families, society, and even the country. Ji Xiaoan is committed to realizing a high-precision, fast, robust, and lightweight anomaly-based intrusion detection system. It can be deployed on the [Internet of Things Cloud Computing Platform ](http://www.nlecloud.com/about), training models on the cloud layer and performing Traffic detection on the detection layer is lightweight and practical.

      We preset the application model of the semi-supervised intrusion detection framework, which consists of a cloud layer, a detection layer and an edge layer. After collecting Traffic at the edge layer, the collected Traffic will be subjected to feature processing and Model Training in the cloud layer, and anomaly detection will be performed on the subsequent Traffic at the detection layer. With the support of powerful Deep learning prediction speed and accuracy, it can predict the intrusion detection behavior of the IoT system in real time and alert users.

      In the implementation method, we design a semi-supervised model architecture for real-time application of semi-supervised prediction, make full use of unlabeled network Traffic data to construct a real-time NID system, and use the self-designed credibility selector module to provide quality assurance for pseudo-labels based on the sensitivity of kitnet Algorithm to malignant Traffic data. We propose a frequency domain coding converter, which realizes the analysis of extracted frequency domain features and byte coding features.

      - In terms of operation effect, under the premise that it becomes difficult to manually label a large number of IoT records, only a small part of IoT Traffic can be labeled, and most of the rest can be unlabeled. Ji Xiaoan can learn efficiently from a small amount of labeled data and a large amount of unlabeled data. He achieved excellent performance on NID with a small part of labeled data (10%) on IDS2017 and IDS2018 datasets (F1 score: 99.48%). In extreme cases, using only 1% of the data, the F1 value exceeds 97%. At the same time, for current attacks against ML /DL weaknesses, we perform different types of tests by simulating the behavior of the adversary, PDR less than 5%, showing high robustness.

      - - 1. ##  business value

      With the advent of the "Internet +" era, the Internet of Things is developing rapidly and is gradually penetrating into all fields of life. The scale of IoT devices is showing an explosive growth trend. The era of the Internet of Everything is coming, and the importance of IoT security is becoming more and more prominent in the rapid development of the Internet of Things. According to the business form, the Internet of Things can be divided into three parts: industrial control Internet of Things, vehicle Internet of Things, and smart home Internet of Things, and different business forms have different business requirements for security.

      However, with the rapid development of IoT technology, privacy and security are issues worth thinking about. According to the survey of the 10 most popular IoT smart devices by HP Security Research, almost all devices have high-risk Vulnerability. Some key data are as follows:

      - 80% of IoT devices are at risk of privacy leakage or abuse;

      - 80% of IoT devices allow weak passwords;

      - 70% of IoT devices communicate with the Internet or LAN without encryption;

      - 60% of IoT devices have security vulnerabilities in their web interfaces.

      - 60% of IoT devices download software updates without encryption;

      While the Internet of Things brings us convenience, the devices, networks, and applications of the Internet of Things are also facing severe security threats, such as:

      In 2015, two cyber security experts used a man-in-the-middle attack to remotely control a Jeep on a highway (for example, controlling air conditioning, radios, windshield wipers, brakes, etc.). The attack demonstrated the dangers of a man-in-the-middle attack and led to the manufacturer to match 1.4 million vehicles. " The cameras in the "Water Drop LIVE" and "Hikvision" incidents were hacked and peeped at; the US created a zero-day Vulnerability virus, which used "Stuxnet" to break into Iranian nuclear power plants and sabotage Iran's nuclear implementation plan; in 2015, the United Kingdom's network provider Talk Talk suffered several cyber security Vulnerability attacks, which exposed unencrypted stored customer data to the cloud. Hackers were able to easily access and steal millions of customers' credit card and bank details.

      - In terms of the share of IDS/IPS (Intrusion Detection/Prevention) market, Hardware accounts for the major part of IDS/IPS, accounting for about 45%, followed by hosted IDS/ISP, with a market share of about 31%, and web-based software accounting for 24%. With the development of the market, the growth rate of web-based IDS/IPS software is getting faster and faster. According to the product structure proportion distribution of Gartner cyber security industry, in 2019, the market size of intrusion detection/prevention equipment in China is about 1.9 billion yuan. The Internet of Things because of its openness, multi-source heterogeneity, ubiquity and other characteristics, the security of the Internet of Things is related to the security of individuals, families, society, and even the country, the emergence of various security threats, but also continue to confirm the Internet of Things network intrusion detection system The necessity.

      - - 1. ##  Outlook of works

      Ji Xiaoan-IoT Qualitative Intrusion Detection System is an accurate and rapid IoT intrusion detection system with powerful semi-supervised training model support, which can accurately and quickly predict the intrusion behavior of IoT network intrusion behavior; in continuous improvement, we will improve the functions of Ji Xiaoan-IoT Qualitative Intrusion Detection System from the following aspects:

      In terms of security defense, the Ji Xiaoan-IoT qualitative intrusion detection system can accurately locate the IoT intrusion Traffic, intrusion point, intrusion time and traffic type at the same time for accurate prediction and tracking. However, in the overall defense strategy, a relatively single "disconnected connection" method is adopted to deal with the IoT connection of the attacked device, without considering the actual activities being carried out by different devices. In terms of response strategy, intrusion detection systems are divided into two modes - active response and passive response. The former only sends an alert notification for the collected abnormal conditions, without trying to reduce the damage caused or fight back against the attacker; the latter may control the attacked system and block or mitigate the impact of the attack. We will integrate different corresponding strategies. We will comprehensively consider the operating status of different devices, so as to block malicious traffic sources while saving the normal operating parameters of the devices, and minimize the wind direction without affecting the operating status of the devices.

      In the architecture deployment, the data interaction between the "cloud layer" and the "detection layer" includes the transmission with the training model, the transmission of training data, and the transmission of detection data packets. Due to time and Hardware conditions, this part of the transmission is not well protected in the design of this model. If an attacker attacks the model during this transmission process, it will bring serious consequences. In the subsequent improvements, we will build an intranet protection mechanism and establish absolutely secure data transmission between the "cloud layer" and the "detection layer" to ensure the reliability of the entire Internet of Things detection system.

      In the Application Area, the IoT security detection system designed by Ji Xiaoan cyber security experts is suitable for large enterprise-level network architectures and small home intelligent architectures. But not every home network can support servers with high computing power of cloud devices. Therefore, in the subsequent design, we negotiate a larger level system that can separate the Cloud as a Service and interweave many IoT security networks. This makes the training data more independent of the detection module and can be performed on the server cluster, so that you can not change the overall model performance without reducing the hardware consumption.

      1. # References

      1. M. Stoyanova, Y. Nikoloudakis, S. Panagiotakis, E. Pallis, and E. K. Markakis, "A survey on the Internet of Things (IoT) forensics: Challenges, approaches, and open issues," IEEE Commun. Surveys Tuts., vol. 22, no. 2, pp. 1191–1221, 2nd Quart., 2020, doi: 10.1109/COMST.2019.2962586.

      1. M. M. Hassan, S. Huda, S. Sharmeen, J. Abawajy, and G. Fortino, "An adaptive trust boundary protection for IIoT networks using deep-learning feature-extraction-based semisupervised model,” IEEE Trans. Ind. Informat., vol. 17, no. 4, pp. 2860–2870, Apr. 2021, doi: 10.1109/TII.2020.3015026. 

      1. M. Saharkhizan, A. Azmoodeh, A. Dehghantanha, K.-K. R. Choo, and R. M. Parizi, "An ensemble of deep recurrent neural networks for detecting IoT cyber attacks using network traffic," IEEE Internet Things J., vol. 7, no. 9, pp. 8852–8859, Sep. 2020, doi: 10.1109/JIOT.2020.2996425.

      1. M. A. Al-Garadi, A. Mohamed, A. K. Al-Ali, X. Du, I. Ali, and M. Guizani, “A survey of machine and deep learning methods for Internet of Things (IoT) security,” IEEE Commun. Surveys Tuts., vol. 22, no. 3, pp. 1646–1685, 3rd Quart., 2020, doi: 10.1109/COMST.2020.2988293

      1. L. Li, J. Yan, H. Wang, and Y. Jin, “Anomaly detection of time series with smoothness-inducing sequential variational auto-encoder,” IEEE Trans. Neural Netw. Learn. Syst., early access, Apr. 13, 2020, doi: 10.1109/TNNLS.2020.2980749.

      1. J. Wu, Z. Zhao, C. Sun, R. Yan, and X. Chen, “Fault-attention generative probabilistic adversarial autoencoder for machine anomaly detection,” IEEE Trans. Ind. Informat., vol. 16, no. 12, pp. 7479–7488, Dec. 2020, doi: 10.1109/TII.2020.2976752.

      1. X. Wang, Y. Han, V. C. M. Leung, D. Niyato, X. Yan, and X. Chen, “Convergence of edge computing and deep learning: A comprehensive survey,” IEEE Commun. Surveys Tuts., vol. 22, no. 2, pp. 869–904, 2nd Quart., 2020, doi: 10.1109/COMST.2020.2970550.

      1. M. Shafiq, Z. Tian, A. K. Bashir, X. Du, and M. Guizani, “CorrAUC: A malicious bot-IoT traffic detection method in IoT network using machine-learning techniques,” IEEE Internet Things J., vol. 8, no. 5, pp. 3242–3254, Mar. 2021, doi: 10.1109/JIOT.2020.3002255.

      1. S. Gamage and J. Samarabandu, “Deep learning methods in network intrusion detection: A survey and an objective comparison,” J. Netw. Comput. Appl., vol. 169, Nov. 2020, Art. no. 102767.

      1. Y. Cheng, Y. Xu, H. Zhong, and Y. Liu, “Leveraging semisupervised hierarchical stacking temporal convolutional network for anomaly detection in IoT communication,” IEEE Internet Things J., vol. 8, no. 1, pp. 144–155, Jan. 2021, doi: 10.1109/JIOT.2020.3000771.

      1. L. Vu, V. L. Cao, Q. U. Nguyen, D. N. Nguyen, D. T. Hoang, and E. Dutkiewicz, “Learning latent representation for IoT anomaly detection,” IEEE Trans. Cybern., early access, Sep. 18, 2020, doi: 10.1109/TCYB.2020.3013416

      1. J. Gao et al., “Omni SCADA intrusion detection using deep learning algorithms,” IEEE Internet Things J., vol. 8, no. 2, pp. 951–961, Jan. 2021, doi: 10.1109/JIOT.2020.3009180.

      1. L. Xiao, X. Wan, X. Lu, Y. Zhang, and D. Wu, “IoT security techniques based on machine learning: How do IoT devices use AI to enhance security?” IEEE Signal Process. Mag., vol. 35, no. 5, pp. 41–49, Sep. 2018.

      1. T. Ergen and S. S. Kozat, “Unsupervised anomaly detection with LSTM neural networks,” IEEE Trans. Neural Netw. Learn. Syst., vol. 31, no. 8, pp. 3127–3141, Aug. 2020, doi: 10.1109/TNNLS.2019.2935975.

      1. J. Wang, C. Jiang, H. Zhang, Y. Ren, K.-C. Chen, and L. Hanzo, “Thirty years of machine learning: The road to Pareto-optimal wireless networks,” IEEE Commun. Surveys Tuts., vol. 22, no. 3, pp. 1472–1514, 3rd Quart., 2020, doi: 10.1109/COMST.2020.2965856.

      1. F. Hussain, R. Hussain, S. A. Hassan, and E. Hossain, “Machine learning in IoT security: Current solutions and future challenges,” IEEE Commun. Surveys Tuts., vol. 22, no. 3, pp. 1686–1721, 3rd Quart., 2020, doi: 10.1109/COMST.2020.2986444.

      1. N. Ravi and S. M. Shalinie, “Semisupervised-learning-based security to detect and mitigate intrusions in IoT network,” IEEE Internet Things J., vol. 7, no. 11, pp. 11041–11052, Nov. 2020, doi: 10.1109/JIOT.2020.2993410.

      1. Ying Gao, Yu Liu, Yaqia Jin, Juequan Chen, and Hongrui Wu. 2018. A Novel Semi-Supervised Learning Approach for Network Intrusion Detection on Cloud-Based Robotic System. IEEE Access 6 (2018), 50927–50938. https://doi.org/10.1109/ACCESS.2018.2868171

      1. G Karatas, O Demir, O K Sahingoz, Increasing the Performance of Machine Learning-Based IDSs on an Imbalanced and Up-to-Date Dataset[J], IEEE Access 8 (2020) 32150–32162.

      1. WIDE. Accessed January 2021. MAWI Working Group Traffic Archive. http://mawi.wide.ad.jp/mawi/.

      1. Dongqi Han, Zhiliang Wang, Ying Zhong, Wenqi Chen, Jiahai Yang, Shuqiang Lu, Xingang Shi, and Xia Yin. 2021. Evaluating and Improving Adversarial Robustness of Machine Learning-Based Network Intrusion Detectors. IEEE Journal on Selected Areas in Communications 39, 8 (2021), 2632–2647. https://doi.org/10.1109/JSAC.2021.3087242

      1. Md Ashraful Alam Milton. 2018. Evaluation of Momentum Diverse Input Iterative Fast Gradient Sign Method (M-DI2-FGSM) Based Attack Method on MCS 2018 Adversarial Attacks on Black Box Face Recognition System. https://doi.org/10.

      48550/ARXIV.1806.08970

      1. Mirsky, Yisroel & Doitshman, Tomer & Elovici, Yuval & Shabtai, Asaf. (2018). Kitsune: An Ensemble of Autoencoders for Online Network Intrusion Detection. 