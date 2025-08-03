Configuring BGP to Generate a Summary Default Route
===================================================

Configuring BGP to Generate a Summary Default Route

#### Prerequisites

Before configuring BGP to generate a summary default route, you have completed the following task:

* [Configure basic BGP functions](vrp_bgp_cfg_0014.html).

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0000001130783932__fig_dc_vrp_bgp_feature_200001), DeviceC is connected to the Internet and advertises all specific routes to DeviceB. DeviceA, however, has only a limited routing capacity. To conserve resources on DeviceA, configure BGP on DeviceB to generate a summary default route. When the specific routes match an IPv4 prefix list, DeviceB uses the matched routes to generate a summary default route and then advertises it to DeviceA.

**Figure 1** Configuring BGP to generate a summary default route  
![](figure/en-us_image_0000001130784024.png)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure an IPv4 prefix list.
   
   
   ```
   [ip ip-prefix](cmdqueryname=ip+ip-prefix+index+match-network+greater-equal+less-equal) ip-prefix-name [ index index-number ] matchMode ipv4-address masklen [ match-network ] [ greater-equal greater-equal-value ] [ less-equal less-equal-value ]
   ```
3. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
4. Enter the BGP-IPv4 unicast address family view.
   
   
   ```
   [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
   ```
5. Configure BGP to generate a summary default route based on an IPv4 prefix list.
   
   
   ```
   [aggregate default-route origin-ip-prefix](cmdqueryname=aggregate+default-route+origin-ip-prefix+attribute-policy) ip-prefix-name [ attribute-policy  attribute-policy-name ]
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After configuring the function, verify the configuration.

* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) [ *network* [ *mask* | *mask-length* ] ] command to check information about the BGP summary default route.