Configuring a Route-Policy to Control Label Distribution
========================================================

You need to configure a route-policy to control label allocation for the inter-AS BGP LSP. If labeled IPv4 routes are advertised to the PE of the local AS, you need to re-allocate the MPLS label to these routes. If routes sent by the PE of the local AS are advertised to the peer ASBR, you need to allocate the MPLS label to these routes.

#### Context

The MPLS label distribution for IPv4 routes is controlled by the routing policy. Labels are distributed to the routes that satisfy certain requirements.

Perform the following steps on the ASBR.


#### Procedure

* Create a route-policy.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**route-policy**](cmdqueryname=route-policy) *policy-name1* **permit** **node** *seq-number*
     
     
     
     A route-policy applied to the local PE is created. For labeled IPv4 routes advertised to PEs in the same AS, the PE reallocates MPLS labels to the routes.
  3. Run [**if-match mpls-label**](cmdqueryname=if-match+mpls-label)
     
     
     
     IPv4 routes with labels are matched.
  4. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
     
     
     
     Labels are allocated to IPv4 routes.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  6. Run [**route-policy**](cmdqueryname=route-policy) *policy-name2* **permit** **node** *seq-number*
     
     
     
     The route-policy applied to the peer ASBR is created.
     
     For labeled IPv4 routes advertised to PEs in the same AS, the ASBR re-allocates MPLS labels to the routes.
  7. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
     
     
     
     The label is allocated to the IPv4 route.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Apply the route-policy.
  
  
  
  The route-policy applies to the ASBR.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *policy-name1* **export**
     
     
     
     The route-policy adopted when routes are advertised to the local PE is applied.
  4. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *policy-name2* **export**
     
     
     
     The route-policy adopted when the routes are advertised to the peer ASBR is applied.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.