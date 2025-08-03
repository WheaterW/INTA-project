Enabling a BGP4+ Device to Add the Community Attribute to Routes to Be Advertised
=================================================================================

The community attribute is used to simplify route-policy management.

#### Context

The community attribute is transmitted between BGP4+ peers, and its transmission is not restricted within ASs. With the community attribute, a group of routes can share the same route-policy. Before sending a route with the community attribute to peers, BGP4+ can change the original community attribute carried by the route.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
   
   
   
   The IPv6 unicast address family view is displayed.
4. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } **route-policy** *route-policy-name* **export**
   
   
   
   An export route-policy is applied to routes to be advertised to a specified peer or peer group.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * When configuring a BGP4+ community, use a route-policy to define a specific community attribute. Then, apply the route-policy to the routes to be advertised.
   * For details about the route-policy configuration, see [Routing Policy Configuration](dc_vrp_route-policy_cfg_0000.html).
5. Run either of the following commands to configure the device to advertise community attributes to a peer or peer group:
   
   
   * To configure the device to advertise standard community attributes to a specified peer or peer group, run the [**peer**](cmdqueryname=peer+advertise-community) { *ipv4-address* | *ipv6-address* | *group-name* } **advertise-community** command.
   * To configure the device to advertise extended community attributes to a specified peer or peer group, run the [**peer**](cmdqueryname=peer+advertise-ext-community) { *ipv4-address* | *ipv6-address* | *group-name* } **advertise-ext-community** command.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.