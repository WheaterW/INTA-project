Configuring Inter-AS VPN Option C in the Labeled-Unicast Address Family (Solution 1)
====================================================================================

To allow PEs in different ASs to exchange VPNv4 routes, configure inter-AS VPN Option C. This enables multi-hop EBGP connections to be established between PEs. The labeled-unicast address family (also known as the BGP-labeled or BGP-LU address family) can be used to negotiate the capability to distribute independent labels.

#### Usage Scenario

If the MPLS backbone network carrying VPN routes spans multiple ASs, the inter-AS VPN is required.

If each AS needs to exchange a large number of VPN routes, inter-AS VPN Option C is a good choice to prevent the ASBR from becoming a bottleneck that impedes network expansion. The following solutions can be used to implement inter-AS VPN Option C:

* Solution 1: A local ASBR learns a labeled BGP public network route from the peer ASBR, automatically assigns a label to this route, and advertises it to an IBGP peer that supports the label capability, a PE in the same AS. Then, a complete public network LSP is established.
* Solution 2: The IBGP peer relationship between the PE and ASBR is not needed. In this solution, an ASBR learns the labeled public BGP routes of the remote AS from the peer ASBR. These labeled public BGP routes are then imported into the IGP to trigger the establishment of an LDP LSP. In this manner, a complete LDP LSP is established between the two PEs.

Solution 1 is described here, and solution 2 is described in [Configuring Inter-AS VPN Option C in the Labeled-Unicast Address Family (Solution 2)](dc_vrp_mpls-l3vpn-v4_cfg_0193.html).

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In inter-AS VPN Option C, do not enable LDP between ASBRs. If LDP is enabled on the interfaces between ASBRs, LDP sessions are then established between the ASBRs. As a result, the ASBRs establish an egress LSP and send Mapping messages to upstream ASBRs. After receiving Mapping messages, the upstream ASBRs establish a transit LSP. If a large number of BGP routes exist, enabling LDP on the interfaces between ASBRs leads to the occupation of a large number of LDP labels.



#### Pre-configuration Tasks

Before configuring inter-AS VPN Option C (solution 1), complete the following tasks:

* Configure IGP on the MPLS backbone network in each AS to ensure IP connectivity within each AS.
* Configure MPLS and MPLS LDP both globally and per interface on each node of the MPLS backbone network.
* Configure an IBGP peer relationship between the PE and ASBR in the same AS.
* [Configure a VPN instance on each PE](dc_vrp_mpls-l3vpn-v4_cfg_0155.html) and [bind the interface that connects a PE to a CE to the VPN instance on that PE](dc_vrp_mpls-l3vpn-v4_cfg_0156.html).
* Configure an IP address for the interface connecting a CE to a PE.


[(Optional) Configuring Per-Path Label Distribution for BGP Add-Path Labeled Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0192.html)

After per-path label distribution is configured for BGP Add-Path labeled routes, a device can apply for a unique label for each route when advertising multiple routes to a BGP Add-Path peer. After the peer receives multiple routes with different labels, it can implement BGP LSP load balancing.

[Enabling BGP Peers to Exchange Labeled IPv4 Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0187.html)

In inter-AS VPN Option C networking, a BGP LSP needs to be established between ASs, and labeled IPv4 routes need to be exchanged between BGP peers.

[Establishing an MP-EBGP Peer Relationship Between PEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0189.html)

By introducing extended community attributes into BGP, MP-EBGP can advertise VPNv4 routes between PEs. PEs of different ASs are generally not directly connected. Therefore, to set up the EBGP connection between the PEs of different ASs, you need to configure the permitted maximum hops between PEs.

[Configuring Route Exchange Between a CE and a PE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0190.html)

A PE and a CE can communicate using BGP, an IGP, or a static route.

[Verifying the Configuration of Inter-AS VPN Option C in an Independent Labeled Address Family (Solution 1)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0191.html)

After configuring inter-AS VPN Option C (solution 1), check information about all BGP peer relationships, VPNv4 routes on PEs or ASBRs, and labels of IPv4 routes on ASBRs.