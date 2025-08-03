Configuring a BGP Peer Group
============================

Configuring BGP peer groups simplifies the BGP network configuration and improves the route advertisement efficiency.

#### Usage Scenario

A BGP peer group consists of BGP peers that have the same update policies and configurations.

A large-scale BGP network has a large number of peers. Configuring and maintaining these peers is difficult. To address this problem, configure a BGP peer group for BGP peers with the same configurations. Configuring BGP peer groups simplifies peer management and improves the route advertisement efficiency.

Based on the ASs where peers reside, peer groups are classified as follows:

* IBGP peer group: The peers of an IBGP peer group are in the same AS.
* Pure EBGP peer group: The peers of a pure EBGP peer group are in the same external AS.
* Mixed EBGP peer group: The peers of a mixed EBGP peer group are in different external ASs.

If a function is configured on a peer and its peer group, the function configured on the peer takes precedence. After a peer group is created, peers can be added to the peer group. If these peers are not configured separately, they will inherit the configurations of the peer group. If a peer in a peer group has a specific configuration requirement, the peer can be configured separately. The configuration of this peer will override the configuration that the peer has inherited from the peer group.


#### Pre-configuration Tasks

Before configuring BGP peer groups, [configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).


[Creating an IBGP Peer Group](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3030.html)

If multiple IBGP peers exist, adding them to an IBGP peer group can simplify the BGP network configuration and management. When creating an IBGP peer group, you do not need to specify an AS number for it.

[Creating a Pure EBGP Peer Group](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3031.html)

If multiple EBGP peers exist in an AS, adding them to an EBGP peer group can simplify the BGP network configuration and management. All the peers in a pure EBGP peer group must have the same AS number.

[Creating a Mixed EBGP Peer Group](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3032.html)

If multiple EBGP peers exist in different ASs, adding them to a mixed EBGP peer group can simplify the BGP network configuration and management. When creating a mixed EBGP peer group, specify an AS number for each peer.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3033.html)

After configuring a BGP peer group, check information about BGP peers and BGP peer groups.