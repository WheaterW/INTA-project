Setting the BGP Preference
==========================

Setting the BGP Preference

#### Prerequisites

Before setting the BGP preference, you have completed the following task:

* [Configure basic BGP functions](vrp_bgp_cfg_0014.html).

#### Context

Routing protocols may share and select the same routing information if a device runs multiple dynamic routing protocols at the same time. As such, the system sets a default preference for each routing protocol. When different protocols discover the same route, the route with the highest priority is selected. For example, when BGP routes are imported to OSPF, the imported BGP routes do not take effect if the same routes exist in OSPF and BGP because the default priority of BGP routes is lower than that of OSPF routes. To allow the imported BGP routes to take effect, run the [**preference**](cmdqueryname=preference) command to increase their priority.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. (Optional) Enter the IPv4 unicast address family view.
   
   
   ```
   [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
   ```
   
   By default, the configuration is performed in the IPv4 unicast address family view.
4. Set the BGP preference.
   
   
   ```
   [preference](cmdqueryname=preference+route-policy) { external internal local | route-policy route-policy-name }
   ```
   
   A smaller value indicates a higher priority.
   
   BGP has the following types of routes:
   
   * Routes learned from external peers (EBGP)
   * Routes learned from internal peers (IBGP)
   * Locally generated routes: summary routes generated using the [**summary automatic**](cmdqueryname=summary+automatic) or [**aggregate**](cmdqueryname=aggregate) command. The former command is used for automatic summarization, and the latter command for manual summarization.
   
   By default, the preference of the three types of routes is 255. However, you can set different preferences for all three types of routes.
   
   
   
   You can set a preference for BGP routes that match the filtering rules in a route-policy, and the routes that do not match the filtering rules will use the default preference.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Currently, the [**peer route-policy**](cmdqueryname=peer+route-policy) command cannot be used to set a preference for BGP routes through a route-policy.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```