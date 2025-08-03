Redirecting a BGP IPv6 FlowSpec Route to an SRv6 TE Policy
==========================================================

Redirecting a BGP IPv6 FlowSpec route to an SRv6 TE Policy helps implement more accurate traffic filtering.

#### Context

In traditional BGP IPv6 FlowSpec-based traffic optimization, traffic transmitted over paths with the same source and destination nodes can be redirected to only one path, which does not achieve accurate traffic steering. With the function to redirect a BGP IPv6 FlowSpec route to an SRv6 TE Policy, a device can redirect traffic transmitted over paths with the same source and destination nodes to different SRv6 TE Policies.


[Configuring BGP IPv6 FlowSpec Route Redirection to an SRv6 TE Policy (Manual Configuration)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0127.html)

Manually configure a BGP IPv6 FlowSpec route and define a redirection rule to redirect the route to an SRv6 TE Policy.

[Configuring BGP IPv6 FlowSpec Route Redirection to an SRv6 TE Policy (Dynamic Delivery by a Controller)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0128.html)

Use a controller to dynamically deliver a BGP IPv6 FlowSpec route to a forwarder and define a redirection rule on the forwarder to redirect the route to a specified SRv6 TE Policy.