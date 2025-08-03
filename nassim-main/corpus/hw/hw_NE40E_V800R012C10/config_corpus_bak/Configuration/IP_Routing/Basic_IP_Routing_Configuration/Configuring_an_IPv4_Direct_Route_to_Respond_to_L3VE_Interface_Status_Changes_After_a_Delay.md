Configuring an IPv4 Direct Route to Respond to L3VE Interface Status Changes After a Delay
==========================================================================================

This section describes how to configure an IPv4 direct route to respond to Layer 3 virtual Ethernet (L3VE) interface status changes after a delay on an IP radio access network (RAN). During traffic switchback after the master AGG recovers, this configuration can reduce traffic loss and improve network reliability.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0172365339__fig_dc_vrp_ip-route_cfg_003501), a Layer 2 virtual private network (VPN) connection is set up between each AGG and the CSG through L2VE interfaces, and Border Gateway Protocol (BGP) VPNv4 peer relationships are set up between the AGGs and RSGs on an L3VPN. L3VE interfaces are configured on the AGGs, and VPN instances are bound to the L3VE interfaces so that the CSG can access the L3VPN. BGP is configured on the AGGs to import IPv4 direct routes between the CSG and AGGs. The AGGs convert these IPv4 direct routes to BGP VPNv4 routes before advertising them to the RSGs.

**Figure 1** Networking for the IPv4 direct route responding to L3VE interface status changes after a delay  
![](images/fig_dc_vrp_ip-route_cfg_003501.png)

AGG1 functions as the master device. In most cases, the RSGs select routes advertised by AGG1, and traffic travels along Link A. If AGG1 or the CSG-AGG1 link fails, traffic switches over to Link B. After AGG1 or the CSG-AGG1 link recovers, the L3VE interface on AGG1 goes from down to up, and AGG1 immediately generates an IPv4 direct route and advertises the route to the corresponding RSG. Downstream traffic then switches back to Link A. However, AGG1 has not learned the MAC address of the base station yet. As a result, downstream traffic is lost.

After a delay is configured for IPv4 direct routes to respond to L3VE interface status changes, the cost of the IPv4 direct route increases when the L3VE interface on AGG1 goes from down to up. In this case, RSGs do not preferentially select the route advertised by AGG1. Therefore, downstream traffic still travels along Link B. After the specified delay elapses, AGG1 learns the MAC address of the base station, and the cost of the IPv4 direct route restores to the default value 0. In this case, RSGs preferentially select the IPv4 direct route advertised by AGG1, preventing downstream traffic loss during switchback.


#### Pre-configuration Tasks

Before you configure an IPv4 direct route to respond to L3VE interface status changes after a delay, configure link-layer protocol parameters and IP addresses for interfaces and ensure that the link layer protocol of each interface is Up.


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
   
   
   
   A VE sub-interface is created, and the VE sub-interface view is displayed.
6. Run [**direct-route degrade-delay**](cmdqueryname=direct-route+degrade-delay) *delay-time* **degrade-cost** *cost*
   
   
   
   The IPv4 direct route is configured to respond to L3VE interface status changes after a delay.
   
   
   
   After you run the [**direct-route degrade-delay**](cmdqueryname=direct-route+degrade-delay) command on an L3VE interface, and the L3VE interface goes from Down to Up, the cost of the L3VE interface's IPv4 direct route to the CSG is modified to the configured cost. After the configured *delay-time* expires, the IPv4 direct route cost is restored to the default value 0.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**direct-route track pw-state**](cmdqueryname=direct-route+track+pw-state), [**direct-route degrade-delay**](cmdqueryname=direct-route+degrade-delay), and [**direct-route track vrrp**](cmdqueryname=direct-route+track+vrrp) commands cannot all be configured on one L3VE interface. If you run the three commands on one L3VE interface, the latest configuration overrides the previous ones.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

If an AGG's L3VE interface goes from Down to Up, run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* [ *ip-address* ] [ **verbose** ] command on the AGG. The command output shows that the cost of the L3VE interface's IPv4 direct route to the CSG is the configured cost. After the configured *delay-time* expires, run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* [ *ip-address* ] [ **verbose** ] command on the AGG. The command output shows that the cost of the IPv4 direct route to the L3VE interface is the default value 0.