Configuring the Level 1 Carrier CE to Access the Level 1 Carrier PE (Using the BGP Labeled Route Solution)
==========================================================================================================

When the Level 1 carrier and Level 2 carrier are in different ASs, the Level 1 carrier takes the Level 2 carrier as its VPN user.

#### Procedure

1. Create a VPN instance on the Level 1 carrier PE.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
      
      
      
      A VPN instance is created, and the VPN instance view is displayed.
   3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
      
      
      
      The VPN instance IPv4 address family is enabled, and the view of this address family is displayed.
   4. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
      
      
      
      An RD is set for the VPN instance IPv4 address family.
   5. Run [**apply-label**](cmdqueryname=apply-label) **per-route**
      
      
      
      The label distribution mode is set to one-label-per-route.
   6. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ]
      
      
      
      A VPN target is configured for the VPN instance IPv4 address family.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   8. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The view of the interface connected to the Level 1 carrier CE is displayed.
   9. Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
      
      
      
      The interface is associated with the VPN instance.
   10. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
       
       
       
       The IP address is configured for the interface.
   11. Run [**mpls**](cmdqueryname=mpls)
       
       
       
       MPLS is enabled on the interface.
   12. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
2. Configure labeled BGP on a Level 1 carrier PE.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* **permit node** *seq-number*
      
      
      
      A route-policy is created for the Level 1 carrier CE.
   3. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
      
      
      
      An action of allocating MPLS labels to the selected IPv4 routes is configured in the route-policy.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   5. Run [**bgp**](cmdqueryname=bgp) *as-number1*
      
      
      
      The BGP view is displayed.
   6. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name*
      
      
      
      The BGP-VPN instance IPv4 address family view is displayed.
   7. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number2*
      
      
      
      The Level 1 carrier CE is configured as an EBGP peer of the Level 1 carrier PE.
   8. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
      
      
      
      The capability of exchanging labeled IPv4 routes is enabled.
   9. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *route-policy-name* **export**
      
      
      
      Labels are assigned to the routes advertised to the Level 1 carrier CE.
   10. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
3. Configure labeled BGP on the Level 1 carrier CE between it and the Level 1 carrier PE.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The view of the interface connected to the Level 1 carrier PE is displayed.
   3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
      
      
      
      The IP address is configured for the interface.
   4. Run [**mpls**](cmdqueryname=mpls)
      
      
      
      MPLS is enabled on the interface.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   6. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* **permit node** *seq-number*
      
      
      
      A route-policy is created for the Level 1 carrier PE.
   7. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
      
      
      
      An action of allocating MPLS labels to the selected IPv4 routes is configured in the route-policy.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   9. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   10. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
       
       
       
       The Level 1 carrier PE is configured as an EBGP peer of the Level 1 carrier CE.
   11. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
       
       
       
       The capability of exchanging labeled IPv4 routes is enabled.
   12. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *route-policy-name* **export**
       
       
       
       Labels are assigned to the routes advertised to the Level 1 carrier PE.
   13. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
4. Configure labeled BGP on the Level 1 carrier CE between it and the Level 2 carrier PE.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* **permit node** *seq-number*
      
      
      
      A route-policy is created for the Level 2 carrier PE.
   3. Run [**if-match mpls-label**](cmdqueryname=if-match+mpls-label)
      
      
      
      Packets are matched against labeled IPv4 routes.
   4. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
      
      
      
      An action of allocating MPLS labels to the selected IPv4 routes is configured in the route-policy.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   6. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   7. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
      
      
      
      The Level 2 carrier PE is configured as an IBGP peer of the Level 1 carrier CE.
   8. Run [**peer**](cmdqueryname=peer) *ipv4-address* **connect-interface loopback** *interface-number*
      
      
      
      The interface for setting up a TCP connection is specified.
   9. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
      
      
      
      The capability of exchanging labeled IPv4 routes is enabled.
   10. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *route-policy-name* **export**
       
       
       
       Labels are allocated to the labeled IPv4 routes to be advertised to the Level 2 carrier PE.
   11. Run [**import-route**](cmdqueryname=import-route) { **ospf** | **rip** | **isis** } *process-id*
       
       
       
       The internal routes of the Level 2 carrier network are imported.
   12. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
5. Configure labeled BGP on a Level 2 carrier PE.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
      
      
      
      The Level 1 carrier CE is configured as an IBGP peer of the Level 2 carrier PE.
   4. Run [**peer**](cmdqueryname=peer) *ipv4-address* **connect-interface loopback** *interface-number*
      
      
      
      The interface for setting up a TCP connection is specified.
   5. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
      
      
      
      The capability of exchanging labeled IPv4 routes is enabled.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.