Controlling MBGP Route Advertisement
====================================

MBGP can filter or apply routing policies to the routes to be advertised to a peer or peer group.

#### Usage Scenario

To exchange routing information between devices, MBGP advertises routes to peers based on network planning. MBGP can filter or apply routing policies to the routes to be advertised to a peer or peer group.


#### Pre-configuration Tasks

Before controlling MBGP route advertisement, [configure an MBGP peer](dc_vrp_multicast_cfg_1003.html).


[Summarizing Local MBGP Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_1006.html)

Configuring route summarization can reduce the size of a routing table on a peer.

[Configuring MBGP to Advertise Default Routes to Peers](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_1007.html)

A device sends a default route with the local address as the next hop address to the specified peer for load balancing, regardless of whether there are default routes in the local routing table. This greatly reduces the number of routes on the network.

[Configuring MBGP to Advertise the Community Attribute](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_1008.html)

The community and extended community attributes are used to simplify routing policy management.

[Verifying the Configuration of MBGP Route Advertisement](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_1009.html)

After configuring MBGP route advertisement, verify MBGP routing information.