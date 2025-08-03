Configuring IPv4 Static Route Detection
=======================================

With IPv4 static route detection, if a link through which an IPv4 static route travels fails, a rapid link switchover is performed, preventing lengthy service interruptions.

#### Usage Scenario

Unlike dynamic routes, static routes do not have a detection mechanism. As a result, administrator intervention is required if a fault occurs on the network. Static route detection methods can be used to quickly detect link faults. If a link fails, a link switchover is performed quickly to prevent lengthy service interruption.

The following IPv4 static route detection methods are available:

* BFD for IPv4 static route: BFD for IPv4 static route can be used to bind a BFD session to each static route. BFD sessions can be used to detect link faults in milliseconds. BFD is classified as static BFD or dynamic BFD.
* Network quality analysis (NQA) for IPv4 static route: Although BFD for IPv4 static route implements fast link fault detection, it cannot be deployed in some scenarios (when Layer 2 devices exist on the network, for example) because both ends of the link must support BFD. NQA for IPv4 static route, however, can monitor the link status of a static route even when only one end supports NQA. NQA for IPv4 static route implements second-level detection.
* Association between Ethernet in the First Mile (EFM) and IPv4 static routes: After EFM OAM is enabled, EFM can be associated with IPv4 static routes. EFM for IPv4 static routes enables the system to respond to interface up or down events and determine whether to activate static routes. This mechanism controls route advertisement and ensures that the traffic from the remote end can be correctly forwarded.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only one of the preceding static route detection methods can be deployed. Therefore, choose one based on the live network requirements.



#### Pre-configuration Tasks

Before configuring IPv4 static route detection, configure link-layer protocol parameters and IP addresses for interfaces to ensure that the link layer protocol of each interface is up.


[Configuring Dynamic BFD for IPv4 Static Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_static-route_disjoin_cfg_0012.html)

Dynamic BFD for IPv4 static routes enables devices to fast detect link changes, improving network reliability.

[Configuring Static BFD for IPv4 Static Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_static-route_disjoin_cfg_0027.html)

Static BFD for IPv4 static routes enables devices to fast detect link changes, improving network reliability.

[Configuring NQA for IPv4 Static Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_static-route_disjoin_cfg_0035.html)

If an IPv4 static route is associated with a network quality analysis (NQA) test instance, NQA tests the link status periodically. If NQA detects a fault along the associated IPv4 static route, the IPv4 static route is deleted, and traffic is switched to another route.

[Configuring NQA Group for IPv4 Static Route](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_static-route_disjoin_cfg_0075.html)

After an IPv4 static route is associated with an NQA group, if the NQA group detects a link fault, it withdraws the IPv4 static route, triggering traffic switching and ensuring network stability.

[Associating EFM with IPv4 Static Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_static-route_disjoin_cfg_0048.html)

After EFM is associated with IPv4 static routes, the system determines whether to activate the static routes based on the EFM session status.