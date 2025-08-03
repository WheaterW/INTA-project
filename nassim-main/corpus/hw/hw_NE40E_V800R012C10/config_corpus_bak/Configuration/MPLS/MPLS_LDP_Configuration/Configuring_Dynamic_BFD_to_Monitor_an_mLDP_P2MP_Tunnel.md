Configuring Dynamic BFD to Monitor an mLDP P2MP Tunnel
======================================================

Dynamic BFD can be configured to monitor a specified mLDP P2MP tunnel. If a primary tree fails, traffic can be rapidly switched to a backup tree, which reduces traffic loss.

#### Usage Scenario

No tunnel protection is provided for mLDP P2MP tunnels. If an LSP fails, traffic can only be switched using route change-induced hard convergence, which renders low performance. BFD for mLDP P2MP tunnel applies to NG-MVPNs and VPLS networks on which mLDP P2MP trees with primary and backup roots are configured. If a P2MP tunnel fails, BFD for mLDP P2MP tunnel rapidly detects the fault and switches traffic to the backup tunnel, which reduces traffic loss and improves fault convergence performance in an NG-MVPN over mLDP P2MP scenario or a VPLS over mLDP P2MP scenario.![](../../../../public_sys-resources/note_3.0-en-us.png) 

Perform the configuration on each root and leaf node.




#### Pre-configuration Tasks

Before configuring dynamic BFD to monitor an mLDP P2MP tunnel, complete the following tasks:

* [Configure an mLDP P2MP tunnel.](dc_vrp_ldp-p2p_cfg_0060.html)


[Enabling Dynamic BFD to Monitor an mLDP P2MP Tunnel](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0113.html)

Dynamic BFD for mLDP P2MP tunnel can detect the primary tree faults of a P2MP tunnel.

[(Optional) Adjusting Dynamic BFD Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0114.html)

You can adjust BFD parameters, including the minimum interval at which BFD packets are sent, the minimum interval at which BFD packets are received, and the BFD detection multiplier.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0115.html)

After configuring dynamic BFD to monitor an mLDP P2MP tunnel, you can check BFD session information.