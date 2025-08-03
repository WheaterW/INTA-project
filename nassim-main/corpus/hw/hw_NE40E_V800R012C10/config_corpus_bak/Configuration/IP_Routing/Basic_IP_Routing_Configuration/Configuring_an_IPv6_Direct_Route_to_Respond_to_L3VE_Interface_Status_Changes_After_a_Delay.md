Configuring an IPv6 Direct Route to Respond to L3VE Interface Status Changes After a Delay
==========================================================================================

This section describes how to configure an IPv6 direct route to respond to Layer 3 Virtual Ethernet (L3VE) interface status changes after a delay. During traffic switchback after an L3VE interface recovers, this configuration can reduce traffic loss and improve network reliability.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0172365343__fig_dc_vrp_ip-route_cfg_006001), L2VPN connections are set up between AGGs and the CSG, and BGP VPNv6 peer relationships are set up between AGGs and RSGs. L3VE interfaces are configured on AGGs and VPN instances are bound to the L3VE interfaces, so that the CSG can access the L3VPN. BGP is configured on AGGs to import direct routes between the CSG and AGGs. These direct routes are converted to BGP VPNv6 routes and advertised to RSGs.

**Figure 1** Networking of an IPv6 direct route responding to L3VE interface status changes after a delay  
![](images/fig_dc_vrp_ip-route_cfg_006001.png)  

AGG1 is used as the master device in the preceding figure. In normal cases, RSGs select routes advertised by AGG1 and traffic travels along LinkA. If AGG1 or the CSG-AGG1 link fails, traffic is switched over to LinkB. After AGG1 or the CSG-AGG1 link recovers, the L3VE interface on AGG1 goes from Down to Up, and AGG1 immediately generates an IPv6 direct route destined for the CSG and advertises the route to RSGs. Downstream traffic is then switched over to LinkA. However, AGG1 has not learned the MAC addresses of the base stations yet, so downstream traffic will be lost.

After you configure a cost for an IPv6 direct route and allow the direct route to restore its default cost 0 after a delay, when the L3VE interface on AGG1 goes from Down to Up, the cost of the direct route between the CSG and AGG1 is modified to the configured cost. In this case, RSGs do not select routes advertised by AGG1 and downstream traffic still travels along LinkB. After the configured delay expires, the cost of the IPv6 direct route on AGG1 is restored to the default value 0. RSGs select the routes advertised by AGG1. At this time, AGG1 has learned the MAC address of the base station, and downstream traffic loss is reduced after a downstream traffic switchover.


#### Pre-configuration Tasks

Before you configure an IPv6 direct route to respond to L3VE interface status changes after a delay, complete the following task:

* Set data link layer protocol parameters and IPv6 addresses for interfaces to ensure that the data link layer protocol status of each interface is up.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface virtual-ethernet**](cmdqueryname=interface+virtual-ethernet) *interface-number*
   
   
   
   A VE interface is created, and the VE interface view is displayed.
3. Run [**ve-group**](cmdqueryname=ve-group) *ve-group-id* **l3-access**
   
   
   
   The VE interface is configured as an L3VE interface for MPLS L3VPN access and bound to a VE-group.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The L2VPN can access the L3VPN only if the L2VE and L3VE interfaces are bound to the same VE-group and reside on the same board.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**interface virtual-ethernet**](cmdqueryname=interface+virtual-ethernet) *interface-number.subinterface-number*
   
   
   
   An L3VE sub-interface is created, and its view is displayed.
6. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   The IPv6 capability is enabled.
7. Run [**direct-route ipv6 degrade-delay**](cmdqueryname=direct-route+ipv6+degrade-delay) *delay-time* **degrade-cost** *cost*
   
   
   
   The direct route is configured to respond to L3VE interface status changes after a delay.
   
   After you run the [**direct-route ipv6 degrade-delay**](cmdqueryname=direct-route+ipv6+degrade-delay) command on an L3VE interface, and the L3VE interface goes from Down to Up, the cost of the L3VE interface's direct route is modified to the configured cost. After the configured delay-time expires, the direct route cost is restored to the default value 0.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**direct-route ipv6 degrade-delay**](cmdqueryname=direct-route+ipv6+degrade-delay) command and the [**direct-route ipv6 track pw-state**](cmdqueryname=direct-route+ipv6+track+pw-state) command cannot be both configured on one L3VE interface.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

If an AGG's L3VE interface goes from Down to Up, run the [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* [ *ipv6-address* ] [ **verbose** ] command on the AGG. The command output shows that the cost of the L3VE interface's IPv6 direct route to the CSG is the configured cost. After the configured *delay-time* expires, run the [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* [ *ipv6-address* ] [ **verbose** ] command on the AGG. The command output shows that the cost of the IPv6 direct route to the L3VE interface is the default value 0.