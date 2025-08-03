Configuring Level 1 Carrier CEs to Access Level 1 Carrier PEs (Using LDP Multi-Instance)
========================================================================================

If the Level 1 and Level 2 carriers are in the same AS, the Level 1 carrier takes the Level 2 carrier as its VPN user.

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
   6. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ] **evpn**
      
      
      
      VPN targets are configured for EVPN routes in the VPN instance IPv4 address family.
   7. Run [**evpn mpls routing-enable**](cmdqueryname=evpn+mpls+routing-enable)
      
      
      
      EVPN is enabled to generate and advertise IP prefix routes and IRB routes.
      
      
      
      In an EVPN L3VPN service scenario where MPLS or SR-MPLS tunnels are used as public network tunnels (including interworking scenarios), you need to run this command to enable EVPN to generate and advertise IP prefix routes and IRB routes, so that the local device can advertise IP prefix routes and IRB routes to its EVPN peers.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   9. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The view of the interface connected to the Level 1 carrier CE is displayed.
   10. Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
       
       
       
       The interface is associated with the VPN instance.
   11. Run [**commit**](cmdqueryname=commit)
       
       
       
       The configuration is committed.
2. Configure LDP multi-instance and IGP multi-instance on the Level 1 carrier PEs.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**mpls ldp**](cmdqueryname=mpls+ldp) **vpn-instance** *vpn-instance-name*
      
      
      
      LDP is enabled for the created VPN instance.
   3. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The view of the interface connected to the Level 1 carrier CE is displayed.
   5. Run [**mpls**](cmdqueryname=mpls)
      
      
      
      MPLS is enabled on the interface.
   6. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
      
      
      
      LDP is enabled on the interface.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   8. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   9. Configure an IGP between Level 1 carrier PEs and CEs.
      
      
      
      The RIP multi-instance, OSPF multi-instance, or IS-IS multi-instance can be used as an IGP on Level 1 carrier PEs. In the IGP multi-instance view, BGP routes are imported; in the BGP-VPN instance address family view, IGP routes are imported. The detailed configuration is not provided here.
3. Configure LDP and an IGP on Level 1 carrier CEs.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The view of the interface connected to the Level 1 carrier PE is displayed.
   3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
      
      
      
      An IP address is configured for the interface.
   4. Run [**mpls**](cmdqueryname=mpls)
      
      
      
      MPLS is enabled on the interface.
   5. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
      
      
      
      LDP is enabled on the interface.
   6. Run [**mpls ldp transport-address**](cmdqueryname=mpls+ldp+transport-address) **interface**
      
      
      
      The IP address of the current interface is used to set up an LDP session.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   8. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   9. Configure an IGP between Level 1 carrier CEs and PEs.
      
      
      
      RIP, OSPF, or IS-IS can be used as an IGP between Level 1 carrier CEs and PEs. The detailed configuration is not provided here.