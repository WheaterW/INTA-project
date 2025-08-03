Redirecting a Public IPv4 BGP FlowSpec Route to an SR-MPLS TE Policy (Dynamic Delivery by a Controller)
=======================================================================================================

After a controller dynamically delivers a BGP FlowSpec route and an SR-MPLS TE Policy to a forwarder, the forwarder needs to redirect the BGP FlowSpec route to the SR-MPLS TE Policy.

#### Usage Scenario

If a controller is deployed, the controller can be used to deliver a public IPv4 BGP FlowSpec route and an SR-MPLS TE Policy. The procedure involved in redirecting the public IPv4 BGP FlowSpec route to the SR-MPLS TE Policy is as follows:

1. Establish a BGP-LS peer relationship between the controller and forwarder, enabling the controller to collect network information, such as topology and label information, through BGP-LS.
2. Establish a BGP IPv4 SR-MPLS TE Policy peer relationship between the controller and forwarder, enabling the controller to deliver a dynamically computed SR-MPLS TE Policy path to the ingress through the peer relationship. After receiving the SR-MPLS TE Policy, the ingress generates corresponding entries.
3. Establish a BGP-Flow address family peer relationship between the controller and forwarder, enabling the controller to dynamically deliver a BGP FlowSpec route.

The following procedure focuses on forwarder configurations.


#### Prerequisites

Before redirecting a public IPv4 BGP FlowSpec route to an SR-MPLS TE Policy, complete the following tasks:

* [Configuring a BGP Peer](dc_vrp_bgp_cfg_3006.html)
* [Configuring an SR-MPLS TE Policy (Dynamic Delivery by a Controller)](dc_vrp_sr_all_cfg_0067.html)

#### Procedure

1. Establish BGP-LS and BGP IPv4 SR-MPLS TE Policy peer relationships. For details, see [Configuring a BGP IPv4 SR-MPLS TE Policy Peer Relationship Between a Controller and a Forwarder](dc_vrp_sr_all_cfg_0069.html).
2. Establish a BGP-Flow address family peer relationship.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bgp**](cmdqueryname=bgp) *as-number*
      
      
      
      The BGP view is displayed.
   3. Run [**ipv4-family flow**](cmdqueryname=ipv4-family+flow)
      
      
      
      The BGP-Flow address family view is displayed.
   4. Run [**peer**](cmdqueryname=peer) *ipv4-address* [**enable**](cmdqueryname=enable)
      
      
      
      The BGP FlowSpec peer relationship is enabled.
      
      After the BGP FlowSpec peer relationship is established in the BGP-Flow address family view, the manually created BGP FlowSpec route is automatically imported to the BGP-Flow routing table and then sent to each BGP FlowSpec peer.
   5. Run [**peer**](cmdqueryname=peer) *ipv4-address* **redirect ip**
      
      
      
      The device is enabled to process the BGP FlowSpec route's redirection next hop attribute that is received from a peer and configured using the **apply redirect ip** command.
   6. Run [**redirect ip recursive-lookup tunnel**](cmdqueryname=redirect+ip+recursive-lookup+tunnel) [ **tunnel-selector** *tunnel-selector-name* ]
      
      
      
      The device is enabled to recurse the received routes that carry the redirection next hop attribute to tunnels.
   7. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.

#### Verifying the Configuration

After configuring the redirection, verify the configuration.

* Run the [**display bgp flow peer**](cmdqueryname=display+bgp+flow+peer) [ [ *ipv4-address* ] **verbose** ] command to check information about BGP FlowSpec peers.
* Run the [**display bgp flow routing-table**](cmdqueryname=display+bgp+flow+routing-table) command to check BGP FlowSpec routing information.
* Run the [**display flowspec statistics**](cmdqueryname=display+flowspec+statistics) *reindex* command to check statistics about traffic transmitted over BGP FlowSpec routes.