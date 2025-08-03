Verifying the IPv6 User-Side Multicast Configuration
====================================================

This section describes how to verify multicast group joining information of online users and statistics about MLD messages.

#### Procedure

* Run the following commands to display statistics about MLD messages:
  
  
  + Run the [**display mld statistics**](cmdqueryname=display+mld+statistics) command to display statistics about MLD messages.
  + Run the [**display mld-snooping bas invalid-packet**](cmdqueryname=display+mld-snooping+bas+invalid-packet) **user-id**  *user-id* command to display statistics about invalid MLD messages on broadband access server (BAS) interfaces.
* Run the following commands to display information about users and the multicast programs they join:
  
  
  + Run the [**display multicast user-id**](cmdqueryname=display+multicast+user-id) *UserIdValue* command to display information about multicast programs that a specified user joins on BAS interfaces.
  + Run the [**display multicast group-ip**](cmdqueryname=display+multicast+group-ip) *group-ipv6-address* command to display information about users of a specified multicast group.
  + Run the [**display multicast user-info**](cmdqueryname=display+multicast+user-info) **out-interface**  *oif-port-name* command to display information about users and the multicast programs they join on a specified slot or interface.
  + Run the [**display mld-snooping bas port-info**](cmdqueryname=display+mld-snooping+bas+port-info)  **interface** *interface-name* command to display user information of multicast programs on a specified BAS interface.
  + Run the [**display mld-snooping bas group-info**](cmdqueryname=display+mld-snooping+bas+group-info) *interface-name* **user-id** *user-id* command to display information about multicast groups that a specified user joins on a BAS interface.
* Run the following command to display information about IPv6 Protocol Independent Multicast (PIM) entries and IPv6 multicast routing entries:
  
  
  + Run the [**display pim ipv6 routing-table**](cmdqueryname=display+pim+ipv6+routing-table) command to display information about IPv6 PIM routing entries.
  + Run the [**display multicast ipv6 routing-table**](cmdqueryname=display+multicast+ipv6+routing-table) command to display information about IPv6 multicast routing entries.