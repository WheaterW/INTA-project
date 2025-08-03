Understanding STP/RSTP/MSTP
===========================

IEEE developed three protocols: first the Spanning Tree Protocol (STP), then the Rapid Spanning Tree Protocol (RSTP), and, thirdly, the Multiple Spanning Tree Protocol (MSTP). All three of them are used to eliminate network loops and implement link redundancy. Devices running STP, RSTP, or MSTP exchange BPDUs to perform spanning tree calculation. As well as having such similarities, the three spanning tree protocols also have some differences, which can be seen in [Table 1](#EN-US_CONCEPT_0000001292078880__table12984145313512). For example, one spanning tree is generated in STP and RSTP, whereas multiple spanning trees are generated in MSTP. Of the three, STP has the slowest convergence speed.

**Table 1** Comparison of STP, RSTP, and MSTP
| **Spanning Tree Protocol** | **Convergence Speed** | **Traffic Forwarding** | **Configuration Complexity** |
| --- | --- | --- | --- |
| STP (defined in IEEE 802.1d) | Slowest | All VLANs share a spanning tree, through which all their traffic is forwarded. | Slow |
| RSTP (defined in IEEE 802.1w) | RSTP and MSTP provide faster convergence than STP, however, they are equally fast in convergence. | All VLANs share a spanning tree, through which all their traffic is forwarded. | Slow |
| MSTP (defined in IEEE 802.1s) | Through the mapping between instances and VLANs, multiple spanning trees can load balance traffic among VLANs. Traffic from different VLANs is forwarded along different paths. Each spanning tree is independent of each other. | High |


#### RSTP Background

As LANs grow in scale, STP's slow convergence becomes more of an issue. The reasons for its slow convergence are as follows:

* The STP algorithm does not determine that a topology changes until the timer expires, delaying network convergence.
* The STP algorithm requires the root bridge to send configuration BPDUs after the network topology becomes stable, with other devices processing and spreading the configuration BPDUs throughout the entire network.

Additionally, STP does not differentiate between port roles when it comes to their states. That is, ports in Listening, Learning, and Blocking states are the same because all such ports are prevented from forwarding service traffic. So, in terms of port use and configuration, the essential differences between ports lie in their roles, not states. STP's inability to distinguish between these different situations is its major downfall.

To overcome such disadvantages, RSTP builds on STP with the following improvements.

* RSTP adds the port roles of alternate, backup, and edge ports, as well as reducing the number of the port states. For details, see [Device Roles, Port Roles, and Port States](vrp_stp_cfg_1066.html). Additionally, RSTP changes the configuration BPDU format and uses the Flags field to describe port roles.
* RSTP processes configuration BPDUs differently.
  + RSTP allows non-root bridges to send configuration BPDUs at Hello Time intervals after the topology becomes stable, regardless of whether they receive configuration BPDUs from the root bridge.
  + In STP, a device has to wait for one interval of the Max Age timer before determining that a negotiation has failed. In contrast, a device with RSTP enabled determines that the negotiation between its port and the upstream device has failed if the port does not receive any configuration BPDUs sent from the upstream device within the timeout period. (timeout period = Hello Time Ã 3 Ã Timer Factor)
  + When an RSTP port receives an RST BPDU from the upstream designated bridge, the port compares the received RST BPDU with its own RST BPDU. If its own RST BPDU is superior, the port discards the received RST BPDU and immediately responds to the upstream device with its own RST BPDU. After receiving the RST BPDU, the upstream device replaces its own RST BPDU with the received RST BPDU based on corresponding fields. This therefore leads to fast convergence, as RSTP ports process inferior BPDUs without having to wait for a timer to expire.
* RSTP introduces several rapid convergence mechanisms, including the Proposal/Agreement mechanism, fast switchover of the root port, and the addition of edge ports.
* RSTP introduces multiple protection functions, including BPDU protection, root protection, loop prevention, and TC protection.

#### MSTP Background

In STP and RSTP, all VLANs on a LAN use the same spanning tree, which means that VLAN-based load balancing cannot be performed. Also, once a link is blocked, it will no longer transmit traffic, which wastes bandwidth and may cause some VLAN packets unable to be forwarded.

In the LAN shown in [Figure 1](#EN-US_CONCEPT_0000001292078880__fig1568614172616), STP or RSTP is enabled, DeviceD is the root device, and the broken line represents the spanning tree. The links between DeviceA and DeviceF and between DeviceB and DeviceE are blocked.

HostB and HostD belong to VLAN 2, but are unable to communicate with each other due to the link between DeviceB and DeviceE being blocked and the link between DeviceC and DeviceD denying packets from VLAN 2.

**Figure 1** STP/RSTP networking  
![](figure/en-us_image_0000001291919008.png)

To overcome this issue, MSTP divides one switched network into multiple regions, known as Multiple Spanning Tree (MST) regions. Each MST region has multiple spanning trees, known as Multiple Spanning Tree Instances (MSTIs), that are independent of each other.

An instance is a collection of VLANs, and multiple VLANs can be bound to the same instance to save communication costs and reduce resource usage. The topology of each MSTI is calculated independently, and traffic can be balanced among MSTIs. Multiple VLANs that have the same topology can be mapped to one instance. The status of a port in the MSTI determines whether it forwards packets from a VLAN.

As shown in [Figure 2](#EN-US_CONCEPT_0000001292078880__fig20369162795818), MSTP uses a VLAN mapping table to map VLANs to MSTIs. Each VLAN can be mapped to only one MSTI, meaning that traffic of a VLAN can be transmitted in only one MSTI. An MSTI, however, can be bound to multiple VLANs. Two spanning trees are eventually calculated:

* MSTI 1 uses DeviceF as the root device to forward packets of VLAN 2.
* MSTI 2 uses DeviceD as the root device to forward packets of VLAN 3.

In this manner, hosts within the same VLAN can communicate with each other, whereas packets of different VLANs are load balanced along different paths.

**Figure 2** Multiple spanning trees in an MST region  
![](figure/en-us_image_0000001345238537.png)