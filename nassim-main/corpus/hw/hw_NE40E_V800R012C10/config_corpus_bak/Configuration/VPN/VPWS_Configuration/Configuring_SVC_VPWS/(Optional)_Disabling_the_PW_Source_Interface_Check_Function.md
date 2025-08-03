(Optional) Disabling the PW Source Interface Check Function
===========================================================

On a VPLS/VPWS network, the PW source interface check function is enabled by default, affecting system performance.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls pw static source-tunnel check disable**](cmdqueryname=mpls+pw+static+source-tunnel+check+disable)
   
   
   
   The PW source interface check function is disabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.