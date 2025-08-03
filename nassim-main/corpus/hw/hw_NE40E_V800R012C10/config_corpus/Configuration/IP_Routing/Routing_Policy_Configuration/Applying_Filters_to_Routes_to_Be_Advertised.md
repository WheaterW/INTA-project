Applying Filters to Routes to Be Advertised
===========================================

By applying filters of routing policies to routing protocols, you can filter routes to be advertised.

#### Usage Scenario

To enable a device to advertise required routes, define the filter (such as the IP prefix list, ACL, or route-policy) for a routing policy, apply the filter to routing protocols, and run the **filter-policy** command specified with the filter in the related protocol view to filter the routes to be advertised.

The function of the [**filter-policy export**](cmdqueryname=filter-policy+export) command varies the protocol type. And the functions to a distance-vector protocol and a link-state protocol are as follows:

* Distance-vector protocol
  
  A distance-vector protocol generates routes based on the routing table. Therefore, the command filters the routes received from neighbors and the routes to be advertised to neighbors.
* Link-state protocol
  
  A link-state protocol generates routes based on the LSDB. The **filter-policy** command does not affect any Link State Advertisement (LSA) or LSDB.
  
  When advertising routes, you can run the [**filter-policy export**](cmdqueryname=filter-policy+export) command to determine whether to advertise the imported routes (such as the imported RIP routes). Only the LSAs or Link State PDUs (LSPs) that are imported using the [**filter-policy import**](cmdqueryname=filter-policy+import) command are added to the LSDB. This does not affect the LSAs advertised to other routers.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* BGP has the powerful filtering function. For the configuration of BGP routing policies, refer to "BGP Configuration."
* For details of the **filter-policy** and [**import-route**](cmdqueryname=import-route) commands and their applications in RIP, OSPF, IS-IS, and BGP, refer to related configurations.


#### Pre-configuration Tasks

Before applying filters to routes to be advertised, complete the following tasks:

* [Configure an IP prefix list](dc_vrp_route-policy_cfg_0003.html).
* Configure an ACL.
* [Configure a route-policy](dc_vrp_route-policy_cfg_0007.html).


[Configuring RIP to Filter the Routes to Be Advertised](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_route-policy_cfg_0035.html)

You can set conditions to filter the routes to be advertised. Only the routes that meet the conditions can be advertised.

[Configuring OSPF to Filter the Routes to Be Advertised](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_route-policy_cfg_0036.html)

After a filtering policy is configured for routes imported by OSPF, only the routes that match the policy can be advertised.

[Configuring IS-IS to Filter the Routes to Be Advertised](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_route-policy_cfg_0037.html)

By configuring IS-IS to filter the routes to be advertised, you can effectively control the number of IS-IS routes on the network.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_route-policy_cfg_0021.html)

After applying filters to the routes to be advertised, check information about the routing table of each protocol.