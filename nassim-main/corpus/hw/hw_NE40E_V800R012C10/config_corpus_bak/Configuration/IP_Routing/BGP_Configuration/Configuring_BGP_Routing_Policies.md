Configuring BGP Routing Policies
================================

BGP is used to transmit routing information between ASs, and its routing policies can be used to flexibly control route advertisement and acceptance, which directly affect traffic forwarding.

#### Usage Scenario

A large number of routes typically exist in a BGP routing table, and transmitting such extensive routing information brings heavy burden to a device. In order to address this problem, it is necessary to filter those routes to be advertised. You can configure a device to advertise only necessary routes or those that its peers require. Multiple routes to the same destination may exist and traverse different ASs. To direct traffic to specific ASs, routes to be advertised also need to be filtered.

A BGP device may receive multiple routes to the same destination network from different peers. To control the network traffic forwarding path, BGP needs to filter the received routes. In addition, due to potential service attacks, the BGP device may receive an excessively large number of routes from its peers, consuming many resources on the device. Regardless of whether malicious attacks or incorrect configurations result in the reception of numerous BGP routes, the administrator must limit the device resources to be consumed based on the network planning and device capacity.

Filters can be used to filter the routes to be advertised and received by BGP. BGP can filter the routes to be advertised by a peer or peer group, the routes that are received globally, or the routes received from a peer or peer group. If multiple filter policies are configured, BGP advertises or accepts only the routes that match all the filter policies.


#### Pre-configuration Tasks

Before configuring BGP to advertise routes, complete the following tasks:

* [Configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).


[Configuring BGP Filters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3113.html)

BGP filters can be used to flexibly filter routes to be advertised.

[Applying a Policy to BGP Route Advertisement](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3114.html)

After a route advertisement policy is configured on a device, the device advertises only the routes that match the policy to its BGP peers.

[Applying a Policy to BGP Route Acceptance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3115.html)

After an import policy is configured, only the routes that match the import policy are accepted.

[(Optional) Configuring Outbound BGP Soft Reset](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_31160.html)

After a BGP export policy changes, you can configure outbound BGP soft reset to enable BGP to immediately apply the new export policy without tearing down BGP connections.

[(Optional) Configuring Inbound BGP Soft Reset](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3116.html)

The inbound BGP soft reset allows the system to apply new import policies immediately and refresh BGP routing table dynamically without tearing down any BGP connection.

[Configuring BGP Message Extension](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3216.html)

With the enhancement of BGP capabilities, a BGP session needs to negotiate multiple capabilities and use BGP messages to carry information about the routes and route attributes to be advertised. However, the length of BGP messages is limited. You can enable BGP message extension to remove the limit on the length of BGP messages.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_bgp_cfg_3117.html)

After the configurations for controlling BGP route advertisement and acceptance are configured, you can view information about the configured filters, routes that match the specified filter, routes advertised to peers, and the imported routes that match the specified filter.