Configuring Inter-AS BGP VPLS Option A
======================================

In Option A, an ASBR must reserve an interface as an AC interface for each inter-AS VC. Option A can be used when the number of inter-AS VCs is small. Compared with L3VPN, inter-AS L2VPN Option A consumes more resources and requires more configuration workload. Therefore, inter-AS L2VPN Option A is not recommended.

#### Procedure

1. Configure BGP VPLS on the PEs and ASBRs in each AS. For configuration details, see [Configuring BGP VPLS](dc_vrp_vpls_cfg_6005.html).
2. Configure an AC link between ASBRs in different ASs.
   
   
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the view of the interface connected to the peer ASBR.
   3. Run the [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name* command to bind the interface connected to the peer ASBR to the specified VSI.
   4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.