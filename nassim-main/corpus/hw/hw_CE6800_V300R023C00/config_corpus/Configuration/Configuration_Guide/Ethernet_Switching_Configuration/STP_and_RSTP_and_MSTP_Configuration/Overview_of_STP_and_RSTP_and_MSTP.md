Overview of STP/RSTP/MSTP
=========================

Overview of STP/RSTP/MSTP

#### Definition

Spanning Tree Protocol (STP), Rapid Spanning Tree Protocol (RSTP), and Multiple Spanning Tree Protocol (MSTP) have been introduced to prevent loops on Ethernet networks. Devices running STP, RSTP, or MSTP exchange information in order to discover loops on the network and block appropriate ports, thereby trimming a ring topology into a loop-free tree topology. Further, if an active link fails and a redundant link exists, STP, RSTP, and MSTP activate the redundant link to ensure network connectivity.


#### Purpose

On an Ethernet network, redundant links are used to implement link backup and enhance network reliability. A disadvantage of this approach is that it may produce loops, leading to broadcast storms and an unstable MAC address table. As a result, communication on the network may deteriorate or even be interrupted. In order to prevent this, IEEE has introduced STP, RSTP, and MSTP.

RSTP is an enhancement of STP, allowing for fast network topology convergence.

STP and RSTP cannot implement VLAN-based load balancing, because all the VLANs on a LAN share a spanning tree, along which packets in all VLANs are forwarded. In addition, a blocked link does not carry any traffic, which wastes bandwidth and potentially causing a failure to forward packets from some VLANs. MSTP is compatible with STP and RSTP, and can implement fast convergence and provide multiple redundant paths for forwarding data, effectively load balancing traffic of VLANs.

STP, RSTP, and MSTP can eliminate loops and implement link backup. [Table 1](#EN-US_CONCEPT_0000001345238481__table12984145313512) shows the differences between these protocols.

**Table 1** Comparison between STP, RSTP, and MSTP
| Spanning Tree Protocol | Convergence Speed | Traffic Forwarding | Configuration Complexity |
| --- | --- | --- | --- |
| STP (standardized as IEEE 802.1d) | Slowest | All VLANs share one spanning tree, through which all their traffic is forwarded. | Low |
| RSTP (standardized as IEEE 802.1w) | RSTP and MSTP offer equal convergence speeds, faster than that of STP. | All VLANs share one spanning tree, through which all their traffic is forwarded. | Low |
| MSTP (standardized as IEEE 802.1s) | Based on mappings between instances and VLANs, multiple spanning trees are generated so that traffic from different VLANs is forwarded through different spanning trees, which are independent of each other. | High |