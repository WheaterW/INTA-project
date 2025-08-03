Configuring the BGP Large-Community Attribute
=============================================

The Large-Community attribute can be used to flexibly apply route-policies.

#### Usage Scenario

The Large-Community attribute can represent a 2-byte or 4-byte Autonomous System Number (ASN), and has two 4-byte LocalData IDs. The administrator can therefore apply route-policies more flexibly. As an enhancement to community attributes, Large-Community can be used together with community attributes.


#### Pre-configuration Tasks

Before configuring the BGP Large-Community attribute, [configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).


[Configuring a Route-Policy Related to the Large-Community Attribute](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_4059.html)

Before configuring the Large-Community attribute for routes, configure a route-policy in which the Large-Community attribute is applied.

[Configuring the Device to Advertise the Large-Community Attribute](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_4060.html)

The Large-Community attribute defined in a routing policy takes effect only after the Large-Community attribute is advertised.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_4061.html)

After configuring the BGP Large-Community attribute, verify the configuration.