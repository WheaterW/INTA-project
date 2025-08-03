Enabling Slow Peer Detection
============================

After slow peer detection is configured on a device, the device identifies the slow BGP peer (if any) and removes it from the update peer-group to prevent this slow peer from affecting route advertisement to other peers in this update peer-group. Slow peer detection speeds up BGP network convergence.

#### Context

An update peer-group may consist of multiple peers. If a network problem (congestion for example) occurs and slows down the speed at which the local device advertises routes to a peer in the update peer-group, the speed at which the local device advertises routes to other peers in the update peer-group is affected. Slow peer detection is enabled by default so that route advertisement to other peers in the update peer-group is not affected.

After slow peer detection is enabled, the local device calculates the difference between the time taken to send messages to each peer in the update peer-group and the shortest time taken to send messages to each peer in the group. If the difference between the time taken to send messages to a peer and the shortest time is greater than the threshold specified for slow peer detection, the local device considers this peer as a slow peer and removes it from the update peer-group, which prevents this slow peer from affecting route advertisement to other peers in the group.

If BGP Update messages fail to be advertised, slow peers cannot be detected using the original slow peer detection mode. To address this problem, configure the absolute mode for slow peer detection. If the delay in sending messages to a peer is greater than the absolute time threshold, the peer is considered a slow peer.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**slow-peer detection**](cmdqueryname=slow-peer+detection+threshold) **threshold** *threshold-value*
   
   
   
   A threshold is configured for slow peer detection.
   
   **threshold** *threshold-value* specifies a slow peer detection threshold. If the difference between the time taken to send messages to a peer in an update peer-group and the shortest time taken to send messages to each peer in the group is greater than the *threshold-value*, the local device considers this peer as a slow peer and removes it from the update peer-group.
4. (Optional) Run [**slow-peer absolute-detection**](cmdqueryname=slow-peer+absolute-detection+threshold) **threshold** *absolute-threshold-value*
   
   
   
   Slow peer detection in absolute time mode is enabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.