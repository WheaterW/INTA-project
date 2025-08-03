Configuring a Device to Send Default Routes to Its Peer
=======================================================

After a device is configured to send a default route to its peer, the device sends a default route with the local address as the next hop address to the specified peer, regardless of whether there are default routes in the local routing table, which reduces the number of routes on the network.

#### Usage Scenario

The BGP routing table of the Router on a medium or large BGP network contains a large number of routing entries. Storing the routing table consumes a large number of memory resources, and transmitting and processing routing information consume lots of network resources. If a device needs to send multiple routes to its peer, you can configure the device to send only a default route with the local address as the next hop address to its peer, regardless of whether there are default routes in the local routing table. This greatly reduces the number of routes on the network and the consumption of memory resources on the peer and network resources.

**Figure 1** Configuring a device to send a default route to its peer  
![](images/fig_dc_vrp_bgp_cfg_305201.png)

On the network shown in [Figure 1](#EN-US_TASK_0172366229__fig_dc_vrp_bgp_cfg_305201), Device A and Device B have established a BGP peer relationship. Device B has added routes to 10.1.1.0/24, 10.2.1.0/24, and 10.3.1.0/24 to its BGP routing table. Device A needs to learn these routes from Device B. In this way, Device A retains three BGP routes. To reduce the memory consumption on Device A and bandwidth used by Device B for sending routing information to Device A, configure Device B to send a default route to its peer (Device A) and use a routing policy to prevent Device B from sending all the routes to 10.1.1.0/24, 10.2.1.0/24, and 10.3.1.0/24 to Device A. Then, Device A stores only one default route but can still send traffic to the three network segments.


#### Pre-configuration Tasks

Before configuring a BGP device to send a default route to its peer, [configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
   
   
   
   The IPv4 unicast address family view is displayed.
4. Run [**peer**](cmdqueryname=peer+default-route-advertise+route-policy) { *group-name* | *ipv4-address* } **default-route-advertise** [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ] [ **conditional-route-match-all** { *ipv4-address1* { *mask1* | *mask-length1* } } &<1-4> | **conditional-route-match-any** { *ipv4-address2* { *mask2* | *mask-length2* } } &<1-4> ]
   
   
   
   The device is configured to send default routes to the specified peer or a peer group.
   
   
   
   You can specify **route-policy** *route-policy-name* or **route-filter** *route-filter-name* to change attributes of the default routes to be advertised.
   
   If **conditional-route-match-all** { *ipv4-address1* { *mask1* | *mask-length1* } } &<1-4> is set, the BGP device sends default routes to the peer only when routes that match all the all specified conditions exist in the local IP routing table.
   
   If **conditional-route-match-any** { *ipv4-address2* { *mask2* | *mask-length2* } } &<1-4> is set, the local device sends default routes to the peer when routes that match any of the specified conditions exist in the local IP routing table.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the [**peer default-route-advertise**](cmdqueryname=peer+default-route-advertise) command is used on a device, the device sends a default route with the local address as the next-hop address to a specified peer, regardless of whether there is a default route in the routing table.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, you can run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) [ *ipv4-address* [ *mask* | *mask-length* ] ] command on the peer to view the received BGP default route.