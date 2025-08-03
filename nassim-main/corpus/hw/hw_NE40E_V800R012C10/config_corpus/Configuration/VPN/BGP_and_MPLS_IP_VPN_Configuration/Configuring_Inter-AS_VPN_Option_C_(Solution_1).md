Configuring Inter-AS VPN Option C (Solution 1)
==============================================

Multi-hop EBGP connections are established between PEs of different ASs to exchange VPNv4 routes.

#### Usage Scenario

If the MPLS backbone network carrying VPN routes spans multiple ASs, the inter-AS VPN is required.

If each AS needs to exchange a large number of VPN routes, inter-AS VPN Option C is a good choice to prevent the ASBR from becoming a bottleneck that impedes network expansion. The following solutions can be used to implement inter-AS VPN Option C:

* Solution 1: After learning the labeled BGP routes of the public network in the remote AS from the remote ASBR, the local ASBR allocates labels for these routes, and advertises these routes to the IBGP peer that supports the label switching capability. In this manner, a complete LSP is set up.
* Solution 2: The IBGP peer relationship between the PE and ASBR is not needed. In this solution, an ASBR learns the labeled public BGP routes of the remote AS from the peer ASBR. These labeled public BGP routes are then imported into IGP to trigger the establishment of an LDP LSP. In this manner, a complete LDP LSP is established between the two PEs.

Solution 1 is described in this section, and solution 2 is described in [Configuring Inter-AS VPN Option C (Solution 2)](dc_vrp_mpls-l3vpn-v4_cfg_0143.html).

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In inter-AS VPN-Option C mode, do not enable LDP between ASBRs. If LDP is enabled on the interfaces between ASBRs, LDP sessions are then established between the ASBRs. As a result, the ASBRs establish an egress LSP and send Mapping messages to upstream ASBRs. After receiving Mapping messages, the upstream ASBRs establish a transit LSP. If a large number of BGP routes exist, enabling LDP on the interfaces between ASBRs leads to the occupation of a large number of LDP labels.



#### Pre-configuration Tasks

Before configuring inter-AS VPN Option C (solution 1), complete the following tasks:

* Configure IGP on the MPLS backbone network in each AS to ensure IP connectivity within each AS.
* Configure MPLS and MPLS LDP both globally and per interface on each node of the MPLS backbone network in each AS.
* Configure an IBGP peer relationship between the PE and ASBR in the same AS.
* [Configure a VPN instance on each PE](dc_vrp_mpls-l3vpn-v4_cfg_0155.html) and [bind the interface that connects a PE to a CE to the VPN instance on that PE](dc_vrp_mpls-l3vpn-v4_cfg_0156.html).
* Configure an IP address for the interface connecting a CE to a PE.


[Enabling the Exchange of Labeled IPv4 Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0137.html)

In inter-AS VPN Option C mode, a BGP LSP needs to be established between ASs, and labeled IPv4 routes need to be exchanged between BGP peers.

[Configuring a Route-Policy to Control Label Distribution](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0138.html)

You need to configure a route-policy to control label allocation for each inter-AS BGP LSP. If labeled IPv4 routes are advertised to a PE of the local AS, you need to re-allocate MPLS labels to these routes. If routes sent by a PE of the local AS are advertised to the peer ASBR, you need to allocate MPLS labels to these routes.

[Establishing an MP-EBGP Peer Relationship Between PEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0139.html)

By introducing extended community attributes into BGP, MP-EBGP can advertise VPNv4 routes between PEs. PEs of different ASs are generally not directly connected. Therefore, to set up the EBGP connection between the PEs of different ASs, you need to configure the permitted maximum hops between PEs.

[Configuring Route Exchange Between a CE and a PE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0140.html)

A PE and a CE can communicate using BGP, an IGP, or a static route.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0141.html)

After configuring inter-AS VPN Option C (solution 1), check information about all BGP peer relationships, VPNv4 routes on PEs, and IPv4 route labels on ASBRs.