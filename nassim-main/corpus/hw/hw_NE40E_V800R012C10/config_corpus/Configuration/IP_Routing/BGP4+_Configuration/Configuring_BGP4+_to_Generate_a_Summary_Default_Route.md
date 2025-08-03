Configuring BGP4+ to Generate a Summary Default Route
=====================================================

You can configure BGP4+ to generate a summary default route and then determine whether to advertise the default route to a peer by using a route-policy.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0200834097__fig163525561417), a VPNv6 peer relationship is established between PE1 and PE2. In addition, an EBGP-VPN peer relationship is established between PE2 and the core network device, and another EBGP-VPN peer relationship is established between PE1 and CE1. The core network device advertises routes to PE2 through the EBGP-VPN peer relationship. PE2 then advertises the received routes to PE1 through the VPNv6 peer relationship. Upon receipt, PE1 leaks the routes to its VPN instance. A default route can be generated only if routes with a specific prefix exist among the leaked routes. You can perform this configuration task so that PE1 advertises a default route to CE1 based on an IP prefix list filter. In this way, traffic corresponding to the routes that do not match the filter is not diverted to PE1, thereby conserving PE1's bandwidth resources.

**Figure 1** Typical networking  
![](figure/en-us_image_0200847639.png)

#### Pre-configuration Tasks

Before configuring BGP4+ to generate a summary default route, [configure basic BGP4+ functions](dc_vrp_bgp6_cfg_0003.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip ipv6-prefix**](cmdqueryname=ip+ipv6-prefix+index+match-network+greater-equal+less-equal) *ipv6-prefix-name* [ **index** *index-number* ] *matchMode* *ipv6-address* *masklen* [ **match-network** ] [ **greater-equal** *greater-equal-value* ] [ **less-equal** *less-equal-value* ]
   
   
   
   An IPv6 prefix list is configured.
3. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
4. Run [**ipv6-family**](cmdqueryname=ipv6-family) **unicast**
   
   
   
   The IPv6 unicast address family view is displayed.
5. Run [**aggregate default-route origin-ipv6-prefix**](cmdqueryname=aggregate+default-route+origin-ipv6-prefix+attribute-policy) *ipv6-prefix-name* [ **attribute-policy** *attribute-policy-name* ]
   
   
   
   The device is enabled to generate a summary default route based on an IPv6 prefix list.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) command to check information about BGP4+ summary default routes.