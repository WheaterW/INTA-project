Setting a BGP4+ Preference
==========================

Setting the BGP4+ preference can control route selection between BGP routes and routes of another routing protocol.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
   
   
   
   The IPv6 unicast address family view is displayed.
4. Run [**preference**](cmdqueryname=preference) { *external* *internal* *local* | **route-policy** *route-policy-name* | **route-filter** *route-filter-name* }
   
   
   
   The BGP4+ preference is set.
   
   
   
   BGP4+ has the following types of routes:
   
   * EBGP routes, which are learned from peers in other ASs
   * IBGP routes, which are learned from peers in the same AS
   * Locally originated routes, which are summary route generated using the [**aggregate**](cmdqueryname=aggregate) command
   
   You can set different preferences for the three types of routes.
   
   You can also apply routing policies to set preferences for the specified routes that meet the requirements. You can set default preferences for the routes that do not meet the requirements.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Currently, the [**peer route-policy**](cmdqueryname=peer+route-policy) or [**peer route-filter**](cmdqueryname=peer+route-filter) command cannot be used to set a preference for BGP4+ routes through a route-policy.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.