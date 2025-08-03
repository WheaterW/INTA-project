Configuring a Routing Policy to Control Label Distribution on ASBRs
===================================================================

Configure a routing policy to control MPLS label allocation for each IPv4 route. The ASBR only allocates labels to the IPv4 routes that match the rules in the policy.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**route-policy**](cmdqueryname=route-policy) *policy-name1* **permit** **node** *seq-number*
   
   
   
   The routing policy for local PE is configured. For the labeled IPv4 routes established to PEs in the same AS, allocate a new MPLS label for them.
3. Run [**if-match mpls-label**](cmdqueryname=if-match+mpls-label)
   
   
   
   A filter rule is configured to match IPv4 routes with labels.
4. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
   
   
   
   New labels are allocated to matched IPv4 routes.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   The system view is displayed.
6. Run [**route-policy**](cmdqueryname=route-policy) *policy-name2* **permit** **node** *seq-number*
   
   
   
   The routing policy for peer ASBRs is configured. For the routes received from PE of local AS, ASBR allocates MPLS labels to them before establish them to peer ASBRs.
7. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
   
   
   
   New labels are allocated to matched IPv4 routes.
8. Run [**quit**](cmdqueryname=quit)
   
   
   
   The system view is displayed.
9. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
10. Run [**ipv4-family**](cmdqueryname=ipv4-family) **unicast**
    
    
    
    The unicast IPv4 address family view is displayed.
11. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *route-policy-name1* **export**
    
    
    
    The route policy applicable to the local PE is applied.
12. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *route-policy-name2* **export**
    
    
    
    The route policy applicable to the peer ASBR is applied.
13. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
    
    
    
    The capability to exchange labeled IPv4 routes with the local PE and the peer ASBR is configured.
    
    
    
    In Option C, an inter-AS LSP must be established and the public network routes advertised between PEs and ASBRs carry MPLS labels.
    
    An EBGP peer relationship must be established between ASBRs in different ASs for them to exchange labeled IPv4 routes.
    
    The public network routes carrying MPLS labels are advertised through MP-BGP. According to relevant standards, label mappings about routes can be piggybacked inside the BGP Update messages that are used to advertise these routes. This feature is implemented through an extended BGP attribute, which enables BGP peers to process labeled IPv4 routes.
14. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.