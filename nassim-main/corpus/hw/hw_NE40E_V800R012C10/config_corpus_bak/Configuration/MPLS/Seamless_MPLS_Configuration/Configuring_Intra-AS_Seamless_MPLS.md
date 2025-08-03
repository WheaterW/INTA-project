Configuring Intra-AS Seamless MPLS
==================================

In the intra-seamless MPLS networking, the access, aggregation, and core layers are within a single AS. A BGP LSP is established across the three layers within the AS to implement E2E service connectivity.

#### Usage Scenario

As shown in [Figure 1](#EN-US_TASK_0172368636__fig_dc_vrp_seamless_mpls_cfg_000501), the access, aggregation, and core layers belong to the same AS. Intra-AS seamless MPLS can be configured to transmit services between gNodeBs or eNodeBs and a Mobility Management Entity (MME) or Serving Gateway (SGW). Intra-AS seamless MPLS applies to mobile bearer networks.

**Figure 1** Intra-AS seamless MPLS networking  
![](images/fig_dc_vrp_seamless_mpls_cfg_000501.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

When intra-AS seamless MPLS is configured for an L3VPN, BGP LSPs can be recursed to load-balancing LDP, TE, or LDP over TE tunnels and support ECMP/UCMP.



#### Pre-configuration Tasks

Before configuring intra-AS seamless MPLS, complete the following tasks:

* Configure IGP protocols to implement connectivity at the access, aggregation, and core layers and enable MPLS LDP or MPLS TE to implement MPLS forwarding on a public network.
* Configure IBGP peer relationships between each Cell Site Gateway (CSG) and Aggregation (AGG), between each AGG and Core ABR, and between each Core ABR and Mobile Aggregate Service Gateway (MASG).

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If MPLS TE tunnels are used across the three layers, a tunnel policy or tunnel selector must be configured. For configuration details, see [VPN Tunnel Management Configuration](dc_vrp_tnlm_cfg_0001.html).



[Configuring an AGG and a Core ABR as RRs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_seamless_mpls_cfg_0006.html)

In the intra-AS seamless MPLS networking, the AGG and core ABR can be configured as RRs so that CSGs and MASGs can learn loopback routes from one another. The loopback route information is used to establish an MP-IBPG peer relationship between each CSG and MASG.

[Enabling BGP Peers to Exchange Labeled IPv4 Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_seamless_mpls_cfg_0008.html)

In the seamless MPLS networking, before an E2E BGP LSP is established, BGP peers must be able to exchange labeled IPv4 routes with each other.

[Configuring a BGP LSP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_seamless_mpls_cfg_0009.html)

Before a BGP LSP is established, a routing policy must be configured to control label distribution. The egress of the BGP LSP to be established needs to assign an MPLS label to the route advertised to an upstream node. If a transit node receives a labeled IPv4 route from downstream, the downstream node must re-assign an MPLS label to the transit node and advertises the label upstream.

[(Optional) Configuring Traffic Statistics Collection for BGP LSPs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_seamless_mpls_cfg_0045.html)

To check the traffic statistics of BGP LSPs, configure traffic statistics collection on the ingress and transit nodes of the BGP LSPs.

[(Optional) Configuring the Protection Switching Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_seamless_mpls_cfg_0010.html)

Protection switching can be configured to provide high availability for an intra-AS seamless MPLS network.

[(Optional) Configuring the Egress Protection Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_seamless_mpls_cfg_0043.html)

The egress protection function reduces E2E BFD sessions to be established, bandwidth resources to be consumed, and the burden on devices.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_seamless_mpls_cfg_0011.html)

After configuring intra-AS seamless MPLS, you can check established LSPs and the connectivity of the BGP LSPs between a CSG and an MASG.