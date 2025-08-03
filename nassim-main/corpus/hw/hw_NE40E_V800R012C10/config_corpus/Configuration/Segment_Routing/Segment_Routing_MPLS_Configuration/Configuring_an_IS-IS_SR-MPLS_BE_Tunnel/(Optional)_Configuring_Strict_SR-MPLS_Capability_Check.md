(Optional) Configuring Strict SR-MPLS Capability Check
======================================================

Strict SR-MPLS capability check enables a node, when computing an SR-MPLS BE LSP (SR LSP for short), to check whether all nodes along the SR LSP support SR-MPLS. This prevents forwarding failures caused by the existence of SR-MPLS-incapable nodes on the SR LSP.

#### Context

If strict SR-MPLS capability check is configured and SR-MPLS-incapable nodes exist on the optimal path from the current node to the destination node, the SR LSP to the destination node fails to be established.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   The IS-IS view is displayed.
3. Run [**sr-lsp strict-check**](cmdqueryname=sr-lsp+strict-check)
   
   
   
   Strict SR-MPLS capability check is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.