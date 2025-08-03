Configuring Level 1 Carrier CE to Access Level 1 Carrier PE (Inter-AS)
======================================================================

If the Level 1 carrier and the Level 2 carrier are in different ASs, the Level 1 carrier takes the Level 2 carrier as its VPN user, and the configuration of carrier's carrier is similar to the configuration of CE accessing PE in the basic BGP/MPLS IP VPN.

#### Procedure

* Create a VPN instance on the Level 1 carrier PE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
     
     
     
     A VPN instance is created and the VPN instance view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
     
     
     
     The IPv4 address family is enabled for the VPN instance and the VPN instance IPv4 address family view is displayed.
  4. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher-name*
     
     
     
     The RD of the VPN instance IPv4 address family is set.
  5. Run [**apply-label**](cmdqueryname=apply-label) **per-route**
     
     
     
     The label distribution mode is set to one-label-per-route.
  6. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ]
     
     
     
     One or multiple VPN targets are configured for the VPN instance IPv4 address family.
  7. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  8. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of interface connected to the Level 1 carrier CE is displayed.
  9. Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
     
     
     
     The interface is bound to the VPN instance.
  10. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
      
      
      
      An IP address is configured for the interface.
  11. Run [**mpls**](cmdqueryname=mpls)
      
      
      
      MPLS is enabled on the interface.
  12. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure labeled BGP on the Level 1 carrier PE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* **permit** **node** *seq-number*
     
     
     
     A route-policy is created for the Level 1 carrier CE.
  3. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
     
     
     
     Labels are allocated to IPv4 routes.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**bgp**](cmdqueryname=bgp) *as-number1*
     
     
     
     The BGP view is displayed.
  6. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name*
     
     
     
     The BGP VPN-instance IPv4 address family view is displayed.
  7. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number2*
     
     
     
     The Level 1 carrier CE is specified as the EBGP peer.
  8. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
     
     
     
     The function of exchanging labeled IPv4 routes is enabled.
  9. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *route-policy-name* **export**
     
     
     
     Labels are assigned to routes advertised to the Level 1 carrier CE.
  10. Run [**import-route**](cmdqueryname=import-route) **direct**
      
      
      
      Direct routes are imported.
  11. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure labeled BGP on the Level 1 carrier CE between it and the Level 1 carrier PE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface connected to the Level 1 carrier PE is displayed.
  3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
     
     
     
     An IP address is configured for the interface.
  4. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     MPLS is enabled on the interface.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  6. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* **permit** **node** *seq-number*
     
     
     
     The route-policy is created for the Level 1 carrier PE.
  7. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
     
     
     
     Labels are assigned to IPv4 routes.
  8. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  9. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  10. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number1*
      
      
      
      The Level 1 carrier PE is specified as the EBGP peer.
  11. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
      
      
      
      The function of exchanging labeled IPv4 routes is enabled.
  12. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *route-policy-name1* **export**
      
      
      
      Labels are assigned to the routes advertised to the Level 1 carrier PE.
  13. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure labeled BGP on the Level 1 carrier CE between it and the Level 2 carrier PE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* **permit** **node** *seq-number*
     
     
     
     A route-policy is created for the Level 2 carrier PE.
  3. Run [**if-match mpls-label**](cmdqueryname=if-match+mpls-label)
     
     
     
     The labeled IPv4 routes are matched.
  4. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
     
     
     
     Labels are assigned to IPv4 routes.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  6. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  7. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
     
     
     
     The Level 2 carrier PE is configured as the IBGP peer.
  8. Run [**peer**](cmdqueryname=peer) *ipv4-address* **connect-interface loopback** *interface-number*
     
     
     
     The interface used to set up a TCP connection is specified.
  9. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
     
     
     
     The function of exchanging labeled IPv4 routes is enabled.
  10. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *route-policy-name* **export**
      
      
      
      Labels are assigned to the labeled IPv4 routes advertised to the Level 2 carrier PE.
  11. Run [**import-route**](cmdqueryname=import-route) { **rip** | **isis** | **ospf** } *processId*
      
      
      
      The internal routes of the Level 2 carrier network are imported.
  12. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure labeled BGP on the Level 2 carrier PE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
     
     
     
     The Level 1 carrier CE is specified as the IBGP peer.
  4. Run [**peer**](cmdqueryname=peer) *ipv4-address* **connect-interface loopback** *interface-number*
     
     
     
     The interface used to set up a TCP connection is specified.
  5. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
     
     
     
     The function of exchanging labeled IPv4 routes is enabled.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.