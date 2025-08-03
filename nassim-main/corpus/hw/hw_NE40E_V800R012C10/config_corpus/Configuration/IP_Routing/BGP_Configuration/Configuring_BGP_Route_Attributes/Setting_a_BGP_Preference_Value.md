Setting a BGP Preference Value
==============================

Setting a BGP preference value can affect route selection between BGP routes and other routing protocols' routes.

#### Context

Multiple dynamic routing protocols can run on a device. The system sets a default preference value for each routing protocol for inter-protocol route sharing and selecting. If different protocols have routes to the same destination, the route with the highest priority is selected.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
   
   
   
   The IPv4 unicast address family view is displayed.
4. Run [**preference**](cmdqueryname=preference+route-policy) { *external* *internal* *local* | **route-policy** *route-policy-name* | **route-filter** *route-filter-name* }
   
   
   
   A preference value is set for BGP.
   
   
   
   The lower the value, the higher the priority.
   
   
   
   BGP has the following types of routes:
   
   * EBGP routes: routes learned from external peers
   * IBGP routes: routes learned from internal peers
   * Locally originated BGP routes: summary routes generated automatically using the [**summary automatic**](cmdqueryname=summary+automatic) command or manually using the [**aggregate**](cmdqueryname=aggregate) command
   
   You can set different preference values for the three types of routes.
   
   You can also set a preference value only for the routes that match the filtering rules in a route-policy. The routes that do not match the filtering rules will use the default preference value.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Currently, the [**peer route-policy**](cmdqueryname=peer+route-policy) or [**peer route-filter**](cmdqueryname=peer+route-filter) command cannot be used to set a preference value for the BGP routes received from or advertised to a specified peer.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.