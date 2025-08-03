Overview of iQCN
================

Overview of iQCN

#### Definition

If congestion occurs on a network but the NIC of the sender does not receive Congestion Notification Packets (CNPs) from the receiver in a timely manner, the NIC increases its packet sending rate, exacerbating congestion. To address this problem, intelligent Quantized Congestion Notification (iQCN) enables an intermediate forwarding device to intelligently send CNPs so that the NIC of the sender can receive CNPs in a timely manner and does not increase its packet sending rate.


#### Purpose

Data Center Quantized Congestion Notification (DCQCN) is the most widely used congestion control algorithm on Remote Direct Memory Access (RDMA) networks. For DCQCN to work, network devices only need to support Explicit Congestion Notification (ECN), and other DCQCN functions are implemented on NICs of hosts. DCQCN ensures high throughput on RDMA networks that require zero packet loss, meeting the high requirements of lossless services.

In the traditional congestion control mechanism provided by DCQCN, a forwarding device sends ECN-marked packets to the receiver after detecting queue congestion. Upon receiving the packets, the receiver sends CNPs to the sender to instruct the NIC of the sender to reduce its packet sending rate. However, when congestion occurs on the network, the sender may fail to receive CNPs in a timely manner. In this case, the sender considers that congestion has been eliminated and increases its packet sending rate. As a result, the buffer of the forwarding device may be further congested, and even devices on the entire network stop sending traffic due to Priority-based Flow Control (PFC).

iQCN is designed to cope with the situation that the NIC of the sender does not receive CNPs in a timely manner. Specifically, iQCN enables the forwarding device to intelligently detect network congestion. The iQCN-enabled forwarding device proactively sends CNPs to the sender based on the interval at which the receiver sends CNPs and the interval between rate increase events of the NIC of the sender. In this case, the sender can receive CNPs in a timely manner and will not increase its packet sending rate, preventing congestion from being exacerbated.