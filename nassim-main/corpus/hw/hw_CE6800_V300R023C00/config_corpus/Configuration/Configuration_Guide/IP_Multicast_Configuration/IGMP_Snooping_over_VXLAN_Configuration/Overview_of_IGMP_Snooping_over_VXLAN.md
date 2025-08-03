Overview of IGMP Snooping over VXLAN
====================================

Overview of IGMP Snooping over VXLAN

#### Definition

Internet Group Management Protocol (IGMP) snooping over virtual extensible local area network (VXLAN) is a VXLAN-based Layer 2 multicast technology that implements on-demand multicast traffic forwarding on a VXLAN Layer 2 network, preventing multicast data from being broadcast in a bridge domain (BD).


#### Purpose

VXLAN networks are widely deployed in scenarios with a large amount of data. More and more service traffic, including IP multicast traffic, such as live webcasting, video conferencing, and online gaming, needs to be transmitted over VXLAN networks. When both the multicast source and receivers are on the VXLAN overlay network and in the same BD, IGMP snooping over VXLAN can be deployed so that Layer 2 multicast traffic is transmitted on demand on the VXLAN overlay network and encapsulated data is forwarded on the VXLAN underlay network in ingress replication mode.


#### Benefits

IGMP snooping over VXLAN implements on-demand multicast data forwarding on a VXLAN network and offers the following benefits:

* Reduces device performance pressure by reducing broadcast traffic on the VXLAN network.
* Conserves VXLAN network bandwidth.
* Ensures the quality of IP multicast services deployed on the VXLAN network.