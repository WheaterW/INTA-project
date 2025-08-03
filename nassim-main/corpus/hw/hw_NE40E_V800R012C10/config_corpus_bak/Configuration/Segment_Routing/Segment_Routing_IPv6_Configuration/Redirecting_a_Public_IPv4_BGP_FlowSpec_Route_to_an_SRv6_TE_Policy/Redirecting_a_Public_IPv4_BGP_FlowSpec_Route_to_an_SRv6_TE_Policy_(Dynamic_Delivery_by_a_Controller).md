Redirecting a Public IPv4 BGP FlowSpec Route to an SRv6 TE Policy (Dynamic Delivery by a Controller)
====================================================================================================

Use a controller to dynamically deliver a BGP FlowSpec route to a forwarder and configure a redirection rule on the forwarder to redirect the route to a specified SRv6 TE Policy.

#### Prerequisites

Before redirecting a public IPv4 BGP FlowSpec route to an SRv6 TE Policy in controller-based dynamic delivery mode, complete the following tasks:

* [Configure a BGP peer relationship.](dc_vrp_bgp_cfg_3006.html)
* [Configure an SRv6 TE Policy in controller-based dynamic delivery mode.](dc_vrp_srv6_cfg_all_0116.html)

#### Context

If a controller is deployed, the controller can be used to configure a public IPv4 BGP FlowSpec route to be redirected to an SRv6 TE Policy. The configuration process is as follows:

1. Establish a BGP-LS peer relationship between the controller and forwarder, enabling the controller to collect network information, such as topology and label information, through BGP-LS.
2. Establish an IPv6 SR-Policy address family-specific BGP peer relationship between the controller and forwarder, so that the controller can deliver the route of a dynamically computed SRv6 TE Policy path to the headend through the peer relationship. After receiving the SRv6 TE Policy, the ingress generates corresponding entries.
3. Establish a BGP-Flow address family peer relationship between the controller and forwarder, enabling the controller to dynamically deliver a BGP FlowSpec route.

The following procedure focuses on forwarder configurations.


#### Procedure

1. Establish BGP-LS and BGP IPv6 SR-Policy peer relationships. For details, see [Configuring BGP Peer Relationships Between the Controller and Forwarder](dc_vrp_srv6_cfg_all_0119.html).
2. Establish a BGP-Flow address family peer relationship.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv4-family flow**](cmdqueryname=ipv4-family+flow)
      
      
      
      The BGP-Flow address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer) *ipv4-address* [**enable**](cmdqueryname=enable)
      
      
      
      The BGP FlowSpec peer relationship is enabled.
      
      After the BGP FlowSpec peer relationship is established in the BGP-Flow address family view, the manually generated BGP FlowSpec route is automatically imported to the BGP-Flow routing table and then sent to each peer.
   5. Run [**peer**](cmdqueryname=peer) *ipv4-address* **redirect tunnelv6**
      
      
      
      The device is enabled to process the redirection next-hop IPv6 address, color, and prefix SID attributes carried in BGP FlowSpec routes received from a peer.
   6. Run [**redirect tunnelv6 tunnel-selector**](cmdqueryname=redirect+tunnelv6+tunnel-selector) *tunnel-selector-name*
      
      
      
      The device is enabled to recurse received routes with the redirection next-hop IPv6 address, color, and prefix SID attributes to SRv6 TE Policies.
   7. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.

#### Verifying the Configuration

After configuring the redirection, verify the configuration.

* Run the [**display bgp flow peer**](cmdqueryname=display+bgp+flow+peer) [ [ *ipv4-address* ] **verbose** ] command to check information about BGP FlowSpec peers.
* Run the [**display bgp flow routing-table**](cmdqueryname=display+bgp+flow+routing-table) command to check BGP FlowSpec routing information.
* Run the [**display flowspec statistics**](cmdqueryname=display+flowspec+statistics) *reindex* command to check statistics about traffic transmitted over BGP FlowSpec routes.