Applying Filters to Received Routes
===================================

By applying filters of routing policies to routing protocols, you can filter received routes.

#### Usage Scenario

When exchanging routes on a network, devices need to accept only required routes. After defining a filter (such as the IP prefix list, ACL, or route-policy) of a routing policy, you need to apply the filter to routing protocols. You can use the **filter-policy** command in the protocol view and apply an ACL or an IP prefix list to filter the received routes. Only the routes that meet the matching rules are accepted.

The [**filter-policy import**](cmdqueryname=filter-policy+import) command is used to filter received routes. The influence of running the **filter-policy** command for a distance-vector protocol is different from that for a link-state protocol.

* Distance-vector protocol
  
  Distance-vector protocols generate routes based on their routing tables. Running the preceding command filters the routes received from neighbors and the routes to be advertised to neighbors.
* Link-state protocol
  
  Link-state routing protocols generate routes based on their LSDBs. Running the **filter-policy** command does not affect the integrity of link state advertisements or LSDBs. Therefore, running the **filter-policy** command has different impacts on route acceptance and advertisement.
  
  After routes are received, the **filter-policy** command determines which routes are to be added from the protocol routing table to the local core routing table. Therefore, running this command affects the local core routing table rather than the protocol routing table.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* BGP has powerful filtering functions. For the configuration of BGP routing policies, see "BGP Configuration."
* For details about **filter-policy** and [**import-route**](cmdqueryname=import-route) commands and their applications in RIP, OSPF, IS-IS, and BGP, see related configurations.


#### Pre-configuration Tasks

Before applying filters to imported routes, complete the following tasks:

* [Configure an IP prefix list](dc_vrp_route-policy_cfg_0003.html).
* Configure an ACL.
* [Configure a route-policy](dc_vrp_route-policy_cfg_0007.html).


[Configuring RIP to Filter the Received Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_route-policy_cfg_0041.html)

You can configure an inbound or outbound filtering policy by specifying Access Control Lists (ACLs) and IP address prefix lists to filter routes to be received and advertised. You can also configure a device to receive only the RIP packets from a specified neighbor.

[Configuring OSPF to Filter the Received Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_route-policy_cfg_0033.html)

After a filtering policy is configured for the OSPF routes that need to be delivered to the routing management module, only the routes that match the policy will be added to the routing table.

[Configuring IS-IS to Filter the Received Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_route-policy_cfg_0034.html)

By configuring IS-IS to filter the received routes, you can control the number of IS-IS routes to be added to the IP routing table, and thus reduce the size of the IP routing table.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_route-policy_cfg_0016.html)

After applying filters to the received routes, check information about the routing table of each protocol.