Configuring BGP Peer Tracking
=============================

BGP peer tracking provides fast link or peer fault detection for BGP to speed up network convergence.

#### Context

BFD can be configured to detect peer relationship status changes in order to implement rapid BGP convergence. BFD, however, needs to be configured on the entire network and has poor extensibility. If BFD cannot be deployed to detect BGP peer relationship status changes, you can configure BGP peer tracking on the local device to quickly detect link or peer unreachability, implementing rapid network convergence. In addition, you can adjust the interval between peer unreachability discovery and connection interruption to suppress BGP peer relationship flapping caused by route flapping. This improves BGP network stability.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer+tracking+delay) { *group-name* | *ipv4-address* } **tracking** [ **delay** *delay-time* ]
   
   
   
   BGP peer tracking is configured for a specified peer or peer group.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.