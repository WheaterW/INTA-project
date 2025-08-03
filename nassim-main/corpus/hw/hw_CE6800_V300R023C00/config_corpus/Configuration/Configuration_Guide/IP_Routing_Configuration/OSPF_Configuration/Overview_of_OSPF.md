Overview of OSPF
================

Overview of OSPF

#### Definition

Open Shortest Path First (OSPF) is a link-state Interior Gateway Protocol (IGP) developed by the Internet Engineering Task Force (IETF).

OSPF version 2 (OSPFv2) is intended for IPv4, and OSPF version 3 (OSPFv3) is intended for IPv6.

![](../public_sys-resources/note_3.0-en-us.png) 

Unless otherwise stated, OSPF refers to OSPFv2 in this document.

The CE6885-LL in low latency mode does not support OSPFv3.



#### Purpose

Before the emergence of OSPF, the Routing Information Protocol (RIP) was the most widely used IGP. RIP is a distance-vector routing protocol which is gradually being replaced with OSPF, due to the former's slow convergence, tendency to form routing loops, and poor scalability. The most common IGPs are RIP, OSPF, and Intermediate System to Intermediate System (IS-IS). [Table 1](#EN-US_CONCEPT_0000001130783228__tab_dc_vrp_ospf_feature_002901) describes the differences between these IGPs.

**Table 1** Differences between IGPs
| Item | RIP | OSPF | IS-IS |
| --- | --- | --- | --- |
| Protocol type | IP layer protocol | IP layer protocol | Link layer protocol |
| Applicable scope | Applies to small networks with simple architectures, such as campus networks. | Applies to medium-sized networks with several hundred devices, such as small- and medium-sized enterprise networks. | Applies to large networks, such as large-scale Internet service provider (ISP) networks. |
| Routing algorithm | Uses the distance-vector (D-V) algorithm to calculate routes. | Uses the shortest path first (SPF) algorithm to calculate a shortest path tree (SPT) to all destinations based on the network topology information, which is advertised through link state advertisements (LSAs). | Uses the SPF algorithm to generate an SPT based on the network topology and calculate shortest paths to all destinations.  In IS-IS, the SPF algorithm runs independently in Level-1 and Level-2 databases. |
| Convergence speed | Slow | Fast, less than 1 second. | Fast, less than 1 second. |
| Scalability | Not supported | Supported by partitioning a network into areas. | Supported by defining device levels. |



#### Benefits

OSPF offers the following benefits:

* Wide application scope: OSPF is suitable for medium-sized networks featuring several hundred devices, such as small- and medium-sized enterprise networks.
* Mask support: As OSPF packets carry mask information, OSPF is not subject to natural masks. Instead, OSPF can process variable length subnet masks (VLSMs).
* Fast convergence: If the network topology changes, OSPF immediately sends link state update (LSU) packets to synchronize the changes to the link state databases (LSDBs) of all devices in the same autonomous system (AS).
* Loop-free routing: OSPF uses the SPF algorithm to calculate loop-free routes based on the collected link status.
* Area partitioning: OSPF allows an AS to be partitioned into areas, leading to simplified management. In this way, routing information transmitted between areas can be summarized, reducing network bandwidth consumption.
* Equal-cost routes: OSPF supports multiple equal-cost routes to the same destination.
* Route classification: OSPF uses intra- and inter-area routes, as well as Type 1 and Type 2 external routes, listed here in descending order of priority.
* Authentication: OSPF supports area-based and interface-based packet authentication, ensuring packet exchange security.