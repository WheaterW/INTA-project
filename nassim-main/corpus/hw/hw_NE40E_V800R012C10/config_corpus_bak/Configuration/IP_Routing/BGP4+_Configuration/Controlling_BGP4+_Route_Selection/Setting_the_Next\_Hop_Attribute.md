Setting the Next\_Hop Attribute
===============================

BGP4+ route selection can be flexibly controlled by setting the Next\_Hop attribute.

#### Context

The Next\_Hop attribute of BGP4+ is different from that of an IGP because it is not necessarily the IPv6 address of a neighboring Router.


#### Procedure

* Change the next-hop address when advertising a route to an IBGP peer.
  
  
  
  Perform the following steps on the IBGP Router:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     
     
     The IPv6 unicast address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } [**next-hop-local**](cmdqueryname=next-hop-local)
     
     
     
     The device is configured to use its own IP address as the next-hop address of the routes when advertising them.
     
     
     
     To ensure that an IBGP peer can find the correct next hop, you can configure the local device to use its own address as the next-hop address of each route when the local device advertises routes to the IBGP peer.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If BGP load balancing is configured, the local Router changes the next-hop address of a route to its own IP address when advertising the route to an IBGP peer, regardless of whether the [**peer next-hop-local**](cmdqueryname=peer+next-hop-local) command is run.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a device to retain the original Next\_Hop of imported IGP routes when the device advertises the routes to an IBGP peer.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     
     
     The IPv6 unicast address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer+next-hop-invariable+include-static-route) { *peerIpv6Addr* | *peerGroupName* } **next-hop-invariable** [ ****include-static-route**** | ****include-unicast-route**** ] \*
     
     
     
     The device is configured not to change the next hop address of an imported IGP route when advertising the route.
     
     
     
     If the **peer next-hop-invariable include-static-route** command is run, the BGP speaker retains the original next hop address of an imported public network static route when advertising the route to an IBGP peer under the condition that the original next hop address is valid; if the original next hop address of the static route is invalid, the public network static route recurses to a VPN route, or the public network static route is imported from a VPN instance, the BGP speaker uses its interface address as the next hop of the route.
     
     If the **peer next-hop-invariable include-unicast-route** command is run, the BGP speaker does not change the next hop address when advertising to an EBGP peer the unicast routes learned from another peer.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Prevent an ASBR from changing the next hop address when advertising routes to an EBGP peer.
  
  
  
  Perform the following steps on a PE:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpnv6** [ **unicast** ]
     
     
     
     The BGP-VPNv6 unicast address family view is displayed.
  4. Run the [**peer**](cmdqueryname=peer) { *ipv6-address* | *group-name* } [**next-hop-invariable**](cmdqueryname=next-hop-invariable) command to configure the device not to change the next hop when advertising routes to the specified EBGP peer. Alternatively, run the [**peer**](cmdqueryname=peer+next-hop-invariable+include-static-route) { *ipv6-address* | *group-name* } **next-hop-invariable** [ **include-static-route** | **include-unicast-route** ] \* command.
     
     
     
     If the **peer next-hop-invariable include-static-route** command is run, the BGP speaker retains the original next hop address of an imported static route when it advertises the static route to the specified IBGP peer. However, the local interface address is used as the next hop in the following situations: (1) The imported static route is a public network static route, and its original next hop is invalid. (2) The imported static route is a public network static route, and its original next hop recurses to a VPN route. (3) The imported static route is a VPN static route and is imported from the public network instance.
     
     If the **peer next-hop-invariable include-unicast-route** command is run, the BGP speaker does not change the next hop address when advertising to an EBGP peer the unicast routes learned from another peer.
     
     
     
     On the network shown in [Figure 1](#EN-US_TASK_0172366446__fig434343516016), a BGP LSP is established between PE1 and PE2. VPNv6 routes are exchanged between PE1 and RR1, between RR1 and RR2, and between RR2 and PE2 through BGP VPNv6 peer relationships.**Figure 1** Inter-AS VPN Option C networking with RRs deployed  
     ![](figure/en-us_image_0000001402412029.png)
     
     Assume that PE1 needs to advertise a VPNv6 route to PE2. The route will be advertised through the following process:
     1. PE1 advertises the route to RR1, with the route next hop being PE1.
     2. Upon receipt, RR1 changes the route next hop to itself and then advertises the route to RR2 through the EBGP peer relationship.
     3. RR2 advertises the received route to its IBGP peer PE2. By default, the Router changes the next hop of a labeled route received from an EBGP peer before advertising the route to an IBGP peer. Therefore, RR2 changes the next hop of the route to itself before advertising the route to PE2.The next hop of the VPNv6 route received by PE2 is RR2. However, the destination of the BGP LSP is PE1. As a result, the VPNv6 route on PE2 cannot recurse to the BGP LSP, causing traffic interruption.
     
     To solve the preceding problem, run the [**peer next-hop-invariable**](cmdqueryname=peer+next-hop-invariable) command on RR1 to ensure that RR1 does not change the next hop address when advertising routes to RR2. In addition, run the [**peer next-hop-invariable**](cmdqueryname=peer+next-hop-invariable) command on RR2 to ensure that the next hop of the route advertised by RR2 to PE2 is not changed. In this way, the next hop of the VPNv6 route received by PE2 is PE1, and the route can recurse to the BGP LSP.
     
     Similar to the preceding process, if PE2 also attempts to advertise a VPNv6 route to PE1, run the [**peer next-hop-invariable**](cmdqueryname=peer+next-hop-invariable) command on both RR2 and RR1 so that RR2 does not change the next hop before advertising the route to RR1 and RR1 does not change the next hop before advertising the route to PE1. In this way, the VPNv6 route received by PE1 is PE2, and the route can recurse to the BGP LSP.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure route-policy-based next hop recursion.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     
     
     The IPv6 unicast address family view is displayed.
  4. Run [**nexthop recursive-lookup**](cmdqueryname=nexthop+recursive-lookup+route-policy) { **route-policy** *route-policy-name* | **route-filter** *route-filter-name* }
     
     
     
     Route-policy-based next hop recursion is configured.
     
     
     
     Next-hop recursion based on a specified route-policy can control the recursive next hop based on specific conditions. If a route fails to match the specified route-policy, the route recursion fails.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Prevent the device from changing the next hop address of a route to ensure that traffic is transmitted along the optimal route when the device advertises the route to a peer in the following scenarios:
  
  
  + The route is learned from a directly connected peer and is to be advertised to a directly connected EBGP peer, the original next hop of the route resides on the same network segment as the local interface that is used to establish the BGP4+ peer relationship with the EBGP peer, and directly connected interfaces are broadcast interfaces.
  + The route is locally imported and is to be advertised to a directly connected IBGP or EBGP peer, the next hop to which the route recurses resides on the same network segment as the local interface that is used to establish the BGP4+ peer relationship with the IBGP or EBGP peer, and directly connected interfaces are broadcast interfaces.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     
     
     The IPv6 unicast address family view is displayed.
  4. Run [**nexthop third-party**](cmdqueryname=nexthop+third-party)
     
     
     
     The device is prevented from changing the next hop address of a route when the device advertises the route to a peer in the specified scenarios.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.