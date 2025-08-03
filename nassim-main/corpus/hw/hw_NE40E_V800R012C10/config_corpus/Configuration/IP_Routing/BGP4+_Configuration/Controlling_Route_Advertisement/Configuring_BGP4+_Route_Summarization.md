Configuring BGP4+ Route Summarization
=====================================

Configuring route summarization can reduce the size of a routing table on a peer.

#### Context

On a large-scale BGP4+ network, configuring route summarization can reduce the number of advertised route prefixes and improve BGP4+ stability.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
   
   
   
   The IPv6 unicast address family view is displayed.
4. Run one of the following commands to configure route summarization as needed.
   
   
   * To advertise all summary routes and specific routes, run the [**aggregate**](cmdqueryname=aggregate) *ipv6-address* *mask-length* command.
   * To advertise only summary routes, run the [**aggregate**](cmdqueryname=aggregate+detail-suppressed) *ipv6-address* *mask-length* **detail-suppressed** command.
   * To advertise some of the specific routes, run the [**aggregate**](cmdqueryname=aggregate+suppress-policy) *ipv6-address* *mask-length* **suppress-policy** *route-policy-name* command.
     
     You can also run the [**peer route-policy**](cmdqueryname=peer+route-policy) command to achieve the same effect.
   * To generate a summary route used for loop detection, run the [**aggregate**](cmdqueryname=aggregate+as-set) *ipv6-address* *mask-length* **as-set** command.
   * To configure attributes for summary routes, run the [**aggregate**](cmdqueryname=aggregate+attribute-policy) *ipv6-address* *mask-length* **attribute-policy** *route-policy-name* command.
     
     You can also run the [**peer route-policy**](cmdqueryname=peer+route-policy) command to achieve the same effect.
     
     If **as-set** is specified in the [**aggregate**](cmdqueryname=aggregate) command and the AS\_Path attribute is configured in the policy using the [**apply as-path**](cmdqueryname=apply+as-path) command, the configured AS\_Path attribute does not take effect.
   * To generate summary routes based on some of the specific routes, run the [**aggregate**](cmdqueryname=aggregate+origin-policy) *ipv6-address* *mask-length* **origin-policy** *route-policy-name* command.
   
   Manual route summarization is valid for the routing entries that exist in the local BGP4+ routing table. For example, if the **aggregate 2001:db8::1 64** command is run to summarize routes but no route with a mask length greater than 64 (for example, 2001:db8::1/128) exists in the BGP4+ routing table, BGP4+ does not advertise the summary route.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.