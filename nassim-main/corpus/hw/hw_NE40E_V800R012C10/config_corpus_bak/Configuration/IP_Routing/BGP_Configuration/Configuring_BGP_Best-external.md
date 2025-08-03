Configuring BGP Best-external
=============================

Border Gateway Protocol (BGP) Best-external can speed up route convergence if the primary link fails.

#### Usage Scenario

If multiple routes to the same destination are available, a BGP device selects one optimal route based on BGP route selection policies and advertises the route to its BGP peers. This optimal route may be advertised by either an External Border Gateway Protocol (EBGP) peer or an Internal Border Gateway Protocol (IBGP) peer.

However, in scenarios with master and backup provider edges (PEs), if routes are selected based on the preceding policies and the primary link fails, the BGP route convergence takes a long time because no backup route is available. To address this problem, configure BGP Best-external on the backup PE.

The following figure shows the networking with master and backup PEs.

**Figure 1** Networking with master and backup PEs  
![](images/fig_dc_vrp_bgp_cfg_309102.png)

BGP Best-external must be enabled on the backup PE (PE2).


#### Pre-configuration Tasks

Before configuring BGP Best-external, [configure basic BGP functions](dc_vrp_bgp_cfg_3004.html).


#### Configuration Procedures

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   The BGP view is displayed.
3. Run [**bestroute best-external**](cmdqueryname=bestroute+best-external)
   
   The device is enabled to select BGP Best-external routes.
4. Run [**peer**](cmdqueryname=peer+advertise+best-external) { *ipv4-address* | *group-name* } **advertise best-external**
   
   BGP is enabled to advertise Best-external routes to the specified peer.
5. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

Run the [**display bgp peer**](cmdqueryname=display+bgp+peer+verbose) **verbose** command to check the BGP Best-external status.