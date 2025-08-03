Configuring a Route Attribute Set
=================================

Route attribute sets can be referenced by route-filters
to filter the routes with the same or similar route attribute.

#### Usage Scenario

If the routes to be filtered
have the same or similar route attribute, you can configure a route
attribute set for them, and the route attribute set can be referenced
by a route-filter to filter the routes. The route attribute sets supported
by the NE40E are as follows:

* IPv4 prefix sets: apply to all dynamic routing protocols and can
  be used to match source, destination, and next hop IP addresses.
* IPv6 prefix sets: apply to all dynamic routing protocols and can
  be used to match source, destination, and next hop IPv6 addresses.
* AS\_Path sets: apply only to BGP and are used to match the AS\_Path
  attribute of BGP routes.
* Community sets: apply only to BGP and are used to match the community
  attribute of BGP routes.
* RD sets: match the RD attributes of VPN routes.
* Route target sets: match the RTs of VPN routes.
* Site of origin (SoO) sets: match the SoOs of VPN routes.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Sets do not have the permit or deny function
as routing policies do. Instead, sets are only groups of data used
as matching rules, and the actions to be applied are specified in
route-filters.

Route attribute sets can have no elements.

The easiest
method to configure route-filters to reference route attribute sets
is to use the format {element A, element B...}, **if ip route-source
in { 1.1.1.0 24, 2.2.2.2 32 } then** for example. However, if a
route-filter needs to reference a set multiple times, configure named
route attribute sets.


#### Pre-configuration Tasks

Before configuring a route attribute set, complete the following
tasks:

* Select a route attribute set based on the characteristics of
  the routes to be filtered.
* If some values need to be frequently used, configure a global
  variable set, which is easy to configure and use.

Perform one or more of the following configurations as
required:



[Configuring an IPv4 Prefix Set](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_xpl_cfg_0004.html)

IPv4 prefix sets apply to all dynamic routing protocols and can be used to match source, destination, and next hop IP addresses.

[Configuring an IPv6 Prefix Set](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_xpl_cfg_0005.html)

IPv6 prefix sets apply to all dynamic routing protocols and can be used to match source, destination, and next hop IPv6 addresses.

[Configuring an AS\_Path Set](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_xpl_cfg_0006.html)

AS\_Path sets apply only to BGP and are used to match the AS\_Path attribute of BGP routes. This section describes how to configure AS\_Path sets.

[Configuring a Community Set](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_xpl_cfg_0007.html)

Community sets apply only to BGP and are used to match the community attribute of BGP routes. This section describes how to configure community sets.

[Configuring Large-Community Sets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_xpl_cfg_0022.html)

Large-Community sets apply to BGP and are used to match the Large-Community attribute of BGP routes. This section describes how to configure Large-Community sets.

[Configuring an RD Set](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_xpl_cfg_0018.html)

RD sets are used to match the RD attributes of VPN routes.

[Configuring a Route Target Set](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_xpl_cfg_0019.html)

Route target sets are used to match the RTs of VPN routes.

[Configuring an SoO Set](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_xpl_cfg_0020.html)

Site of origin (SoO) sets are used to match the SoOs of VPN routes.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_xpl_cfg_0008.html)

After configuring route attribute sets, verify the configuration.