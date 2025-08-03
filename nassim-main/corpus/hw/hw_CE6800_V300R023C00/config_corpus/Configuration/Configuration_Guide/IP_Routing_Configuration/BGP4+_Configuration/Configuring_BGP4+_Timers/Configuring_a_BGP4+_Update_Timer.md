Configuring a BGP4+ Update Timer
================================

Configuring a BGP4+ Update Timer

#### Prerequisites

Before configuring a BGP4+ Update timer, you have completed the following task:

* [Configure basic BGP4+ functions](vrp_bgp6_cfg_0006.html).

#### Context

BGP4+ does not periodically update its routing table. Once BGP4+ routes change, BGP4+ updates the changed BGP4+ routes in the routing table by sending Update messages. If a route changes frequently, to prevent a BGP4+ device from sending Update messages upon every change, set the interval at which Update messages are sent.


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
4. Set the interval at which BGP4+ Update messages are sent.
   
   
   ```
   [peer](cmdqueryname=peer+route-update-interval) { group-name | ipv6-address | ipv4-address } route-update-interval interval
   ```
   
   By default, a device sends Update messages to IBGP peers at an interval of 15s and to EBGP peers at an interval of 30s.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```