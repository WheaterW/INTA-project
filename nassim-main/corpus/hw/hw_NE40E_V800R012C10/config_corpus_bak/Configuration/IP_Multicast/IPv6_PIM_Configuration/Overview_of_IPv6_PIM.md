Overview of IPv6 PIM
====================

IPv6 PIM is an intra-domain multicast routing protocol that uses existing IPv6 unicast routing information to perform RPF check on IPv6 multicast packets and to create IPv6 multicast routing entries. IPv6 PIM can also dynamically respond to network topology changes and maintain IPv6 multicast forwarding tables.

IPv6 Protocol Independent Multicast (PIM) is independent of any specific unicast routing protocol. It can leverage whichever unicast routing protocols are used to populate the unicast routing table. These unicast routing protocols include IPv6 static routes, Routing Information Protocol next generation (RIPng), Open Shortest Path First Version 3 (OSPFv3), Intermediate System-Intermediate System for IPv6 (IS-ISv6), or Border Gateway Protocol (BGP4+). It uses unicast routing information to implement the multicast forwarding function.

PIM implements multicast packet forwarding by means of the Reverse Path Forwarding (RPF) mechanism. The RPF mechanism uses existing unicast routing information to build an MDT on a network. When a multicast packet reaches a Router, the Router performs the RPF check first.

* If the multicast packet passes the RPF check, the Router creates a multicast routing entry, and then forwards the multicast packet based on the entry.
* If the multicast packet fails the RPF check, the Router discards it.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Information in this chapter concerns PIM configurations on an IPv6 network only. Unless otherwise noted, the term PIM refers to IPv6 PIM.


#### PIM Mode

PIM has two modes: PIM-SMand PIM-SSM. PIM-SM use group addresses in the Any-Source Multicast (ASM) group address range, whereas PIM-SSM uses group addresses in the SSM group address range.

* PIM-SM
  
  PIM-SM applies to large-scale networks on which multicast data receivers are sparsely distributed. Key PIM-SM mechanisms include neighbor discovery, Assert, Designated router (DR) election, Rendezvous Point (RP) discovery, Join, Prune, Register, and shortest path tree (SPT) switchover.
* PIM-SSM
  
  PIM-SSM applies to networks on which multicast data receivers can learn source locations before they join multicast groups and require multicast data from specific multicast sources. PIM-SSM adopts only some of PIM-SM technologies. PIM-SSM does not need to maintain an RP, construct rendezvous point trees (RPTs), or register multicast sources. In PIM-SSM, an SPT can be built directly between the source's DR and the receiver's DR.