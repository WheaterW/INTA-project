Enabling the L2TP Function
==========================

To set up an L2TP tunnel between a LAC and an LNS, L2TP must be first enabled.

#### Context

L2TP functions can be used only after L2TP is enabled. If L2TP is disabled, L2TP functions cannot be used on the NE40E, even if L2TP parameters are configured.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**l2tp enable**](cmdqueryname=l2tp+enable)
   
   
   
   L2TP is enabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.