Overview of BGP/MPLS IP VPN
===========================

Overview of BGP/MPLS IP VPN

#### Definition

BGP/MPLS IP VPN is a type of Layer 3 virtual private network (L3VPN), which uses BGP to advertise VPN routes and uses MPLS to forward VPN packets on the service provider (SP) backbone network. IP here means that the SP backbone network is an IP network.

[Figure 1](#EN-US_CONCEPT_0172369212__en-us_concept_0172356025_fig_dc_vrp_mpls-l3vpn-v4_feature_000201) shows a basic BGP/MPLS IP VPN model.

**Figure 1** BGP/MPLS IP VPN model  
![](images/fig_feature_image_0003997569.png)  

The basic BGP/MPLS IP VPN model consists of the following roles:

* Customer edge (CE): edge device on the customer network. A CE provides interfaces to directly connect to the SP network. A CE can be a router, switch, or host. Generally, a CE is unaware of VPNs and does not need to support MPLS.
* Provider edge (PE): edge device on the SP network. A PE directly connects to CEs. On an MPLS network, PEs process all VPN services and must have high performance.
* Provider device (P): backbone device on the SP network. A P does not directly connect to CEs. Ps only need to possess basic MPLS forwarding capabilities and do not maintain VPN information.

Generally, PEs and Ps are managed by SPs, and CEs are managed by users. Users can also delegate CE management to SPs.

A PE can connect to multiple CEs. A CE can connect to multiple PEs of the same SP or of different SPs.


#### Purpose

* MPLS seamlessly integrates the flexibility of IP routing and simplicity of asynchronous transfer mode (ATM) label switching. MPLS adds a connection-oriented control plane to a connectionless IP network, facilitating IP network management and operations. On IP networks, MPLS TE has become an important tool in managing network traffic, reducing network congestion, and ensuring QoS.
  
  Therefore, VPNs using MPLS-based IP networks as backbone networks (MPLS VPNs) have become an important means for IP network service providers to provide value-added services.
* Unlike the Interior Gateway Protocol (IGP), BGP focuses on controlling route transmission and choosing the optimal routes instead of discovering and calculating routes. A VPN uses the public network to transmit VPN data, and the public network use an IGP to discover and calculate routes. The key to constructing a VPN is controlling the transmission of VPN routes and choosing the optimal route between two PEs.
  
  BGP uses TCP (port number 179) as its transport layer protocol, enhancing reliability. This allows VPN routes to be directly exchanged between two PEs with Routers located between them.
  
  BGP can append any information to a route as optional BGP attributes. Such information is transparently forwarded by BGP devices incapable of identifying those attributes. This facilitates VPN route transmission between PEs.
  
  When routes are updated, BGP sends only updated routes rather than all routes. This implementation saves the bandwidth consumed by route transmission, making the transmission of large numbers of VPN routes over a public network possible.
  
  As an Exterior Gateway Protocol (EGP), BGP is suitable for VPNs that spans the networks of multiple carriers.