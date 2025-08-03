Configuring Inter-AS Seamless MPLS+HVPN
=======================================

In the inter-AS seamless MPLS+HVPN networking, an HVPN between each CSG and AGG is configured, and inter-AS seamless MPLS is configured for the link between each AGG and MASG. The networking integrates the seamless MPLS and HVPN advantages.

#### Usage Scenario

[Figure 1](#EN-US_TASK_0172368659__fig_dc_vrp_seamless_mpls_cfg_002101) illustrates the inter-AS seamless MPLS+HVPN networking. A Cell Site Gateway (CSG) and an Aggregation (AGG) establish an HVPN connection, and the AGG and a Mobile Aggregate Service Gateway (MASG) establish a seamless MPLS LSP. The AGG provides hierarchical L3VPN access services and routing management services. Seamless MPLS+HVPN combines the advantages of both seamless MPLS and HVPN. Seamless MPLS allows any two nodes to be interconnected through an LSP in scenarios where the access, aggregation, and core layers involve different domains, providing high service scalability. HVPN enables carriers to cut down network deployment costs by deploying devices with layer-specific capacities to meet service requirements.

**Figure 1** Inter-AS seamless MPLS+HVPN networking  
![](images/fig_dc_vrp_seamless_mpls_cfg_002101.png)

#### Pre-configuration Tasks

Before configuring inter-AS seamless MPLS+HVPN, complete the following tasks:

* Configure IGP protocols to implement connectivity at the access, aggregation, and core layers and enable MPLS LDP or MPLS TE to implement MPLS forwarding on a public network.
* Configure an EBGP peer relationship for each AGG ASBR-and-core ASBR pair and an IBGP peer relationship between each pair of the following nodes:
  
  + CSG and AGG
  + AGG and AGG ASBR
  + Core ASBR and MASG
* Configure an HVPN for each CSG-and-AGG pair.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If MPLS TE tunnels are used across the three layers, a tunnel policy or tunnel selector must be configured. For configuration details, see [VPN Tunnel Management Configuration](dc_vrp_tnlm_cfg_0001.html).



[Establishing an MP-EBGP Peer Relationship Between Each AGG and MASG](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_seamless_mpls_cfg_0023.html)

MP-EBGP supports BGP extended community attributes that are used to advertise VPNv4 routes between each pair of the AGG and MASG.

[Enabling BGP Peers to Exchange Labeled IPv4 Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_seamless_mpls_cfg_0024.html)

In the inter-AS seamless MPLS+HVPN networking, before an E2E BGP LSP is established between an AGG and MASG, these two BGP peers must be able to exchange labeled IPv4 routes with each other.

[Configuring a BGP LSP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_seamless_mpls_cfg_0025.html)

Before a BGP LSP is established, a routing policy must be configured to control label distribution. The egress of the BGP LSP to be established needs to assign an MPLS label to the route advertised to an upstream node. If a transit node receives a labeled IPv4 route from downstream, the downstream node must re-assign an MPLS label to the transit node and advertises the label upstream.

[(Optional) Configuring Traffic Statistics Collection for BGP LSPs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_seamless_mpls_cfg_00452.html)

To check the traffic statistics of BGP LSPs, configure traffic statistics collection on the ingress and transit nodes of the BGP LSPs.

[(Optional) Configuring the Mode in Which a BGP Label Inherits the QoS Priority in an Outer Tunnel Label](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_seamless_mpls_cfg_0036.html)

When data packets are transmitted from a core ASBR to an AGG ASBR, you can determine whether a BGP label inherits the QoS priority carried in an outer tunnel label.

[(Optional) Configuring the Protection Switching Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_seamless_mpls_cfg_0026.html)

A protection switching function, such as link or node protection, can be configured to provide high availability for an inter-AS seamless MPLS+HVPN network.

[(Optional) Configuring the Egress Protection Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_seamless_mpls_cfg_0043-2.html)

The egress protection function reduces E2E BFD sessions to be established, bandwidth resources to be consumed, and the burden on devices.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_seamless_mpls_cfg_0027.html)

After configuring inter-AS seamless MPLS+HVPN, you can check all BGP peer relationships, VPNv4 routing information on AGGs and MASGs, and the connectivity of the BGP LSP between each pair of an AGG and MASG.