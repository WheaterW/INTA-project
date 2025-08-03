Configuring OSPF on the NBMA or P2MP Network
============================================

This section describes how to configure OSPF and modify attributes on the NBMA or point-to-multipoint (P2MP) network to flexibly construct the OSPF network.

#### Usage Scenario

OSPF classifies networks into four types according to link layer protocols, as shown in [Table 1](#EN-US_TASK_0172365555__tab_dc_vrp_ospf_cfg_202801).![](../../../../public_sys-resources/note_3.0-en-us.png) 

This section describes only the OSPF configurations that are different on the NBMA network and P2MP network. The OSPF configurations not provided here are applicable to the four types of networks.


**Table 1** Network types supported by OSPF
| Network Type | Characteristic | Default Configuration |
| --- | --- | --- |
| Broadcast | On such a type of network, Hello, LSU, and LSAck packets are multicast; DD and LSR packets are unicast. | If the link layer protocol is Ethernet or Fiber Distributed Data Interface (FDDI), OSPF regards the network as a broadcast network by default. |
| Non-broadcast multiple access (NBMA) | On such a type of network, Hello, DD, LSR, LSU, and LSAck packets are unicast.  The NBMA network must be fully meshed. Any two Routers on the NBMA network must be directly reachable. | -  If the link layer protocol is ATM, OSPF regards the network as an NBMA network by default. |
| Point-to-point (P2P) | On such a type of network, Hello, DD, LSR, LSU, and LSAck packets are multicast. | If the link layer protocol is PPP, HDLC, or Link Access Procedure Balanced (LAPB), OSPF regards the network as a P2P network by default. |
| Point-to-multipoint (P2MP) | On such a type of network, Hello packets are multicast; DD, LSR, LSU, and LSAck packets are unicast.  The mask lengths of the devices on the P2MP network must be the same. | OSPF does not regard a network as a P2MP network by default regardless of any link layer protocol. A P2MP network is forcibly changed from the network of another type. |


As shown in [Table 1](#EN-US_TASK_0172365555__tab_dc_vrp_ospf_cfg_202801), OSPF sends packets in different manners on networks of different types. Therefore, the difference between OSPF configurations on the networks lies in the packet sending configurations.

#### Pre-configuration Tasks

Before configuring session parameters for the OSPF neighbor or adjacency relationship, complete the following tasks:

* Configure a link layer protocol.
* Configure IP addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* [Configure basic OSPF functions](dc_vrp_ospf_cfg_0003.html).


[Configuring Network Types for OSPF Interfaces](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2029.html)

OSPF classifies networks into four types based on the types of link layer protocols. You can configure the network type for an OSPF interface to forcibly change its original network type.

[Configuring NBMA Network Attributes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2030.html)

To implement OSPF functions, configure NBMA network attributes.

[Configuring P2MP Network Attributes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_2031.html)

This section describes how to configure P2MP network attributes to implement OSPF functions.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospf_cfg_0023.html)

After OSPF attributes are set on networks of different types, you can check OSPF neighbor and interface information.