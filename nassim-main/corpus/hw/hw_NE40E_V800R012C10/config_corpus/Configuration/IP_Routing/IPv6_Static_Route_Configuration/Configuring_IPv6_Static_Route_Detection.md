Configuring IPv6 Static Route Detection
=======================================

With IPv6 static route detection, if a link through which an IPv6 static route travels fails, a rapid link switchover is performed, preventing lengthy service interruptions.

#### Usage Scenario

Unlike dynamic routes, static routes do not have a detection mechanism. As a result, administrator intervention is required if a fault occurs on the network. To prevent the need for administrator intervention, deploy IPv6 static route detection to implement automatic rapid link switchover if a link failure occurs. IPv6 static route detection prevents lengthy service interruptions.

The following IPv6 static route detection methods are available:

* BFD for IPv6 static routes: After BFD for IPv6 static routes is configured, each static route can be bound to a BFD session. BFD for IPv6 static routes implements millisecond-level detection. BFD is classified as static BFD or dynamic BFD.
* Network quality analysis (NQA) for IPv6 static routes: Although BFD for IPv6 static routes implements fast link fault detection, it cannot be deployed in some scenarios (when Layer 2 devices exist on the network, for example) because both ends of the link must support BFD. NQA for IPv6 static routes, however, can monitor the link status of a static route even when only one end supports NQA. NQA for IPv6 static routes implements second-level detection.![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Only one of the IPv6 static route detection methods can be deployed. Therefore, choose one based on the live network requirements.

#### Pre-configuration Tasks

Before configuring IPv6 static route detection, configure link-layer protocol parameters and IPv6 addresses for interfaces to ensure that the link layer protocol of each interface is Up.


[Configuring Dynamic BFD for IPv6 Static Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_static-route_disjoin_cfg_0023.html)

Dynamic BFD for IPv6 static routes enables devices to fast detect link changes, improving network reliability.

[Configuring Static BFD for IPv6 Static Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_static-route_disjoin_cfg_0028.html)

Static BFD for IPv6 static routes enables devices to fast detect link changes, improving network reliability.

[Configuring NQA for IPv6 Static Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_static-route_disjoin_cfg_0039.html)

If an IPv6 static route is associated with a network quality analysis (NQA) test instance, NQA tests the link status periodically. If NQA detects a fault along the associated IPv6 static route, the IPv6 static route is deleted, and traffic is switched to another route.

[Configuring NQA Group for IPv6 Static Route](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_static-route_disjoin_cfg_0076.html)

After an IPv6 static route is associated with an NQA group, if the NQA group detects a link fault, it withdraws the IPv6 static route, triggering traffic switching and ensuring network stability.