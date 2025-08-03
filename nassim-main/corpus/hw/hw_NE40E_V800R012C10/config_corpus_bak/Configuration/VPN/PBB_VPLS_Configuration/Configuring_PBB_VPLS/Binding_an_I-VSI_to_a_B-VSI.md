Binding an I-VSI to a B-VSI
===========================

A CE can access a PW only after the corresponding I-VSI is bound to a B-VSI.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name*
   
   
   
   The I-VSI view is displayed.
3. Run [**pbb binding b-vsi**](cmdqueryname=pbb+binding+b-vsi) *vsi-name*
   
   
   
   The I-VSI is bound to a B-VSI.
   
   
   
   The [**pbb binding b-vsi**](cmdqueryname=pbb+binding+b-vsi) command can be configured only in an I-VSI.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.