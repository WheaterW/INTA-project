Configuring MPLS OAM for an Associated Bidirectional LSP
========================================================

This section describes how to configure MPLS OAM to check the connectivity of an associated bidirectional LSP.

#### Usage Scenario

Associated bidirectional LSPs provide bandwidth protection for bidirectional services. Bidirectional switching can be performed for associated bidirectional LSPs if faults occur. A forward LSP and a reverse LSP between two nodes are established. Each LSP is bound to the ingress of its reverse LSP. The two LSPs then form an associated bidirectional LSP. The associated bidirectional LSP is used to prevent traffic congestion. If a fault occurs on one end, the other end is notified of the fault so that both ends trigger traffic switchovers, preventing service interruptions.

MPLS OAM can check the connectivity of an associated bidirectional LSP and supports multiple detection intervals. If MPLS OAM detects a fault on an associated bidirectional LSP, it triggers a traffic switchover to prevent traffic loss.


#### Pre-configuration Tasks

Before configuring MPLS OAM for an associated bidirectional LSP, configure the associated bidirectional LSP.


[Configuring Basic Detection Functions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mplsoam_cfg_0005.html)

This section describes how to configure proper MPLS OAM parameters on both ends of an associated bidirectional LSP for network loads.

[Verifying the Configuration of MPLS OAM for an Associated Bidirectional LSP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mplsoam_cfg_0007.html)

After configuring MPLS OAM for an associated bidirectional LSP, verify the configurations.