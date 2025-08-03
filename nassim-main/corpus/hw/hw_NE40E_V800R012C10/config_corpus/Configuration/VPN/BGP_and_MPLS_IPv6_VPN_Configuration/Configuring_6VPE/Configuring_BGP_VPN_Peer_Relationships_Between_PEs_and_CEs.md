Configuring BGP VPN Peer Relationships Between PEs and CEs
==========================================================

In a 6VPE scenario, BGP VPN peer relationships must be configured between PEs and CEs to allow them to communicate.

#### Context

In the 6VPE scenario, a routing protocol must be configured between each pair of a PE and a CE to allow them to communicate and to allow the CE to obtain routes from other CEs. Choose one of the following configurations as needed:

* [Configure BGP VPN peer relationships between PEs and CEs (IP forwarding).](#EN-US_TASK_0172369602__cmd335474236214051)
* [Configure IBGP VPN peer relationships between PEs and CEs (tunnel forwarding).](#EN-US_TASK_0172369602__cmd471704394214051)
* [Configure direct EBGP VPN peer relationships between PEs and CEs (tunnel forwarding).](#EN-US_TASK_0172369602__cmd697691121214051)
* [Configure indirect EBGP VPN peer relationships between PEs and CEs (tunnel forwarding).](#EN-US_TASK_0172369602__cmd678516251214051)

If you want to use IP forwarding between PEs and CEs, be sure to configure IPv4 and IPv6 addresses on link interfaces between PEs and CEs.

The routing protocol configurations on CEs and PEs are different:

* A CE is located at the client side and unaware of the VPN. Therefore, you do not need to configure VPN parameters when configuring a routing protocol on the CE.
* A PE is located at the edge of the carrier's network. It connects to a CE and exchanges VPN routing information with other PEs. If the CEs that access a PE belong to different VPNs, the PE must maintain different VRF tables. When configuring a routing protocol on the PE, specify the name of the VPN instance to which the routing protocol applies and configure the routing protocol and MP-BGP to import routes from each other.


#### Procedure

* Configure BGP VPN peer relationships between PEs and CEs (IP forwarding).
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Before configuring BGP VPN peer relationships between PEs and CEs, configure IPv6 addresses for interfaces connecting PEs to CEs.
  
  
  
  Perform the following steps on a PE:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **permit** | **deny** } **node** *node*
     
     
     
     A route-policy node is created, and the route-policy view is displayed.
  3. (Optional) Configure if-match clauses to filter routes transmitted between sites. For configuration details, see [(Optional) Configuring an if-match Clause](dc_vrp_route-policy_cfg_0009.html).
  4. Run [**apply ipv6 next-hop**](cmdqueryname=apply+ipv6+next-hop) *address*
     
     
     
     The next hop of the route is changed and *ipv6-address* is set to the IPv6 address of the PE interface that connects to a CE.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the previous view.
  6. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  7. Run [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name*
     
     
     
     A BGP VPN instance is created, and its view is displayed.
  8. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
     
     
     
     The CE is configured as a BGP VPN peer.
  9. (Optional) Run [**peer**](cmdqueryname=peer) *ipv4-address* [**connect-interface**](cmdqueryname=connect-interface) *interface-type* *interface-number* [ *ipv4-source-address* ]
     
     
     
     The source interface and source address are specified for establishing a TCP connection between BGP peers.
  10. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the previous view.
  11. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
      
      
      
      The BGP-VPN instance IPv6 address family view is displayed.
  12. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
      
      
      
      The device is enabled to exchange BGP route information with a specified BGP IPv4 peer (group).
  13. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *route-policy-name* **export**
      
      
      
      An export route-policy is applied.
  14. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the previous view.
  15. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
  
  
  
  Perform the following steps on a CE:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**route-policy**](cmdqueryname=route-policy) *route-policy-name* { **permit** | **deny** } **node** *node*
     
     
     
     A route-policy node is created, and the route-policy view is displayed.
  3. (Optional) Configure if-match clauses to filter routes transmitted between sites. For configuration details, see [(Optional) Configuring an if-match Clause](dc_vrp_route-policy_cfg_0009.html).
  4. Run [**apply ipv6 next-hop**](cmdqueryname=apply+ipv6+next-hop) *address*
     
     
     
     The next hop of the route is changed and *ipv6-address* is set to the IPv6 address of the CE interface that connects to a PE.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the previous view.
  6. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  7. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
     
     
     
     A BGP peer is configured.
  8. (Optional) Run [**peer**](cmdqueryname=peer) *ipv4-address* [**connect-interface**](cmdqueryname=connect-interface) *interface-type* *interface-number* [ *ipv4-source-address* ]
     
     
     
     The source interface and source address are specified for establishing a TCP connection between BGP peers.
  9. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     
     
     The BGP-IPv6 unicast address family view is displayed.
  10. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
      
      
      
      The BGP IPv4 peer is enabled.
  11. Run [**peer**](cmdqueryname=peer) *ipv4-address* **route-policy** *route-policy-name* **export**
      
      
      
      An export route-policy is applied.
  12. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure IBGP VPN peer relationships between PEs and CEs (tunnel forwarding).
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Before configuring IBGP VPN peer relationships between PEs and CEs (tunnel forwarding), configure a VPN IGP or VPN static routes on PEs and CEs. To implement communication between PEs and CEs, see [Configuring Route Exchange Between PEs and CEs](dc_vrp_mpls-l3vpn-v4_cfg_0158.html).
  
  
  
  Perform the following steps on a PE:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls lsr-id**](cmdqueryname=mpls+lsr-id) *lsr-id*
     
     
     
     An LSR ID is set.
     
     When setting an LSR ID, note the following:
     + Setting an LSR ID is the prerequisite of all MPLS configurations.
     + An LSR ID must be manually configured because no default LSR ID is available.
     + It is advised to use the IP address of a loopback interface on an LSR as the LSR ID.
  3. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     MPLS is enabled globally.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the previous view.
  5. Run [**mpls ldp**](cmdqueryname=mpls+ldp) **vpn-instance** *vpn-instance-name*
     
     
     
     LDP is enabled for a specified VPN instance, and the MPLS LDP VPN instance view is displayed.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the previous view.
  7. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface connecting to the CE is displayed.
  8. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     MPLS is enabled.
  9. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     MPLS LDP is enabled.
  10. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the previous view.
  11. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
  12. Run [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name*
      
      
      
      A BGP VPN instance is created, and its view is displayed.
  13. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
      
      
      
      The CE is configured as a VPN peer.
  14. Run [**peer**](cmdqueryname=peer) *ipv4-address* [**connect-interface**](cmdqueryname=connect-interface) *interface-type* *interface-number* [ *ipv4-source-address* ]
      
      
      
      The source interface and source address are specified for establishing a TCP connection between BGP peers.
  15. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the previous view.
  16. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
      
      
      
      The BGP-VPN instance IPv6 address family view is displayed.
  17. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
      
      
      
      The device is enabled to exchange BGP route information with a specified BGP IPv4 peer (group).
  18. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
      
      
      
      The device is configured to exchange labeled IPv4 routes with CEs.
  19. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the previous view.
  20. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
  
  
  
  Perform the following steps on a CE:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls lsr-id**](cmdqueryname=mpls+lsr-id) *lsr-id*
     
     
     
     An LSR ID is set.
     
     When setting an LSR ID, note the following:
     + Setting an LSR ID is the prerequisite of all MPLS configurations.
     + An LSR ID must be manually configured because no default LSR ID is available.
     + It is advised to use the IP address of a loopback interface on an LSR as the LSR ID.
  3. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     MPLS is enabled globally.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the previous view.
  5. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     MPLS LDP is enabled globally.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the previous view.
  7. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface connecting to the PE is displayed.
  8. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     MPLS is enabled.
  9. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     MPLS LDP is enabled.
  10. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the previous view.
  11. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
  12. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
      
      
      
      A BGP peer is configured.
  13. Run [**peer**](cmdqueryname=peer) *ipv4-address* [**connect-interface**](cmdqueryname=connect-interface) *interface-type* *interface-number* [ *ipv4-source-address* ]
      
      
      
      The source interface and source address are specified for establishing a TCP connection.
  14. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
      
      
      
      The BGP-IPv6 unicast address family view is displayed.
  15. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
      
      
      
      The device is enabled to exchange BGP route information with a specified BGP IPv4 peer.
  16. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
      
      
      
      The device is configured to exchange labeled IPv4 routes with PEs.
  17. Run [**unicast-route recursive-lookup tunnel-v4**](cmdqueryname=unicast-route+recursive-lookup+tunnel-v4) [ **tunnel-selector** *tunnel-selector-name* ]
      
      
      
      The device is enabled to recurse BGP IPv6 unicast routes to tunnels.
  18. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure direct EBGP VPN peer relationships between PEs and CEs (tunnel forwarding).
  
  
  
  Perform the following steps on a PE:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls lsr-id**](cmdqueryname=mpls+lsr-id) *lsr-id*
     
     
     
     An LSR ID is set.
     
     When setting an LSR ID, note the following:
     + Setting an LSR ID is the prerequisite of all MPLS configurations.
     + An LSR ID must be manually configured because no default LSR ID is available.
     + It is advised to use the IP address of a loopback interface on an LSR as the LSR ID.
  3. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     MPLS is enabled globally.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the previous view.
  5. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface connecting to the CE is displayed.
  6. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     MPLS is enabled.
  7. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the previous view.
  8. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  9. Run [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name*
     
     
     
     A BGP VPN instance is created, and its view is displayed.
  10. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
      
      
      
      The CE is configured as a VPN peer.
  11. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **ebgp-max-hop** [ *hop-count* ]
      
      
      
      The maximum number of hops allowed for an EBGP connection is configured.
  12. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the previous view.
  13. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
      
      
      
      The BGP-VPN instance IPv6 address family view is displayed.
  14. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
      
      
      
      The device is enabled to exchange BGP route information with a specified BGP IPv4 peer.
  15. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
      
      
      
      The device is configured to exchange labeled IPv4 routes with CEs.
  16. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the previous view.
  17. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
  
  
  
  Perform the following steps on a CE:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls lsr-id**](cmdqueryname=mpls+lsr-id) *lsr-id*
     
     
     
     An LSR ID is set.
     
     When setting an LSR ID, note the following:
     + Setting an LSR ID is the prerequisite of all MPLS configurations.
     + An LSR ID must be manually configured because no default LSR ID is available.
     + It is advised to use the IP address of a loopback interface on an LSR as the LSR ID.
  3. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     MPLS is enabled globally.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the previous view.
  5. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface connecting to the PE is displayed.
  6. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     MPLS is enabled.
  7. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the previous view.
  8. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  9. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
     
     
     
     A BGP peer is configured.
  10. Run [**peer**](cmdqueryname=peer) *ipv4-address* **ebgp-max-hop** [ *hop-count* ]
      
      
      
      The maximum number of hops allowed for an EBGP connection is configured.
  11. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
      
      
      
      The BGP-IPv6 unicast address family view is displayed.
  12. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
      
      
      
      The device is enabled to exchange BGP route information with a specified BGP IPv4 peer.
  13. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
      
      
      
      The device is configured to exchange labeled IPv4 routes with PEs.
  14. Run [**unicast-route recursive-lookup tunnel-v4**](cmdqueryname=unicast-route+recursive-lookup+tunnel-v4) [ **tunnel-selector** *tunnel-selector-name* ]
      
      
      
      The device is enabled to recurse BGP IPv6 unicast routes to tunnels.
  15. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure indirect EBGP VPN peer relationships between PEs and CEs (tunnel forwarding).
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Before configuring indirect EBGP VPN peer relationships between PEs and CEs (tunnel forwarding), configure PEs and CEs to implement route reachability. For example, configure static routes on PEs and CEs.
  
  
  
  Perform the following steps on a PE:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls lsr-id**](cmdqueryname=mpls+lsr-id) *lsr-id*
     
     
     
     An LSR ID is set.
     
     When setting an LSR ID, note the following:
     + Setting an LSR ID is the prerequisite of all MPLS configurations.
     + An LSR ID must be manually configured because no default LSR ID is available.
     + It is advised to use the IP address of a loopback interface on an LSR as the LSR ID.
  3. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     MPLS is enabled globally.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the previous view.
  5. Run [**mpls ldp**](cmdqueryname=mpls+ldp) **vpn-instance** *vpn-instance-name*
     
     
     
     LDP is enabled for a specified VPN instance, and the MPLS LDP VPN instance view is displayed.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the previous view.
  7. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface connecting to the CE is displayed.
  8. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     MPLS is enabled.
  9. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     MPLS LDP is enabled.
  10. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the previous view.
  11. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
  12. Run [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name*
      
      
      
      A BGP VPN instance is created, and its view is displayed.
  13. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
      
      
      
      The CE is configured as a VPN peer.
  14. Run [**peer**](cmdqueryname=peer) *ipv4-address* **ebgp-max-hop** [ *hop-count* ]
      
      
      
      The maximum number of hops allowed for an EBGP connection is configured.
  15. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the previous view.
  16. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
      
      
      
      The BGP-VPN instance IPv6 address family view is displayed.
  17. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
      
      
      
      The device is enabled to exchange BGP route information with a specified BGP IPv4 peer.
  18. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
      
      
      
      The device is configured to exchange labeled IPv4 routes with CEs.
  19. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the previous view.
  20. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
  
  
  
  Perform the following steps on the CE:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls lsr-id**](cmdqueryname=mpls+lsr-id) *lsr-id*
     
     
     
     An LSR ID is set.
     
     When setting an LSR ID, note the following:
     + Setting an LSR ID is the prerequisite of all MPLS configurations.
     + An LSR ID must be manually configured because no default LSR ID is available.
     + It is advised to use the IP address of a loopback interface on an LSR as the LSR ID.
  3. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     MPLS is enabled globally.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the previous view.
  5. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     MPLS LDP is enabled globally.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the previous view.
  7. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface connecting to the PE is displayed.
  8. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     MPLS is enabled.
  9. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
     
     
     
     MPLS LDP is enabled.
  10. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the previous view.
  11. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
  12. Run [**peer**](cmdqueryname=peer) *ipv4-address* **as-number** *as-number*
      
      
      
      A BGP peer is configured.
  13. Run [**peer**](cmdqueryname=peer) *ipv4-address* **ebgp-max-hop** [ *hop-count* ]
      
      
      
      The maximum number of hops allowed for an EBGP connection is configured.
  14. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
      
      
      
      The BGP-IPv6 unicast address family view is displayed.
  15. Run [**peer**](cmdqueryname=peer) *ipv4-address* **enable**
      
      
      
      The device is enabled to exchange BGP route information with a specified BGP IPv4 peer.
  16. Run [**peer**](cmdqueryname=peer) *ipv4-address* **label-route-capability**
      
      
      
      The device is configured to exchange labeled IPv4 routes with PEs.
  17. Run [**unicast-route recursive-lookup tunnel-v4**](cmdqueryname=unicast-route+recursive-lookup+tunnel-v4) [ **tunnel-selector** *tunnel-selector-name* ]
      
      
      
      The device is enabled to recurse BGP IPv6 unicast routes to tunnels.
  18. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.