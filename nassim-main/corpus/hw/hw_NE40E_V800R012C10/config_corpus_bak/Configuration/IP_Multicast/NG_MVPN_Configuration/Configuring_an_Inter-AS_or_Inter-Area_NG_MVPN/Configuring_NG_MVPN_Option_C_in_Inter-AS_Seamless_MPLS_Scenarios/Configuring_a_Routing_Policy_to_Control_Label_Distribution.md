Configuring a Routing Policy to Control Label Distribution
==========================================================

Configure a routing policy to control MPLS label allocation for each IPv4 route. The ASBR only allocates label to the routes that match the rules in the policy. The routing policy used for peer ASBR needs to be configured on PE and ABR.

#### Procedure

* Perform the following steps on PEs:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**route-policy**](cmdqueryname=route-policy) *policy-name1* **permit** **node** *seq-number*
     
     
     
     The routing policy is configured.
  3. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
     
     
     
     New labels are allocated to matched IPv4 routes.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  6. Run [**ipv4-family**](cmdqueryname=ipv4-family) **unicast**
     
     
     
     The unicast IPv4 address family view is displayed.
  7. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *route-policy-name1* **export**
     
     
     
     The route policy applicable to a peer is applied.
  8. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
     
     
     
     The capability to exchange labeled IPv4 routes with the local ABR is configured.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Perform the following steps on an ABR:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**route-policy**](cmdqueryname=route-policy) *policy-name1* **permit** **node** *seq-number*
     
     
     
     The routing policy is configured.
  3. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
     
     
     
     New labels are allocated to matched IPv4 routes.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     The system view is displayed.
  5. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  6. Run [**ipv4-family**](cmdqueryname=ipv4-family) **unicast**
     
     
     
     The unicast IPv4 address family view is displayed.
  7. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *route-policy-name1* **export**
     
     
     
     The route policy applicable to a peer is applied.
  8. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
     
     
     
     The capability to exchange labeled IPv4 routes with the local PE and ASBR is configured.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Perform the following steps on an ASBR:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**route-policy**](cmdqueryname=route-policy) *policy-name1* **permit** **node** *seq-number*
     
     
     
     The routing policy used for peer ASBR is configured.
  3. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
     
     
     
     New labels are allocated to matched IPv4 routes.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**route-policy**](cmdqueryname=route-policy) *policy-name2* **permit** **node** *seq-number*
     
     
     
     The routing policy used for peers is configured.
  6. Run [**if-match mpls-label**](cmdqueryname=if-match+mpls-label)
     
     
     
     A filter rule is configured to match IPv4 routes with labels.
  7. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
     
     
     
     New labels are allocated to matched IPv4 routes.
  8. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  9. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  10. Run [**ipv4-family**](cmdqueryname=ipv4-family) **unicast**
      
      
      
      The unicast IPv4 address family view is displayed.
  11. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *route-policy-name1* **export**
      
      
      
      The route policy applicable to a peer is applied.
  12. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
      
      
      
      The capability to exchange labeled IPv4 routes with peers is configured.
  13. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *route-policy-name2* **export**
      
      
      
      The route policy applicable to a peer is applied.
  14. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
      
      
      
      The capability to exchange labeled IPv4 routes with peers is configured.
  15. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.