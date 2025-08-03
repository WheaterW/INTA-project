Enabling a BGP4+ Device to Add the Large-Community Attribute to Routes to Be Advertised
=======================================================================================

The Large-Community attribute can be flexibly applied in route-policies.

#### Context

The Large-Community attribute can represent a 2-byte or 4-byte Autonomous System Number (ASN), and has two 4-byte LocalData IDs. The administrator can therefore apply route-policies more flexibly. As an enhancement to community attributes, Large-Community can be used together with community attributes.


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
   * When configuring the BGP4+ Large-Community attribute, use a route-policy to define specific Large-Community values, and then apply the route-policy to the routes to be advertised.
   * For details about the route-policy configuration, see [Routing Policy Configuration](dc_vrp_route-policy_cfg_0000.html).
5. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* | *group-name* } **advertise-large-community**
   
   
   
   The device is configured to advertise the Large-Community attribute to the specified peer or peer group.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.