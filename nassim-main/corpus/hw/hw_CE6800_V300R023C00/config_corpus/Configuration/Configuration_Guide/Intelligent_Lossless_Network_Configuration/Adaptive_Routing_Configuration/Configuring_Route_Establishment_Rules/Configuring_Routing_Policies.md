Configuring Routing Policies
============================

Configuring Routing Policies

#### Context

The adaptive routing function can be used only after specific routing policies are configured and policy parameters are correctly set. The following routing policies need to be configured:

* Policy for importing public network routes to the routing table of the Mix VPN instance
* Policy for importing public network routes to the routing table of the Non-min VPN instance
* Policy for importing routes from the Non-min VPN instance to the routing table of the Mix VPN instance
* Policy for advertising EBGP routes of the public network instance
* Policies for advertising and receiving IBGP routes of the public network instance
* Policies for advertising and receiving IBGP routes of the Non-min VPN instance

Routing policy parameters must be set by following the rule that the cost of a route within a group and between groups increments by 1 and 1000, respectively, each time the route is advertised to a new hop. In addition, you must correctly use the corresponding routing policy when configuring BGP routes and cannot modify other parameters except the policy name. For details about how to set routing policy parameters, see the operations of configuring routing policies in [Example for Configuring Adaptive Routing](galaxy_adaptive_routing_cfg_0016.html).


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a route-policy with a node and enter the route-policy view.
   
   
   ```
   [route-policy](cmdqueryname=route-policy) route-policy-name matchMode node node
   ```
3. Configure if-match clauses in the route-policy to match the cost of routes.
   
   
   ```
   [if-match cost](cmdqueryname=if-match+cost) cost
   [if-match cost](cmdqueryname=if-match+cost) { greater-equal greater-equal-value [ less-equal less-equal-value ] | less-equal less-equal-value }
   ```
4. Configure if-match clauses in the route-policy to match BGP routes.
   
   
   ```
   [if-match route-type](cmdqueryname=if-match+route-type) { ibgp | ebgp }
   ```
5. Configure the apply clauses in the route-policy to set the cost of routes.
   
   
   ```
   [apply cost](cmdqueryname=apply+cost) [ + | - ] cost
   ```
6. In the routing policy for receiving routes, configure apply clauses in the route-policy to set the next hop address of the route received from the peer to the IP address of the peer.
   
   
   ```
   [apply ip-address next-hop](cmdqueryname=apply+ip-address+next-hop) peer-address
   ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```