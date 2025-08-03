Overview of IPv6 PIM
====================

Overview of IPv6 PIM

#### Definition

IPv6 Protocol Independent Multicast (PIM) is an intra-domain multicast routing protocol. It uses IPv6 unicast routing information to perform RPF checks on multicast messages and create IPv6 multicast routing entries. The protocol that provides routing information for IPv6 multicast can be any unicast routing protocol, such as IPv6 static routing, RIPng, OSPFv3, IS-ISv6, and BGP4+. Multicast generates multicast routing entries based on the unicast routing table, regardless of the type of unicast routing protocol.

IPv6 PIM has two modes: PIM-Sparse Mode (PIM-SM), which uses the any-source multicast (ASM) model, and PIM-Source-Specific Multicast (PIM-SSM), which uses the SSM model. [Table 1](#EN-US_CONCEPT_0000001589190277__tab_007243_01) compares the two modes.

**Table 1** Comparisons between IPv6 PIM modes
| Protocol | Full Name | Model | Application Scenario |
| --- | --- | --- | --- |
| PIM-SM | Protocol Independent Multicast-Sparse Mode | ASM model | Large-scale network where multicast group members are distributed sparsely |
| PIM-SSM | Protocol Independent Multicast-Source-Specific Multicast | SSM model | Scenarios where user hosts know the exact locations of multicast sources in advance and can specify the sources from which they want to receive data before they join multicast groups |



#### Purpose

On a network, multicast data is replicated and forwarded through a multicast network from a multicast source to receivers. To construct a multicast network, a multicast protocol is required. IPv6 PIM is the most widely used intra-domain multicast protocol. The multicast distribution trees (MDTs) constructed using PIM can be used to guide multicast data forwarding on the network.

IPv6 PIM can help implement such functions as creating multicast routing entries on demand, forwarding packets based on these entries, and dynamically responding to network topology changes.

IPv6 PIM can work with other multicast protocols to construct a multicast network and can be used in the following scenarios:

* Multimedia and streaming media applications
* Training and tele-learning communication
* Data warehouse and finance applications (for example, stock trading applications)
* Video conference and online education