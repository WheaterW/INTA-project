Configuring BGP IPv6 FlowSpec Route Redirection to an SRv6 TE Policy (Dynamic Delivery by a Controller)
=======================================================================================================

Use a controller to dynamically deliver a BGP IPv6 FlowSpec route to a forwarder and define a redirection rule on the forwarder to redirect the route to a specified SRv6 TE Policy.

#### Prerequisites

Before configuring BGP IPv6 FlowSpec route redirection to an SRv6 TE Policy, complete the following tasks:

* [Configure a BGP peer relationship.](dc_vrp_bgp_cfg_3006.html)
* [Configure an SRv6 TE Policy in controller-based dynamic delivery mode.](dc_vrp_srv6_cfg_all_0116.html)

#### Context

In a scenario where a controller is deployed, the controller can be used to deliver a BGP IPv6 FlowSpec route and an SRv6 TE Policy. The process of redirecting the BGP IPv6 FlowSpec route to the SRv6 TE Policy mainly includes the following steps:

1. Establish a BGP-LS peer relationship between the controller and forwarder, enabling the controller to collect such information as topology information and SIDs through BGP-LS. Network topology information includes the link cost, latency, and packet loss rate.
2. Establish an IPv6 SR-Policy address family-specific BGP peer relationship between the controller and forwarder, so that the controller can dynamically compute an SRv6 TE Policy path based on link cost, latency, packet loss rate, and other factors and then deliver the path to the headend through the peer relationship. Upon receipt, the headend generates an SRv6 TE Policy entry.
3. Establish a BGP-Flow-IPv6 address family-specific peer relationship between the controller and forwarder, so that the controller can dynamically deliver a BGP IPv6 FlowSpec route to the forwarder through the peer relationship.

The following procedure focuses on forwarder configurations.


#### Procedure

1. Establish a BGP-LS peer relationship and a BGP IPv6 SR-Policy address family-specific peer relationship. For details, see [Configuring BGP Peer Relationships Between the Controller and Forwarder](dc_vrp_srv6_cfg_all_0119.html).
2. Establish a BGP-Flow-IPv6 address family-specific peer relationship.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv6-family flow**](cmdqueryname=ipv6-family+flow)
      
      
      
      The BGP-Flow-IPv6 address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* } **enable**
      
      
      
      A BGP IPv6 FlowSpec peer relationship is established.
      
      After the BGP IPv6 FlowSpec peer relationship is established in the BGP-Flow-IPv6 address family view, the BGP IPv6 FlowSpec route created by the traffic analysis server is imported automatically to the BGP routing table and then advertised to the specified BGP IPv6 FlowSpec peer.
   5. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *ipv6-address* } **redirect ipv6 recursive-lookup tunnel** **tunnel-selector** *tunnel-selector-name*
      
      
      
      The device is allowed to recurse the BGP IPv6 FlowSpec routes received from a peer to corresponding tunnels.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.

#### Verifying the Configuration

After configuring BGP IPv6 FlowSpec route redirection to an SRv6 TE Policy, verify the configuration.

* Run the [**display bgp flow ipv6 peer**](cmdqueryname=display+bgp+flow+ipv6+peer) command to check BGP IPv6 FlowSpec peer information.
* Run the [**display bgp flow ipv6 routing-table**](cmdqueryname=display+bgp+flow+ipv6+routing-table) command to check BGP IPv6 FlowSpec routing information.
* Run the [**display bgp flow ipv6 routing-table statistics**](cmdqueryname=display+bgp+flow+ipv6+routing-table+statistics) command to check BGP IPv6 FlowSpec route statistics.