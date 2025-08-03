Setting the Hop Limit for a CR-LSP
==================================

The hop limit set on an ingress is the maximum number of hops on a path along which a CR-LSP is to be established. The hop limit is a constraint used during path selection.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *tunnel-number*
   
   
   
   The view of the MPLS TE tunnel interface is displayed.
3. Run [**mpls te hop-limit**](cmdqueryname=mpls+te+hop-limit) *hop-limit-value* [ **best-effort** | **secondary** ]
   
   
   
   The hop limit of a CR-LSP is set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.