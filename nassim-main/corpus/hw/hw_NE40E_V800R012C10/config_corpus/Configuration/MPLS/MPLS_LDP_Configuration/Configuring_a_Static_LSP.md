Configuring a Static LSP
========================

LSPs can be established using statically configured labels.

#### Context

The establishment of static LSPs does not require a label distribution protocol or exchange of control packets. As such, static LSPs consume fewer resources and are applicable to small networks with a simple and stable topology. Static LSPs cannot dynamically adapt to network topology changes. Once the network topology changes, an administrator must modify configurations on each LSR of each involved LSP so that the LSPs can work properly.


#### Pre-configuration Tasks

Before configuring a static LSP, configure a unicast static route or an IGP to implement network connectivity between LSRs.


[Enabling MPLS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0198.html)

After MPLS is enabled, related MPLS configurations can be performed.

[Configuring the Ingress of a Static LSP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0192.html)

A static LSP must be manually configured on the ingress.

[Configuring a Transit Node of a Static LSP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0193.html)

A static LSP needs to be manually configured on each transit node.

[Configuring the Egress of a Static LSP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0194.html)

A static LSP needs to be manually configured on the egress.

[Verifying the Static LSP Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0195.html)

After configuring the static LSP, verify its information on a local node.