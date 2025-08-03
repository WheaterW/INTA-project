Configuring BGP4+ Auto FRR
==========================

Configuring BGP4+ Auto FRR

#### Prerequisites

Before configuring BGP4+ Auto FRR, you have completed the following tasks:

* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).
* [Configure BFD for BGP4+.](vrp_bgp6_cfg_0061.html)

#### Context

As networks continue to develop, real-time services, such as voice, online video, and financial services, pose higher requirements for real-time transmission. As such, primary and backup links are typically deployed on a network to ensure the stability of these services. In the traditional forwarding mode, a BGP4+ device selects the optimal route out of several routes destined for the same network and delivers the route to the FIB table to guide data forwarding. If the optimal route fails, the BGP4+ device must wait for route convergence to be completed, after which the BGP4+ device reselects an optimal route and delivers it to the FIB table to restore services. This process leads to long service interruption, resulting in a failure to meet service requirements.

BGP4+ Auto FRR allows a routing device to select the optimal route from the routes that are bound for the same destination network and automatically add information about the sub-optimal route to the backup forwarding entries of the optimal route. If the primary link fails, the routing device quickly switches traffic to the backup link. This switchover does not rely on route convergence and can be performed within sub-seconds, greatly reducing service interruption time.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enter the BGP-IPv6 unicast address family view.
   
   
   ```
   [ipv6-family](cmdqueryname=ipv6-family+unicast) unicast
   ```
4. Enable BGP4+ Auto FRR for unicast routes.
   
   
   ```
   [auto-frr](cmdqueryname=auto-frr)
   ```
   
   By default, BGP4+ Auto FRR is not enabled for unicast routes.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After configuring the function, verify the configuration.

* Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) *ipv6-address* *prefix-length* [ **longer-match** ] [ **verbose** ] command to check the backup forwarding information of BGP4+ routes in the routing table.