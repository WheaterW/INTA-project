Configuring BGP4+ Load Balancing
================================

Configuring BGP4+ load balancing better utilizes network resources.

#### Usage Scenario

On large networks, there may be multiple valid routes to the same destination. BGP4+, however, advertises only the optimal route to its peers. This may result in traffic imbalance.

Either of the following methods can be used to resolve the traffic imbalance:

* Use BGP4+ route-policies for load balancing. For example, you can use a route-policy to modify the Local\_Pref, AS\_Path, Origin, or MED attribute of BGP4+ routes to control traffic forwarding paths, helping implement load balancing.
* Use multiple paths to implement traffic load balancing. This method requires that multiple equal-cost routes exist and the number of routes allowed to participate in load balancing be set. Load balancing can be implemented globally or based on a specified peer.

#### Pre-configuration Tasks

Before configuring BGP4+ load balancing, [configure basic BGP4+ functions](dc_vrp_bgp6_cfg_0003.html).


#### Procedure

* Configure BGP4+ peer or peer group-based load balancing.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     The BGP view is displayed.
  3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
     
     The IPv6 unicast address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer+load-balancing+as-path-ignore+as-path-relax) { *ipv4-address* | *ipv6âaddress* | *group-name* } **load-balancing** [ **as-path-ignore** | **as-path-relax** ]
     
     BGP4+ peer or peer group-based load balancing is configured.
     
     After the **peer load-balancing** command is run, BGP peer-based load balancing is implemented only when the following conditions are met:
     + The routes are received from the specified peer or peer group.
     + The optimal route and optimal equal-cost routes exist.
     + The AS\_Path attribute is the same as that of the optimal route, or **as-path-ignore** or **as-path-relax** is specified in the **peer load-balancing** command.
       - If **as-path-ignore** is specified, the device ignores comparing AS\_Path attributes when selecting routes for load balancing. In this case, routes can participate in load balancing even if their AS\_Path attributes are different.
       - If **as-path-relax** is specified, the device ignores comparing the AS\_Path attributes of the same length when selecting routes for load balancing. In this case, routes cannot participate in load balancing if their AS\_Path attributes are of different lengths. For example, the AS\_Path attribute of route A is **10**, and the AS\_Path attribute of route B is **10, 20**. Because the two AS\_Path attributes are of different lengths, the two routes cannot participate in load balancing.
  5. (Optional) Change load balancing rules.
     
     + To prevent the device from comparing AS\_Path attributes when selecting routes for load balancing, run the [**load-balancing as-path-ignore**](cmdqueryname=load-balancing+as-path-ignore) command.
     + To prevent the device from comparing the AS\_Path attributes of the same length when selecting routes for load balancing, run the [**load-balancing as-path-relax**](cmdqueryname=load-balancing+as-path-relax) command.
     + To prevent the device from comparing IGP costs when selecting routes for load balancing, run the [**load-balancing igp-metric-ignore**](cmdqueryname=load-balancing+igp-metric-ignore) command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The address family views supported by the preceding commands are different. When running any of the commands, ensure that the command is run in the correct address family view.
     
     Change load balancing rules based on networking. Exercise caution when running the preceding commands.
  6. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure global BGP4+ load balancing.
  
  
  + Set the maximum number of BGP4+ routes for load balancing.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**bgp**](cmdqueryname=bgp) *as-number*
       
       The BGP view is displayed.
    3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
       
       The IPv6 unicast address family view is displayed.
    4. Run [**maximum load-balancing**](cmdqueryname=maximum+load-balancing+ebgp+ibgp+ecmp-nexthop-changed) [ **ebgp** | **ibgp** ] *number* [ **ecmp-nexthop-changed** ]
       
       The maximum number of BGP4+ equal-cost routes for load balancing is set.
       
       - **ebgp** indicates that load balancing is implemented only among EBGP routes.
       - **ibgp** indicates that load balancing is implemented only among IBGP routes.
       - If neither **ebgp** nor **ibgp** is specified, EBGP and IBGP routes can compete for preferred routes to balance traffic, and the number of allowed load-balancing EBGP routes is the same as the number of allowed load-balancing IBGP routes.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       If multiple routes with the same destination address exist on the public network, the system selects the optimal route first. If IBGP routes are optimal, only IBGP routes carry out load balancing. If EBGP routes are optimal, only EBGP routes carry out load balancing. This means that load balancing cannot be implemented using both IBGP and EBGP routes with the same destination address.
    5. (Optional) Change load balancing rules.
       
       - To prevent the device from comparing AS\_Path attributes when selecting routes for load balancing, run the [**load-balancing as-path-ignore**](cmdqueryname=load-balancing+as-path-ignore) command.
       - To prevent the device from comparing the AS\_Path attributes of the same length when selecting routes for load balancing, run the [**load-balancing as-path-relax**](cmdqueryname=load-balancing+as-path-relax) command.
       - To prevent the device from comparing IGP costs when selecting routes for load balancing, run the [**load-balancing igp-metric-ignore**](cmdqueryname=load-balancing+igp-metric-ignore) command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       The address family views supported by the preceding commands are different. When running any of the commands, ensure that the command is run in the correct address family view.
       
       Change load balancing rules based on networking. Exercise caution when running the preceding commands.
    6. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
  + Set the maximum number of EBGP and IBGP routes for load balancing.
    
    This configuration is used in a VPN where a CE is dual-homed to two PEs. When the CE resides in the same AS as only one of the PEs, you can set the maximum number of EBGP and IBGP routes for load balancing so that VPN traffic can be balanced among EBGP and IBGP routes.
    
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**bgp**](cmdqueryname=bgp) *as-number*
       
       The BGP view is displayed.
    3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **vpn-instance** *vpn-instance-name*
       
       The BGP-VPN instance IPv6 address family view is displayed.
    4. Run [**maximum load-balancing eibgp**](cmdqueryname=maximum+load-balancing+eibgp+ecmp-nexthop-changed) *number* [ **ecmp-nexthop-changed** ]
       
       The maximum number of EBGP and IBGP routes for load balancing is set.
       
       After the [**maximum load-balancing eibgp**](cmdqueryname=maximum+load-balancing+eibgp) *number* command is run on a device, the device, by default, changes the next hop of each BGP4+ route to itself before advertising the route to a peer, regardless of whether the route is to be used for load balancing. However, in RR or BGP confederation scenarios, the device does not change the next hop addresses of non-local routes to be advertised to a local address. As a result, besides the routes for load-balancing, those routes that are not supposed to participate in load balancing divert traffic to the device, which overburdens the device. To address this problem, you can set **ecmp-nexthop-changed** so that the device changes the next hop of only the BGP4+ routes that are to be used for load balancing to itself before advertising them to peers.
    5. (Optional) Change load balancing rules.
       
       - To prevent the device from comparing AS\_Path attributes when selecting routes for load balancing, run the [**load-balancing as-path-ignore**](cmdqueryname=load-balancing+as-path-ignore) command.
       - To prevent the device from comparing the AS\_Path attributes of the same length when selecting routes for load balancing, run the [**load-balancing as-path-relax**](cmdqueryname=load-balancing+as-path-relax) command.
       - To prevent the device from comparing IGP costs when selecting routes for load balancing, run the [**load-balancing igp-metric-ignore**](cmdqueryname=load-balancing+igp-metric-ignore) command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       The address family views supported by the preceding commands are different. When running any of the commands, ensure that the command is run in the correct address family view.
       
       Change load balancing rules based on networking. Exercise caution when running the preceding commands.
    6. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
  + Configure load balancing among VPN unicast routes and leaked routes.
    
    This configuration is mainly used in an EIBGP load balancing scenario where a CE that is single-homed to a PE accesses a CE that is dual-homed to PEs. As shown in [Figure 1](#EN-US_TASK_0172366460__fig9635181442219), CE2 is dual-homed to PE1 and PE2. CE1 and CE2 are connected to PE1, and CE2 and CE3 are connected to PE2. When CE1 or CE3 needs to access CE2, you can configure load balancing among VPN unicast routes and leaked routes on PE1 and PE2. In this manner, when CE1 or CE3 accesses CE2, load balancing can be implemented through PE1 and PE2, that is, load balancing among VPN routes and leaked routes.
    
    **Figure 1** Load balancing among VPN unicast routes and leaked routes  
    ![](figure/en-us_image_0000001159076430.png)
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
       
       A VPN instance is created, and its view is displayed.
    3. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
       
       An RD is configured for the VPN instance.
    4. Run [**apply-label**](cmdqueryname=apply-label+per-nexthop+per-route+pop-go) {**per-nexthop** | **per-route** } **pop-go**
       
       A label distribution mode is configured for the current VPN.
    5. Run [**quit**](cmdqueryname=quit)
       
       The VPN instance view is displayed.
    6. Run [**quit**](cmdqueryname=quit)
       
       The system view is displayed.
    7. Run [**bgp**](cmdqueryname=bgp) *as-number*
       
       The BGP view is displayed.
    8. Run [**ipv6-family**](cmdqueryname=ipv6-family+vpn-instance) **vpn-instance** *vpn-instance-name*
       
       The BGP-VPN instance IPv6 address family view is displayed.
    9. Run [**load-balancing local-learning cross**](cmdqueryname=load-balancing++local-learning+cross)
       
       Load balancing among VPN unicast routes and leaked routes is configured.
       
       The [**load-balancing local-learning cross**](cmdqueryname=load-balancing+local-learning+cross) command can be run only after the [**apply-label**](cmdqueryname=apply-label+per-nexthop+per-route+pop-go) {**per-nexthop** | **per-route** } **pop-go** command is run in the corresponding address family view of the VPN instance. If the [**apply-label**](cmdqueryname=apply-label+per-nexthop+per-route+pop-go) {**per-nexthop** | **per-route** } **pop-go** command is not run, routing loops may occur between PEs.
       
       The [**load-balancing local-learning cross**](cmdqueryname=load-balancing+local-learning+cross) command is mutually exclusive with the [**segment-routing ipv6 locator evpn**](cmdqueryname=segment-routing+ipv6+locator+evpn), [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator), [**vxlan vni**](cmdqueryname=vxlan+vni), and [**evpn mpls routing-enable**](cmdqueryname=evpn+mpls+routing-enable) commands.
    10. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.

#### Follow-up Procedure

When BGP4+ routes carrying the link bandwidth extended community attribute are available for load balancing and they all recurse to IP routes or tunnels, you can run the [**load-balancing ucmp**](cmdqueryname=load-balancing+ucmp) command in the BGP-IPv6 unicast address family view to implement unequal-cost load balancing among BGP4+ routes based on the link bandwidth extended community attribute. With this function, when there are multiple egress devices to the destination, unequal-cost load balancing can be implemented based on the actual bandwidth capability of each egress device. The methods of configuring the link bandwidth extended community attribute are as follows:

* Use [XPL to configure the link bandwidth extended community attribute](dc_vrp_xpl_cfg_0017.html#EN-US_CONCEPT_0172366625__section856910644816).
* Run the [**peer generate-link-bandwidth**](cmdqueryname=peer+generate-link-bandwidth) command to configure the local device to obtain the link bandwidth of a specified directly connected EBGP peer and generate the extended community attribute accordingly.

#### Verifying the Configuration

After the configuration is complete, verify it.

Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) *ipv6-address* *prefix-length* command to check routes in the BGP4+ routing table.