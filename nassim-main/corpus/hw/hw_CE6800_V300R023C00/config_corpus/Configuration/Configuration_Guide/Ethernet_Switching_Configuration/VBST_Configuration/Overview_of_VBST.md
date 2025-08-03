Overview of VBST
================

Overview of VBST

#### Definition

VLAN-based Spanning Tree (VBST), a Huawei spanning tree protocol, constructs a spanning tree in each VLAN so that traffic from different VLANs is forwarded through different spanning trees. VBST is equivalent to Spanning Tree Protocol (STP) or Rapid Spanning Tree Protocol (RSTP) running in each VLAN, and spanning trees in different VLANs are independent of each other.


#### Purpose

On an Ethernet network, redundant links are used to implement link backup and enhance network reliability. A disadvantage of this approach is that it may produce loops, leading to broadcast storms and an unstable MAC address table. As a result, communication on the network may deteriorate or even be interrupted. In order to prevent this, IEEE has introduced STP, RSTP, and Multiple Spanning Tree Protocol (MSTP).

STP and RSTP cannot implement VLAN-based load balancing, as all VLANs on a LAN use the same spanning tree, along which packets of all VLANs are forwarded. In addition, the blocked link does not carry any traffic, wasting bandwidth and potentially preventing the packets of some VLANs from being forwarded.

MSTP is compatible with both STP and RSTP, and in addition to implementing fast convergence, also provides multiple redundant paths for forwarding data, effectively load balancing traffic for VLANs. However, the concepts and configuration of MSTP multi-instance and multi-process are complex.

To address this issue, Huawei has developed VBST, which constructs a spanning tree in each VLAN so that their respective traffic is load balanced along different spanning trees. In addition, VBST is easy to configure and maintain.

STP, RSTP, MSTP, and VBST can eliminate loops and implement link backup. [Table 1](#EN-US_CONCEPT_0000001563888325__table12984145313512) shows the differences between these protocols.

**Table 1** Comparison between STP, RSTP, MSTP, and VBST
| Spanning Tree Protocol | Convergence Speed | Traffic Forwarding | Configuration Complexity |
| --- | --- | --- | --- |
| STP (standardized as IEEE 802.1d) | Slowest | All VLANs are mapped to one spanning tree, through which all their traffic is forwarded. | Low |
| RSTP (standardized as IEEE 802.1w) | RSTP, MSTP, and VBST offer equal convergence speeds, faster than that of STP. | All VLANs are mapped to one spanning tree, through which all their traffic is forwarded. | Low |
| MSTP (standardized as IEEE 802.1s) | Based on mappings between instances and VLANs, multiple spanning trees are generated so that traffic from different VLANs is forwarded through different spanning trees, which are independent of each other. | High |
| VBST | A spanning tree is formed in each VLAN, so that traffic from different VLANs is forwarded through different spanning trees that are independent of each other.  VBST interworks with PVST, PVST+, and Rapid PVST+. | Medium |