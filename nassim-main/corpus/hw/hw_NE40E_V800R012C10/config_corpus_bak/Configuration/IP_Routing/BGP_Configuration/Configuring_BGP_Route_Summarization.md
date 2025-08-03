Configuring BGP Route Summarization
===================================

Configuring BGP route summarization on a device can reduce the sizes of routing tables on the peers of the device.

#### Usage Scenario

The BGP routing table of the Router on a medium or large BGP network contains a large number of routing entries. Storing the routing table consumes a large number of memory resources, and transmitting and processing routing information consume lots of network resources. Configuring route summarization can reduce the size of a routing table, prevent specific routes from being advertised, and minimize the impact of route flapping on network performance. BGP route summarization and routing policies enable BGP to effectively transmit and control routes.

BGP supports automatic and manual summarization. Manual summarization takes precedence over automatic summarization.


#### Pre-configuration Tasks

Before configuring BGP route summarization, complete the following task:

* [Configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).

#### Procedure

* Configure automatic route summarization.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The IPv4 unicast address family view is displayed.
  4. Run [**summary automatic**](cmdqueryname=summary+automatic)
     
     
     
     Automatic summarization is configured for locally imported routes.
     
     
     
     The [**summary automatic**](cmdqueryname=summary+automatic) command summarizes routes imported by BGP. The routes can be direct routes, static routes, RIP routes, OSPF routes, or IS-IS routes. After this command is run, BGP summarizes routes based on natural network segments. The command, however, cannot summarize the routes imported using the [**network**](cmdqueryname=network) command.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure manual route summarization.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     
     
     The IPv4 unicast address family view is displayed.
  4. Run one of the following commands to configure route summarization as needed.
     
     
     + To advertise both the summary route and specific routes, run the [**aggregate**](cmdqueryname=aggregate) *ipv4-address* { *mask* | *mask-length* } command.
     + To advertise only the summary route, run the [**aggregate**](cmdqueryname=aggregate+detail-suppressed) *ipv4-address* { *mask* | *mask-length* } **detail-suppressed** command.
     + To advertise specific routes selectively, run the [**aggregate**](cmdqueryname=aggregate+suppress-policy) *ipv4-address* { *mask* | *mask-length* } **suppress-policy** *route-policy-name* command.
       
       Alternatively, you can run the [**peer route-policy**](cmdqueryname=peer+route-policy) command to achieve the same effect.
     + To generate a summary route that can be used for routing loop detection, run the [**aggregate**](cmdqueryname=aggregate+as-set) *ipv4-address* { *mask* | *mask-length* } **as-set** command.
     + To set attributes for the summary route, run the [**aggregate**](cmdqueryname=aggregate+attribute-policy) *ipv4-address* { *mask* | *mask-length* } **attribute-policy** *route-policy-name* command.
       
       You can also run the [**peer route-policy**](cmdqueryname=peer+route-policy) command to achieve the same effect.
       
       If **as-set** is specified in the [**aggregate**](cmdqueryname=aggregate+as-set) command and the AS\_Path attribute is configured in the policy using the [**apply as-path**](cmdqueryname=apply+as-path) command, the configured AS\_Path attribute does not take effect.
     + To generate a summary route based on some specific routes, run the [**aggregate**](cmdqueryname=aggregate+origin-policy) *ipv4-address* { *mask* | *mask-length* } **origin-policy** *route-policy-name* command.
     
     Manual summarization is valid for the existing routing entries in the local BGP routing table. For example, if a route with the mask length longer than 16, such as 10.1.1.0/24, does not exist in the BGP routing table, BGP does not advertise the summary route even after the **[**aggregate**](cmdqueryname=aggregate) 10.1.1.1 16** command is run.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) [ *network* [ *mask* | *mask-length* ] ] command to check information about BGP summary routes.