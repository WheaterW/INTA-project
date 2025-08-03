Configuring MPLS-TP OAM for a PW
================================

This section describes how to configure MPLS-TP OAM for a PW. The NE40E can monitor PWs using MPLS-TP OAM.

#### Usage Scenario

MPLS-TP has been widely used on transport networks. Since traditional transport networks (such as SDH) set high benchmarks for reliability and operation and maintenance, MPLS-TP must provide comprehensive OAM capabilities.

MPLS-TP OAM can detect faults in a PW over a bidirectional LSP and collect performance statistics. On the PW shown in [Figure 1](#EN-US_CONCEPT_0172362416__fig_dc_vrp_mpls-tp_oam_cfg_001201)), T-PEs are the MEPs, and S-PEs are the MIPs. MPLS-TP OAM runs on the MEPs and provides connectivity check, frame loss measurement, and frame delay measurement.

**Figure 1** PW over a bidirectional LSP  
![](images/fig_dc_vrp_mpls-tp_oam_cfg_001201.png)  

[Table 1](#EN-US_CONCEPT_0172362416__table_0000038022) describes the support of MPLS-TP OAM detection for different types of PWs.

**Table 1** Support of MPLS-TP OAM detection for different types of PWs
| Function | Static VPWS | Static VPLS |
| --- | --- | --- |
| CC/CV | Support | Support |
| LB | Support | Not support |
| LM | Support | Not support |
| DM | Support | Not support |



#### Pre-configuration Tasks

Before configuring MPLS-TP OAM for a PW, complete the following tasks:

* Configure a PW over a bidirectional LSP.
* Enable performance statistics collection for the attachment circuit (AC) interface of the PW.


[Creating an ME Instance and Binding It to a PW](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-tp_oam_cfg_0013.html)

This section describes how to create an ME instance and bind it to a PW.

[(Optional) Configuring CC and CV for an LSPa TE-LSP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-tp_oam_cfg_0014.html)

This section describes how to configure CC and CV for LSP.

[(Optional) Configuring LB for an LSP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-tp_oam_cfg_0015.html)

This section describes how to configure loopback (LB) to monitor the connectivity of MPLS-TP links.

[(Optional) Configuring Frame LM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-tp_oam_cfg_0016.html)

This section describes how to configure frame loss measurement (LM) for MPLS-TP services.

[(Optional) Configuring Frame DM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-tp_oam_cfg_0017.html)

This section describes how to configure one- and two-way frame delay measurement (DM) to collect reliability statistics for MPLS-TP services.

[Verifying the Configuration of MPLS-TP OAM for a PW](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mpls-tp_oam_cfg_0019.html)

After configuring Multiprotocol Label Switching Transport Profile (MPLS-TP) operation, administration and maintenance (OAM) for a pseudo wire (PW), verify the configurations by querying performance statistics and fault detection information.