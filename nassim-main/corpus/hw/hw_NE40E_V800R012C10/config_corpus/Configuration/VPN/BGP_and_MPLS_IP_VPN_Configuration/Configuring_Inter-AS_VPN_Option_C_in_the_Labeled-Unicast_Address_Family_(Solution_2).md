Configuring Inter-AS VPN Option C in the Labeled-Unicast Address Family (Solution 2)
====================================================================================

After LDP LSPs are established for the labeled BGP routes of the public network, multi-hop EBGP connections are established between PEs of different ASs to exchange VPNv4 routes. The labeled-unicast address family (also known as the BGP-labeled or BGP-LU address family) can be used to negotiate the capability to distribute independent labels.

#### Usage Scenario

If the MPLS backbone network carrying VPN routes spans multiple ASs, the inter-AS VPN is required.

If each AS needs to exchange a large number of VPN routes, inter-AS VPN-Option C is a good choice to prevent the ASBR from becoming a bottleneck that impedes network expansion. The following solutions can be used to implement inter-AS VPN-Option C:

* Solution 1: After learning the labeled BGP routes of the public network in the remote AS from the remote ASBR, the local ASBR allocates labels for these routes, and advertises these routes to the IBGP peer that supports the label switching capability. In this manner, a complete LSP is set up.
* Solution 2: The IBGP peer relationship between the PE and ASBR is not needed. In this solution, an ASBR learns the labeled public BGP routes of the remote AS from the peer ASBR. These labeled public BGP routes are then imported into IGP to trigger the establishment of an LDP LSP. In this manner, a complete LDP LSP is established between the two PEs.

If an ASBR is ready to access a large number of PEs, solution 2 is recommended for its easy configuration.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In inter-AS VPN-Option C networking, do not enable LDP between ASBRs. If LDP is enabled on the interfaces between ASBRs, LDP sessions are then established between the ASBRs. As a result, the ASBRs establish an egress LSP and send Mapping messages to upstream ASBRs. After receiving Mapping messages, the upstream ASBRs establish a transit LSP. When there are a large number of BGP routes, enabling LDP on the interfaces between ASBRs leads to the occupation of a large number of LDP labels.



#### Pre-configuration Tasks

Before configuring inter-AS VPN Option C (solution 2), complete the following tasks:

* Configure IGP on the MPLS backbone network in each AS to ensure IP connectivity within each AS.
* Configure MPLS and MPLS LDP both globally and per interface on each node of the MPLS backbone network in each AS.
* Configure a VPN instance on each PE and bind the interface that connects a PE to a CE to the VPN instance on that PE.
* Configure an IP address for the interface connecting a CE to a PE.
* Configure a name for the IP prefix list used to filter labeled BGP routes of the public network.


[Establishing an EBGP Peer Relationship Between ASBRs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0194.html)

An EBGP peer relationship is established between ASBRs to advertise routes destined for the loopback interfaces on PEs.

[Advertising the Routes of a PE in the Local AS to the Remote PE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0195.html)

After the routes of the loopback interface on a PE in an AS are advertised to the remote PE in another AS, the MP-EBGP peer relationship is established between PEs.

[Adding a BGP Peer to the Labeled Address Family](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0196.html)

To establish an inter-AS BGP LSP, enable ASBRs to exchange labeled IPv4 routes.

[Establishing an LDP LSP for the Labeled BGP Routes of the Public Network](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0197.html)

By enabling LDP on ASBRs to allocate labels for BGP routes, you can establish LDP LSPs for labeled BGP routes of the public network that are filtered in the IP prefix list

[Importing Labeled Routes to a Public Network's Unicast Routing Table](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0183.html)

To allow mutual access between public network users and users with labeled routes, configure labeled routes to be imported into the public network's unicast routing table.

[Establishing an MP-EBGP Peer Relationship Between PEs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0198.html)

By introducing extended community attributes into BGP, MP-IBGP can advertise VPNv4 routes between PEs. PEs of different ASs are generally not directly connected. To set up an EBGP connection between the PEs of different ASs, you must configure the permitted maximum number of hops between PEs.

[Configuring Route Exchange Between a CE and a PE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0199.html)

A PE and a CE can communicate using BGP, IGP, or a static route.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-l3vpn-v4_cfg_0185.html)

After configuring inter-AS VPN Option C (solution 2), check information about all BGP peer relationships, VPNv4 routes on PEs, and labels of IPv4 routes on ASBRs.