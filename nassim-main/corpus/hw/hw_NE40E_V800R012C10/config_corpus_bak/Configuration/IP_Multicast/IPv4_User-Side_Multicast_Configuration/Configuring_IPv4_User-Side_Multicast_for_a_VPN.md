Configuring IPv4 User-Side Multicast for a VPN
==============================================

To enable a device to identify users of multicast programs in a VPN and to implement refined management of users in the VPN, configure IPv4 user-side multicast for the VPN.

#### Usage Scenario

User-side multicast for a VPN enables a device to identify users of multicast programs in the VPN, thus allowing for refined management of the users. Before configuring user-side multicast for a VPN, bind a BAS interface to the multicast VPN. A BAS interface can be bound to multiple multicast VPN instances, and the binding configurations apply to all sub-interfaces of the BAS interface. In this manner, when users send Join messages, the device can identify the VPN information of the users on each sub-interface and forward the messages to the corresponding VPNs. If a user does not belong to any VPN instance configured on the BAS interface, the device drops the multicast messages sent by this user.


#### Pre-configuration Tasks

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This configuration process is supported only on the Admin-VS.

Before configuring IPv4 user-side multicast for a VPN, complete the following tasks:

* [Configure user-side multicast.](dc_vrp_bras-multicast_cfg_0003.html)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**multicast binding vpn-instance**](cmdqueryname=multicast+binding+vpn-instance) *vpn-instance-name*
   
   
   
   The interface is bound to a specified multicast VPN instance.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command can be run only on main interfaces.
   
   An interface can be bound to multiple multicast VPN instances.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

Run the following commands to check information about users and the multicast programs they join:

* Run the [**display multicast user-ip**](cmdqueryname=display+multicast+user-ip) *UserIpV4* command to check information about multicast programs that a specified user orders on a specified BAS interface in a specified VPN instance.
* Run the [**display multicast group-ip**](cmdqueryname=display+multicast+group-ip) command to check information about users that join a specified multicast group, with the group address, outbound interface, and VPN instance name being specified.
* Run the [**display igmp-snooping bas port-info**](cmdqueryname=display+igmp-snooping+bas+port-info) command to check information about programs and their users on a specified BAS interface and in a specified VPN instance.
* Run the [**display igmp-snooping bas group-info**](cmdqueryname=display+igmp-snooping+bas+group-info) command to check information about a specified multicast group that a user joins, with the BAS interface, user ID, group address, and VPN instance name being specified.

Run the following commands to check information about the PIM and multicast routing entries of a VPN instance:

* Run the [**display pim**](cmdqueryname=display+pim) **vpn-instance** *vpn-instance-name* **routing-table** command to check PIM entries of a specified VPN instance.
* Run the [**display multicast**](cmdqueryname=display+multicast) **vpn-instance** *vpn-instance-name* **routing-table** command to check multicast routing entries of a specified VPN instance.