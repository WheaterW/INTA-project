Configuring BGP4+ to Generate a Summary Default Route
=====================================================

Configuring BGP4+ to Generate a Summary Default Route

#### Prerequisites

Before configuring BGP4+ to generate a summary default route, you have completed the following task:

* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0000001176661969__fig_dc_vrp_bgp_feature_200001), DeviceC is connected to the Internet and advertises all specific routes to DeviceB. DeviceA, however, has only a limited routing capacity. To conserve resources on DeviceA, configure BGP4+ on DeviceB to generate a summary default route. When the specific routes match an IPv6 prefix list, DeviceB uses the matched routes to generate a summary default route and then advertises it to DeviceA.

**Figure 1** Configuring BGP4+ to generate a summary default route  
![](figure/en-us_image_0000001130622456.png)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure an IPv6 prefix list.
   
   
   ```
   [ip ipv6-prefix](cmdqueryname=ip+ipv6-prefix+index+match-network+greater-equal+less-equal) ipv6-prefix-name [ index index-number ] matchMode ipv6-address masklen [ match-network ] [ greater-equal greater-equal-value ] [ less-equal less-equal-value ]
   ```
3. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
4. Enter the BGP-IPv6 unicast address family view.
   
   
   ```
   [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
   ```
5. Configure BGP to generate a summary default route based on an IPv6 prefix list.
   
   
   ```
   [aggregate default-route origin-ipv6-prefix](cmdqueryname=aggregate+default-route+origin-ipv6-prefix+attribute-policy) ipv6-prefix-name [ attribute-policy  attribute-policy-name ]
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After completing the configuration, verify the configuration.

* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) *ipv6-address* *prefix-length* command to check information about the BGP4+ routing table.