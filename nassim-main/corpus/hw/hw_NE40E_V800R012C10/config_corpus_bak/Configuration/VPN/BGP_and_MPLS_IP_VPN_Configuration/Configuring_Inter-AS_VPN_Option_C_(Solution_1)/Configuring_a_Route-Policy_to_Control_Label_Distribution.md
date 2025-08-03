Configuring a Route-Policy to Control Label Distribution
========================================================

You need to configure a route-policy to control label allocation for each inter-AS BGP LSP. If labeled IPv4 routes are advertised to a PE of the local AS, you need to re-allocate MPLS labels to these routes. If routes sent by a PE of the local AS are advertised to the peer ASBR, you need to allocate MPLS labels to these routes.

#### Procedure

* Create a route-policy.
  
  
  
  Perform the following steps on the ASBR:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**route-policy**](cmdqueryname=route-policy) *policy-name1* **permit** **node** *node*
     
     
     
     The route-policy applied to the local PE is created.
     
     
     
     For the labeled IPv4 routes received from the peer ASBR, this policy ensures that the local ASBR allocates a new MPLS label to them when advertising them to PEs in the local AS.
  3. Run [**if-match mpls-label**](cmdqueryname=if-match+mpls-label)
     
     
     
     The IPv4 routes with labels are matched.
  4. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
     
     
     
     A label is allocated to the IPv4 routes.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  6. Run [**route-policy**](cmdqueryname=route-policy) *policy-name2* **permit** **node** *node*
     
     
     
     A route-policy applicable to the peer ASBR is created.
     
     
     
     When an ASBR advertises the routes received from a PE in the same AS to the peer ASBR, the ASBR allocates MPLS labels to the routes.
  7. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
     
     
     
     A label is allocated to the IPv4 routes.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Apply a route-policy.
  
  
  
  Perform the following steps on each ASBR:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *policy-name1* **export**
     
     
     
     The route-policy used when routes are advertised to the local PE is applied.
  4. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *policy-name2* **export**
     
     
     
     The route-policy used when routes are advertised to the peer ASBR is applied.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Control the creation of ingress LSPs for labeled BGP routes based on route-policies.
  
  
  
  Perform the following steps on the PE.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ingress-lsp trigger**](cmdqueryname=ingress-lsp+trigger) { **route-policy** *route-policy-name* | **route-filter** *route-filter-name* }
     
     
     
     The device is configured to create ingress LSPs for labeled BGP routes based on route-policies or route-filters.
     
     
     
     On a MAN where the hybrid access mode is used, a large number of labeled BGP routes are used to establish E2E LSPs. On certain transit nodes where VPN services do not need to be supported, excessive ingress LSPs are created, wasting network resources. In this case, you can run this command to create ingress LSPs for desired labeled BGP routes based on route-policies or route-filters to save network resources.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.