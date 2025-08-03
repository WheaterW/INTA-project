(Optional) Enabling CFM
=======================

To suppress unidirectional multicast and unknown unicast packets, enable CFM for PBB VPLS.

#### Context

In PBB VPLS, SPEs broadcast unidirectional multicast and unknown unicast packets to all VSIs in a VPLS domain. To suppress unidirectional multicast and unknown unicast packets, enable CFM for PBB VPLS. After CFM is enabled, SPEs can learn the B-SMAC addresses of UPEs and unidirectionally forward unidirectional multicast and unknown unicast packets to UPEs. When network resources are tight, enabling CFM for PBB VPLS is recommended.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cfm enable**](cmdqueryname=cfm+enable)
   
   
   
   CFM is enabled.
3. Run [**vsi**](cmdqueryname=vsi) *vsi-name*
   
   
   
   The I-VSI view is displayed.
4. Run [**cfm enable**](cmdqueryname=cfm+enable)
   
   
   
   PBB VPLS is enabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.