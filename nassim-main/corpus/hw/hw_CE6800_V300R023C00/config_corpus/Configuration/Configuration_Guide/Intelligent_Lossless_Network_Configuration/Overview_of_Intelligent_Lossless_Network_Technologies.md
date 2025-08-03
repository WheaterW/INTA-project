Overview of Intelligent Lossless Network Technologies
=====================================================

Overview of Intelligent Lossless Network Technologies

#### Overview

As a growing number of enterprises around the world undergo digital transformation, the focus of networks is shifting from fast service provisioning to efficient data processing. Specifically, popular applications such as distributed storage, artificial intelligence (AI), and high-performance computing (HPC) require networks with zero packet loss, low delay, and high throughput in order to improve data processing efficiency. However, such high requirements cannot be met by traditional TCP/IP-based networks as the delay is high and large amounts of resources are consumed in key phases such as data copying. Remote Direct Memory Access (RDMA) uses related hardware and network technologies to enable the NICs of hosts to directly read memory data, achieving high bandwidth, low delay, and low resource consumption. However, the dedicated InfiniBand network architecture for RDMA is closed and incompatible with large-scale live IP networks, resulting in high usage and maintenance costs.

RDMA over Converged Ethernet (RoCE) technology effectively solves these problems. RoCE is available in two versions: RoCEv1 and RoCEv2. RoCEv1 is a link layer protocol which cannot be used in different broadcast domains, whereas RoCEv2 is a network layer protocol capable of implementing routing functions.

RoCEv2 is used by applications including distributed storage, AI, and HPC to reduce the CPU processing workload and delay and to improve application performance. However, because RDMA was used on lossless InfiniBand networks, RoCEv2 lacks a complete packet loss protection mechanism and is therefore sensitive to packet loss on networks. In addition, these distributed high-performance applications use the many-to-one incast traffic model. For Ethernet devices, incast traffic may cause instantaneous burst and congestion or even packet loss in the internal queue buffer on the devices, increasing the application delay and decreasing the throughput. This will ultimately cause the performance of distributed applications to deteriorate.

To avoid packet loss caused by network congestion, you need to ensure that the device buffer or link is not overloaded by preventing too much data from entering the network. On live networks, flow control and congestion control must be used together to solve network congestion. The difference between flow control and congestion control is as follows: Flow control is an end-to-end process in which the transmission rate of the sender is suppressed, enabling the receiver to receive all packets. In contrast, congestion control is a global process involving all hosts, network devices, and factors related to network transmission performance degradation.

The iLossless algorithm provided by intelligent lossless network technologies is a collection of a series of technologies. They cooperate with each other to solve the packet loss problem caused by congestion on traditional Ethernet networks and provide a network environment with zero packet loss, low delay, and high throughput for RoCEv2 traffic to meet high-performance requirements of RoCEv2 applications. Intelligent lossless network technologies are classified into the following types:

* Flow Control
* Congestion Control
* Intelligent Lossless NVMe Over Fabrics (iNOF)
* Network Scale Load Balance (NSLB)
* Adaptive Routing

#### Flow Control Technologies

Flow control, also known as link-level flow control, is used to suppress the data transmission rate of the traffic sender so that the traffic receiver can receive all packets, thereby preventing packet loss when the traffic receiving interface is congested.

Priority-based Flow Control (PFC) is the most widely used flow control technology. When a PFC-enabled queue on a device is congested, the upstream device stops sending traffic in the queue, implementing zero packet loss. The system does not perform PFC for a PFC-disabled queue, and instead discards packets from the queue when it is congested.

Services can be categorized as lossless or lossy services, depending on whether packets need to be transmitted with no loss.

* Lossless services require zero packet loss during transmission. A queue that requires zero packet loss during transmission is a lossless queue.
* Lossy services allow packet loss during transmission. A queue that allows packet loss during transmission is a lossy queue.

PFC effectively prevents packet loss, but some traffic is stopped due to PFC. Therefore, PFC should be used as a last resort. Otherwise, a PFC deadlock may occur if PFC is triggered frequently. If congestion occurs on multiple network devices simultaneously due to a loop or other causes, the interface buffer usage of each device exceeds the threshold, and these devices wait for each other to release resources. As a result, data flows on these devices are permanently blocked. This network state is known as the PFC deadlock state.

To solve the PFC deadlock problem, the device provides the PFC deadlock prevention function to prevent PFC deadlocks in advance.

The device also provides buffer optimization, which optimizes the buffer space based on actual service scenarios to fully ensure lossless packet forwarding of lossless queues.

In a long-distance Data Center Interconnect (DCI) scenario, to ensure lossless packet forwarding of lossless queues across data centers, the intelligent lossless network feature provides the antilocking PFC function, which optimizes the flow control mechanism to support long-distance lossless transmission scenarios.


#### Congestion Control Technologies

Congestion control is a global process that enables the network to bear existing traffic load. To mitigate and relieve congestion, the forwarding device, traffic sender, and traffic receiver need to collaborate with each other, and congestion feedback mechanisms need to be used to adjust traffic on the entire network.

Data Center Quantized Congestion Notification (DCQCN) is the most widely used congestion control algorithm on RDMA networks. For DCQCN to work, network devices are only required to support Explicit Congestion Notification (ECN), with other DCQCN functions implemented on the NICs of hosts. When congestion occurs on a forwarding device, the forwarding device sends ECN-marked packets to the traffic receiver. The traffic receiver sends Congestion Notification Packets (CNPs) to the traffic sender. The traffic sender then reduces its packet sending rate to relieve network congestion.

However, DCQCN has problems that cannot be ignored. For example, to use the traditional static ECN function, you must manually configure parameters such as ECN thresholds. However, traffic models on live networks are complex and devices with static ECN configurations cannot cope with traffic changes. In addition, the DCQCN control loop delay, which is already too long due to the long congestion feedback path, becomes even longer on a larger network. As a result, the sender cannot reduce the packet sending rate in a timely manner, and even the congestion is exacerbated.

To solve these DCQCN problems, the device provides Artificial Intelligence Explicit Congestion Notification (AI ECN), Intelligent Quantized Congestion Notification (iQCN), and Network-based Proactive Congestion Control (NPCC). In addition, the device provides ECN Overlay to apply DCQCN functions to VXLAN networks and extend DCQCN application scenarios.


#### iNOF

A storage system consists of compute and storage nodes, and requires a network with zero packet loss, low delay, and high throughput. Intelligent lossless network technologies enable Ethernet networks to meet network performance requirements of storage systems. A storage system that stores large amounts of data usually needs to manage a large number of hosts, and a growing number of new hosts are connected to network devices in the system. The device provides the iNOF function to quickly manage and control hosts so that intelligent lossless network technologies can be better applied to storage systems. In this way, Ethernet networks can replace conventional Fibre Channel (FC) networks to implement network convergence.


#### NSLB

NSLB technology combines Flow Matrix and Rail Group to fully utilize network resources and improve network-wide throughput.


#### Adaptive Routing

Building a large supercomputing center requires interconnection between a large number of compute nodes. However, expanding the cluster scale increases the network latency and deployment costs, failing to meet requirements regarding computing power and deployment. A direct topology features large-scale access and a small network diameter. In such a topology, adaptive routing can be deployed to dynamically determine routes based on the network topology and traffic load changes. By proactively detecting the link congestion status, adaptive routing preferentially selects a short and non-congested packet forwarding path. In this way, unequal-cost paths are fully utilized to improve bandwidth utilization, meeting the requirements of high throughput, low latency, and low costs while supporting large-scale networking.


#### Recommended Feature Configuration

This section describes specific intelligent lossless network features used on devices of different roles in different scenarios, as listed in the following table.

* Y: The feature is recommended on the device of the corresponding role in the corresponding scenario.
* N/A: The feature is not required on the device of the corresponding role in the corresponding scenario.

| Intelligent Lossless Network Feature | | | Scenario Classification | | | |
| --- | --- | --- | --- | --- | --- | --- |
| Feature Category | Feature Name | Device Role | Distributed Storage | Centralized Storage | AI GPU | HPC |
| Flow Control | PFC | Leaf | Y | Y | Y | Y |
| Spine | Y | Y | Y | Y |
| PFC Deadlock Prevention | Leaf | Y | Y | Y | Y |
| Spine | N/A | N/A | N/A | N/A |
| Antilocking PFC | Leaf | N/A | N/A | N/A | N/A |
| Spine | N/A | N/A | N/A | N/A |
| DCI Leaf | N/A | Y | N/A | N/A |
| Congestion Control | AI ECN | Leaf | Y | Y | Y | Y |
| Spine | Y | Y | Y | Y |
| ECN Overlay | Leaf | Y (VXLAN scenario) | N/A | Y (VXLAN scenario) | Y (VXLAN scenario) |
| Spine | N/A | N/A | N/A | N/A |
| NPCC | Leaf | N/A | N/A | N/A | N/A |
| Spine | N/A | N/A | N/A | N/A |
| DCI Leaf | N/A | Y | N/A | N/A |
| iNOF | iNOF | Leaf | N/A | Y | N/A | N/A |
| Spine | N/A | Y | N/A | N/A |
| Adaptive Routing | Adaptive Routing | Leaf | N/A | N/A | N/A | Y |