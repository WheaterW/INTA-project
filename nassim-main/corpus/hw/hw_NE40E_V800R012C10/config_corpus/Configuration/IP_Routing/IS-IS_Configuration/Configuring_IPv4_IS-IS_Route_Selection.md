Configuring IPv4 IS-IS Route Selection
======================================

Configuring IS-IS route selection can achieve refined control over route selection.

#### Usage Scenario

After basic IPv4 IS-IS functions are configured, IS-IS routes will be generated, enabling communication between different nodes on a network.

If multiple routes are available, the route discovered by IS-IS may not be the expected one, which does not meet network planning requirements nor facilitate traffic management. To address this issue, configure IPv4 IS-IS route selection to implement refined control over route selection.

To implement refined control over IPv4 IS-IS route selection, perform the following operations:

* [Configure the costs for IPv4 IS-IS interfaces.](dc_vrp_isis_cfg_1003.html)![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Changing the IS-IS cost for an interface can control route selection, but routes on the interface need to be recalculated if a network topology changes, especially on a large-scale network. In addition, the configuration result may not meet your expectation.
  
  Therefore, configure IS-IS costs before configuring basic IS-IS functions.
* Configure IPv4 IS-IS route leaking.
* Configure rules for selecting equal-cost IPv4 IS-IS routes.
* Filter IPv4 IS-IS routes.
* Configure an overload bit for an IPv4 IS-IS device.
* Configure an IPv4 IS-IS interface to automatically adjust the link cost.


#### Pre-configuration Tasks

Before configuring IPv4 IS-IS route selection, complete the following tasks:

* Configure IP addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* [Configure basic IPv4 IS-IS functions](dc_vrp_isis_cfg_1000.html).


[Configuring IS-IS Route Leaking (IPv4)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1007.html)

Configuring IS-IS route leaking enables you to optimize IS-IS route selection on a two-level-area network.

[Configuring a Method for IS-IS to Process Equal-Cost Routes (IPv4)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1008.html)

If multiple equal-cost routes are available on an IS-IS network, you can configure load balancing to increase the bandwidth usage of each link, or configure weights for the equal-cost routes to facilitate service traffic management.

[Filtering IPv4 IS-IS Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1009.html)

If some IS-IS routes are not preferred, configure conditions to filter IS-IS routes. Only IS-IS routes meeting the specified conditions can be added to an IP routing table.

[Configuring an Overload Bit for an IPv4 IS-IS Device](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1010.html)

If an IS-IS device needs to be temporarily isolated, configure the overload state for it to prevent other devices from forwarding traffic to this IS-IS device and prevent routing black holes.

[Configuring IS-IS to Generate IPv4 Default Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1011.html)

This section describes how to configure IS-IS to generate default routes to control the advertising of IS-IS routing information.

[Configuring an IPv4 IS-IS Interface to Automatically Adjust the Link Cost](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1046.html)

Configuring an IS-IS interface to automatically adjust the link cost based on link quality facilitates route selection control and improves network reliability.

[Configuring IPv4 IS-IS Route Recursion to IPv6 Next Hops](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1065.html)

Configuring IPv4 IS-IS route recursion to IPv6 next hops allows IPv4 routes to be forwarded on IPv6 networks, improving network compatibility.

[Verifying the IPv4 IS-IS Route Selection Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1012.html)

After configuring IPv4 IS-IS route selection, check the configurations.