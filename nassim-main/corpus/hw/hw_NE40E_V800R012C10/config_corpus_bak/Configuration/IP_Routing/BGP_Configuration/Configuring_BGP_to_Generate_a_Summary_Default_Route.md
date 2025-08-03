Configuring BGP to Generate a Summary Default Route
===================================================

You can configure BGP to generate a summary default route and then determine whether to advertise the default route to a peer by using a route policy.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0200579125__fig163525561417), a BGP-VPNv4 peer relationship is established between PE1 and PE2. In addition, an EBGP-VPN peer relationship is established between PE2 and the core network device, and another EBGP-VPN peer relationship is established between PE1 and CE1. The core network device advertises routes to PE2 through the EBGP-VPN peer relationship. PE2 then advertises the received routes to PE1 through the BGP-VPNv4 peer relationship. Upon receipt, PE1 leaks the routes to its VPN instance. A summary default route can be generated only if routes with a specific prefix exist among the leaked routes. You can configure BGP to generate a summary default route on PE1 so that PE1 matches the leaked routes against an IP prefix list and summarizes the matched routes into a default route. As a result, PE1 advertises only the summary default route to CE1. Traffic over the unmatched routes will not be diverted to PE1, thereby conserving PE1's bandwidth resources.

**Figure 1** Typical networking  
![](figure/en-us_image_0200597859.png)

#### Pre-configuration Tasks

Before configuring BGP to generate a summary default route, [configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip ip-prefix**](cmdqueryname=ip+ip-prefix+index+match-network+greater-equal+less-equal) ip-prefix-name [ **index** *index-number* ] *matchMode* *ipv4-address* *masklen* [ **match-network** ] [ **greater-equal** *greater-equal-value* ] [ **less-equal** *less-equal-value* ]
   
   
   
   An IPv4 prefix list is configured.
3. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
4. Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
   
   
   
   The IPv4 unicast address family view is displayed.
5. Run [**aggregate default-route origin-ip-prefix**](cmdqueryname=aggregate+default-route+origin-ip-prefix+attribute-policy) *ip-prefix-name* [ **attribute-policy** *attribute-policy-name* ]
   
   
   
   The device is configured to generate a summary default route based on an IPv4 prefix list.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) [ *network* [ *mask* | *mask-length* ] ] command to check information about BGP summary default routes.