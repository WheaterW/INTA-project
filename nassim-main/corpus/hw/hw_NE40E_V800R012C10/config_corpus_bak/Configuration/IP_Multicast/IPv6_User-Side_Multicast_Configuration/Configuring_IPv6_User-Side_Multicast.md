Configuring IPv6 User-Side Multicast
====================================

User-side multicast enables a BRAS on an IPv6 network to identify users who have joined or left a multicast group, implementing user-based multicast service control and management.

#### Usage Scenario

Conventional multicast cannot well support IPTV services on IPv6 networks because it cannot identify users. Carriers need to have user-side multicast supported to identify users for better management. With IPv6 user-side multicast, the BRAS can identify users in a multicast group and implement refined user service control and management.


#### Pre-configuration Tasks

Before configuring IPv6 user-side multicast, complete the tasks shown in [Figure 1](#EN-US_TASK_0172367700__fig_dc_vrp_ipv6bras-multicast_cfg_000301). For configuration details, see [Table 1](#EN-US_TASK_0172367700__table_dc_vrp_ipv6bras-multicast_cfg_000301).

**Figure 1** Pre-configuration tasks for user-side multicast configurations in IPv6  
![](images/fig_dc_vrp_ipv6bras-multicast_cfg_000301.png)

**Table 1** Description of each pre-configuration task
| Item | Description |
| --- | --- |
|  | Configure a local prefix pool and a local address pool. Bind the local prefix pool to the local address pool. |
|  | Configure Authentication, Authorization and Accounting (AAA) schemes. |
|  | Configure a domain and bind the local address pool to the domain. |
|  | Configure the PPPoE or IPoE access mode.   * [Configure the PPPoE access mode.](../ne/dc_ne_pppoe_cfg_0004.html) * Configure the IPoE access mode. |
|  | Configure basic multicast functions.   1. [Enable IPv6 multicast routing.](dc_vrp_multicast_cfg_2006.html) 2. [Enable IPv6 PIM-SM.](dc_vrp_multicast_cfg_2007.html) 3. [Enable MLD.](dc_vrp_multicast_cfg_2074.html) |
|  | Configure a BAS interface. |





#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *ifname*
   
   
   
   The interface or sub-interface view is displayed.
   
   The interface can be a main, a common sub-interface, or a QinQ sub-interface.
3. Run [**bas**](cmdqueryname=bas)
   
   
   
   A BAS interface is created, and the BAS interface view is displayed.
4. Configure a multicast replication mode as required.
   
   
   * To use multicast replication by interface + VLAN, run the [**multicast copy by-vlan**](cmdqueryname=multicast+copy+by-vlan) command.
     
     In a scenario where multiple users order a multicast program through the same interface and VLAN and MLD snooping is enabled on the downstream Layer 2 device, after multicast replication by interface + VLAN is configured, the BRAS replicates only one copy of a multicast traffic flow for the downstream Layer 2 device. Then, the downstream Layer 2 device replicates multicast data packets as needed. This replication mode reduces the burden on the BRAS and the bandwidth consumption. This mode applies to scenarios where user packets carry VLAN tags and inter-VLAN traffic forwarding is not needed.
   * To use multicast replication by user (session), run the [**multicast copy by-session**](cmdqueryname=multicast+copy+by-session) command.
     
     In a scenario where the downstream Layer 2 device does not support MLD snooping, after multicast replication by user is configured, the BRAS replicates multicast packets for each authenticated user. This mode prevents the BRAS from replicating multicast packets for users who fail to be authenticated, thus implementing refined user service control and management.
   * To use multicast replication by multicast VLAN, perform the following steps:
     
     1. Run the [**quit**](cmdqueryname=quit) command to return to the main or sub-interface view.
     2. Run the [**multicast user-aggregation**](cmdqueryname=multicast+user-aggregation) **vlan** *vlan-id* command to configure multicast replication by multicast VLAN.
        
        This replication mode applies to scenarios where users have joined multicast VLANs. In this mode, the BRAS replicates multicast packets based on multicast VLANs, and the downstream Layer 2 device replicates multicast packets based on user VLANs. For users who go online through the same interface and join the same multicast program, the BRAS replicates only one copy of a multicast traffic flow to the downstream Layer 2 device, irrespective of whether the users belong to the same VLAN. The downstream Layer 2 device then replicates multicast packets based on user VLANs. This replication mode reduces the burden on the BRAS and the bandwidth consumption. This mode applies to scenarios where user packets carry VLAN tags and inter-VLAN traffic forwarding is needed.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If all of the preceding multicast replication modes are configured, their priorities are as follows in descending order: replication by interface + VLAN, replication by user, replication by multicast VLAN, and replication by interface.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the following commands to check statistics about MLD messages:

* Run the [**display mld-snooping bas invalid-packet**](cmdqueryname=display+mld-snooping+bas+invalid-packet) command to check statistics about invalid MLD messages on BAS interfaces.

Run the following command to check information about users and the multicast programs they join:

* Run the [**display multicast user-id**](cmdqueryname=display+multicast+user-id) *UserIdValue* command to check information about multicast programs that a specified user joins on a BAS interface.
* Run the [**display multicast group-ip**](cmdqueryname=display+multicast+group-ip) command to check information about users of a specified multicast group.
* Run the [**display mld-snooping bas port-info**](cmdqueryname=display+mld-snooping+bas+port-info) **interface** *interface-name* command to check user information of multicast programs on a BAS interface.

Run the following commands to check IPv6 multicast routing entries:

* Run the [**display multicast ipv6 routing-table**](cmdqueryname=display+multicast+ipv6+routing-table) command to check information about IPv6 multicast routing entries.