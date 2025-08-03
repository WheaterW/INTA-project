Overview of Layer 2 Protocol Tunneling
======================================

Overview of Layer 2 Protocol Tunneling

#### Definition

Layer 2 protocol tunneling is a Layer 2 tunneling technology that enables devices to transparently transmit Layer 2 protocol packets of private network users at different locations over a specified tunnel on an Internet service provider (ISP) network.


#### Purpose

Users often use leased lines provided by ISPs to construct their own Layer 2 networks. As a result, different branches of the same private network may be located at two sides of an ISP network. In [Figure 1](#EN-US_CONCEPT_0000001159323946__fig_dc_fd_l2pt_000401), network 1 and network 2 of user A are connected through an ISP network. When network 1 and network 2 run the same Layer 2 protocol (for example, MSTP), Layer 2 protocol packets from these networks must be able to traverse the ISP network for Layer 2 protocol calculation (for example, spanning tree calculation). Generally, the destination MAC addresses in packets of a Layer 2 protocol are the same. For example, the destination MAC addresses in MSTP bridge protocol data units (BPDUs) are all 0180-C200-0000. Therefore, when Layer 2 protocol packets from a user network reach a PE on the ISP network, the PE cannot identify whether the Layer 2 protocol packets are from a user network or an ISP network, and sends the packets to the CPU to complete spanning tree calculation.

In this way, devices on user network 1 complete spanning tree calculation together with PE1, but not with devices on user network 2. As a result, Layer 2 protocol packets from user network 1 cannot traverse the ISP network to reach user network 2.

**Figure 1** Transparent transmission of Layer 2 protocol packets on an ISP network  
![](figure/en-us_image_0000001204483967.png)
To solve the preceding problem, it is required that Layer 2 protocol packets from user networks can be transparently transmitted on the ISP network. You can use Layer 2 protocol tunneling to meet the requirement as follows:

1. After receiving Layer 2 protocol packets from CE1, PE1 replaces the destination MAC address in the packets with a specified multicast MAC address and forwards the packets on the ISP network.
2. After receiving the packets with the specified multicast MAC address, PE2 restores the original destination MAC address of the packets and sends the packets to CE2.