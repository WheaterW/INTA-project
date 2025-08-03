Configuring MPLS OAM for a Static Bidirectional Co-routed LSP
=============================================================

This section describes how to configure MPLS OAM to check the connectivity of a static bidirectional co-routed LSP.

#### Usage Scenario

Static bidirectional co-routed LSPs are used to build a next-generation packet switched (PS) transport network, which is similar to an optical transport network (OTN) in the aspects of service bearing and OAM. Since traditional transport networks (such as SDH network) set high benchmarks for reliability and operation and maintenance, bidirectional co-routed LSPs must provide comprehensive OAM capabilities.

MPLS OAM can check the connectivity of a static bidirectional co-routed LSP and supports multiple detection intervals. If MPLS OAM detects a fault on a static bidirectional co-routed LSP, it triggers a traffic switchover to prevent traffic loss.


#### Pre-configuration Tasks

Before configuring MPLS OAM for a bidirectional co-routed LSP, configure the bidirectional co-routed LSP.


[Configuring Basic Detection Functions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mplsoam_cfg_0009.html)

This section describes how to configure proper MPLS OAM parameters on both ends of a static bidirectional co-routed LSP for network loads.

[Verifying the Configuration of MPLS OAM for a Static Bidirectional Co-routed LSP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mplsoam_cfg_0011.html)

After configuring MPLS OAM for a static bidirectional co-routed LSP, verify the configurations.