Configuring a MinRouteAdvertisementIntervalTimer
================================================

A proper MinRouteAdvertisementIntervalTimer can be configured to suppress frequent route changes, improving BGP network stability.

#### Context

BGP peers use update messages to exchange routing information. Update messages can be used to advertise reachable routes with the same attributes or delete unreachable routes.

BGP does not periodically update a routing table. When BGP routes change, BGP updates the changed BGP routes in the BGP routing table by sending Update messages. If a route changes frequently, to prevent the Router from sending Update messages upon every change, you can set a timer for sending Update messages.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer+route-update-interval) { *ipv4-address* | *group-name* } **route-update-interval** *interval*
   
   
   
   The timer for sending Update messages is set.
   
   
   
   *ipv4-address* specifies the address of a specific peer, while *group-name* specifies the name of a peer group. The timer for sending Update messages configured for a peer takes precedence over that configured for a peer group.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.