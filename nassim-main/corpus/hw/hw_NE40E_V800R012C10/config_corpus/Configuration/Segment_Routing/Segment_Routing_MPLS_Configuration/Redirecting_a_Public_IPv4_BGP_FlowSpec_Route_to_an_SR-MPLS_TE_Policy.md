Redirecting a Public IPv4 BGP FlowSpec Route to an SR-MPLS TE Policy
====================================================================

Redirecting a public IPv4 BGP FlowSpec route to an SR-MPLS TE Policy helps implement more accurate traffic filtering.

#### Context

In traditional BGP FlowSpec-based traffic optimization, traffic transmitted over paths with the same source and destination nodes can be redirected to only one path, which does not achieve accurate traffic steering. With the function to redirect a public IPv4 BGP FlowSpec route to an SR-MPLS TE Policy, a device can redirect traffic transmitted over paths with the same source and destination nodes to different SR-MPLS TE Policies.


[Redirecting a Public IPv4 BGP FlowSpec Route to an SR-MPLS TE Policy (Manual Configuration)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0114.html)

Manually generate a BGP FlowSpec route and configure redirection rules to redirect the route to an SR-MPLS TE Policy.

[Redirecting a Public IPv4 BGP FlowSpec Route to an SR-MPLS TE Policy (Dynamic Delivery by a Controller)](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_sr_all_cfg_0115.html)

After a controller dynamically delivers a BGP FlowSpec route and an SR-MPLS TE Policy to a forwarder, the forwarder needs to redirect the BGP FlowSpec route to the SR-MPLS TE Policy.