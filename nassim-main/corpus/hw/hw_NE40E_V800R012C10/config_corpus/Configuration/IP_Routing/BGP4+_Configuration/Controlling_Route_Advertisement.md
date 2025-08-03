Controlling Route Advertisement
===============================

BGP4+ can filter or apply routing policies to the routes to be advertised to a peer or peer group.

#### Usage Scenario

BGP4+ advertises routes to peers based on the network plan to exchange routing information between devices. The routes can be filtered or processed based on a routing policy before being advertised to a peer or peer group.


#### Pre-configuration Tasks

Before controlling route advertisement, [configure basic BGP4+ functions](dc_vrp_bgp6_cfg_0003.html).


[Configuring BGP4+ Route Summarization](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0014.html)

Configuring route summarization can reduce the size of a routing table on a peer.

[Configuring BGP4+ to Advertise Default Routes to Peers or Peer Groups](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0015.html)

A device sends a default route with the local address as the next hop address to the specified peer for load balancing, regardless of whether there are default routes in the local routing table. This greatly reduces the number of routes on the network.

[Enabling a BGP4+ Device to Add the Community Attribute to Routes to Be Advertised](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0016.html)

The community attribute is used to simplify route-policy management.

[Enabling a BGP4+ Device to Add the Large-Community Attribute to Routes to Be Advertised](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0047.html)

The Large-Community attribute can be flexibly applied in route-policies.

[(Optional) Setting the Interval at Which Update Messages Are Sent](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0017.html)

When routes change, the Router sends Update messages to notify its peers. If a route changes frequently, to prevent the Router from sending Update messages upon every change, you can set an interval at which Update messages are sent as required.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0018.html)

After controlling route advertisement, check information about filtered and advertised routes.