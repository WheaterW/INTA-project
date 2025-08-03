Configuring Inter-AS IPv6 VPN Option C (Solution 2)
===================================================

After LDP LSPs are established for the labeled BGP routes of the public network, EBGP connections in multi-hop mode are established between PEs of different ASs to exchange VPNv6 routes.

#### Usage Scenario

If the MPLS backbone network carrying VPN-IPv6 routes spans multiple ASs, inter-AS VPN is needed.

If each AS has a large number of VPN-IPv6 routes for exchange, inter-AS VPN Option C can be adopted to prevent ASBRs from becoming a bottleneck. Two solutions can be adopted to realize inter-AS VPN Option C:

* Solution 1: After learning the labeled BGP routes of the public network in the remote AS from the remote ASBR, the local ASBR allocates labels for these routes and advertises these routes to the IBGP peer PE that supports the label switching capability. A complete LSP is then set up.
* Solution 2: No IBGP peer relationship is needed between the PE and ASBR. In this solution, an ASBR learns the labeled public BGP routes of the remote AS from the peer ASBR. Then these labeled public BGP routes are imported into IGP to trigger LDP LSP setup. This process can establish a complete LDP LSP between two PEs.

If an ASBR needs to be accessed by a large number of PEs, solution 2 is recommended due to easy configuration.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In inter-AS IPv6 VPN Option C, do not enable LDP between ASBRs. If LDP is enabled on the interfaces between ASBRs, LDP sessions are then established between the ASBRs. In this case, the ASBRs establish an egress LSP and send Mapping messages to the upstream ASBR. After receiving Mapping messages, the upstream ASBR establishes a transit LSP. If there are a large number of BGP routes, enabling LDP on the interfaces between ASBRs leads to the consumption of a large number of LDP labels.

Solution 2 is described here, and solution 1 is described in [Configuring Inter-AS IPv6 VPN Option C (Solution 1)](dc_vrp_mpls-l3vpn-v6_cfg_2083.html).


#### Pre-configuration Tasks

Before configuring inter-AS IPv6 VPN Option C, complete the following tasks:

* Configure IGP for the MPLS backbone network in each AS to ensure IP connectivity for the backbone network in each AS.
* Configure basic MPLS capabilities on the MPLS backbone network in each AS.
* Configure MPLS LDP to establish an LSP between the PE and ASBR in the same AS.
* [Configure a VPN instance](dc_vrp_mpls-l3vpn-v6_cfg_2058.html) on each PE that connects to a CE and [bind the interface that connects a PE to a CE to the VPN instance on that PE](dc_vrp_mpls-l3vpn-v6_cfg_2059.html).
* Configure IPv6 addresses for CE interfaces connected to PEs.
* Configure a name for the IP prefix list used to filter labeled BGP routes of the public network.


[Establishing an EBGP Peer Relationship Between ASBRs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2090.html)

An EBGP peer relationship is established between ASBRs to advertise routes destined for the loopback interfaces on PEs.

[Advertising the Routes of a PE in the Local AS to the Remote PE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2091.html)

After the routes of the loopback interface on a PE in an AS are advertised to the remote PE in another AS, the MP-EBGP peer relationship is established between PEs.

[Enabling the Capability of Exchanging Labeled IPv4 Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2092.html)

To establish an inter-AS BGP LSP, you must enable ASBRs to exchange labeled IPv4 routes.

[Establishing an LDP LSP for the Labeled BGP Routes of the Public Network](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2093.html)

By enabling LDP on ASBRs to allocate labels for BGP routes, you can establish LDP LSPs for labeled BGP routes of the public network that are filtered in the IP prefix list.

[Establishing an MP-EBGP Peer Relationship Between PEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2094.html)

By importing extended community attributes into BGP, MP-IBGP can advertise VPNv6 routes between PEs. PEs of different ASs are generally not directly connected. To set up an EBGP connection between the PEs of different ASs, you must configure the permitted maximum number of hops between PEs.

[Configuring Route Exchange Between PEs and CEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2095.html)

The routing protocol between a PE and a CE can be BGP4+, static route, RIPng, OSPFv3, or IS-ISv6.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v6_cfg_2096.html)

After configuring inter-AS IPv6 VPN Option C (solution 2), check the establishment status of all BGP peer relationships, VPNv6 and IPv6 VPN routes on PEs, IPv4 route labels on ASBRs, and LDP LSP information on ASBRs.