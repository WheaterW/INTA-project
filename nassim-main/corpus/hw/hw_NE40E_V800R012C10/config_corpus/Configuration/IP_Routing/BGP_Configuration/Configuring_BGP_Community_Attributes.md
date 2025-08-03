Configuring BGP Community Attributes
====================================

Community attributes simplify routing policy management.

#### Usage Scenario

Community attributes are used to simplify routing policy application and facilitate network maintenance. They allow a group of BGP devices in different ASs to share the same routing policies. Before advertising a route with the community attribute to peers, a BGP device can change the original community attribute of this route. Community attributes are route attributes, which are transmitted between BGP peers, and the transmission is not restricted within an AS.


#### Pre-configuration Tasks

Before configuring BGP community attributes, [configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).


[Configuring a Community Attribute-Related Policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3042.html)

A policy that references a community attribute needs to be configured before the community attribute is set for routing information.

[Configuring Community Attribute Advertisement](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_4043.html)

A community attribute defined in a routing policy takes effect only after community attribute advertisement is configured.

[Configuring the Device to Advertise Extended Community Attributes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_4044.html)

The extended community attributes defined in a route-policy take effect only after the extended community attributes are advertised.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3044.html)

After configuring BGP community attributes, verify the configured BGP community attributes.