Configuring BGP4+ XPL
=====================

BGP4+ extended routing-policy language (XPL) route-filters help flexibly control route advertisement and acceptance.

#### Usage Scenario

Route-filters can use condition clauses to filter routes and use action clauses to set and modify route attributes. The routes that match the route-filters are accepted or advertised. Route-filters can flexibly control route advertisement and acceptance.


#### Pre-configuration Tasks

Before configuring BGP4+ route-filters, complete the following tasks:

* Configure network-layer addresses for interfaces to ensure that neighboring devices are reachable at the network layer.
* [Configure basic BGP4+ functions.](dc_vrp_bgp6_cfg_0003.html)


[Using XPL to Filter the BGP4+ Routes to Be Advertised](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0088.html)

This section describes how to use XPL to filter the BGP4+ routes to be advertised to BGP4+ peers.

[Using XPL to Filter the BGP4+ Routes to Be Received](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0089.html)

BGP4+ uses XPL route-filters to filter the routes to be received from BGP4+ peers.