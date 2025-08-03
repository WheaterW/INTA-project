Enabling the Capability of Exchanging Labeled IPv4 Routes
=========================================================

To establish an inter-AS BGP LSP, you must enable ASBRs
to exchange labeled IPv4 routes.

#### Procedure

* Create a routing policy.
  
  Perform the following steps on each ASBR:
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* **permit** **node** *seq-number*
     
     
     
     The routing
     policy used to advertise routes to the remote ASBR is configured.
  3. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
     
     
     
     Labels for IPv4 routes are allocated.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is
     committed.
* Apply the routing policy.
  
  Perform the following steps on each ASBR:
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *route-policy-name* **export**
     
     
     
     The routing policy used to advertise routes to the remote ASBR
     is applied.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is
     committed.
* Enable the function to exchange labeled IPv4 routes.
  
  Perform the following steps on each ASBR.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface connecting the remote ASBR is displayed.
  3. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS capability is enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is
     committed.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  6. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  7. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
     
     
     
     The labeled IPv4 route exchange capability with the remote
     ASBR is configured.
  8. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is
     committed.