Configuring Level 1 Carrier CE to Access the Level 1 Carrier PE (Intra-AS)
==========================================================================

If the Level 1 carrier and the Level 2 carrier are in the same AS, the Level 1 carrier takes the Level 2 carrier as its VPN user. The configuration of carrier's carrier is similar to the configuration of CE accessing PE in the basic BGP/MPLS IP VPN.

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
     
     
     
     Each route is allocated a label.
  6. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ]
     
     
     
     One or multiple VPN targets are configured for the VPN instance IPv4 address family.
  7. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  8. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface connected to the Level 1 carrier CE is displayed.
  9. Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
     
     
     
     The interface is bound to the VPN instance.
  10. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
      
      
      
      An IP address is configured for the interface.
  11. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure LDP and an IGP on the Level 1 carrier PE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls ldp**](cmdqueryname=mpls+ldp) **vpn-instance** *vpn-instance-name*
     
     
     
     LDP is enabled for the created VPN instance.
  3. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of interface connected to the Level 1 carrier CE is displayed.
  5. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     MPLS is enabled on the interface.
  6. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     LDP is enabled on the interface.
  7. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  8. Configure an IGP between the Level 1 carrier PE and the Level 1 carrier CE.
     
     
     
     The RIP multi-instance, the OSPF multi-instance or the IS-IS multi-instance can be used on PE as an IGP between the PE and the Level 1 carrier CE. In the IGP multi-instance view, BGP routes are imported; in the BGP-VPN instance view, IGP routes are imported. The detailed configuration is not mentioned here.
* Configure LDP and an IGP on the Level 1 carrier CE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of interface connected to the Level 1 carrier PE is displayed.
  3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
     
     
     
     An IPv4 address is configured for the interface.
  4. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     MPLS is enabled on the interface.
  5. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     LDP is enabled on the interface.
  6. (Optional) Run [**mpls ldp transport-address**](cmdqueryname=mpls+ldp+transport-address) **interface**
     
     
     
     The IP address of the current interface is used to establish an LDP session.
     
     If the interface is not bound to a VPN instance, by default, the LSR ID is used as the transport address for the local LDP session.
     
     The transport address is used to establish a TCP connection between the local node and its peer. The peer must have a reachable route to this transport address. The default transport address is the loopback interface address (an LSR ID). When the address of the loopback interface is a public network address, configure different transport addresses for LSRs so that LSRs can set up connections to private network addresses.
  7. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  8. Configure an IGP between the Level 1 carrier CE and the Level 1 carrier PE.
     
     
     
     RIP, OSPF or IS-IS can be used on the CE as an IGP between the CE and the Level 1 carrier PE. The detailed configuration is not mentioned here.