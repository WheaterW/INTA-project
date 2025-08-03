Configuring the DCN Compatible Mode on a GNE
============================================

The DCN compatible mode can be configured on a GNE so that it can manage RTNs.

#### Background Information

RTNs use microwave links for service transmission, and no cables are required, which reduces network deployment cost.

A GNE can manage RTNs only when the DCN compatible mode is configured on the GNE for DCN communication with the RTNs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dcn**](cmdqueryname=dcn)
   
   
   
   The DCN view is displayed.
3. Run [**set compatible mode**](cmdqueryname=set+compatible+mode)
   
   
   
   The DCN compatible mode is configured on the GNE.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.