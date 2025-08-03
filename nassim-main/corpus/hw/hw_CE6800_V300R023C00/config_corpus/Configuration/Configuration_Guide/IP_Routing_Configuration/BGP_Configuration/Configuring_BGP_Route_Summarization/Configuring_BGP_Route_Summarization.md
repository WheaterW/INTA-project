Configuring BGP Route Summarization
===================================

Configuring BGP Route Summarization

#### Prerequisites

Before configuring BGP route summarization, you have completed the following task:

* [Configure basic BGP functions](vrp_bgp_cfg_0014.html).

#### Procedure

* Configure automatic route summarization.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. Enter the IPv4 unicast address family view.
     
     
     ```
     [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
     ```
  4. Configure automatic summarization for locally imported routes.
     
     
     ```
     [summary automatic](cmdqueryname=summary+automatic)
     ```
     
     This command summarizes routes imported by BGP, including direct, static, RIP, OSPF, and IS-IS routes. After this command is run, BGP summarizes routes based on natural network segments. This command does not take effect on the routes imported using the [**network**](cmdqueryname=network) command.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure manual route summarization.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  3. Enter the IPv4 unicast address family view.
     
     
     ```
     [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
     ```
  4. Run one of the following commands to configure route summarization as needed.
     
     
     
     **Table 1** Configuring manual route summarization
     | Operation | Command | Description |
     | --- | --- | --- |
     | Configure the device to advertise a summary route and all its specific routes. | [**aggregate**](cmdqueryname=aggregate) *ipv4-address* { *mask* | *mask-length* } | - |
     | Configure the device to advertise only a summary route. | [**aggregate**](cmdqueryname=aggregate+detail-suppressed) *ipv4-address* { *mask* | *mask-length* } **detail-suppressed** | - |
     | Configure the device to advertise a summary route and some of its specific routes. | [**aggregate**](cmdqueryname=aggregate+suppress-policy) *ipv4-address* { *mask* | *mask-length* } **suppress-policy** *route-policy-name* | You can also run the [**peer route-policy**](cmdqueryname=peer+route-policy) command to achieve the same effect. |
     | Configure the device to generate a summary route used for loop detection. | [**aggregate**](cmdqueryname=aggregate+as-set) *ipv4-address* { *mask* | *mask-length* } **as-set** | - |
     | Configure the device to set the attributes for a summary route. | [**aggregate**](cmdqueryname=aggregate+attribute-policy) *ipv4-address* { *mask* | *mask-length* } **attribute-policy** *route-policy-name* | You can also run the [**peer route-policy**](cmdqueryname=peer+route-policy) command to achieve the same effect.  If **as-set** is specified in the [**aggregate**](cmdqueryname=aggregate) command and the AS\_Path attribute is configured in the policy using the [**apply as-path**](cmdqueryname=apply+as-path) command, the configured AS\_Path attribute does not take effect. |
     | Configure the device to generate a summary route based on some of the specific routes. | [**aggregate**](cmdqueryname=aggregate+origin-policy) *ipv4-address* { *mask* | *mask-length* } **origin-policy** *route-policy-name* | - |
     
     Manual route summarization is valid for the routing entries that exist in the local BGP routing table. For example, if the **aggregate 10.1.1.1 16** command is run to summarize routes, but no route with a mask length greater than 16 (for example, 10.1.1.1/24) exists in the BGP routing table, BGP does not advertise the summary route.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

After configuring the function, verify the configuration.

* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) [ *network* [ *mask* | *mask-length* ] ] command to check information about BGP summary routes.