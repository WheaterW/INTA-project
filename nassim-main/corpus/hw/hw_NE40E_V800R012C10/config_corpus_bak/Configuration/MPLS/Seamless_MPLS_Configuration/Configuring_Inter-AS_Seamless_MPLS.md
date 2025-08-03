Configuring Inter-AS Seamless MPLS
==================================

In the inter-AS seamless MPLS networking, the access and aggregation layers belong to one AS, and the core layer belong to another AS. An inter-AS BGP LSP is established across the three layers to implement E2E service connectivity.

#### Usage Scenario

As shown in [Figure 1](#EN-US_TASK_0172368647__fig_dc_vrp_seamless_mpls_cfg_001301), the access and aggregation layers belong to one AS, and the core layer belongs to another AS. Inter-AS seamless MPLS can be configured to transmit services between gNodeBs or eNodeBs and a Mobility Management Entity (MME) or Serving Gateway (SGW).

**Figure 1** Inter-AS seamless MPLS networking  
![](images/fig_dc_vrp_seamless_mpls_cfg_001301.png)  

![](../../../../public_sys-resources/note_3.0-en-us.png) 

When inter-AS seamless MPLS is configured for an L3VPN, BGP LSPs can be recursed to load-balancing LDP, TE, or LDP over TE tunnels and support ECMP/UCMP.



#### Pre-configuration Tasks

Before configuring inter-AS seamless MPLS, complete the following tasks:

* Configure IGP protocols to implement connectivity at the access, aggregation, and core layers and enable MPLS LDP or MPLS TE to implement MPLS forwarding on a public network.
* Configure EBGP peer relationships for each AGG ASBR-and-core ASBR pair and an IBGP peer relationship between each pair of the following nodes:
  + Cell Site Gateway (CSG) and Aggregation (AGG)
  + AGG and AGG ASBR
  + Core ASBR and Mobile Aggregate Service Gateway (MASG)

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If MPLS TE tunnels are used across the three layers, a tunnel policy or tunnel selector must be configured. For configuration details, see [VPN Tunnel Management Configuration](dc_vrp_tnlm_cfg_0001.html).



[Configure an AGG as an RR](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_seamless_mpls_cfg_0014.html)

In the inter-AS seamless MPLS networking, an AGG is configured as an RR to advertise the route to the CSG's loopback interface to an AGG ASBR, and the AGG ASBR advertises the route to the core layer over an EBGP peer connection. The loopback route information is used to establish an MP-EBGP peer relationship between each CSG and MASG.

[Enabling BGP Peers to Exchange Labeled IPv4 Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_seamless_mpls_cfg_0016.html)

In the seamless MPLS networking, before an E2E BGP LSP is established, BGP peers must be able to exchange labeled IPv4 routes with each other.

[Configuring a BGP LSP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_seamless_mpls_cfg_0017.html)

Before a BGP LSP is established, a routing policy must be configured to control label distribution. The egress of the BGP LSP to be established needs to assign an MPLS label to the route advertised to an upstream node. If a transit node receives a labeled IPv4 route from downstream, the downstream node must re-assign an MPLS label to the transit node and advertises the label upstream.

[(Optional) Configuring Traffic Statistics Collection for BGP LSPs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_seamless_mpls_cfg_00451.html)

To check the traffic statistics of BGP LSPs, configure traffic statistics collection on the ingress and transit nodes of the BGP LSPs.

[(Optional) Configuring the Mode in Which a BGP Label Inherits the QoS Priority in an Outer Tunnel Label](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_seamless_mpls_cfg_0035.html)

When data packets are transmitted from a core ASBR to an AGG ASBR, you can determine whether a BGP label inherits the QoS priority carried in an outer tunnel label.

[(Optional) Configuring the Protection Switching Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_seamless_mpls_cfg_0018.html)

A protection switching function, such as link or node protection, can be configured to provide high availability for an inter-AS seamless MPLS network.

[(Optional) Configuring the Egress Protection Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_seamless_mpls_cfg_0043-1.html)

The egress protection function reduces E2E BFD sessions to be established, bandwidth resources to be consumed, and the burden on devices.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_seamless_mpls_cfg_0019.html)

After configuring inter-AS seamless MPLS, you can check established LSPs and the connectivity of BGP LSPs between a CSG and an MASG.