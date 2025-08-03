Configuring Level 1 Carrier CEs Accessing Level 1 Carrier PEs (LDP Label Distribution, Labeled Address Family Mode)
===================================================================================================================

When the Level 1 carrier and Level 2 carrier are in different ASs, the Level 2 carrier functions as the VPN user of the Level 1 carrier, the same as the CE of the PE in the basic BGP/MPLS IP VPN.

#### Procedure

* Create a VPN instance on Level 1 carrier PEs.
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
* Configure labeled BGP on Level 1 carrier PEs.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain1* | *as-number-dot1* }
     
     
     
     The BGP view is displayed.
  3. Run [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name*
     
     
     
     A BGP-VPN instance is created, and its view is displayed.
  4. Run [**peer**](cmdqueryname=peer+as-number) *ipv4-address* **as-number** { *as-number-plain2* | *as-number-dot2* }
     
     
     
     The Level 1 carrier CE is configured as an EBGP peer in the BGP VPN instance view.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the BGP view.
  6. Run [**ipv4-family**](cmdqueryname=ipv4-family) **vpn-instance** *vpn-instance-name*
     
     
     
     The BGP-VPN instance IPv4 address family view is displayed.
  7. Run [**import-rib vpn-instance**](cmdqueryname=import-rib+vpn-instance) *vpn-instance-name* **labeled-unicast** [ **valid-route** ] { **route-policy** *route-policy-name* | **route-filter** *route-filter-name* }
     
     
     
     The function to import labeled BGP VPN routes to the BGP VPN routing table is enabled.
  8. Run [**advertise l2vpn evpn**](cmdqueryname=advertise+l2vpn+evpn)
     
     
     
     The VPN instance is configured to advertise EVPN IP prefix routes.
  9. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the BGP view.
  10. Run [**ipv4-labeled-unicast**](cmdqueryname=ipv4-labeled-unicast) **vpn-instance** *vpn-instance-name*
      
      
      
      The BGP-labeled-VPN instance IPv4 address family view is displayed.
  11. Run [**peer**](cmdqueryname=peer+enable) *ipv4-address* **enable**
      
      
      
      The BGP peer relationship is enabled in the BGP-labeled-VPN instance IPv4 address family view, enabling the Level 1 carrier PE to exchange labeled BGP routes with Level 1 carrier CE.
  12. Run [**import-rib**](cmdqueryname=import-rib) **vpn-instance** *vpn-instance-name* **include-label-route** [ **valid-route** ] [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ]
      
      
      
      The device is configured to import BGP labeled routes leaked to the VPN instance to the routing table of the BGP-labeled-VPN instance IPv4 address family.
  13. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Perform the following steps on Level 1 carrier CEs for the deployment of labeled BGP between Level 1 carrier CEs and Level 1 carrier PEs.
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
  6. Run [**bgp**](cmdqueryname=bgp) { *as-number-plain2* | *as-number-dot2* }
     
     
     
     The BGP view is displayed.
  7. Run [**peer**](cmdqueryname=peer+as-number) *ipv4-address* **as-number** { *as-number-plain1* | *as-number-dot1* }
     
     
     
     The Level 1 carrier PE is configured as an EBGP peer.
  8. Run [**import-rib public**](cmdqueryname=import-rib+public) **labeled-unicast** [ **valid-route** ] { **route-policy** *route-policy-name* }
     
     
     
     The device is configured to import BGP VPN labeled routes into the BGP public network routing table.
  9. Run [**ipv4-family labeled-unicast**](cmdqueryname=ipv4-family+labeled-unicast)
     
     
     
     The BGP-labeled address family view is displayed.
  10. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
      
      
      
      The peer relationship is enabled in the BGP-labeled address family view, enabling the Level 1 carrier CE to exchange labeled BGP routes with the Level 1 carrier PE.
  11. (Optional) Run [**peer**](cmdqueryname=peer+allow-as-loop) *ip-address* **allow-as-loop** [ *number* ]
      
      
      
      Routing loops are permitted.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      Perform this step if the Level 1 and Level 2 carriers belong to different ASs but Level 2 carriers belong to the same AS.
  12. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.