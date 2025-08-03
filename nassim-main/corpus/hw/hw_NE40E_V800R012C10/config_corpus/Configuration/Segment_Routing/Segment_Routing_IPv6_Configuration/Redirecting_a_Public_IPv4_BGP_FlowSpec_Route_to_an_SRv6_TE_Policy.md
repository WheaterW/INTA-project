Redirecting a Public IPv4 BGP FlowSpec Route to an SRv6 TE Policy
=================================================================

Redirecting a public IPv4 BGP FlowSpec route to an SRv6 TE Policy helps implement more accurate traffic filtering.

#### Context

In traditional BGP FlowSpec-based traffic optimization, traffic transmitted over paths with the same source and destination nodes can be redirected to only one path, which does not achieve accurate traffic steering. With the function to redirect a public IPv4 BGP FlowSpec route to an SRv6 TE Policy, a device can redirect traffic transmitted over paths with the same source and destination nodes to different SRv6 TE Policies.


[Configuring Public IPv4 BGP FlowSpec Route Redirection to an SRv6 TE Policy (Manual Configuration)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0124.html)

Manually generate a BGP FlowSpec route and configure redirection rules to redirect the route to an SRv6 TE Policy.

[Redirecting a Public IPv4 BGP FlowSpec Route to an SRv6 TE Policy (Dynamic Delivery by a Controller)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_srv6_cfg_all_0125.html)

Use a controller to dynamically deliver a BGP FlowSpec route to a forwarder and configure a redirection rule on the forwarder to redirect the route to a specified SRv6 TE Policy.