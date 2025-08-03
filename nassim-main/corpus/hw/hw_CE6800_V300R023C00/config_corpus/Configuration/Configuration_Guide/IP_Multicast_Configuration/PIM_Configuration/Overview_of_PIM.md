Overview of PIM
===============

Overview of PIM

#### Definition

Protocol Independent Multicast (PIM) is an intra-domain multicast routing protocol. It uses unicast routing information to perform RPF checks on multicast messages and create multicast routing entries. The protocol that provides routing information for IP multicast can be any unicast routing protocol, such as static routing, RIP, OSPF, IS-IS, or BGP. Multicast generates multicast routing entries based on the unicast routing table, regardless of the type of unicast routing protocol.

PIM has three modes: PIM-DM, PIM-SM using the Any-Source Multicast (ASM) model, and PIM-SSM using the Source-Specific Multicast (SSM) model. [Table 1](#EN-US_CONCEPT_0000001176663359__tab_007243_01) compares the three modes. Note that PIM-DM and PIM-SM cannot run in the same PIM domain.

**Table 1** Comparisons between PIM implementations
| Protocol | Name | Model | Application Scenario |
| --- | --- | --- | --- |
| PIM-DM | Protocol Independent Multicast-Dense Mode | ASM model | Small-scale networks with densely distributed multicast group members |
| PIM-SM | Protocol Independent Multicast-Sparse Mode | ASM model | Large-scale network where multicast group members are distributed sparsely |
| PIM-SSM | Protocol Independent Multicast-Source-Specific Multicast | SSM model | Scenarios where user hosts know the exact locations of multicast sources in advance and can specify the sources from which they want to receive data before they join multicast groups |



#### Purpose

On a network, multicast data is replicated and forwarded through a multicast network from a multicast source to receivers. To construct a multicast network, a multicast protocol is required. PIM is the most widely used intra-domain multicast protocol. The multicast distribution trees (MDTs) constructed using PIM can be used to guide multicast data forwarding on the network.

PIM can help implement such functions as creating multicast routing entries on demand, forwarding packets based on these entries, and dynamically responding to network topology changes.

PIM can work with other multicast protocols to construct a multicast network and can be used in the following scenarios:

* Multimedia and streaming media applications
* Training and tele-learning communication
* Data warehouse and finance applications (for example, stock trading applications)
* Video conference and online education