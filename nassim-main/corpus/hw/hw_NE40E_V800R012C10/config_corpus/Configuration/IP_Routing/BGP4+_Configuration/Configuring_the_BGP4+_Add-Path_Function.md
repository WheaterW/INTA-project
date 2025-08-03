Configuring the BGP4+ Add-Path Function
=======================================

BGP4+ Add-Path allows a device to send multiple routes with the same prefix to a specified IBGP peer. These routes can back up each other or load-balance traffic, which improves network reliability.

#### Usage Scenario

In a scenario with a route reflector (RR) and clients, if the RR has multiple routes to the same destination (with the same prefix), the RR selects an optimal route from these routes according to BGP4+ route selection rules and then sends only the optimal route to its clients. Therefore, the clients have only one route to the destination. If a link along this route fails, route convergence takes a long time, which cannot meet the requirements for high reliability.

To address this issue, deploy BGP4+ Add-Path on the RR. With BGP4+ Add-Path, the RR can send two or more routes with the same prefix to a specified peer. These routes can back up each other or load-balance traffic, which ensures high reliability in data transmission. The BGP4+ Add-Path feature does not affect BGP4+ route selection rules.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Add-Path takes effect only for routes learned from peers, not for local routes.

If BGP4+ Add-Path is enabled and the device is also configured to change the next hops of the routes to be advertised to the local address, a routing loop may occur.



#### Pre-configuration Tasks

Before configuring the BGP4+ Add-Path function, complete the following task:

* [Configure basic BGP4+ functions](dc_vrp_bgp6_cfg_0003.html).

#### Procedure

* Perform the following steps on a device that needs to send Add-Path routes:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. (Optional) Run [**route-policy**](cmdqueryname=route-policy+node) *route-policy-name* *matchMode* **node** *node*
     
     
     
     A route-policy is created, and the route-policy view is displayed.
  3. (Optional) Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. (Optional) Run [**xpl route-filter**](cmdqueryname=xpl+route-filter) *route-filter-name*
     
     
     
     A route-filter is created, and the route-filter view is displayed.
  5. (Optional) Run [**end-filter**](cmdqueryname=end-filter)
     
     
     
     Return to the system view.
  6. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  7. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *peerGroupName* } [**as-number**](cmdqueryname=as-number) *as-number*
     
     
     
     An IP address and AS number are specified for a peer.
  8. Run [**ipv6-family**](cmdqueryname=ipv6-family+unicast) **unicast**
     
     
     
     The IPv6 unicast address family view is displayed.
  9. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } [**enable**](cmdqueryname=enable)
     
     
     
     The IPv6 peer is enabled.
  10. Run [**bestroute add-path**](cmdqueryname=bestroute+add-path+path-number) **path-number** *path-number*
      
      
      
      BGP Add-Path is enabled, and the number of preferred routes is specified.
  11. Run [**peer**](cmdqueryname=peer+capability-advertise+add-path+send) { *ipv4-address* | *ipv6-address* | *group-name* } **capability-advertise** **add-path** **send**
      
      
      
      The device is enabled to send Add-Path routes to the specified peer.
  12. Run [**peer**](cmdqueryname=peer+advertise+add-path+path-number+route-policy+route-filter) { *peerIpv4Addr* | *peerIpv6Addr* | *groupName* } **advertise add-path path-number** *number* { **route-policy** *route-policy-name* | **route-filter** *route-filter-name* }
      
      
      
      The maximum number of preferred routes to be advertised to a specified peer is specified.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      To configure **route-policy** *route-policy-name*, you need to enter the route-policy view.
      
      To configure **route-filter** *route-filter-name*, you need to enter the route-filter view.
  13. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Perform the following steps on a device that needs to accept Add-Path routes:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     
     
     The IPv6 unicast address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer+capability-advertise+add-path+receive) { *ipv4-address* | *ipv6-address* | *group-name* } **capability-advertise** **add-path** **receive**
     
     
     
     The device is enabled to accept the Add-Path routes received from the specified peer.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After completing the configurations, check the configurations on the device that advertises Add-Path routes.

Run the [**display bgp peer**](cmdqueryname=display+bgp+peer+verbose) **verbose** command to check the status of BGP4+ Add-Path.