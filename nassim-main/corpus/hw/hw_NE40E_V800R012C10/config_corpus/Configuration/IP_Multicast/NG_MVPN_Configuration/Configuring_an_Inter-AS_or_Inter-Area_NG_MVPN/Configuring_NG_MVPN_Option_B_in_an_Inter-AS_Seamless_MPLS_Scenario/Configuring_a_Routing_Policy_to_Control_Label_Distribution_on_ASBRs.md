Configuring a Routing Policy to Control Label Distribution on ASBRs
===================================================================

Configure a routing policy to control MPLS label allocation for each IPv4 route. The ASBR only allocates label to the routes that match the rules in the policy.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed on an ASBR.
2. Run [**route-policy**](cmdqueryname=route-policy) *policy-name1* **permit** **node** *seq-number*
   
   
   
   The routing policy for peer ASBR is configured. For the labeled IPv4 routes received from local peers, allocate new MPLS labels for them before they are established to peer ASBRs.
3. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
   
   
   
   New labels are allocated to IPv4 routes.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   The system view is displayed.
5. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
6. Run [**ipv4-family**](cmdqueryname=ipv4-family) **unicast**
   
   
   
   The unicast IPv4 address family view is displayed.
7. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *route-policy-name1* **export**
   
   
   
   The route policy applicable to the peer ASBRs is applied.
8. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
   
   
   
   The capability to exchange labeled IPv4 routes with the local ABR is configured.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.