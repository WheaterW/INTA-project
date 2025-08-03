Configuring BGP LSP Load Balancing
==================================

Configuring BGP LSP load balancing improves network resource utilization and reduces network congestion.

#### Usage Scenario

On large networks, there may be multiple valid routes to the same destination. BGP, however, advertises only the optimal route to its peers, which may result in load imbalance.

Either of the following methods can be used to resolve the problem:

* Use BGP policies for load balancing. For example, use a routing policy to modify the Local\_Pref, AS\_Path, Origin, or MED attribute of BGP routes to divert traffic to different forwarding paths for load balancing.
* Use multiple paths for load balancing. To use this method, equal-cost routes must exist and you need to configure the maximum number of load-balancing routes.

In some BGP LSP scenarios, for example, in the scenario where BGP unicast routes recurse to LSPs, or in the scenario where BGP LSPs can recurse to multiple TE/LDP tunnels, traffic must be balanced to prevent network congestion. BGP LSP load balancing allows traffic to be balanced based on the maximum number of load-balancing routes configured on ingress and transit nodes of BGP LSPs when the traffic is forwarded along the BGP LSPs, which improves network resource utilization and reduces network congestion.


#### Pre-configuration Tasks

Before configuring BGP LSP load balancing, establish BGP LSPs.


#### Procedure

* Configure ingress LSP load balancing on an ingress node.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     The BGP view is displayed.
  3. (Optional) Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     The IPv4 unicast address family view is displayed.
  4. Run [**maximum load-balancing ingress-lsp**](cmdqueryname=maximum+load-balancing+ingress-lsp) *ingressNumber*
     
     The maximum number of equal-cost BGP labeled routes is set for ingress LSP load balancing.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Configure transit LSP load balancing on a transit node.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     The BGP view is displayed.
  3. (Optional) Run [**ipv4-family**](cmdqueryname=ipv4-family+unicast) **unicast**
     
     The IPv4 unicast address family view is displayed.
  4. Run [**maximum load-balancing transit-lsp**](cmdqueryname=maximum+load-balancing+transit-lsp) *transitNumber*
     
     The maximum number of equal-cost BGP labeled routes is set for transit LSP load balancing.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.

#### Verifying the Configuration

After configuring transit LSP load balancing, you can run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) and [**display ip routing-table**](cmdqueryname=display+ip+routing-table) commands to check whether load balancing has taken effect on the transit node. If the same destination IP address corresponds to more than one next hop, load balancing has taken effect.