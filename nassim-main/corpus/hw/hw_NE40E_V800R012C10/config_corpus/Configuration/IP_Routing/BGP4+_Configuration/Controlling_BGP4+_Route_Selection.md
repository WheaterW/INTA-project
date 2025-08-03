Controlling BGP4+ Route Selection
=================================

The policy on BGP4+ route selection can be changed by configuring BGP4+ route attributes.

#### Usage Scenario

BGP4+ has many route attributes. These attributes are used to define the routing policy and describe the BGP4+ route prefix. Configuring these attributes can change the policy used by BGP4+ for route selection.


#### Pre-configuration Tasks

Before controlling BGP4+ route selection, [configure basic BGP4+ functions](dc_vrp_bgp6_cfg_0003.html).


[Setting a BGP4+ Preference](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0020.html)

Setting the BGP4+ preference can control route selection between BGP routes and routes of another routing protocol.

[Setting a PrefVal for BGP4+ Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0021.html)

After a PrefVal is set for BGP4+ routes, the route with the greatest value is preferred when multiple routes to the same destination exist in the BGP4+ routing table.

[Setting the Default Local\_Pref Attribute for the Local Device](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0022.html)

After the Local\_Pref attribute is set for BGP4+ routes, the route with the greatest attribute value is preferred when multiple routes to the same destination exist in the BGP4+ routing table. The preferred value takes precedence over the Local\_Pref attribute.

[Setting the MED Attribute](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0023.html)

The MED attribute is equal to the metric used in IGP. After the MED attribute is set for routes, an EBGP peer can select a route with the smallest MED value for the traffic that enters an AS.

[Setting the Next\_Hop Attribute](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0024.html)

BGP4+ route selection can be flexibly controlled by setting the Next\_Hop attribute.

[Setting the AS\_Path Attribute](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0025.html)

The AS\_Path attribute is used to prevent routing loops and control route selection.

[Configuring AIGP Attributes for Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0103.html)

The Accumulated Interior Gateway Protocol (AIGP) attribute allows devices in an AIGP domain to use the optimal routes to forward data.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp6_cfg_0026.html)

After configuring BGP4+ route attributes, verify information about the route attributes.