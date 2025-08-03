Overview of IPv4 Layer 3 Multicast over VXLAN
=============================================

Overview of IPv4 Layer 3 Multicast over VXLAN

#### Definition

IPv4 Layer 3 multicast over VXLAN is a VXLAN-based Layer 3 multicast technology that implements accurate forwarding of multicast traffic between a VXLAN overlay network and a non-overlay network or within a VXLAN overlay network.


#### Purpose

VXLAN networks are widely deployed in data center scenarios. The amount of service traffic, including IP multicast traffic, such as live webcasting, video conferencing, and online gaming, that needs to be transmitted over VXLAN networks is constantly growing. When a multicast source or receiver is on an external network, or both the multicast source and receiver are on a VXLAN overlay network but belong to different bridge domains (BDs), this function can be deployed to transmit Layer 3 multicast traffic on the VXLAN overlay network. When this function is enabled, encapsulated data is forwarded on the VXLAN underlay network in multicast replication mode of BUM packets.


#### Benefits

IPv4 Layer 3 multicast over VXLAN implements on-demand multicast data forwarding on a VXLAN network and offers the following benefits:

* Reduces device performance pressure by decreasing broadcast traffic on the VXLAN network.
* Conserves VXLAN network bandwidth.
* Ensures the quality of IP multicast services deployed on the VXLAN network.