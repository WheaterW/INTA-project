Configuring Level 1 Carrier CEs Accessing Level 1 Carrier PEs (LDP Label Distribution, Labeled Route Mode)
==========================================================================================================

When the Level 1 carrier and Level 2 carrier are in different ASs, the Level 2 carrier functions as the VPN user of the Level 1 carrier, the same as the CE of the PE in the basic BGP/MPLS IP VPN.

#### Procedure

1. Create a VPN instance on Level 1 carrier PEs.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
      
      
      
      A VPN instance is created, and its view is displayed.
   3. Run [**ipv4-family**](cmdqueryname=ipv4-family)
      
      
      
      The VPN instance IPv4 address family is enabled, and its view is displayed.
   4. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
      
      
      
      An RD is configured for the VPN instance IPv4 address family.
   5. Run [**apply-label**](cmdqueryname=apply-label) **per-route** **evpn**
      
      
      
      The label distribution mode is set to one-label-per-route.
   6. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* & <1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ] **evpn**
      
      
      
      VPN targets are configured for the VPN instance IPv4 address family.
   7. Run [**evpn mpls routing-enable**](cmdqueryname=evpn+mpls+routing-enable)
      
      
      
      EVPN is enabled to generate and advertise IP prefix routes and IRB routes.
      
      
      
      In an EVPN L3VPN service scenario where MPLS or SR-MPLS tunnels are used as public network tunnels (including interworking scenarios), you need to run this command to enable EVPN to generate and advertise IP prefix routes and IRB routes, so that the local device can advertise IP prefix routes and IRB routes to its EVPN peers.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   9. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The view of the interface connected to the Level 1 carrier CE is displayed.
   10. Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
       
       
       
       The interface is associated with the VPN instance.
   11. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
       
       
       
       An IP address is configured for the interface.
   12. Run [**mpls**](cmdqueryname=mpls)
       
       
       
       MPLS is enabled on the interface.
   13. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
2. Configure labeled BGP on Level 1 carrier PEs.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* **permit** **node** *node*
      
      
      
      A route-policy is created for the Level 1 carrier CE.
   3. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
      
      
      
      An action of allocating labels to IPv4 routes is configured in the route-policy.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   5. Run [**bgp**](cmdqueryname=bgp) *as-number1*
      
      
      
      The BGP view is displayed.
   6. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name*
      
      
      
      The BGP-VPN instance IPv4 address family view is displayed.
   7. Run [**peer**](cmdqueryname=peer+as-number) *ipv4-address* **as-number** *as-number*
      
      
      
      The Level 1 carrier CE is configured as an EBGP peer.
   8. Run [**peer**](cmdqueryname=peer+label-route-capability) *ipv4-address* **label-route-capability**
      
      
      
      The capability of exchanging labeled IPv4 routes is enabled.
   9. Run [**peer**](cmdqueryname=peer+route-policy+export) *ipv4-address* **route-policy** *route-policy-name* **export**
      
      
      
      The function to allocate labels to routes to be advertised to the Level 1 carrier CE is enabled.
   10. Run [**advertise l2vpn evpn**](cmdqueryname=advertise+l2vpn+evpn)
       
       
       
       The VPN instance is configured to advertise EVPN IP prefix routes.
   11. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
3. Perform the following steps on Level 1 carrier CEs for the deployment of labeled BGP between Level 1 carrier CEs and Level 1 carrier PEs.
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
   6. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name1* **permit** **node** *node*
      
      
      
      A route-policy is created for the Level 1 carrier PE.
   7. Run [**apply mpls-label**](cmdqueryname=apply+mpls-label)
      
      
      
      An action of allocating labels to IPv4 routes is configured in the route-policy.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   9. Run [**bgp**](cmdqueryname=bgp) *as-number2*
      
      
      
      The BGP view is displayed.
   10. Run [**peer**](cmdqueryname=peer+as-number) *ipv4-address* **as-number** *as-number*
       
       
       
       The Level 1 carrier PE is configured as an EBGP peer.
   11. Run [**peer**](cmdqueryname=peer+label-route-capability) *ipv4-address* **label-route-capability**
       
       
       
       The capability of exchanging labeled IPv4 routes is enabled.
   12. Run [**peer**](cmdqueryname=peer+route-policy+export) *ipv4-address* **route-policy** *route-policy-name* **export**
       
       
       
       The function to allocate labels to routes to be advertised to the Level 1 carrier PE is enabled.
   13. (Optional) Run [**peer**](cmdqueryname=peer+allow-as-loop) *ip-address* **allow-as-loop** [ *number* ]
       
       
       
       Routing loops are permitted.
       
       
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       Perform this step if the Level 1 and Level 2 carriers belong to different ASs but Level 2 carriers belong to the same AS.
   14. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.