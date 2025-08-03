Configuring BGP4+ Load Balancing
================================

Configuring BGP4+ Load Balancing

#### Prerequisites

Before configuring BGP4+ load balancing, you have completed the following task:

* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).

#### Context

Configuring BGP4+ load balancing better utilizes network resources.

On large networks, there may be multiple valid routes to the same destination. BGP4+, however, advertises only the optimal route to its peers. This may result in traffic imbalance.

Either of the following methods can be used to resolve the traffic imbalance:

* Use BGP4+ route-policies for load balancing. For example, you can use a route-policy to modify the Local\_Pref, AS\_Path, Origin, or MED attribute of BGP4+ routes to control traffic forwarding paths, helping implement load balancing.
* Use multiple paths to implement traffic load balancing. This method requires that multiple equal-cost routes exist and the number of routes allowed to participate in load balancing be set. Load balancing can be implemented globally or for a specified peer or peer group.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enter the IPv6 unicast address family view.
   
   
   ```
   [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
   ```
4. Set the maximum number of BGP4+ equal-cost routes for load balancing.
   
   
   * Configure BGP4+ peer- or peer group-based load balancing.
     ```
     [peer](cmdqueryname=peer+load-balancing+as-path-ignore+as-path-relax) ipv4-address load-balancing [ as-path-ignore | as-path-relax ]
     ```
     ```
     [peer](cmdqueryname=peer+load-balancing+as-path-ignore+as-path-relax) ipv6-address load-balancing [ as-path-ignore | as-path-relax ]
     ```
     ```
     [peer](cmdqueryname=peer+load-balancing+as-path-ignore+as-path-relax) group-name load-balancing [ as-path-ignore | as-path-relax ]
     ```
   * Set the maximum number of BGP4+ equal-cost routes for load balancing globally.
     ```
     [maximum load-balancing](cmdqueryname=maximum+load-balancing+ebgp+ibgp+ecmp-nexthop-changed) [ ebgp | ibgp ] number [ ecmp-nexthop-changed ]
     ```
     
     By default, the maximum number of BGP4+ equal-cost routes for load balancing is 1, indicating that load balancing is not implemented.
     
     **ebgp** indicates that load balancing is implemented only among EBGP routes.
     
     **ibgp** indicates that load balancing is implemented only among IBGP routes.
     
     If neither **ebgp** nor **ibgp** is specified, EBGP and IBGP routes can compete for preferred routes to balance traffic, and the number of allowed load-balancing EBGP routes is the same as the number of allowed load-balancing IBGP routes.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     Before routes to the same destination implement load balancing on a public network, a device determines the type of optimal route. If IBGP routes are optimal, only IBGP routes carry out load balancing. If EBGP routes are optimal, only EBGP routes carry out load balancing. This means that load balancing cannot be implemented using both IBGP and EBGP routes with the same destination address.
5. (Optional) Run one of the following commands to change a load balancing rule as needed:
   
   
   * Disable the device from comparing the AS\_Path attributes of the routes for load balancing.
     ```
     [load-balancing as-path-ignore](cmdqueryname=load-balancing+as-path-ignore)
     ```
   * Disable the device from comparing the AS\_Path attributes of the same length of the routes for load balancing.
     ```
     [load-balancing as-path-relax](cmdqueryname=load-balancing+as-path-relax)
     ```
   * Disable the device from comparing the IGP metric values of the routes for load balancing.
     ```
     [load-balancing igp-metric-ignore](cmdqueryname=load-balancing+igp-metric-ignore)
     ```
   * Disable the device from comparing the MED values of the routes for load balancing.
     ```
     [load-balancing med-ignore](cmdqueryname=load-balancing+med-ignore)
     ```![](public_sys-resources/note_3.0-en-us.png) 
   
   Address family views of the preceding commands are different. When running any of the commands, ensure that the command is run in a correct address family view.
   
   Change load balancing rules based on networking. Exercise caution when running the preceding commands.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After completing the configuration, verify it.

* Run the [**display bgp ipv6 routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) *ipv6-address* *prefix-length* command to check information about routes in the BGP4+ routing table.