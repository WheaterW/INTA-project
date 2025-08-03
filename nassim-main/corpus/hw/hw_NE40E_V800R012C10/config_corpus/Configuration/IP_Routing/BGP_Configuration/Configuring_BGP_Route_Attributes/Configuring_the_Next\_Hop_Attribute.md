Configuring the Next\_Hop Attribute
===================================

Configuring the Next\_Hop attribute allows for flexible control of BGP route selection.

#### Procedure

* Configure the device to change the next hop address of a route when the device advertises the route to an IBGP peer.
  
  
  
  When an ASBR learns a route from an EBGP peer and forwards the route to IBGP peers, the ASBR does not change the next hop of the route by default. However, the next hop of the route sent by the EBGP peer is the peer address of the EBGP peer. After the IBGP peers in the AS to which the local peer belongs receive the route, the route is inactive because its next hop is unreachable. To address this problem, configure the ASBR to change the next hop of the route learned from an EBGP peer to the ASBR's own address before the ASBR advertises the route to an IBGP peer. As an IGP runs within the AS, the next hop of the route is reachable to the IBGP peer. As such, the route received by the IBGP peer is active.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The IPv4 unicast address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer+next-hop-local) { *ipv4-address* | *group-name* } [**next-hop-local**](cmdqueryname=peer+next-hop-local)
     
     
     
     The device is configured to change the next hop address of a route to the local address before the device advertises the route.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If BGP load balancing is configured, the local device changes the next hop address of a route to the local address when advertising the route to an IBGP peer or peer group, regardless of whether the [**peer next-hop-local**](cmdqueryname=peer+next-hop-local) command is run.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a device to retain the original Next\_Hop of imported IGP routes when the device advertises the routes to an IBGP peer.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The IPv4 unicast address family view is displayed.
  4. To configure the device not to change the next hop address of an imported IGP route when the device advertises the IGP route, run either of the following commands as required:
     
     
     
     Run the [**peer**](cmdqueryname=peer+next-hop-invariable) { *ipv4-address* | *group-name* } [**next-hop-invariable**](cmdqueryname=peer+next-hop-invariable) command to configure the device not to change the next hop address of an imported IGP route when the device advertises the route to the specified peer.
     
     Run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } [**next-hop-invariable**](cmdqueryname=peer+next-hop-invariable) **include-static-route** command to configure the BGP speaker to retain the original next hop address of an imported static route when it advertises the static route to the specified IBGP peer. However, the local interface address is used as the next hop in the following situations: (1) The imported static route is a public network static route, and its original next hop is invalid. (2) The imported static route is a public network static route, and its original next hop recurses to a VPN route. (3) The imported static route is a VPN static route and is imported from the public network instance.
     
     Run the [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } [**next-hop-invariable**](cmdqueryname=peer+next-hop-invariable) **include-unicast-route** command to configure the BGP speaker not to change the next hop address when advertising a unicast route learned from a peer to the specified EBGP peer.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Prevent an ASBR from changing the next hop address of a route when the ASBR advertises the route to an EBGP peer.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+vpnv4+unicast) **vpnv4** [ **unicast** ]
     
     
     
     The BGP-VPNv4 address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer+next-hop-invariable) { *group-name* | *ipv4-address* } [**next-hop-invariable**](cmdqueryname=peer+next-hop-invariable)
     
     
     
     The device is configured not to change the next hop address of a route before the device advertises the route to an EBGP peer.
     
     
     
     In an inter-AS VPN Option C scenario where an RR is deployed, the [**peer next-hop-invariable**](cmdqueryname=peer+next-hop-invariable) command needs to be run on the RR to prevent the RR from changing the next hop address of a route before the RR advertises the route to an EBGP peer. This ensures that the remote PE forwards traffic through the BGP LSP destined for the local PE.
     
     On the network shown in [Figure 1](#EN-US_TASK_0172366170__fig_peer_next-hop-invariable), a BGP LSP is established between PE1 and PE2. VPNv4 routes are exchanged through BGP-VPNv4 peer relationships established between PE1 and RR1, between RR1 and RR2, and between RR2 and PE2.**Figure 1** Inter-AS VPN Option C networking with RRs deployed  
     ![](figure/en-us_image_0206849170.png)
     
     If PE1 needs to advertise a VPNv4 route to PE2, the following process is implemented:
     1. PE1 advertises the route to RR1, and the route next hop is PE1.
     2. Upon receipt, RR1 changes the route next hop to itself and then advertises the route to RR2 through the EBGP peer relationship.
     3. RR2 advertises the received route to its IBGP peer PE2. By default, the Router changes the next hop address of a labeled route received from an EBGP peer before advertising the labeled route to an IBGP peer. Therefore, RR2 changes the next hop address of the route to its own address before advertising the route to PE2.The next hop of the VPNv4 route received by PE2 is RR2. However, the destination of the BGP LSP is PE1. As a result, the VPNv4 route on PE2 cannot recurse to the BGP LSP, causing traffic interruption.
     
     To solve the preceding problem, run the [**peer next-hop-invariable**](cmdqueryname=peer+next-hop-invariable) command on RR1 to ensure that RR1 does not change the next hop address when advertising routes to RR2. In addition, run the [**peer next-hop-invariable**](cmdqueryname=peer+next-hop-invariable) command on RR2 to ensure that the next hop of the route advertised by RR2 to PE2 is not changed. In this way, the next hop of the route received by PE2 is PE1, and the VPNv4 route on PE2 can recurse to the BGP LSP properly.
     
     Similar to the preceding process, if PE2 also attempts to advertise a VPNv4 route to PE1, run the [**peer next-hop-invariable**](cmdqueryname=peer+next-hop-invariable) command on both RR2 and RR1 so that RR2 does not change the next hop before advertising the route to RR1 and RR1 does not change the next hop before advertising the route to PE1. In this way, the next hop of the route received by PE1 is PE2, and the VPNv4 route on PE1 can recurse to the BGP LSP properly.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure route-policy-based next hop recursion.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The IPv4 unicast address family view is displayed.
  4. Run [**nexthop recursive-lookup**](cmdqueryname=nexthop+recursive-lookup+route-policy) { **route-policy** *route-policy-name* | **route-filter** *route-filter-name* }
     
     
     
     Route-policy-based next hop recursion is configured.
     
     
     
     Route-policy-based next hop recursion helps flexibly control the recursion result based on specific conditions. If a route does not match the specified route-policy, the route fails to recurse.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Prevent the device from changing the next hop address of a route to ensure that traffic is transmitted along the optimal route when the device advertises the route to a peer in the following scenarios:
  
  
  + The route is learned from a directly connected peer and is to be advertised to a directly connected EBGP peer, the original next hop of the route resides on the same network segment as the local interface that is used to establish the BGP peer relationship with the EBGP peer, and all directly connected interfaces are broadcast interfaces.
  + The route is locally imported and is to be advertised to a directly connected IBGP or EBGP peer, the next hop to which the route recurses resides on the same network segment as the local interface that is used to establish the BGP peer relationship with the peer end, and all directly connected interfaces are broadcast interfaces.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The IPv4 unicast address family view is displayed.
  4. Run [**nexthop third-party**](cmdqueryname=nexthop+third-party)
     
     
     
     The device is prevented from changing the next hop address of a route when the device advertises the route to a peer in the specified scenarios.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  On the network shown in [Figure 2](#EN-US_TASK_0172366170__fig_nexthop_third-party), DeviceA establishes EBGP peer relationships with DeviceB and DeviceC. DeviceB and DeviceC do not establish a peer relationship with each other.**Figure 2** Network diagram of Layer 2 transparent transmission  
  ![](figure/en-us_image_0206817756.png)
  
  Assume that DeviceA receives an EBGP route 1.1.1.1 from DeviceB. If the [**nexthop third-party**](cmdqueryname=nexthop+third-party) command is not run, the next hop address of the route is changed as follows:
  1. Before DeviceB advertises the route 1.1.1.1 to DeviceA, DeviceB changes the next hop to 192.168.10.1.
  2. Before DeviceA advertises the route 1.1.1.1 to DeviceC, DeviceA changes the next hop to 192.168.10.2.
  
  When traffic is transmitted from DeviceC to DeviceB, the traffic passes through DeviceA.
  
  After the [**nexthop third-party**](cmdqueryname=nexthop+third-party) command is run on DeviceA, the next hop address of the route 1.1.1.1 is changed as follows:
  1. Before DeviceB advertises the route 1.1.1.1 to DeviceA, DeviceB changes the route next hop to 192.168.10.1.
  2. Before DeviceA advertises the route to DeviceC, DeviceA detects that the address (192.168.10.2) of its local interface that is used to establish the BGP peer relationship with DeviceC belongs to the same network segment as the original next hop address 192.168.10.1 of the route. Therefore, DeviceA does not change the next hop address of the route. As a result, the next hop address of the BGP route 1.1.1.1 received by DeviceC remains 192.168.10.1.
  
  In this way, traffic from DeviceC can be directly forwarded to DeviceB, without passing through DeviceA.