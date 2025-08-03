Configuring Delayed Response to BGP Next Hop Recursion Changes
==============================================================

Configuring delayed response to BGP next hop recursion changes can minimize traffic loss during route changes.

#### Usage Scenario

As shown in [Figure 1](#EN-US_TASK_0172366257__fig_dc_vrp_bgp_cfg_410201), PE1, PE2, and PE3 are the clients of the RR. CE2 is dual-homed to PE1 and PE2. PE1 and PE2 advertise their routes destined for CE2 to the RR. The RR advertises the route from PE1 to PE3. PE3 has only one route to CE2 and advertises this route to CE1. After the route exchange, CE1 and CE2 can communicate. If PE1 fails, PE3 detects that the next hop is unreachable and instructs CE1 to delete the route to CE2. Traffic is interrupted. After BGP route convergence is complete, the RR selects the route advertised by PE2 and sends a route update message to PE3. PE3 then advertises this route to CE1, and traffic forwarding is restored. A high volume of traffic will be lost during traffic interruption because BGP route convergence is rather slow.

If delayed response to BGP next hop recursion changes is enabled on PE3, PE3 does not reselect a route or instruct CE1 to delete the corresponding route immediately after detecting that the route to PE1 is unreachable. After BGP convergence is complete, the RR selects the route advertised by PE2 and sends the route to PE3. PE3 then reselects a route and sends a route update message to CE1. Traffic forwarding is restored. After delayed response to BGP next hop recursion changes is enabled on PE3, PE3 does not need to delete the route or instruct CE1 to delete the route. This delayed response speeds up BGP route convergence and minimizes traffic loss.

**Figure 1** Networking diagram for configuring the BGP next hop recursion change delayed response  
![](images/fig_dc_vrp_bgp_cfg_410201.png)  

There are two links between DeviceA and DeviceD, and traffic passes through link DeviceA -> DeviceB -> DeviceC -> DeviceD.

* On the network shown in [Figure 2](#EN-US_TASK_0172366257__fig1523333211323), if the link between DeviceB and DeviceC fails, BGP cannot find the next hop route or tunnel for recursion to DeviceC. As a result, traffic is interrupted and is switched to the link DeviceA -> DeviceE -> DeviceF -> DeviceD. In this case, when the next hop recursion changes, the reachability also changes. This is called a critical recursion change.**Figure 2** Networking diagram for a critical recursion change  
  ![](figure/en-us_image_0000001385732317.png)

* On the network shown in [Figure 3](#EN-US_TASK_0172366257__fig1519121912531), when the link between DeviceB and DeviceC is normal, the cost of this link is increased. Due to route selection, traffic is switched to the link DeviceA -> DeviceE -> DeviceF -> DeviceD. In this case, the next hop recursion result changes, but the reachability remains unchanged. This is called a non-critical recursion result change.**Figure 3** Networking diagram for a non-critical recursion change  
  ![](figure/en-us_image_0000001385087357.png)

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Delayed response to BGP next hop recursion changes applies only to scenarios where multiple links exist between the downstream device and the same destination. If there is only one link between the downstream device and the destination, configuring delayed response to BGP next hop recursion changes may cause heavier traffic loss when the link fails because link switching is impossible.



#### Pre-configuration Tasks

Before configuring the BGP next hop recursion change delayed response, complete the following task:

* [Configure basic BGP functions.](dc_vrp_bgp_cfg_3004.html)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Configure delayed response to next hop recursion changes.
   * To configure a delay in responding to next hop recursion changes, run the [**nexthop recursive-lookup delay**](cmdqueryname=nexthop+recursive-lookup+delay) [ *delay-time* ] [ **include-tunnel** ] command. After the command is run, the system delays to respond to both critical and non-critical next hop recursion changes.
   * To configure a delay in responding to non-critical next hop recursion changes, run the [**nexthop recursive-lookup non-critical-event delay**](cmdqueryname=nexthop+recursive-lookup+non-critical-event+delay)[ **nonCrit-delay-time** ] command.
   * To configure a delay in responding to critical next hop recursion changes (from unreachability to reachability), run the [**nexthop recursive-lookup critical-event-reachable delay**](cmdqueryname=nexthop+recursive-lookup+critical-event-reachable+delay)[ **critReach-delay-time** ] [ ****include-tunnel**** ] command.
   
   
   
   These commands can be configured separately or together. If they are all configured, the first command has a lower priority than the [**nexthop recursive-lookup non-critical-event delay**](cmdqueryname=nexthop+recursive-lookup+non-critical-event+delay)[ **nonCrit-delay-time** ] command or the [**nexthop recursive-lookup critical-event-reachable delay**](cmdqueryname=nexthop+recursive-lookup+critical-event-reachable+delay)[ **critReach-delay-time** ] [ ****include-tunnel**** ] command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring delayed response to BGP next hop recursion changes, you can run the [**display current-configuration**](cmdqueryname=display+current-configuration+configuration+bgp+%7C+include) **configuration** **bgp** **|** **include** **nexthop recursive-lookup** command to view the delay in responding to BGP next hop recursion changes.