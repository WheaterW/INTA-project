Configuring BGP Load Balancing
==============================

Configuring BGP Load Balancing

#### Prerequisites

Before configuring BGP load balancing, you have completed the following task:

* [Configure basic BGP functions.](vrp_bgp_cfg_0014.html)

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enter the IPv4 unicast address family view.
   
   
   ```
   [ipv4-family](cmdqueryname=ipv4-family+unicast) unicast
   ```
4. Set the maximum number of BGP equal-cost routes that can participate in load balancing.
   
   
   * Configure BGP peer or peer group-based load balancing.
     ```
     [peer](cmdqueryname=peer+load-balancing+as-path-ignore+as-path-relax) { ipv4-address | group-name } load-balancing [ as-path-ignore | as-path-relax ]
     ```
   * Set the maximum number of BGP equal-cost routes that can participate in load balancing globally.
     ```
     [maximum load-balancing](cmdqueryname=maximum+load-balancing+ebgp+ibgp+ecmp-nexthop-changed) [ ebgp | ibgp ] number [ ecmp-nexthop-changed ]
     ```
     
     By default, the maximum number of BGP equal-cost routes for load balancing is 1, indicating that load balancing is not implemented.
     
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

After configuring the function, verify the configuration.

* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) [ *network* ] [ *mask* | *mask-length* ] [ **longer-prefixes** ] command to check information about the BGP routing table.
* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) [ **verbose** ] command to check information about routes in the IP routing table.