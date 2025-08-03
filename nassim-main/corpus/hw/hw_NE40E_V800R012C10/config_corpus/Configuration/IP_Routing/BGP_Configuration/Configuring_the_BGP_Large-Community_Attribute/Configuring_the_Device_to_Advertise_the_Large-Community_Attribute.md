Configuring the Device to Advertise the Large-Community Attribute
=================================================================

The Large-Community attribute defined in a routing policy takes effect only after the Large-Community attribute is advertised.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
   
   
   
   The IPv4 unicast address family view is displayed.
4. Run [**peer**](cmdqueryname=peer+route-policy) { *ipv4-address* | *group-name* } [**route-policy**](cmdqueryname=peer+route-policy) *route-policy-name* **export**
   
   
   
   An export route-policy is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   When configuring the BGP Large-Community attribute, use a route-policy to define specific Large-Community values, and then apply the route-policy to the routes to be advertised.
   
   For details about the route-policy configuration, see the chapter "Routing Policy Configuration".
5. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } [**advertise-large-community**](cmdqueryname=advertise-large-community)
   
   
   
   The device is enabled to advertise the Large-Community attribute to a peer or peer group.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.