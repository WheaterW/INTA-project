Configuring BGP Load Balancing
==============================

Configuring BGP load balancing better utilizes network resources and reduces network congestion.

#### Usage Scenario

On large networks, there may be multiple valid routes to the same destination. BGP, however, advertises only the optimal route to its peers, which may result in load imbalance.

Either of the following methods can be used to resolve the load imbalance:

* Use BGP routing policies to allow traffic to be balanced. For example, use a route-policy to modify the Local\_Pref, AS\_Path, Origin, or MED attribute of BGP routes to control traffic forwarding paths, helping implement load balancing.
* Use multiple paths to implement traffic load balancing. This method requires that multiple equal-cost routes exist and the number of routes allowed to participate in load balancing be set. Load balancing can be implemented globally or for a specified peer or peer group.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* You can change load balancing rules through configurations. For example, you can prevent the device from comparing AS\_Path attributes or IGP costs. When performing these configurations, ensure that no routing loops will occur.
* Locally leaked routes and routes imported between public network and VPN instances do not support load balancing.


#### Pre-configuration Tasks

Before configuring BGP load balancing, [configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).


#### Procedure

* Configure BGP peer or peer group-based load balancing.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     The BGP-IPv4 unicast address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer+load-balancing+as-path-ignore+as-path-relax) { *ipv4-address* | *group-name* } **load-balancing** [ **as-path-ignore** | **as-path-relax** ]
     
     BGP peer or peer group-based load balancing is enabled.
     
     After the [**peer load-balancing**](cmdqueryname=peer+load-balancing) command is run, load balancing is implemented only when the following conditions are met:
     + The routes are received from a specified peer or peer group.
     + The routes are optimal routes or optimal equal-cost routes.
     + The AS\_Path attribute of the routes is the same as that of the optimal route, or **as-path-ignore** or **as-path-relax** is specified when peer-based load balancing is configured.
       - If **as-path-ignore** is specified, the device ignores comparing AS\_Path attributes when selecting routes for load balancing. In this case, routes can participate in load balancing even if their AS\_Path attributes are different.
       - If **as-path-relax** is specified, the device ignores comparing the AS\_Path attributes of the same length when selecting routes for load balancing. In this case, routes cannot participate in load balancing if their AS\_Path attributes are of different lengths. For example, the AS\_Path attribute of route A is (10), and the AS\_Path attribute of route B is (10, 20). Because the two AS\_Path attributes are of different lengths, the two routes cannot participate in load balancing.
  5. (Optional) Enable peer or peer group-based load balancing among VPN routes.
     1. Run [**quit**](cmdqueryname=quit)
        
        Return to the BGP view.
     2. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     3. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
        
        The VPN instance view is displayed.
     4. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
        
        The VPN instance IPv4 address family view is displayed.
     5. Run **route-distinguisher** *route-distinguisher*
        
        An RD is configured for the VPN instance IPv4 address family.
     6. Run [**quit**](cmdqueryname=quit)
        
        Return to the VPN instance view.
     7. Run [**quit**](cmdqueryname=quit)
        
        Return to the system view.
     8. Run [**bgp**](cmdqueryname=bgp) *as-number*
        
        The BGP view is displayed.
     9. Run **vpn-instance** *vpn-instance-name*
        
        A VPN instance is specified.
     10. Run **peer** { *ipv4-address* | *group-name* } **as-number** *as-number*
         
         A peer relationship is established with the peer with the specified AS number.
     11. Run [**quit**](cmdqueryname=quit)
         
         Return to the BGP view.
     12. Run **ipv4-labeled-unicast vpn-instance** *vpn-instance-name*
         
         The BGP labeled VPN instance IPv4 address family view is displayed.
     13. Run [**peer**](cmdqueryname=peer+enable) { *ipv4-address* | *group-name* } **enable**
         
         The device is enabled to exchange routing information with the specified peer.
     14. Run [**peer**](cmdqueryname=peer+load-balancing+as-path-ignore+as-path-relax) { *ipv4-address* | *group-name* } **load-balancing** [ **as-path-ignore** | **as-path-relax** ]
         
         Peer or peer group-based load balancing among VPN routes is enabled.
  6. (Optional) Change load balancing rules.
     
     + To prevent the device from comparing AS\_Path attributes when selecting routes for load balancing, run the [**load-balancing as-path-ignore**](cmdqueryname=load-balancing+as-path-ignore) command.
     + To configure the device to ignore comparing the AS\_Path attributes of the same length when selecting routes for load balancing, run the [**load-balancing as-path-relax**](cmdqueryname=load-balancing+as-path-relax) command.
     + To prevent the device from comparing IGP costs when selecting routes for load balancing, run the [**load-balancing igp-metric-ignore**](cmdqueryname=load-balancing+igp-metric-ignore) command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The address family views supported by the preceding commands are different. When running any of the commands, ensure that the command is run in the correct address family view.
     
     Change load balancing rules based on networking. Exercise caution when running the preceding commands.
  7. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure global BGP load balancing.
  
  
  + Set the maximum number of BGP routes for load balancing.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**bgp**](cmdqueryname=bgp) *as-number*
       
       The BGP view is displayed.
    3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
       
       The IPv4 unicast address family view is displayed.
    4. Run [**maximum load-balancing**](cmdqueryname=maximum+load-balancing+ebgp+ibgp+ecmp-nexthop-changed) [ **ebgp** | **ibgp** ] *number* [ **ecmp-nexthop-changed** ]
       
       The maximum number of BGP equal-cost routes for load balancing is set.
       
       - **ebgp** indicates that load balancing is implemented only among EBGP routes.
       - **ibgp** indicates that load balancing is implemented only among IBGP routes.
       - If neither **ebgp** nor **ibgp** is specified, both EBGP and IBGP routes can balance traffic, and the number of EBGP routes for load balancing is the same as the number of IBGP routes for load balancing.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       If multiple routes with the same destination address exist on the public network, the system selects the optimal route first. If IBGP routes are optimal, only IBGP routes carry out load balancing. If EBGP routes are optimal, only EBGP routes carry out load balancing. This means that load balancing cannot be implemented using both IBGP and EBGP routes with the same destination address.
    5. (Optional) Change load balancing rules.
       
       - To prevent the device from comparing AS\_Path attributes when selecting routes for load balancing, run the [**load-balancing as-path-ignore**](cmdqueryname=load-balancing+as-path-ignore) command.
       - To configure the device to ignore comparing the AS\_Path attributes of the same length when selecting routes for load balancing, run the [**load-balancing as-path-relax**](cmdqueryname=load-balancing+as-path-relax) command.
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
    3. Run [**ipv4-family**](cmdqueryname=ipv4-family+vpn-instance) **vpn-instance** *vpn-instance-name*
       
       The BGP-VPN instance IPv4 address family view is displayed.
    4. Run [**maximum load-balancing eibgp**](cmdqueryname=maximum+load-balancing+eibgp+ecmp-nexthop-changed) *number* [ **ecmp-nexthop-changed** ]
       
       The maximum number of EBGP and IBGP routes for load balancing is set.
       
       After the [**maximum load-balancing eibgp**](cmdqueryname=maximum+load-balancing+eibgp+ecmp-nexthop-changed) *number* command is run on a device, the device, by default, changes the next hop of each route to itself before advertising the route to a peer, regardless of whether the route is to be used for load balancing. However, in RR or BGP confederation scenarios, the device does not change the next hop addresses of non-local routes to be advertised to a local address. As a result, besides the routes for load-balancing, those routes that are not supposed to participate in load balancing divert traffic to the device, which overburdens the device. To address this problem, you can set **ecmp-nexthop-changed** so that the device changes the next hop of only routes that are to be used for load balancing to itself before advertising them to peers.
    5. (Optional) Change load balancing rules.
       
       - To prevent the device from comparing AS\_Path attributes when selecting routes for load balancing, run the [**load-balancing as-path-ignore**](cmdqueryname=load-balancing+as-path-ignore) command.
       - To configure the device to ignore comparing the AS\_Path attributes of the same length when selecting routes for load balancing, run the [**load-balancing as-path-relax**](cmdqueryname=load-balancing+as-path-relax) command.
       - To prevent the device from comparing IGP costs when selecting routes for load balancing, run the [**load-balancing igp-metric-ignore**](cmdqueryname=load-balancing+igp-metric-ignore) command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       The address family views supported by the preceding commands are different. When running any of the commands, ensure that the command is run in the correct address family view.
       
       Change load balancing rules based on networking. Exercise caution when running the preceding commands.
    6. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
  + Configure load balancing among VPN unicast routes and leaked routes.
    
    This configuration is mainly used in an EIBGP load balancing scenario where a CE that is single-homed to a PE accesses a CE that is dual-homed to PEs. As shown in [Figure 1](#EN-US_TASK_0172366233__fig9635181442219), CE2 is dual-homed to PE1 and PE2. CE1 and CE2 are connected to PE1, and CE2 and CE3 are connected to PE2. When CE1 or CE3 needs to access CE2, you can configure load balancing among VPN unicast routes and leaked routes on PE1 and PE2. In this manner, when CE1 or CE3 accesses CE2, load balancing can be implemented through PE1 and PE2, that is, load balancing among VPN routes and leaked routes.
    
    **Figure 1** Load balancing among VPN unicast routes and leaked routes  
    ![](figure/en-us_image_0000001159139198.png)
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**ip vpn-instance**](cmdqueryname=ip+vpn-instance) *vpn-instance-name*
       
       A VPN instance is created, and its view is displayed.
    3. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
       
       An RD is configured for the VPN instance.
    4. Run [**apply-label**](cmdqueryname=apply-label+per-nexthop+per-route+pop-go) {**per-nexthop** | **per-route** } **pop-go**
       
       A label distribution mode is configured for the current VPN.
    5. Run [**quit**](cmdqueryname=quit)
       
       Return to the system view.
    6. Run [**bgp**](cmdqueryname=bgp) *as-number*
       
       The BGP view is displayed.
    7. Run [**ipv4-family**](cmdqueryname=ipv4-family+vpn-instance) **vpn-instance** *vpn-instance-name*
       
       The BGP-VPN instance IPv4 address family view is displayed.
    8. Run [**load-balancing local-learning cross**](cmdqueryname=load-balancing+local-learning+cross)
       
       Load balancing among VPN unicast routes and leaked routes is configured.
       
       The [**load-balancing local-learning cross**](cmdqueryname=load-balancing+local-learning+cross) command can be run only after the [**apply-label**](cmdqueryname=apply-label+per-nexthop+per-route+pop-go) {**per-nexthop** | **per-route** } **pop-go** command is run in the corresponding address family view of a VPN instance. If the [**apply-label**](cmdqueryname=apply-label+per-nexthop+per-route+pop-go) {**per-nexthop** | **per-route** } **pop-go** command is not run, routing loops may occur between PEs.
       
       The [**load-balancing local-learning cross**](cmdqueryname=load-balancing+local-learning+cross) command is mutually exclusive with the [**segment-routing ipv6 locator evpn**](cmdqueryname=segment-routing+ipv6+locator+evpn), [**segment-routing ipv6 locator**](cmdqueryname=segment-routing+ipv6+locator), [**vxlan vni**](cmdqueryname=vxlan+vni), and [**evpn mpls routing-enable**](cmdqueryname=evpn+mpls+routing-enable) commands.
    9. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.

#### Follow-up Procedure

When BGP routes carrying the link bandwidth extended community attribute are available for load balancing and they all recurse to IP routes or tunnels, you can run the [**load-balancing ucmp**](cmdqueryname=load-balancing+ucmp) command in the BGP-IPv4 unicast address family view or BGP view to implement unequal-cost load balancing among BGP routes based on the link bandwidth extended community attribute. With this function, when there are multiple egress devices to the destination, unequal-cost load balancing can be implemented based on the actual bandwidth capability of each egress device. The methods of configuring the link bandwidth extended community attribute are as follows:

* Use [XPL to configure the link bandwidth extended community attribute](dc_vrp_xpl_cfg_0017.html#EN-US_CONCEPT_0172366625__section856910644816).
* Run the [**peer generate-link-bandwidth**](cmdqueryname=peer+generate-link-bandwidth) command to configure the local device to obtain the link bandwidth of a specified directly connected EBGP peer and generate the extended community attribute accordingly.
* Run the [**peer generate-link-bandwidth**](cmdqueryname=peer+generate-link-bandwidth) command to configure the local device to obtain the link bandwidth of a specified directly connected EBGP peer and generate the extended community attribute accordingly.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table+longer-prefixes) [ *network* ] [ *mask* | *mask-length* ] [ **longer-prefixes** ] command to check information about the BGP routing table.
* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table+verbose) [ **verbose** ] command to check information about the IP routing table.