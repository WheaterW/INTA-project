Configuring BGP4+ Community Attributes
======================================

The community attribute is used to simplify route-policy management.

#### Context

The community attribute is used to simplify the application, maintenance, and management of route-policies. With the community attribute used, a group of BGP4+ peers in multiple ASs can share a route-policy. Before advertising a route carrying a community attribute to peers, a BGP4+ device can be configured to change the original community attribute of this route. Community attributes are route attributes, which are transmitted between BGP4+ peers, and the transmission is not restricted within an AS.


#### Pre-configuration Tasks

Before configuring BGP4+ community attributes, complete the following task:

* [Configuring Basic BGP4+ Functions](dc_vrp_bgp6_cfg_0003.html)


[Configuring a Community Attribute-Related Policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_3042.html)

A policy that references a community attribute needs to be configured before the community attribute is set for routing information.

[Configuring Community Attribute Advertisement](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_4043.html)

A community attribute defined in a rout-policy takes effect only after community attribute advertisement is configured.

[Configuring the Device to Advertise Extended Community Attributes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_4044.html)

The extended community attributes defined in a route-policy take effect only after the extended community attributes are advertised.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_3044.html)

After configuring BGP4+ community attributes, verify the configuration.