(Optional) Disabling LDP LSP Flapping Suppression
=================================================

LDP LSP flapping suppression helps effectively prevent label flapping. This function can be disabled.

#### Context

After an LDP LSP goes Up, it goes Down due to a protocol or interface failure. A device attempts to reestablish the LDP LSP, which maximizes the LDP LSP protocol hard convergence. If LDP LSP alternates between Up and Down when a downstream node frequently sends a label to an upstream node or a label is withdrawn, CPU usage increases. To prevent label suppression, configure LDP LSP flapping suppression.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   MPLS LDP is enabled globally.
4. Run [**protocol-packets suppress disable**](cmdqueryname=protocol-packets+suppress+disable)
   
   
   
   LDP LSP flapping suppression is disabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.