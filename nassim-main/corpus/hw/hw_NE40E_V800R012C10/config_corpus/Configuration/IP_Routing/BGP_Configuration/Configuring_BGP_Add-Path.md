Configuring BGP Add-Path
========================

BGP Add-Path allows a device to send multiple routes with the same prefix to a specified IBGP peer. These routes can back up each other or load-balance traffic, which improves network reliability.

#### Usage Scenario

In a scenario with an RR and clients, if the RR has multiple routes to the same destination (with the same prefix), the RR selects an optimal route from these routes and then sends only the optimal route to its clients. Therefore, the clients have only one route to the destination. If a link along this route fails, route convergence takes a long time, which cannot meet the requirements for high reliability.

To address this issue, deploy the BGP Add-Path feature on the RR. With BGP Add-Path, the RR can send two or more routes with the same prefix to a specified IBGP peer. These routes can back up each other or load-balance traffic, which ensures high reliability in data transmission. The BGP Add-Path feature does not affect BGP route selection rules.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Add-Path takes effect only for routes learned from peers, not for local routes.

If BGP Add-Path is enabled and the device is also configured to change the next hops of the routes to be advertised to the local address, a routing loop may occur.

Generally, BGP Add-Path is configured on an RR, and the Add-Path route receiver needs to be configured to accept such routes. In [Figure 1](#EN-US_TASK_0172366275__fig_dc_vrp_bgp_cfg_309601), you can enable BGP Add-Path on the RR, enable DeviceA to accept BGP Add-Path routes received from the RR so that DeviceA obtains two routes destined for 1.1.1.1/32, with next hops of 172.16.6.2 and 172.16.7.2. The two routes can back up each other or load-balance traffic.

**Figure 1** Networking for configuring BGP Add-Path  
![](images/fig_dc_vrp_bgp_cfg_309601.png)

#### Pre-configuration Tasks

Before configuring BGP Add-Path, [configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).


#### Procedure

* Perform the following steps on the RR that needs to advertise Add-Path routes:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. (Optional) Run [**route-policy**](cmdqueryname=route-policy+node) *route-policy-name* *matchMode* **node** *node*
     
     
     
     A route-policy is created, and the route-policy view is displayed.
  3. (Optional) Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  4. (Optional) Run [**xpl route-filter**](cmdqueryname=xpl+route-filter) *route-filter-name*
     
     
     
     A route-filter is created, and the route-filter view is displayed.
  5. (Optional) Run [**end-filter**](cmdqueryname=end-filter)
     
     
     
     The system view is displayed.
  6. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  7. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *peerGroupName* } [**as-number**](cmdqueryname=as-number) *as-number*
     
     
     
     An IP address and AS number are specified for a peer.
  8. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The IPv4 unicast address family view is displayed.
  9. Run [**bestroute add-path**](cmdqueryname=bestroute+add-path+path-number) **path-number** *path-number*
     
     
     
     BGP Add-Path is enabled, and the number of preferred routes is specified.
  10. Run [**peer**](cmdqueryname=peer+capability-advertise+add-path+send) { *ipv4-address* | *group-name* } **capability-advertise** **add-path** **send**
      
      
      
      The device is enabled to send Add-Path routes to the specified peer.
  11. Run [**peer**](cmdqueryname=peer+advertise+add-path+path-number+route-policy+route-filter) { *peerIpv4Addr* | *groupName* } **advertise add-path path-number** *number* [ **route-policy** *route-policy-name* | **route-filter** *route-filter-name* ]
      
      
      
      The maximum number of preferred routes to be advertised to a specified peer is specified.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      To configure **route-policy** *route-policy-name*, you need to enter the route-policy view.
      
      To configure **route-filter** *route-filter-name*, you need to enter the route-filter view.
  12. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Perform the following steps on the device (DeviceA in this example) that needs to accept Add-Path routes:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer+capability-advertise+add-path+receive) { *ipv4-address* | *group-name* } **capability-advertise** **add-path** **receive**
     
     
     
     The device is enabled to accept Add-Path routes from the specified peer.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, run the [**display bgp peer**](cmdqueryname=display+bgp+peer+verbose) **verbose** command to check the BGP Add-Path status.