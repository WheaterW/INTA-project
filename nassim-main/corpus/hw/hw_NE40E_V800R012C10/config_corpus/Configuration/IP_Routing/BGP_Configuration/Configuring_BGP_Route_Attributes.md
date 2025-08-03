Configuring BGP Route Attributes
================================

Configuring BGP route attributes can change BGP route selection results.

#### Usage Scenario

BGP has many route attributes. You can change route selection results by configuring attributes for routes.

* BGP priority
  
  Setting the BGP priority can control route selection between BGP routes and routes of other routing protocols.
* Preferred values
  
  After preferred values are set for BGP routes, the route with the greatest value is preferred when multiple routes to the same destination exist in the BGP routing table.
* Local\_Pref
  
  The Local\_Pref attribute has the same function as the preferred value of a route. If both of them are configured for a BGP route, the preferred value takes precedence over the Local\_Pref attribute.
* MED
  
  The MED attribute is used to determine the optimal route for traffic that enters an AS. The route with the smallest MED value is selected as the optimal route if the other attributes of the routes are the same.
* Next\_Hop
  
  BGP route selection can be controlled by changing Next\_Hop attributes for routes.
* AS\_Path
  
  The AS\_Path attribute is used to prevent routing loops and control route selection.
* AIGP
  
  The AIGP attribute ensures that all devices in an AIGP domain forward data along the optimal path.

#### Pre-configuration Tasks

Before configuring BGP route attributes, [configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).


[Setting a BGP Preference Value](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_4011.html)

Setting a BGP preference value can affect route selection between BGP routes and other routing protocols' routes.

[Setting a PrefVal for BGP Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3012.html)

After PrefVals are set for routes, the route with the largest PrefVal is preferred when multiple routes to the same destination exist in the BGP routing table.

[Setting the Default Local\_Pref Attribute for the Local Device](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3013.html)

The function of the Local\_Pref attribute is similar to that of the preferred value. The priority of the Local\_Pref attribute, however, is lower than that of the preferred value.

[Configuring MED Attributes for BGP Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_4014.html)

The MED attribute is equivalent to the metric used by an IGP. The MED attribute determines the optimal route for the traffic entering an AS.

[Configuring the Next\_Hop Attribute](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_4015.html)

Configuring the Next\_Hop attribute allows for flexible control of BGP route selection.

[Setting the AS\_Path Attribute](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_4016.html)

The AS\_Path attribute is used to prevent routing loops and control route selection.

[Configuring AIGP Attributes for Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_4100.html)

The Accumulated Interior Gateway Protocol (AIGP) attribute allows devices in an AIGP domain to use the optimal routes to forward data.

[Configuring Attr\_Set Attribute Encapsulation or Parsing](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_4106.html)

Configuring the Attr\_Set attribute for BGP routes ensures that CE route attributes are transparently transmitted over the backbone network.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3017.html)

After configuring BGP route selection, verify information about route attributes.