Configuring Inter-AS IPv6 VPN Option C (Solution 1)
===================================================

EBGP connections in multi-hop mode are established between PEs of different ASs to exchange VPNv6 routes.

#### Usage Scenario

If the MPLS backbone network carrying VPN-IPv6 routes spans multiple ASs, inter-AS VPN is needed.

If each AS has a large number of VPN-IPv6 routes for exchange, inter-AS VPN Option C can be adopted to prevent ASBRs from becoming a bottleneck. Two solutions can be adopted to realize inter-AS VPN Option C:

* Solution 1: After learning the labeled BGP routes of the public network in the remote AS from the remote ASBR, the local ASBR allocates labels for these routes and advertises these routes to the IBGP peer PE that supports the label switching capability. A complete LSP is then set up.
* Solution 2: No IBGP peer relationship is needed between the PE and ASBR. In this solution, an ASBR learns the labeled public BGP routes of the remote AS from the peer ASBR. Then these labeled public BGP routes are imported into IGP to trigger LDP LSP setup. This process can establish a complete LDP LSP between two PEs.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In inter-AS IPv6 VPN Option C, do not enable LDP between ASBRs. If LDP is enabled on the interfaces between ASBRs, LDP sessions are then established between the ASBRs. In this case, the ASBRs establish an egress LSP and send Mapping messages to the upstream ASBR. After receiving Mapping messages, the upstream ASBR establishes a transit LSP. If there are a large number of BGP routes, enabling LDP on the interfaces between ASBRs leads to the consumption of a large number of LDP labels.



#### Pre-configuration Tasks

Before configuring inter-AS IPv6 VPN Option C, complete the following tasks:

* Configure IGP for the MPLS backbone network in each AS to ensure IP connectivity for the backbone network in each AS.
* Configure basic MPLS capabilities on the MPLS backbone network in each AS.
* Configure MPLS LDP to establish an LSP between the PE and ASBR in the same AS.
* Configure an IBGP peer relationship between the PE and ASBR in the same AS.
* [Configure a VPN instance](dc_vrp_mpls-l3vpn-v6_cfg_2058.html) on each PE that connects to a CE and [bind the interface that connects a PE to a CE to the VPN instance on that PE](dc_vrp_mpls-l3vpn-v6_cfg_2059.html).
* Configure IPv6 addresses for CE interfaces connected to PEs.


[Enabling Exchange of the IPv4 Routes with Labels](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2084.html)

In inter-AS IPv6 VPN Option C, an inter-AS BGP LSP needs to be established on the backbone network, and BGP peers on the backbone network can exchange labeled IPv4 routes with each other.

[Configuring a Route-Policy to Control Label Distribution](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2085.html)

You need to configure a route-policy to control label allocation for the inter-AS BGP LSP. If labeled IPv4 routes are advertised to the PE of the local AS, you need to re-allocate the MPLS label to these routes. If routes sent by the PE of the local AS are advertised to the peer ASBR, you need to allocate the MPLS label to these routes.

[Establishing the MP-EBGP Peer Between PEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2086.html)

With extended community attributes added to BGP, MP-IBGP can advertise VPNv4 routes between PEs. PEs of different ASs are indirectly connected in most cases. Therefore, to set up the EBGP connections between them, you need to configure the permitted maximum hops between the PEs and ensure that the PEs are reachable.

[Configuring Route Exchange Between the PE and CE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2087.html)

The routing protocol between a PE and a CE can be BGP4+, static route, RIPng, OSPFv3, or IS-ISv6.

[Verifying the Configuration of Inter-AS IPv6 VPN-Option C (Solution 1)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2088.html)

After inter-AS IPv6 VPN Option C is configured, you can view information about all BGP peer relationships, VPNv6 routing information and IPv6 VPN routing information on the PE, and information about labeled IPv4 routes on the ASBR.