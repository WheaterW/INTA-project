Configuring Inter-AS LDP VPLS Option A
======================================

Inter-AS LDP VPLS Option A is recommended for scenarios where few inter-AS PWs are required. In inter-AS LDP VPLS Option A, an ASBR must reserve an interface as an AC interface for each inter-AS PW. Compared with L3VPN, inter-AS LDP VPLS Option A consumes more resources and requires more configuration workload.

#### Procedure

1. Configure LDP VPLS on the PE and ASBR in each AS. For configuration details, see [Configuring LDP VPLS](dc_vrp_vpls_cfg_5003.html).
2. Configure an AC link between ASBRs in different ASs.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The view of the interface that connects to the peer ASBR is displayed.
   3. Run [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name*
      
      
      
      The interface is bound to a VSI.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   5. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.