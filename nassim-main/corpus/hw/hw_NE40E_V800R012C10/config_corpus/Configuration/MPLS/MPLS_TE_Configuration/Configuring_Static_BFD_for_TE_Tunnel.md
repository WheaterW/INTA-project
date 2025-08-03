Configuring Static BFD for TE Tunnel
====================================

This section describes how to configure static BFD for TE tunnel to detect faults in a TE tunnel.

#### Usage Scenario

If a BFD session detects a fault in a TE tunnel, the BFD module instructs VPN FRR to quickly switch traffic, which reduces the adverse impact on services.


#### Pre-configuration Tasks

Before configuring the static BFD for TE tunnel, configure a static CR-LSP or an MPLS TE tunnel.


[Enabling BFD Globally](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0127.html)

BFD must be enabled globally before configurations relevant to BFD are performed.

[Setting BFD Parameters on the Ingress](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0128.html)

After setting BFD parameters on the ingress, you can use BFD sessions to monitor a TE tunnel.

[Setting BFD Parameters on the Egress](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_01241.html)

This section describes how to set BFD parameters on the egress to monitor CR-LSPs using BFD sessions.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0129.html)

After configuring static BFD for TE tunnel, you can view configurations, such as the status of the BFD sessions.