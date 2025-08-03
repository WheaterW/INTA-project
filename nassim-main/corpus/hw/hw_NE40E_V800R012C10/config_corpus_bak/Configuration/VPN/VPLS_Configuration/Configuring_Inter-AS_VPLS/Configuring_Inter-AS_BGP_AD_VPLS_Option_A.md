Configuring Inter-AS BGP AD VPLS Option A
=========================================

In inter-AS BGP AD VPLS Option A, an ASBR must reserve an interface as an AC interface for each inter-AS PW. Inter-AS BGP AD VPLS Option A applies to scenarios where few inter-AS PWs are required. Compared with L3VPN, inter-AS BGP AD VPLS Option A requires more resources and configuration workload.

#### Procedure

1. Configure BGP AD VPLS on the PEs and ASBRs in each AS. For configuration details, see [Configuring BGP AD VPLS](dc_vrp_vpls_cfg_5057.html).
2. Configure an AC link between ASBRs in different ASs.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The view of the interface that connects to the peer ASBR is displayed.
   3. Run [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name*
      
      
      
      The interface is bound to a VSI.
      
      
      
      In inter-AS Option A, each ASBR must reserve an interface as an AC interface for each inter-AS PW.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.