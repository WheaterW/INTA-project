Configuring RPF Routes
======================

A multicast routing protocol creates multicast routing entries based on the Reverse Path Forwarding (RPF) mechanism and then establishes an MDT.

#### Usage Scenario

The RPF check is a basis of multicast routing. The process of performing an RPF check is as follows:

1. Based on the source of a packet, a router searches its unicast routing table and multicast static routing table for optimal routes.
2. The router selects a route with the highest priority from the multiple optimal routes as an RPF route. If the inbound interface of the packet is the same as the RPF interface, the packet passes the RPF check; otherwise, the packet fails the RPF check.
   
   If the priorities of the optimal routes are the same, the router selects the route in the sequence of the multicast static route and unicast route.

By configuring multicast static routes, you can specify an RPF interface and an RPF neighbor for the specific source of packets.

In choosing an upstream interface, a multicast Router prefers the route with the highest next-hop address by default. If there are multiple equal-cost unicast routes, you can configure different policies of implementing multicast load splitting among these routes and designating different upstream interfaces for different multicast entries. In this manner, the transmission of multiple multicast data flows over a network is optimized.


#### Pre-configuration Tasks

Before configuring RPF routes, complete the following tasks:

* Configure a unicast routing protocol to ensure that unicast routes are reachable.
* Configure basic multicast functions.


[Configuring Multicast Static Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0081.html)

Multicast static routes are an important basis of the Reverse Path Forwarding (RPF) check. By configuring multicast static routes, you can specify an RPF interface and an RPF neighbor for the specific source of packets.

[Configuring Multicast Load Splitting](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0082.html)

Multicast load splitting applies to the scenario in which multiple equal-cost unicast routes of the same type exist. In such a case, multicast load splitting can be performed based on configured policies to optimize the transmission of multiple multicast data flows.

[Configuring Longest Match for Multicast Route Selection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2202.html)

If the longest match principle is configured for route selection, an optimal intra-domain unicast route, an optimal inter-domain unicast route, and an optimal multicast static route are selected. One of them is finally selected as the multicast data forwarding path.

[Verifying the RPF Route Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0083.html)

After configuring Reverse Path Forwarding (RPF) routes, verify configuration of the RPF routes.