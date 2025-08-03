Verifying the IPv4 User-Side Multicast Configuration
====================================================

This section describes how to verify multicast group joining information of online users and statistics about IGMP messages.

#### Procedure

* Run the following commands to display statistics about IGMP messages:
  
  
  + Run the [**display igmp statistics**](cmdqueryname=display+igmp+statistics) **user-id** *user-id* command to display statistics about IGMP messages.
  + Run the [**display igmp-snooping bas invalid-packet user-id**](cmdqueryname=display+igmp-snooping+bas+invalid-packet+user-id) *user-id* command to display statistics about invalid IGMP messages on broadband access server (BAS) interfaces.
* Run the following commands to display information about users and the multicast programs they join:
  
  
  + Run the [**display multicast user-id**](cmdqueryname=display+multicast+user-id) *UserIdValue* command to display information about multicast programs that a specified user joins on BAS interfaces.
  + Run the [**display multicast group-ip**](cmdqueryname=display+multicast+group-ip) *group-ipv4-address* command to display information about users of a specified multicast group.
  + Run the [**display multicast user-info**](cmdqueryname=display+multicast+user-info) **slot** *SlotNum* command to display information about users and the multicast programs they join on a specified slot or interface.
  + Run the [**display igmp-snooping bas port-info**](cmdqueryname=display+igmp-snooping+bas+port-info) **interface** *interface-name* command to display information about users and the multicast programs they join on a specified BAS interface.
  + Run the [**display igmp-snooping bas group-info**](cmdqueryname=display+igmp-snooping+bas+group-info) *interface-name* **user-id** *user-id* command to display information about multicast groups that a specified user joins on a BAS interface.
* Run the following command to display information about PIM entries and multicast routing entries:
  
  
  + Run the [**display pim routing-table**](cmdqueryname=display+pim+routing-table) command to display information about Protocol Independent Multicast (PIM) routing entries.
  + Run the [**display multicast routing-table**](cmdqueryname=display+multicast+routing-table) command to display information about multicast routing entries.