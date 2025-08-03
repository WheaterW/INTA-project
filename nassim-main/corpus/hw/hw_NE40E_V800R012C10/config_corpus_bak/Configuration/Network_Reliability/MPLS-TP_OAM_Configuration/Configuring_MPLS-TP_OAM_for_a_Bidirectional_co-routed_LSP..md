Configuring MPLS-TP OAM for a Bidirectional co-routed LSP.
==========================================================

This section describes how to configure Multiprotocol Label Switching Transport Profile (MPLS-TP) operation, administration and maintenance (OAM) to detect a static bidirectional co-routed LSP.

#### Usage Scenario

MPLS-TP has been widely used on transport networks. Traditional transport networks, such as synchronous digital hierarchy (SDH), have set high benchmarks for operation and maintenance, and therefore MPLS-TP must provide comprehensive OAM capabilities.

MPLS-TP OAM can detect faults on bidirectional LSP and collect performance statistics. On the network shown in [Figure 1](#EN-US_CONCEPT_0172362409__fig_dc_vrp_mpls-tp_oam_cfg_000202), the ingress LER is a MEP, the egress LER is the RMEP, and transit LERs are MIPs. MPLS-TP OAM runs on the MEPs, providing connectivity check, packet loss detection, and alarm suppression functions.

**Figure 1** Bidirectional LSP  
![](images/fig_dc_vrp_mpls-tp_oam_cfg_000202.png)


#### Pre-configuration Tasks

Before configuring MPLS-TP OAM for a bidirectional LSP, complete the following tasks:

* Configure a bidirectional LSP.
* Enable packet statistics collection on a tunnel interface.


[Creating an ME Instance and Binding It to a Tunnel Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-tp_oam_cfg_0005.html)

This section describes how to create a ME instance and bind it to a tunnel interface. This is a prerequisite for configuring MPLS-TP OAM for LSP.

[(Optional) Configuring CC/CV](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-tp_oam_cfg_0006.html)

This section describes how to configure CC and CV for LSP.

[(Optional) Configuring LB for an LSP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-tp_oam_cfg_0007.html)

This section describes how to configure loopback (LB) to monitor the connectivity of MPLS-TP links.

[(Optional) Configuring Frame LM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-tp_oam_cfg_0008.html)

This section describes how to configure frame loss measurement (LM) for MPLS-TP services.

[(Optional) Configuring Frame DM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-tp_oam_cfg_0009.html)

This section describes how to configure one- and two-way frame delay measurement (DM) to collect reliability statistics for MPLS-TP services.

[Verifying the Configuration of MPLS-TP OAM for an LSP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-tp_oam_cfg_0011.html)

After configuring MPLS-TP OAM function for a LSP, verify the configuration by querying performance statistics and fault detection information.