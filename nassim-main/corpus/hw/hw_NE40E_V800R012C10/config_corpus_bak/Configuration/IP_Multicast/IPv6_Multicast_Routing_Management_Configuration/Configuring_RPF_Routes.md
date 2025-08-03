Configuring RPF Routes
======================

A multicast routing protocol creates multicast routing entries based on the Reverse Path Forwarding (RPF) mechanism and then establishes an MDT.

#### Usage Scenario

The RPF check is a basis of multicast routing. The process of performing an RPF check is as follows:

1. The device selects an optimal route each from the unicast routing table and multicast static routing table according to the source address of the multicast packet.
2. The device selects a route with the highest priority from multiple optimal routes as an RPF route. If the inbound interface of the packet is the same as the RPF interface, the packet passes the RPF check; otherwise, the packet fails the RPF check.
   
   If the priorities of the optimal routes are the same, the router selects the route in the sequence of the multicast static route and unicast route.

By configuring multicast static routes, you can specify an RPF interface and an RPF neighbor for a specified packet source.

In choosing an upstream interface, a multicast Router prefers the route with the highest next-hop address by default. If there are multiple equal-cost unicast routes, you can configure different policies of implementing multicast load splitting among these routes and designating different upstream interfaces for different multicast entries. In this manner, the transmission of multiple multicast data flows over a network is optimized.


#### Pre-configuration Tasks

Before configuring RPF routes, complete the following tasks:

* Configure a unicast routing protocol to ensure that unicast routes are reachable.
* Configure basic multicast functions.


[Configuring IPv6 Multicast Static Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_ipv6_cfg_0004.html)

Multicast static routes are an important basis for Reverse Path Forwarding (RPF) check. By configuring multicast static routes, you can specify an RPF interface and an RPF neighbor for a specified packet source.

[Configuring IPv6 Multicast Load Splitting](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_ipv6_cfg_0005.html)

IPv6 multicast load splitting is applicable to the scenario where multiple equal-cost IPv6 unicast routes of the same type exist. If multiple equal-cost routes exist on a network, IPv6 multicast load splitting can be performed for multicast traffic based on different policies. This optimizes network traffic transmission in the case of multiple IPv6 multicast data flows.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_ipv6_cfg_0006.html)

After configuring Reverse Path Forwarding (RPF) routes, check RPF routing information of a specified multicast source.