Configuring mLDP P2MP FRR Link Protection
=========================================

mLDP P2MP FRR link protection rectifies link faults on mLDP LSPs, improving user network reliability.

#### Usage Scenario

As user services continue to grow, the demands for using mLDP LSPs to carry multicast traffic are increasing, so are the link faults on mLDP LSPs. mLDP P2MP FRR link protection can be configured to prevent packet loss due to link faults.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

mLDP P2MP FRR link protection does not support backup links on a TE tunnel.



#### Pre-configuration Tasks

Before configuring mLDP P2MP FRR link protection, [configure an automatic P2MP TE tunnel.](dc_vrp_ldp-p2p_cfg_0062.html)


[Enabling mLDP P2MP FRR Link Protection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0201.html)

mLDP P2MP FRR link protection can be configured in the MPLS-LDP view.

[Enabling the Detection of Traffic with New mLDP MBB Incoming Labels](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0211.html)

After the detection of traffic with new mLDP MBB incoming labels is enabled, an MBB switchover can be performed as soon as possible after a fault occurs, reducing traffic loss.

[(Optional) Setting Timers for mLDP P2MP FRR Link Protection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0202.html)

Timers can be set for mLDP P2MP FRR link protection, which helps properly perform a traffic switchover.

[Verifying the Configurations](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0301.html)

After configuring mLDP P2MP FRR, check P2MP multicast LSP information. The command output shows FRR LSP information.