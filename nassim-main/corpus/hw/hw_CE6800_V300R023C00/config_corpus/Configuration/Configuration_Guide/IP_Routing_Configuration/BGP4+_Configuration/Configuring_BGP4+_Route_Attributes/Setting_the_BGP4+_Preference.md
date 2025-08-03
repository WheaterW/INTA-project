Setting the BGP4+ Preference
============================

Setting the BGP4+ Preference

#### Prerequisites

Before configuring BGP4+ route attributes, you have completed the following task:

* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).

#### Context

Setting the BGP4+ preference can affect the selection of routes between BGP4+ and another routing protocol.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enter the IPv6 unicast address family view.
   
   
   ```
   [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
   ```
4. Set the BGP4+ preference.
   
   
   ```
   [preference](cmdqueryname=preference+route-policy) { external internal local | route-policy route-policy-name }
   ```
   
   The lower the value, the higher the preference.
   
   
   
   BGP4+ has the following types of routes:
   
   * Routes learned from external peers (EBGP)
   * Routes learned from internal peers (IBGP)
   * Locally originated routes, which are summary routes generated using the [**aggregate**](cmdqueryname=aggregate) command
   
   The default preference of each type of route is 255. However, you can set different preferences for all three types of routes.
   
   You can set a preference for routes that match the filtering rules in a route-policy, and the routes that do not match the filtering rules will use the default preference.
   
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Currently, the [**peer route-policy**](cmdqueryname=peer+route-policy) command cannot be used to set a preference for BGP4+ routes through a route-policy.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```