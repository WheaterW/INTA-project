Configuring Inter-AS LDP VPLS Option C
======================================

In inter-AS LDP VPLS Option C, ASBRs do not need to maintain inter-AS LDP VPLS information or reserve interfaces for inter-AS LDP VPLS PWs. As LDP VPLS information is exchanged only between PEs, this solution requires few resources and is easy to deploy.

#### Procedure

1. Configure the capability to exchange labeled IPv4 routes.
   
   
   * Perform the following steps on each PE:
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**bgp**](cmdqueryname=bgp) *as-number*
        
        The BGP view is displayed.
     3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
        
        The capability to exchange labeled IPv4 routes with the local ASBR is configured.
     4. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Perform the following steps on each ASBR:
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
        
        The view of the interface connecting to the peer ASBR is displayed.
     3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
        
        An IP address is configured for the interface.
     4. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     5. Run [**mpls**](cmdqueryname=mpls)
        
        MPLS is enabled.
     6. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     7. Run [**bgp**](cmdqueryname=bgp) *as-number*
        
        The BGP view is displayed.
     8. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
        
        The capability to exchange labeled IPv4 routes with the local PE is configured.
     9. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
        
        The peer ASBR is configured as an EBGP peer.
     10. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
         
         The capability to exchange labeled IPv4 routes with the peer ASBR is configured.
         
         In inter-AS LDP VPLS Option C, an inter-AS LSP must be established and the public network routes advertised between PEs and ASBRs carry MPLS labels.
         
         An EBGP peer relationship must be established between ASBRs in different ASs for them to exchange labeled IPv4 routes.
         
         The public network routes carrying MPLS labels are advertised through MP-BGP. According to relevant standards, label mappings about routes can be piggybacked inside the BGP Update messages that are used to advertise these routes. This feature is implemented through an extended BGP attribute, which enables BGP peers to process labeled IPv4 routes.
     11. Run [**commit**](cmdqueryname=commit)
         
         The configuration is committed.
2. Configure routing policies on each ASBR, so that an ASBR reallocates MPLS labels to the labeled IPv4 routes to be advertised to the local PE and allocates MPLS labels to the routes to be advertised to the peer ASBR.
   
   
   
   ASBRs allocate MPLS labels to IPv4 routes based on the configured routing policies.
   
   Perform the following steps on each ASBR:
   
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**route-policy**](cmdqueryname=route-policy) *policy-name1* **permit** **node** *seq-number*
      
      
      
      A routing policy applicable to the local PE is created.
   3. Run [**if-match mpls-label**](cmdqueryname=if-match+mpls-label)
      
      
      
      Filtering out labeled IPv4 routes is configured as a matching rule for the routing policy.
   4. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
      
      
      
      Allocating MPLS labels to IPv4 routes is configured as an action for the routing policy.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   6. Run [**route-policy**](cmdqueryname=route-policy) *policy-name2* **permit** **node** *seq-number*
      
      
      
      A routing policy applicable to the peer ASBR is created.
   7. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
      
      
      
      Allocating MPLS labels to IPv4 routes is configured as an action for the routing policy.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   9. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   10. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *policy-name1* **export**
       
       
       
       The routing policy applicable to the local PE is applied.
   11. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *policy-name2* **export**
       
       
       
       The routing policy applicable to the peer ASBR is applied.
   12. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
3. Establish a remote MPLS LDP session between the PEs in different ASs, so that the PEs can exchange PW information.
   
   
   * Perform the following steps on each ASBR:
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**bgp**](cmdqueryname=bgp) *as-number*
        
        The BGP view is displayed.
     3. Run [**network**](cmdqueryname=network) *ip-address* [ *mask* | *mask-length* ] [ **route-policy** *route-policy-name* ]
        
        The capability to advertise the local PE's loopback interface address used for BGP sessions to the peer ASBR is configured.
     4. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     5. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
   * Perform the following steps on each PE:
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**mpls ldp remote-peer**](cmdqueryname=mpls+ldp+remote-peer) *peer-name*
        
        The name of the remote MPLS LDP session is specified.
     3. Run [**remote-ip**](cmdqueryname=remote-ip) *ip-address*
        
        The peer IP address of the remote MPLS LDP session is specified.
     4. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
4. Configure LDP VPLS on each PE. For configuration details, see [Configuring LDP VPLS](dc_vrp_vpls_cfg_5003.html).