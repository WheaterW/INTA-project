Configuring IPv4 User-Side Multicast
====================================

User-side multicast enables a BRAS to identify users who have joined or left a multicast group, implementing user-based multicast service control and management.

#### Usage Scenario

Conventional multicast cannot well support IPTV services on networks because it cannot identify users. Carriers need to have user-side multicast supported to identify users for better management. With user-side multicast, the BRAS can identify users in a multicast group and implement refined user service control and management.


#### Pre-configuration Tasks

Before configuring user-side multicast, complete the tasks shown in [Figure 1](#EN-US_TASK_0172367625__fig_dc_vrp_bras-multicast_cfg_000301). For configuration details, see [Table 1](#EN-US_TASK_0172367625__table_dc_vrp_bras-multicast_cfg_000301).

**Figure 1** Pre-configuration tasks for user-side multicast configurations  
![](images/fig_dc_vrp_bras-multicast_cfg_000301.png "Click to enlarge")  

**Table 1** Description of each pre-configuration task
| Item | Description |
| --- | --- |
|  | Configure an IPv4 Address Pool to Assign IP Addresses to Online Users. |
|  | Configure Authentication, Authorization and Accounting (AAA) schemes. |
|  | Configure a domain to implement AAA functions and manage access users. |
|  | Configure the PPPoE or IPoE access mode.   * [Configure the PPPoE access mode.](../ne/dc_ne_pppoe_cfg_0004.html) * Configure the IPoE access mode. |
|  | Configure basic multicast functions.   1. Configure multicast static routes. 2. Enable PIM-SM. 3. Enable IGMP. |
|  | Configure a BAS interface. |





#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *ifname*
   
   
   
   The interface or sub-interface view is displayed.
   
   
   
   The interface can be a main, a common sub-interface, or a QinQ sub-interface.
3. Run [**bas**](cmdqueryname=bas)
   
   
   
   A BAS interface is created, and the BAS interface view is displayed.
4. (Optional) Run [**igmp report loose check**](cmdqueryname=igmp+report+loose+check)
   
   
   
   The device is configured not to check the source MAC address or IP address of each received IGMP Report message.
5. Configure a multicast replication mode based on scenario requirements:
   
   
   * To use multicast replication by interface + VLAN, run the [**multicast copy by-vlan**](cmdqueryname=multicast+copy+by-vlan) command.
     
     In a scenario where multiple users order a multicast program through the same interface and VLAN and IGMP snooping is enabled on the downstream Layer 2 device, after multicast replication by interface + VLAN is configured, the BRAS replicates only one copy of a multicast traffic flow for the downstream Layer 2 device. Then, the downstream Layer 2 device replicates multicast data packets as needed. This replication mode therefore reduces the burden on the BRAS and the bandwidth consumption. This mode applies to scenarios where user packets carry VLAN tags and inter-VLAN traffic forwarding is not needed.
   * To use multicast replication by user (session), run the [**multicast copy by-session**](cmdqueryname=multicast+copy+by-session) command.
     
     In a scenario where the downstream Layer 2 device does not support IGMP snooping, after multicast replication by user is configured, the BRAS replicates multicast packets for each authenticated user. This mode prevents the BRAS from replicating multicast packets for users who fail to be authenticated, thus implementing refined user service control and management.
   * To use multicast replication by multicast VLAN, perform the following steps:
     
     1. Run [**quit**](cmdqueryname=quit)
        
        Return to the main or sub-interface view.
     2. Run [**multicast user-aggregation**](cmdqueryname=multicast+user-aggregation) **vlan** *vlan-id*
        
        Multicast replication by multicast VLAN is configured.
        
        This replication mode applies to scenarios where users have joined multicast VLANs. In this mode, the BRAS replicates multicast packets based on multicast VLANs, and the downstream Layer 2 device replicates multicast packets based on user VLANs. For users who go online through the same interface and join the same multicast program, the BRAS replicates only one copy of a multicast traffic flow to the downstream Layer 2 device, irrespective of whether the users belong to the same VLAN. The downstream Layer 2 device then replicates multicast packets based on user VLANs. This replication mode reduces the burden on the BRAS and the bandwidth consumption. This mode applies to scenarios where user packets carry VLAN tags and inter-VLAN traffic forwarding is needed.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If all of the preceding multicast replication modes are configured, their priorities are as follows in descending order: replication by interface + VLAN, replication by user, replication by multicast VLAN, and replication by interface.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the following commands to check statistics about IGMP messages:

* Run the [**display igmp statistics**](cmdqueryname=display+igmp+statistics) **all-user** command to check statistics about IGMP messages of all users.
* Run the [**display igmp-snooping bas invalid-packet**](cmdqueryname=display+igmp-snooping+bas+invalid-packet) command to check statistics about invalid IGMP messages on BAS interfaces.

Run the following command to check information about users and the multicast programs they join:

* Run the [**display multicast user-id**](cmdqueryname=display+multicast+user-id) *UserIdValue* command to check information about multicast programs that a specified user joins on a BAS interface.
* Run the [**display multicast group-ip**](cmdqueryname=display+multicast+group-ip) command to check information about users of a specified multicast group.
* Run the [**display multicast user-info**](cmdqueryname=display+multicast+user-info) command to check information about the users and the multicast programs they join on a specified interface or interface board.
* Run the [**display igmp-snooping bas port-info**](cmdqueryname=display+igmp-snooping+bas+port-info) command to check information about programs and their users on a BAS interface.
* Run the [**display igmp-snooping bas group-info user-id**](cmdqueryname=display+igmp-snooping+bas+group-info+user-id) command to check information about multicast groups that a specified user joins on a BAS interface.

Run the following commands to check Protocol Independent Multicast (PIM) entries and multicast routing entries:

* Run the [**display pim routing-table**](cmdqueryname=display+pim+routing-table) command to check information about PIM routing entries.
* Run the [**display multicast routing-table**](cmdqueryname=display+multicast+routing-table) command to check information about multicast routing entries.