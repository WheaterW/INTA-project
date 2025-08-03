Redirecting a Public IPv4 BGP FlowSpec Route to an SR-MPLS TE Policy (Manual Configuration)
===========================================================================================

Manually generate a BGP FlowSpec route and configure redirection rules to redirect the route to an SR-MPLS TE Policy.

#### Usage Scenario

If no controller is deployed, perform the following operations to manually redirect a public IPv4 BGP Flow Specification route to an SR-MPLS TE Policy:

1. Manually configure an SR-MPLS TE Policy.
2. Manually configure a BGP FlowSpec route and define redirection rules. BGP FlowSpec route redirection is based on <Redirection IP address, Color>. If the redirection IP address and color attributes of a BGP FlowSpec route match the endpoint and color attributes of an SR-MPLS TE Policy, the route can be successfully redirected to the SR-MPLS TE Policy.
3. To enable the device to advertise the BGP FlowSpec route to another device, configure a BGP peer relationship in the BGP-Flow address family.

#### Prerequisites

Before redirecting a public IPv4 BGP FlowSpec route to an SR-MPLS TE Policy, complete the following tasks:

* [Configure a BGP peer relationship.](dc_vrp_bgp_cfg_3006.html)
* [Configure an SR-MPLS TE Policy (manual configuration).](dc_vrp_sr_all_cfg_0059.html)

#### Procedure

* Configure a BGP FlowSpec route.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**flow-route**](cmdqueryname=flow-route) *flowroute-name*
     
     A static BGP FlowSpec route is created, and the Flow-Route view is displayed.
  3. Configure **if-match** clauses. For details, see "BGP Flow Specification Configuration" in *Configuration* - *Security*.
  4. Run [**apply redirect**](cmdqueryname=apply+redirect) **ip** *redirect-ip-rt* **color** *colorvalue*The device is enabled to precisely redirect the traffic that matches the if-match clauses to the SR-MPLS TE Policy.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To enable the device to process the redirection next hop attribute that is received from a peer and configured using the [**apply redirect**](cmdqueryname=apply+redirect) **ip** *redirect-ip-rt* **color** *colorvalue* command, run the [**peer redirect ip**](cmdqueryname=peer+redirect+ip) command.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* (Optional) Configure a BGP peer relationship in the BGP-Flow address family.
  
  
  
  Establish a BGP FlowSpec peer relationship between the ingress of the SR-MPLS TE Policy and the device on which the BGP FlowSpec route is manually generated. If the BGP FlowSpec route is manually generated on the ingress of the SR-MPLS TE Policy, skip this step.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**ipv4-family flow**](cmdqueryname=ipv4-family+flow)
     
     
     
     The BGP-Flow address family view is displayed.
  4. Run [**peer**](cmdqueryname=peer) *ipv4-address* [**enable**](cmdqueryname=enable)
     
     
     
     The BGP FlowSpec peer relationship is enabled.
     
     After the BGP FlowSpec peer relationship is established in the BGP-Flow address family view, the manually generated BGP FlowSpec route is automatically imported to the BGP-Flow routing table and then sent to each peer.
  5. Run [**peer**](cmdqueryname=peer) *ipv4-address* **redirect ip**
     
     
     
     The device is enabled to process the BGP FlowSpec route's redirection next hop attribute that is received from a peer and configured using the [**apply redirect**](cmdqueryname=apply+redirect) **ip** command.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After configuring the redirection, verify the configuration.

* Run the [**display bgp flow peer**](cmdqueryname=display+bgp+flow+peer) [ [ *ipv4-address* ] **verbose** ] command to check information about BGP FlowSpec peers.
* Run the [**display bgp flow routing-table**](cmdqueryname=display+bgp+flow+routing-table) command to check BGP FlowSpec routing information.
* Run the [**display flowspec statistics**](cmdqueryname=display+flowspec+statistics) *reindex* command to check statistics about traffic transmitted over BGP FlowSpec routes.