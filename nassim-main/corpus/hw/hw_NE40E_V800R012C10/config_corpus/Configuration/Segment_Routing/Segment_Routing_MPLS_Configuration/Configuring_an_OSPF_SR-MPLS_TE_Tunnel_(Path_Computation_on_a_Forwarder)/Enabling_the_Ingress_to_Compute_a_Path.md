Enabling the Ingress to Compute a Path
======================================

CSPF is configured on the ingress to compute a path for an SR-MPLS TE tunnel.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls te**](cmdqueryname=mpls+te)
   
   
   
   MPLS TE is enabled.
4. Run [**mpls te cspf**](cmdqueryname=mpls+te+cspf)
   
   
   
   CSPF is enabled on the ingress to compute paths.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.