Configuring BGP4+ Routing Policies
==================================

BGP4+ routing policies can be configured to flexibly control the sending and receiving of routes.

#### Usage Scenario

Routing policies can set or re-set BGP4+ route attributes using some predefined conditions, which provides a flexible and effective method to control BGP4+ route selection. The sending and receiving of routes can be flexibly controlled by applying BGP4+ routing policies.

Based on the import (or export) routing policy specified by the peer, the associated import (or export) routing conditions (**if-match** clauses) can be configured to filter routes, and **apply** clauses can be configured to set or modify route attributes. The routes that match the routing policy will be received (or sent).


#### Pre-configuration Tasks

Before configuring BGP4+ routing policies, complete the following tasks:

* Configure network-layer addresses for interfaces to ensure that neighboring devices are reachable at the network layer.
* [Configure basic BGP4+ functions](dc_vrp_bgp6_cfg_0003.html).


[Configuring BGP4+ Filters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0028.html)

BGP4+ filters can be used in routing policies or when you want to check BGP4+ running status as required.

[Configuring a Route-Policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0029.html)

A route-policy is used to match routes or route attributes, and to change route attributes when the matching rules are met.

[Applying a Policy to BGP4+ Route Advertisement](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0030.html)

If BGP4+ is configured to filter received routes, only the routes that meet the matching rules are added to the local BGP4+ routing table and advertised to BGP4+ peers.

[Configuring a Policy for Receiving BGP4+ Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0031.html)

BGP4+ filters received routes using a policy. Only the routes that match the policy can be added to a routing table.

[Configuring BGP4+ Soft Reset](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0032.html)

BGP4+ soft reset allows the system to refresh a BGP4+ routing table dynamically without tearing down any BGP4+ connection if routing policies are changed.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0033.html)

After configuring BGP4+ routing policies, check routes that are advertised and received by BGP4+.