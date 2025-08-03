Setting Switching and Deletion Delays
=====================================

The switching and deletion delays are set to ensure that a CR-LSP is torn down only after a new CR-LSP has been established, which prevents traffic interruption.

#### Context

MPLS TE uses a make-before-break mechanism. If attributes of an MPLS TE tunnel, such as bandwidth or path change, a new CR-LSP with new attributes is established. Such a CR-LSP is called a modified CR-LSP. The new CR-LSP must be established before the original CR-LSP, also called the primary CR-LSP, is torn down. This prevents data loss and additional bandwidth consumption during traffic switching.

If a forwarding entry associated with the new CR-LSP does not take effect after the original CR-LSP has been torn down, a temporary traffic interruption occurs.

The switching and deletion delays can be set on the ingress of the CR-LSP to prevent the preceding problem.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls te switch-delay**](cmdqueryname=mpls+te+switch-delay) *switch-time* **delete-delay** *delete-time*
   
   
   
   The switching time and deletion delay time are set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.