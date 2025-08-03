Controlling MBGP Route Selection
================================

The policy that controls MBGP route selection can be changed by configuring MBGP route attributes.

#### Usage Scenario

MBGP has many route attributes. These attributes are used to define the routing policy and describe the MBGP route prefix. Configuring these attributes can change the policy that controls MBGP route selection.


#### Pre-configuration Tasks

Before controlling MBGP route selection, [configure an MBGP peer](dc_vrp_multicast_cfg_1003.html).


[Configuring Preferences for MBGP Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_1011.html)

To control route selection among MBGP and other routing protocols, set the MBGP preference.

[(Optional) Setting a Preferred Value for Routes Learned from a Peer](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_1012.html)

After preferred values are set for MBGP routes, the route with the greatest value is preferred when multiple routes to the same destination exist in the MBGP routing table.

[Setting the Local\_Pref Attribute for MBGP Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_1013.html)

The Local\_Pref attribute has the same function as the preferred value of a route. If both of them are configured for an MBGP route, the preferred value takes precedence over the Local\_Pref attribute. 

[Setting the MED Attribute for MBGP Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_1014.html)

The MED attribute indicates the metric used in IGP. After the MED attribute is set for routes, an EBGP peer can select a route with the smallest MED value for the traffic that enters an AS.

[Setting the Next\_Hop Attribute](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_1015.html)

MBGP route selection can be flexibly controlled by setting the Next\_Hop attribute.

[Setting the AS\_Path Attribute](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_1016.html)

The AS\_Path attribute is used to prevent routing loops and control route selection.

[Verifying the MBGP Route Attribute Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_1017.html)

After configuring MBGP route attributes, verify information about the route attributes.