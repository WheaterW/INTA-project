Applying PBR
============

Applying_PBR

#### Context

Policy-based routing (PBR) must be applied to the inbound interface of the Router.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ip policy-based-route**](cmdqueryname=ip+policy-based-route) *policy-name*
   
   
   
   PBR is applied to the interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.