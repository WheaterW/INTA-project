Configuring AGGs to Load Balance Downstream Traffic
===================================================

This section describes how to configure access aggregation gateways (AGGs) to load-balance downstream traffic. The load balancing configuration can improve network resource utilization and reliability.

#### Usage Scenario

[Figure 1](#EN-US_TASK_0172365353__fig_dc_vrp_ip-route_cfg_005201) shows a typical networking for an L2VPN accessing an L3VPN. An L2VPN connection is set up between each AGG and CSG, whereas a BGP VPNv4 peer relationship is set up between each AGG and RSG; L3VE sub-interfaces are configured on each AGG, each L3VE sub-interface is bound to one VPN instance, and the CSGs access the L3VPN. To properly use network resources and improve network reliability, the customer requires that AGG1 forward downstream traffic destined for CSG1 and CSG2 and that AGG2 forward downstream traffic destined for CSG3 and CSG4.

**Figure 1** Networking for an L2VPN accessing an L3VPN  
![](images/fig_dc_vrp_ip-route_cfg_005201.png)
To meet the preceding requirements, perform the following steps on each AGG:

1. Run the [**direct-route cost**](cmdqueryname=direct-route+cost) or [**direct-route ipv6 cost**](cmdqueryname=direct-route+ipv6+cost) command to configure a cost for ARP Vlink routes and direct subnet routes on the L3VE sub-interface corresponding to the secondary PW.
2. Configure a static route to each base station and allow the static route to inherit the cost of the route to which the static route recurses.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After this configuration is complete, each static route recurses to a direct subnet route on an L3VE interface, and the static route inherits the cost of the direct subnet route. Because the [**direct-route cost**](cmdqueryname=direct-route+cost) or [**direct-route ipv6 cost**](cmdqueryname=direct-route+ipv6+cost) command is not run on the L3VE sub-interface corresponding to the primary PW, the default cost 0 is used as the cost of the generated direct routes. After a static route recurses to one of the direct routes, the cost of the static route also becomes 0.
3. Import the static routes into the BGP routing table.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After a static route is imported into the BGP routing table, the cost is changed to the BGP route MED. Because the costs of the static routes are different, the BGP route MED values are also different.

After the preceding configurations are complete, each AGG advertises the routes destined for base stations to its VPNv4 peer (RSG). The RSG can then select routes based on MED values. For routes with the same prefix advertised by AGG1 and AGG2, RSGs select the routes advertised by AGG1 as the primary routes to CSG1 and CSG2 and the routes advertised by AGG2 as the primary routes to CSG3 and CSG4. In this manner, downstream traffic is load balanced between AGGs.


#### Pre-configuration Tasks

Before configuring AGGs to load-balance downstream traffic, configure link-layer protocol parameters and IP addresses for interfaces and ensure that the link layer protocol on each interface is up.


#### Procedure

1. Set a cost for routes to the directly connected network segment.
   1. Run [**interface virtual-ethernet**](cmdqueryname=interface+virtual-ethernet) *interface-number*
      
      
      
      A VE interface is created, and the VE interface view is displayed.
   2. Run [**ve-group**](cmdqueryname=ve-group) *ve-group-id* **l3-access**
      
      
      
      The VE interface is configured as an L3VE interface that accesses a BGP/MPLS IP VPN and bound to a VE-group.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      L2VPN access can be implemented only if the L2VE and L3VE interfaces are bound to the same VE-group and reside on the same board.
   3. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   4. Run [**interface virtual-ethernet**](cmdqueryname=interface+virtual-ethernet) *interface-number.subinterface-number*
      
      
      
      A VE sub-interface is created, and the VE sub-interface view is displayed.
   5. Run [**direct-route cost**](cmdqueryname=direct-route+cost) *cost* or [**direct-route ipv6 cost**](cmdqueryname=direct-route+ipv6+cost) *cost*
      
      
      
      A cost is configured for direct subnet routes on the L3VE sub-interface.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
2. Run [**ip route-static vpn-instance**](cmdqueryname=ip+route-static+vpn-instance) *vpn-source-name* *destination-address* { *mask* | *mask-length* } *nexthop-address* [ **preference** *preference* | **tag** *tag* ] \* **inherit-cost** [ **description** *text* ]
   
   
   
   A static route is configured for the VPN instance, and the static route is configured to inherit the cost of the recursive route.
   
   
   
   *vpn-source-name* specifies the name of the VPN instance bound to the L3VE sub-interface. *nexthop-address* specifies the IP address of the interface connecting the base station to the AGG.
3. Perform either of the following operations to configure BGP to import static routes. After the configuration is complete, the costs of the static routes are changed to the MED values of BGP routes.
   * To import static routes to the BGP routing table automatically, run the [**import-route**](cmdqueryname=import-route) **static** command.
   * To import static routes to the BGP routing table manually, run the [**network**](cmdqueryname=network) command.
   
   
   
   If you run the [**import-route**](cmdqueryname=import-route) **static** command, some unneeded static routes may be imported to the BGP routing table. To import a static route with a specific prefix and mask to the BGP routing table, run the [**network**](cmdqueryname=network) command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, if the L3VE sub-interface is up, run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* [ *ip-address* ] [ **verbose** ] or [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* [ *ip-address* ] [ **verbose** ] command on the AGG. The command output shows that the cost of direct subnet routes on the L3VE sub-interface is changed to the configured cost.