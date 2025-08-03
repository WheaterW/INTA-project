Overview of BIERv6
==================

Overview of BIERv6

#### Definition

Bit Index Explicit Replication IPv6 Encapsulation (BIERv6) is a multicast solution. With it, the ingress on an IPv6 network encapsulates the set of nodes for which each multicast packet is destined as a BitString in the packet header. Based on the BitString, each multicast packet is then replicated and forwarded. In this way, transit nodes do not need to establish a multicast distribution tree (MDT) for each multicast flow or maintain per-flow states.

The combined use of the BitString (64, 128, or 256 bits long) and a set ID (1 byte long at most) determines the destination nodes of each multicast packet. Currently, a BIERv6 sub-domain supports a maximum of 65535 destination nodes.


#### Purpose

Conventional multicast protocols, such as Protocol Independent Multicast (PIM) and next-generation multicast VPN (NG MVPN), need to establish an MDT for each multicast flow, and each node in the MDT needs to maintain per-flow states. When joining a multicast group, a new user needs to be added to the MDT hop by hop from the corresponding receiver PE, which resides at the edge of the network. This mechanism brings the following problems:

* Difficult network capacity expansion: Because each multicast flow requires an MDT to be established and each node in the MDT must maintain per-flow states, there is a linear increase in resource consumption and volume of forwarded traffic. This means that conventional multicast protocols are unsuitable for large-scale networks.
* Complex management and O&M: As multicast services continue to develop, there is a sharp increase in the number of MDTs that need to be managed and maintained. Service management and O&M become more complex due to the creation, teardown, and re-creation of numerous MDTs.
* Slow convergence after a failure occurs: A single point of failure causes the re-establishment of MDTs for all multicast flows. As a result, fast convergence cannot be implemented.
* Difficulty in optimizing service experience: Each request message sent by users must be forwarded along the MDT hop by hop, limiting the scope of optimizing user experience. This means that in an IPTV scenario, for example, users cannot quickly receive program signals of a channel.

To resolve the preceding problems, a next-generation multicast technology is needed. This is where BIER or BIERv6 comes into play. Compared with conventional multicast protocols, BIERv6 has the following advantages (BIER does not have the first two advantages):

* **Programmable IPv6 addresses, independent of MPLS label-based forwarding**: Using the natural programmability of IPv6 addresses, BIERv6 carries multicast service VPN information and BIER forwarding instructions, eliminating the need for MPLS label-based forwarding. (This is not supported in BIER.)
* **Unified unicast and multicast protocols on an SRv6-based network**: Similar to the SRv6 SID function that carries L3VPN and L2VPN services, the IPv6 addresses in BIERv6 carry MVPN and Global Table Multicast (GTM) services, simplifying network management and O&M. (This is not supported in BIER.)
* **Applicable to large-scale networks**: BIERv6 does not need to establish an MDT for each multicast flow or maintain any per-flow state. This reduces resource consumption and allows BIERv6 to support large-scale multicast services.
* **Simplified protocol processing**: Only an IGP and BGP need to be extended, and unicast routes are used to forward traffic, sparing MDT establishment. Therefore, complex protocol processing, such as multicast source sharing and SPT switching, is not involved.
* **Simplified O&M**: Transit nodes are unaware of changes in multicast service deployments. Consequently, they do not need to withdraw or re-establish numerous MDTs when the network topology changes.
* **Fast convergence and high reliability**: Devices do not need to maintain per-flow MDT states, reducing the number of entries that they need to store. Because devices need to update only one entry if a fault occurs on a network node, faster convergence and higher reliability are achieved.
* **Better service experience**: When a multicast user requests to join a BIERv6 domain, the corresponding receiver PE sends the request to the ingress directly, speeding up service response.
* **SDN-oriented**: Receiver PE and service information is set on the ingress. Other network nodes do not need to create or manage complex protocol and tunnel entries. Instead, they only need to execute the instructions contained in packets. This design concept is consistent with that of SDN.

Combining BIER with native IPv6 packet forwarding, BIERv6 does not need to explicitly establish MDTs, nor does it require each transit node to maintain per-flow states. This means that BIERv6 can be seamlessly integrated into an SRv6 network, simplifying protocol complexity and implementing efficient forwarding of multicast packets for various services, such as IPTV, video conferencing, tele-education, telemedicine, and online live telecasting.