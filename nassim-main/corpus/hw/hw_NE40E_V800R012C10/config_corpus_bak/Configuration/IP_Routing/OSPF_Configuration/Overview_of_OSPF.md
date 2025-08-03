Overview of OSPF
================

Open Shortest Path First (OSPF), which is developed by the IETF, is a link-state IGP. OSPF is widely used in access networks and MANs.

#### Definition

Open Shortest Path First (OSPF) is a link-state Interior Gateway Protocol (IGP) developed by the Internet Engineering Task Force (IETF).

OSPF version 2 (OSPFv2) is intended for IPv4. OSPF version 3 (OSPFv3) is intended for IPv6.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this document, OSPF refers to OSPFv2, unless otherwise stated.



#### Purpose

Before the emergence of OSPF, the Routing Information Protocol (RIP) was widely used as an IGP on networks. RIP is a distance-vector routing protocol, which is gradually being replaced with OSPF and IS-IS, due to RIP's slow convergence, tendency to form routing loops, and poor scalability.

RIP, OSPF, and IS-IS are typical IGPs. The differences among them are listed in [Table 1](#EN-US_CONCEPT_0172365510__en-us_concept_0172354030_tab_dc_vrp_ospf_feature_002901).

**Table 1** Differences between IGPs
| Item | RIP | OSPF | IS-IS |
| --- | --- | --- | --- |
| Protocol type | IP layer protocol | IP layer protocol | Link layer protocol |
| Application scope | Applies to small networks with simple architectures, such as campus networks. | Applies to medium-sized networks with several hundred Routers supported, such as small- and medium-sized enterprise networks. | Applies to large networks, such as Internet service provider (ISP) networks. |
| Routing algorithm | Uses a distance-vector algorithm and exchanges routing information over the User Datagram Protocol (UDP). | Uses the shortest path first (SPF) algorithm. It describes the network topology through link state advertisements (LSAs), generates shortest path trees (SPTs) based on the network topology, calculates the shortest paths to all destinations on the network, and exchanges routing information. | Uses the SPF algorithm. The network topology is described through the flooding of link state PDUs (LSPs). An SPT is generated based on the network topology to calculate the shortest paths to all destinations on the network.  In IS-IS, the SPF algorithm runs independently in Level-1 and Level-2 databases. The two-level structure is more applicable to large-scale routing networks. For details, see [Overview of IS-IS](feature_0003992972.html). |
| Route convergence speed | Slow | Fast, less than 1 second. | Fast, less than 1 second. |
| Scalability | Not supported | Supported by partitioning a network into areas | Supported by defining levels |



#### Benefits

OSPF offers the following benefits:

* Wide application scope: It applies to medium-sized networks with several hundred Routers, such as small- and medium-sized enterprise networks.
* Network masks: OSPF packets can carry masks, and therefore the packet length is not limited by natural IP masks. OSPF can process variable length subnet masks (VLSMs).
* Fast convergence: If the network topology changes, it immediately sends update packets to synchronize the changes to the link state databases (LSDBs) of all devices in the same autonomous system (AS).
* Loop-free routing: OSPF uses the SPF algorithm to calculate loop-free routes based on the collected link status.
* Area division: An AS can be divided into areas for management. The routing information transmitted between areas is further abstracted, reducing network bandwidth consumption.
* Equal-cost routes: OSPF supports multiple equal-cost routes to the same destination.
* Route classification: It uses intra- and inter-area routes, as well as Type 1 and Type 2 external routes, listed here in descending order of priority.
* Authentication: OSPF supports area-based and interface-based packet authentication, which ensures packet exchange security.
* Multicast: Protocol packets are sent using multicast addresses on certain types of links, minimizing the impact on other devices.