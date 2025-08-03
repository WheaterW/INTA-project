Configuring IPv6 IS-IS Route Selection
======================================

Configuring IS-IS route selection can achieve refined control over route selection.

#### Usage Scenario

After basic IPv6 IS-IS functions are configured, IS-IS routes will be generated, enabling communication between different nodes on a network.

If multiple routes are available, the route discovered by IS-IS may not be the expected one, which does not meet network planning requirements nor facilitate traffic management. To address this issue, configure IPv6 IS-IS route selection to implement refined control over route selection.

To implement refined control over IPv6 IS-IS route selection, perform the following operations:

* [Configure the costs for IPv6 IS-IS Interfaces](dc_vrp_isis_cfg_1026.html)![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Changing the IS-IS cost for an interface can control route selection, but routes on the interface need to be recalculated if a network topology changes, especially on a large-scale network. In addition, the configuration result may not meet your expectation.
  
  Therefore, configure IS-IS costs before configuring basic IS-IS functions.
* Configure IPv6 IS-IS route leaking.
* Configure rules for selecting equal-cost IPv6 IS-IS routes.
* Filter IPv6 IS-IS routes.
* Configure an overload bit for an IPv6 IS-IS device.


#### Pre-configuration Tasks

Before configuring IPv6 IS-IS route selection, complete the following tasks:

* Configure the link layer protocol on interfaces.
* Configure IP addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* [Configure basic IPv6 IS-IS functions](dc_vrp_isis_cfg_1023.html).


[Configuring IPv6 IS-IS Route Leaking](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1030.html)

Configuring IS-IS route leaking enables you to optimize IS-IS route selection on a two-level-area network.

[Configuring a Method for IS-IS to Process Equal-Cost Routes (IPv6)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1031_23.0.html)

If multiple equal-cost IPv6 routes are available on an IS-IS network, you can configure load balancing to increase the bandwidth utilization of each link, or configure weights for the equal-cost routes to facilitate service traffic management.

[Controlling Whether to Add IS-IS Routes to the IPv6 Routing Table](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1032.html)

If you do not want some IS-IS routes to be selected, you can configure a policy to prevent these routes from being added to the IP routing table.

[Configuring an Overload Bit for an IPv6 IS-IS Device](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1033.html)

If an IS-IS device needs to be temporarily isolated, configure the overload state for it to prevent other devices from forwarding traffic to this IS-IS device and prevent routing black holes.

[Configuring IS-IS to Generate IPv6 Default Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1034.html)

This section describes how to configure IS-IS to generate IPv6 default routes to control the advertising of IS-IS routing information.

[Configuring an IPv6 IS-IS Interface to Automatically Adjust the Link Cost](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1054.html)

Configuring an IPv6 IS-IS interface to automatically adjust the link cost based on link quality facilitates route selection control and improves network reliability.

[Verifying the IPv6 IS-IS Route Selection Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1035.html)

After configuring IPv6 IS-IS route selection, check the configurations.