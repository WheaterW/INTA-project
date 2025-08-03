Overview of Intelligent Traffic Analysis
========================================

Overview of Intelligent Traffic Analysis

#### Definition

The intelligent traffic analysis function is used to monitor and analyze network traffic. It allows O&M personnel to perform in-depth analysis on a specified service flow, obtain data about high-precision performance indicators such as the packet loss rate and latency (nanosecond-level) of the service flow, and export the analysis results to the analyzer for graphical display. This makes it easier for O&M personnel to monitor the network condition and quickly locate network faults.

![](public_sys-resources/note_3.0-en-us.png) 

The device supports the intelligent traffic analysis function, which is used to perform in-depth analysis on specified service traffic and may involve obtaining personal data such as IP address and MAC address. Huawei will not collect or store users' communication information without prior user approval. Therefore, you must use this function in compliance with the local laws and regulations, and take proper security protection measures to ensure that personal data of users is fully protected. For example, technical support engineers must not use this function to obtain packets unless they have been authorized by customers. Ensure obtained packets are deleted completely and immediately after the fault is located and analyzed. Huawei will not bear any legal responsibility or liabilities for any security events (such as personal data leakage) that are not the result of Huawei's misconduct.



#### Purpose

As the digital transformation of industries accelerates, a growing number of services and applications are being deployed in data centers. In addition, some problems may occur during service flow forwarding, such as Transmission Control Protocol (TCP) connection setup failure and high latency, bringing great challenges to data center O&M. Such challenges can be overcome by visualizing network traffic to implement refined service management, fast sensing, and accurate fault locating.

Currently, the device can work with Huawei's FabricInsight to partially implement visualization of network-wide traffic. FabricInsight is an analyzer that collects, analyzes, and displays network traffic. To be specific, traffic classifiers can be configured on the device to match service packets and the device can send a copy of packets matching the classifiers to FabricInsight using the remote flow mirroring capability. FabricInsight uses an algorithm to restore the path through which packets of a service flow are forwarded, implementing statistics collection, analysis, and fault locating for network-wide traffic. Despite the obvious benefits, the following problems still exist:

* Analysis and calculation of service flows mainly depend on FabricInsight, which is remote, putting huge strain on FabricInsight due to huge volumes of traffic in the data center.
* Only short TCP connections can be analyzed. Persistent TCP connections and User Datagram Protocol (UDP) packets cannot be analyzed. In addition, intelligent analysis of different service flow characteristics cannot be performed.
* Faults are mainly located by FabricInsight, which marks service packets to collect statistics on network performance. However, only statistics on the packet loss rate and latency are collected. The round trip time (RTT) cannot be calculated to the nearest nanosecond, and other performance indicators such as the traffic volume cannot be analyzed.
* The current network traffic analysis function on the device supports analysis of sampled packets, with a sampling ratio of at least 2000:1 (only suitable for rough traffic statistics collection). Accurate in-depth analysis based on each service flow cannot be implemented, and information such as packet loss and latency cannot be obtained.

The intelligent traffic analysis function can effectively solve the preceding problems. By performing in-depth analysis on specified service flows, the device can obtain a series of high-precision performance indicators of service flows and export the analysis results to FabricInsight. This function enables O&M personnel to monitor network traffic and provides powerful support for network-wide traffic visualization.