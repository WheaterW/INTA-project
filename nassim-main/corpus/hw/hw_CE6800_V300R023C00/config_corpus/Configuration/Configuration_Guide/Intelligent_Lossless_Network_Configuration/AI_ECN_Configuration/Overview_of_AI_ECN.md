Overview of AI ECN
==================

Overview of AI ECN

#### Definition

The Artificial Intelligence Explicit Congestion Notification (AI ECN) function intelligently adjusts ECN thresholds of lossless queues based on the traffic model on the live network. This function ensures low delay and high throughput with zero packet loss, achieving optimal performance for lossless services.


#### Purpose

Data Center Quantized Congestion Notification (DCQCN) is currently the most widely used congestion control algorithm on Remote Direct Memory Access (RDMA) networks. For DCQCN to work, network devices only need to support ECN, and other DCQCN functions are implemented on NICs of hosts. DCQCN can ensure high throughput on RDMA networks that require zero packet loss, satisfying the high requirements of lossless services.

In the congestion control mechanism provided by DCQCN, a forwarding device sends ECN-marked packets to the receiver after detecting queue congestion. After receiving the ECN-marked packets, the receiver sends Congestion Notification Packets (CNPs) to the sender to instruct the NIC of the sender to reduce its packet sending rate.

The traditional static ECN function requires manual configuration of parameters such as the upper and lower ECN thresholds and ECN marking probability on forwarding devices. For lossless services that require lossless transmission, fixed ECN thresholds cannot adapt to the changing buffer space in a queue. Consequently, the static ECN function cannot prevent Priority-based Flow Control (PFC) from being triggered while meeting the bandwidth requirements of both delay-sensitive mice flows and throughput-sensitive elephant flows.

Using intelligent algorithms, the AI ECN function for lossless queues enables the device to perform AI training based on the traffic model on the live network, predict network traffic changes and the optimal ECN thresholds in a timely manner, and adjust the ECN thresholds in real time based on traffic changes on the live network. In this way, the lossless queue buffer is accurately managed and controlled, ensuring the optimal performance across the entire network. Additionally, in coordination with queue scheduling, the AI ECN function for lossless queues can implement hybrid scheduling of TCP traffic and RDMA over Converged Ethernet version 2 (RoCEv2) traffic on the network. This ensures lossless transmission of RoCEv2 traffic and achieves low delay and high throughput.