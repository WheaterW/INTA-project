(Optional) Disabling TE LSP Flapping Suppression
================================================

TE LSP flapping suppression prevents high CPU usage stemming from TE LSP flapping. This function can be disabled.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls te**](cmdqueryname=mpls+te)
   
   
   
   MPLS TE is globally enabled.
4. Run [**mpls te suppress-flapping disable**](cmdqueryname=mpls+te+suppress-flapping+disable)
   
   
   
   TE LSP flapping suppression is disabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.