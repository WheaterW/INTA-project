Configuring BGP4+ Route Summarization
=====================================

Configuring BGP4+ Route Summarization

#### Prerequisites

Before configuring BGP4+ route summation, you have completed the following task:

* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).

#### Context

On a large-scale BGP4+ network, configuring route summarization can reduce the number of route prefixes to be advertised to peers and improve BGP4+ stability.

BGP4+ supports manual route summarization only. Manual summarization can control the attributes of a summary route and determine whether to advertise specific routes.


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
4. Run one of the following commands to configure route summarization as needed.
   
   
   
   **Table 1** Configuring manual route summarization
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure the device to advertise a summary route and all its specific routes. | [**aggregate**](cmdqueryname=aggregate) *ipv6-address* *mask-length* | - |
   | Configure the device to advertise only a summary route. | [**aggregate**](cmdqueryname=aggregate+detail-suppressed) *ipv6-address* *mask-length* **detail-suppressed** | - |
   | Configure the device to advertise specific routes selectively. | [**aggregate**](cmdqueryname=aggregate+suppress-policy) *ipv6-address* *mask-length* **suppress-policy** *route-policy-name* | You can also run the [**peer route-policy**](cmdqueryname=peer+route-policy) command to achieve the same effect. |
   | Configure the device to generate a summary route used for loop detection. | [**aggregate**](cmdqueryname=aggregate+as-set) *ipv6-address* *mask-length* **as-set** | - |
   | Configure the device to set the attributes for a summary route. | [**aggregate**](cmdqueryname=aggregate+attribute-policy) *ipv6-address* *mask-length* **attribute-policy** *route-policy-name* | You can also run the [**peer route-policy**](cmdqueryname=peer+route-policy) command to achieve the same effect.  If **as-set** is specified in the [**aggregate**](cmdqueryname=aggregate) command and the AS\_Path attribute is configured in the policy using the [**apply as-path**](cmdqueryname=apply+as-path) command, the configured AS\_Path attribute does not take effect. |
   | Configure the device to generate a summary route based on some of the specific routes. | [**aggregate**](cmdqueryname=aggregate+origin-policy) *ipv6-address* *mask-length* **origin-policy** *route-policy-name* | - |
   
   Manual route summarization is valid for the routing entries that exist in the local BGP4+ routing table. For example, if the **aggregate 2001:db8:3::1 64** command is run to summarize routes but no route with a mask length greater than 64 (for example, 2001:db8:3::1/128) exists in the BGP4+ routing table, BGP4+ does not advertise the summary route.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After completing the configuration, verify the configuration.

* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) command to check information about BGP4+ routes.