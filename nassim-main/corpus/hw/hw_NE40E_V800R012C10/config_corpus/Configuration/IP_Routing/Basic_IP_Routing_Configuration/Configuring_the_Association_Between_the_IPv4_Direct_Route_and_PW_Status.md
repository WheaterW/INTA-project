Configuring the Association Between the IPv4 Direct Route and PW Status
=======================================================================

This section describes how to configure the association between the IPv4 direct route and pseudo wire (PW) status. During traffic switchback after the primary PW recovers, this configuration minimizes traffic loss and improves network reliability.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0172365346__fig_dc_vrp_ip-route_cfg_003401), PWs are set up between the AGGs and the CSG. Border Gateway Protocol (BGP) virtual private network version 4 (VPNv4) peer relationships are set up between the AGGs and RSGs. Layer 3 virtual Ethernet (L3VE) interfaces are configured on the AGGs, and VPN instances are bound to the L3VE interfaces so that the CSG can access the L3VPN. BGP is configured on the AGGs to import IPv4 direct routes between the CSG and AGGs. The AGGs convert these IPv4 direct routes to BGP VPNv4 routes before advertising them to the RSGs.

**Figure 1** Networking for the association between the IPv4 direct route and PW status  
![](images/fig_dc_vrp_ip-route_cfg_003401.png)

AGG1 functions as the master device. In most cases, the RSGs select routes advertised by AGG1, and traffic travels along Link A. If AGG1 or the CSG-AGG1 link fails, traffic switches over to Link B. After AGG1 or the CSG-AGG1 link recovers, the L3VE interface on AGG1 goes from Down to Up, and AGG1 immediately generates an IPv4 direct route destined for the CSG and advertises the route to the RSGs. Downstream traffic then switches over to Link A. However, PW1 is on standby. As a result, downstream traffic is lost.

After you configure the association between the IPv6 direct route and PW status, when the L3VE interface on AGG1 goes from Down to Up, PW1 does not become the primary PW immediately, and the cost of the IPv6 direct route between the CSG and AGG1 increases. In this case, RSGs do not preferentially select routes advertised by AGG1 and downstream traffic still travels along LinkB. After PW1 between the CSG and AGG1 becomes the primary PW, the cost of the IPv6 direct route between the CSG and AGG1 is restored to the default value 0. Then, RSGs preferentially select routes advertised by AGG1 and downstream traffic is switched over to LinkA. At this time, AGG1 has learned the MAC addresses of the base stations, downstream traffic loss will be reduced after the traffic is switched back.


#### Pre-configuration Tasks

Before configuring the association between the IPv4 direct route and PW status, configure link-layer protocol parameters and IP addresses for interfaces and ensure that the link layer protocol of each interface is Up.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface virtual-ethernet**](cmdqueryname=interface+virtual-ethernet) *interface-number*
   
   
   
   A VE interface is created, and the VE interface view is displayed.
3. Run [**ve-group**](cmdqueryname=ve-group) *ve-group-id* **l3-access**
   
   
   
   The VE interface is configured as an L3VE interface and bound to a VE-group.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The L2VPN can access the L3VPN only if the L2VE and L3VE interfaces are bound to the same VE-group and reside on the same board.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**interface virtual-ethernet**](cmdqueryname=interface+virtual-ethernet) *interface-number.subinterface-number*
   
   
   
   A VE sub-interface is created, and the VE sub-interface view is displayed.
6. Run [**direct-route track pw-state**](cmdqueryname=direct-route+track+pw-state) **degrade-cost** *cost*
   
   
   
   The association between the IPv4 direct route and PW status is configured.
   
   
   
   After you run the [**direct-route track pw-state**](cmdqueryname=direct-route+track+pw-state) command on an L3VE interface, the system adjusts the cost of the IPv4 direct route to the L3VE interface based on the PW status. If the PW is on standby, the system modifies the IPv4 direct route cost to the configured value *cost*. If the PW is active, the system restores the IPv4 direct route cost to the default value 0.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**direct-route track pw-state**](cmdqueryname=direct-route+track+pw-state), [**direct-route degrade-delay**](cmdqueryname=direct-route+degrade-delay), and [**direct-route track vrrp**](cmdqueryname=direct-route+track+vrrp) commands cannot all be configured on one L3VE interface. If you run the three commands on one L3VE interface, the latest configuration overrides the previous ones.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

If a PW has recovered but has not become active, run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* [ *ip-address* ] [ **verbose** ] command on an AGG. The command output shows that the IPv4 direct route to the L3VE interface has the configured cost. After a PW becomes active, run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* [ *ip-address* ] [ **verbose** ] command on an AGG. The command output shows that the IPv4 direct route to the L3VE interface has the default cost 0.