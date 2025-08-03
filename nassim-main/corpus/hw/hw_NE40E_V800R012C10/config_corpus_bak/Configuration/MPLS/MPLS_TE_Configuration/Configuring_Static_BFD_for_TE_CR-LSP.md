Configuring Static BFD for TE CR-LSP
====================================

By configuring static BFD for TE CR-LSP, you can detect TE CR-LSP faults.

#### Usage Scenario

BFD for TE CR-LSP monitors the primary and hot-standby CR-LSPs and triggers traffic switchovers between them.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

When static BFD for TE CR-LSP is used and the BFD status is Up, the BFD status remains Up even after the tunnel interface of the CR-LSP is shut down.



#### Pre-configuration Tasks

Before configuring static BFD for TE CR-LSP, configure an RSVP-TE tunnel or CR-LSP backup.


[Enabling BFD Globally](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0122.html)

BFD must be enabled globally before configurations relevant to BFD are performed.

[Setting BFD Parameters on the Ingress](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0123.html)

This section describes how to set BFD parameters on the ingress to monitor CR-LSPs using BFD sessions.

[Setting BFD Parameters on the Egress](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0124.html)

This section describes how to set BFD parameters on the egress to monitor CR-LSPs using BFD sessions.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_te-p2p_cfg_0125.html)

After configuring the static BFD for TE CR-LSP, you can view configurations, such as the status of the BFD sessions of Up.