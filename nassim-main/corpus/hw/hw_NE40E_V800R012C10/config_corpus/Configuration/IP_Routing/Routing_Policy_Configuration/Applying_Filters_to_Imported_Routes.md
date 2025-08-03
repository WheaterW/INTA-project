Applying Filters to Imported Routes
===================================

By applying filters of routing policies to routing protocols, you can filter the imported routes.

#### Usage Scenario

After defining a filter (such as the IP prefix list, ACL, or route-policy) of a routing policy, you need to apply the filter to routing protocols.

You can apply routing policies when you want to import external routes:

* You can use the [**import-route**](cmdqueryname=import-route) command in the related protocol view, import the required external routes to the protocols, and apply a route-policy to filter imported routes.
* After external routes are imported, you can run the [**filter-policy export**](cmdqueryname=filter-policy+export) command to filter the imported external routes. Only the routes that meet the matching rules are advertised.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* BGP has the powerful filtering function. For the configuration of BGP routing policies, refer to "BGP Configuration."
* For details of the **filter-policy** and [**import-route**](cmdqueryname=import-route) commands and their applications in RIP, OSPF, IS-IS, and BGP, refer to related configurations.


#### Pre-configuration Tasks

Before applying filters to imported routes, complete the following tasks:

* [Configure an IP prefix list](dc_vrp_route-policy_cfg_0003.html).
* Configure an ACL.
* [Configure a route-policy](dc_vrp_route-policy_cfg_0007.html).


[Configuring RIP to Import External Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_route-policy_cfg_0038.html)

Routing Information Protocol (RIP) can import routes from other processes or other routing protocols to enrich the RIP routing table.

[Configuring OSPF to Import External Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_route-policy_cfg_0039.html)

Importing the routes discovered by other routing protocols can enrich OSPF routing information.

[Configuring IS-IS to Import External Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_route-policy_cfg_0040.html)

By configuring IS-IS to import routes, you can enable IS-IS to learn routing information of other protocols or other IS-IS processes.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_route-policy_cfg_0026.html)

After applying filters to the imported routes, check information about the routing table of each protocol.