(Optional) Configuring a DF Election Mode for EVPN VPWS
=======================================================

In an EVPN VPWS over MPLS scenario where a CE is multi-homed to PEs in single-active mode and no E-Trunk is configured, DF election needs to be performed between the PEs to determine the active/standby status of the PEs.

#### Context

On the EVPN VPWS multi-homing network shown in the following figure, CE1 is multi-homed to PE1 and PE2, and PE1 and PE2 establish MPLS LDP tunnels with PE3, allowing CE1 to communicate with CE2. In a multi-homing single-active scenario where no E-Trunk is configured, to prevent traffic from a remote PE from being load-balanced among multi-homing PEs, select a PE from the multi-homing PEs to forward traffic to the local CE.

**Figure 1** Configuring MPLS EVPN VPWS  
![](images/fig_dc_vrp_evpn_cfg_110002.png)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**evpn**](cmdqueryname=evpn)
   
   
   
   The global EVPN configuration view is displayed.
3. Run [**vpws-df-election type service-id**](cmdqueryname=vpws-df-election+type+service-id)
   
   
   
   Service ID-based DF election is enabled for VPWS EVPN.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.