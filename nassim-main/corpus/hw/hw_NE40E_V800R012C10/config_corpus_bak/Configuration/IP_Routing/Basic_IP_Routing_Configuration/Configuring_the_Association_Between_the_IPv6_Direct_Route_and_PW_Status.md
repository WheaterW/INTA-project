Configuring the Association Between the IPv6 Direct Route and PW Status
=======================================================================

This section describes how to configure the association between the IPv6 direct route and pseudo wire (PW) status. During traffic switchback after the primary PW recovers, this configuration minimizes traffic loss and improves network reliability.

#### Usage Scenario

As shown in [Figure 1](#EN-US_TASK_0172365350__fig_dc_vrp_ip-route_cfg_005901), PWs are set up between access aggregation gateways (AGGs) and the cell site gateway (CSG), while BGP virtual private network version 6 (VPNv6) peer relationships are set up between AGGs and radio network controller site gateways (RSGs). Layer 3 Virtual Ethernet (L3VE) interfaces are configured on AGGs and VPN instances are bound to the L3VE interfaces, so that the CSG can access the Layer 3 virtual private network (L3VPN). BGP is configured on AGGs to import IPv6 direct routes between the CSG and AGGs. These IPv6 direct routes are converted to BGP VPNv6 routes and advertised to RSGs.

**Figure 1** Networking of the association between the IPv6 direct route and PW status  
![](images/fig_dc_vrp_ip-route_cfg_005901.png)  

AGG1 is used as the master device in the preceding figure. In normal cases, RSGs select routes advertised by AGG1 and traffic travels along LinkA. If AGG1 or the CSG-AGG1 link fails, traffic is switched over to LinkB. After AGG1 or the CSG-AGG1 link recovers, the L3VE interface on AGG1 goes from Down to Up, and AGG1 immediately generates an IPv6 direct route destined for the CSG and advertises the route to RSGs. Downstream traffic is then switched over to LinkA. However, AGG1 has not learned the MAC addresses of the base stations yet and PW1 is standing by, so downstream traffic will be lost.

After you configure the association between the IPv6 direct route and PW status, when the L3VE interface on AGG1 goes from Down to Up, PW1 does not become the primary PW immediately, and the cost of the IPv6 direct route between the CSG and AGG1 increases. In this case, RSGs do not preferentially select routes advertised by AGG1 and downstream traffic still travels along LinkB. After PW1 between the CSG and AGG1 becomes the primary PW, the cost of the IPv6 direct route between the CSG and AGG1 is restored to the default value 0. Then, RSGs preferentially select routes advertised by AGG1 and downstream traffic is switched over to LinkA. At this time, AGG1 has learned the MAC addresses of the base stations, downstream traffic loss will be reduced after the traffic is switched back.


#### Pre-configuration Tasks

Before configuring the association between the IPv6 direct route and PW status, complete the following tasks:

* Configure link-layer protocol parameters and IP addresses for interfaces to ensure that the link layer protocol status of each interface is up.

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
7. Run [**direct-route ipv6 track pw-state**](cmdqueryname=direct-route+ipv6+track+pw-state) **degrade-cost** *cost*
   
   
   
   The association between the IPv6 direct route and PW status is configured.
   
   
   
   After you run the [**direct-route ipv6 track pw-state**](cmdqueryname=direct-route+ipv6+track+pw-state) command on an interface, the system adjusts the cost of the IPv6 direct route on an interface based on the PW status. If the PW is standby, the system modifies the IPv6 direct route cost to the configured value *cost*. If the PW is active, the system restores the IPv6 direct route cost to the default value 0.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**direct-route ipv6 track pw-state**](cmdqueryname=direct-route+ipv6+track+pw-state) command and the [**direct-route ipv6 degrade-delay**](cmdqueryname=direct-route+ipv6+degrade-delay) command cannot be both configured on one L3VE interface.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

If a PW has recovered but has not become active, run the [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* [ *ipv6-address* ] [ **verbose** ] command on an AGG. The command output shows that the IPv6 direct route to the L3VE interface has the configured cost. After a PW becomes active, run the [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* [ *ipv6-address* ] [ **verbose** ] command on an AGG. The command output shows that the IPv6 direct route to the L3VE interface has the default cost 0.