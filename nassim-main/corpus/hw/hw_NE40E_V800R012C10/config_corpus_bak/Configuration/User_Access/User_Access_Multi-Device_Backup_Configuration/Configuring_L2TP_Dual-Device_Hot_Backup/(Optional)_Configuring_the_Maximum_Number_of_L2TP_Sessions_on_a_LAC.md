(Optional) Configuring the Maximum Number of L2TP Sessions on a LAC
===================================================================

In some L2TP hot backup scenarios, you can configure the maximum number of L2TP sessions on the LAC.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**l2tp lac session-limit**](cmdqueryname=l2tp+lac+session-limit) *session-limit*
   
   
   
   The maximum number of L2TP sessions is set on the LAC.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.