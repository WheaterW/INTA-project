(Optional) Configuring Per-Path Label Distribution for BGP Add-Path Labeled Routes
==================================================================================

After per-path label distribution is configured for BGP Add-Path labeled routes, a device can apply for a unique label for each route when advertising multiple routes to a BGP Add-Path peer. After the peer receives multiple routes with different labels, it can implement BGP LSP load balancing.

#### Context

On a large-scale network, there may be multiple routes to the same destination. However, BGP does not apply for different labels for the routes when advertising the routes to an Add-Path peer. This may cause traffic imbalance. To balance traffic over BGP LSPs, you can configure a device to accept multiple routes with the same prefix from a BGP labeled address family peer and apply for different labels when advertising the routes to an Add-Path peer. In this manner, traffic can be balanced among multiple BGP LSPs to the remote PE.

On the network shown in [Figure 1](#EN-US_TASK_0000001569331178__fig18507732132816), IBGP peer relationships are established between PEs and ASBRs, and EBGP peer relationships are established between ASBRs. Add-Path is deployed between ASBRs and PEs and between ASBRs so that each ASBR can advertise multiple routes with the same prefix to its peers.

**Figure 1** Typical networking of per-path label distribution for BGP Add-Path labeled routes  
![](figure/en-us_image_0000001569491138.png)

The specific process is as follows:

1. PE1 imports a route to the BGP labeled address family and advertises the labeled route to ASBR1 and ASBR2.
2. After receiving the labeled route from PE1, ASBR1 and ASBR2 advertise the route to ASBR3 and ASBR4.
3. After receiving labeled routes from ASBR1 and ASBR2, ASBR3 and ASBR4 each apply for different labels for the two Add-Path routes with the same prefix before advertising them to peers. Specifically, ASBR3 and ASBR4 each advertise two routes with the same next hop but different labels to ASBR5 and two routes with the same next hop but different labels to ASBR6.
4. After receiving the routes with the same next hop but different labels from ASBR3 and ASBR4, ASBR5 and ASBR6 generate Add-Path routes and apply for different labels when advertising the routes to peers. ASBR5 advertises four routes with the same next hop but different labels to PE2 and PE3, and so does ASBR6. PE2 and PE3 each receive eight labeled routes with the same prefix.
5. After load balancing among labeled BGP routes is enabled on PE2 and PE3, routes with the same prefix but different labels on PE2 and PE3 can load-balance traffic. That is, traffic can be balanced among eight BGP LSPs on PE2 and PE3.

#### Pre-configuration Tasks

Before configuring per-path label distribution for BGP Add-Path labeled routes, complete the following tasks in the BGP labeled address family on PEs and ASBRs:

* [Configure basic BGP functions.](dc_vrp_bgp_cfg_3004.html)
* [Configure BGP Add-Path.](dc_vrp_bgp_cfg_3096.html)

#### Procedure

1. Perform the following configurations on ASBR3 and ASBR4:
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **labeled-unicast** command to enter the BGP labeled address family view.
   4. Run the [**apply-label per-path**](cmdqueryname=apply-label+per-path) command to configure the device to apply for different labels for multiple Add-Path routes with the same prefix when advertising the routes to peers.
   5. Run the [**quit**](cmdqueryname=quit) command to return to the BGP view.
   6. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
2. Perform the following configurations on ASBR5 and ASBR6:
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **labeled-unicast** command to enter the BGP labeled address family view.
   4. Run the [**bestroute add-path nexthop-ignore**](cmdqueryname=bestroute+add-path+nexthop-ignore) command to configure labeled routes with the same prefix and same next hop to form Add-Path routes.
   5. Run the [**apply-label per-path**](cmdqueryname=apply-label+per-path) command to configure the device to apply for different labels for multiple Add-Path routes with the same prefix when advertising the routes to peers.
   6. Run the [**quit**](cmdqueryname=quit) command to return to the BGP view.
   7. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
3. Perform the following configurations on PE2 and PE3:
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **labeled-unicast** command to enter the BGP labeled address family view.
   4. Run the [**maximum load-balancing ingress-lsp**](cmdqueryname=maximum+load-balancing+ingress-lsp) *ingressNumber* command to set the maximum number of equal-cost BGP labeled routes for BGP LSP load balancing.
   5. Run the [**load-balancing nexthop-ignore**](cmdqueryname=load-balancing+nexthop-ignore) command to configure load balancing among labeled routes with the same prefix and same next hop.
   6. Run the [**quit**](cmdqueryname=quit) command to return to the BGP view.
   7. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   8. Run the [**tunnel-policy**](cmdqueryname=tunnel-policy) *policy-name* command to create a tunnel policy and enter its view.
   9. Run the [**tunnel select-seq**](cmdqueryname=tunnel+select-seq) **bgp** **load-balance-number** *load-balance-number* command to configure the sequence in which each type of tunnel is selected and the number of tunnels participating in load balancing.
   10. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

After configuring per-path label distribution for BGP Add-Path labeled routes, run the following commands to check the configurations.

* Run the [**display bgp**](cmdqueryname=display+bgp) **labeled** [**routing-table**](cmdqueryname=routing-table) **label** command to check per-path labels.
* Run the [**display bgp**](cmdqueryname=display+bgp) **labeled** [**routing-table**](cmdqueryname=routing-table) *ipv4-address* { *mask-length* | *mask* } command to check per-path label values.