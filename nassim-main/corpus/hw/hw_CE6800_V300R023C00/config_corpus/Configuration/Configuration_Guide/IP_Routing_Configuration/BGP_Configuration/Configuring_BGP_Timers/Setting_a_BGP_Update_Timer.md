Setting a BGP Update Timer
==========================

Setting a BGP Update Timer

#### Prerequisites

Before setting a BGP Update timer, you have completed the following task:

* [Configure basic BGP functions.](vrp_bgp_cfg_0014.html)

#### Context

BGP peers use Update messages to exchange routes. Update messages can be used to advertise reachable routes with the same attributes or delete unreachable routes.

BGP does not periodically update a routing table. Once BGP routes change, BGP updates the changed BGP routes in the BGP routing table by sending Update messages. To prevent a device from sending Update messages upon every change in case of frequent changes, set a BGP Update timer that is the interval at which Update messages are sent.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Set a BGP Update timer.
   
   
   ```
   [peer](cmdqueryname=peer+route-update-interval) { ipv4-address | group-name } route-update-interval interval
   ```
   
   By default, the interval at which Update messages are sent to IBGP peers is 15s, and the interval at which Update messages are sent to EBGP peers is 30s.
   
   *ipv4-address* and *group-name* specify a peer and a peer group, respectively. The BGP Update timer configured for a peer takes precedence over that configured for a peer group.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```