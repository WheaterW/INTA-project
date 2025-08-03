Enabling Slow Peer Detection
============================

After slow peer detection is configured on a device, the device identifies the slow BGP peer (if any) and removes it from the update peer-group to prevent this slow peer from affecting route advertisement to other peers in this update peer-group. Slow peer detection speeds up BGP network convergence.

#### Context

An update peer-group may consist of multiple peers. If a network problem (congestion for example) occurs and slows down the speed at which the local device advertises routes to a peer in the update peer-group, the speed at which the local device advertises routes to other peers in the update peer-group is affected. To prevent this impact, enable slow peer detection on the device.

After slow peer detection is enabled, the local device calculates the difference between the time taken to send messages to each peer in the update peer-group and the shortest time taken to send messages to each peer in the group. If the difference between the time taken to send messages to a peer and the shortest time is greater than the threshold specified for slow peer detection, the local device considers this peer as a slow peer and removes it from the update peer-group, which prevents this slow peer from affecting route advertisement to other peers in the group.

If BGP Update messages fail to be advertised, slow peers cannot be detected using the original slow peer detection mode. To address this problem, configure the absolute mode for slow peer detection. If the delay in sending messages to a peer is greater than the absolute time threshold, the peer is considered a slow peer.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BGP view.
   
   
   ```
   [bgp](cmdqueryname=bgp) as-number
   ```
3. Enable slow peer detection.
   
   
   ```
   [slow-peer detection](cmdqueryname=slow-peer+detection+threshold) threshold threshold-value
   ```
   
   The **threshold** *threshold-value* parameter specifies a threshold for slow peer detection. If the difference between the time taken to send messages to a BGP peer and the time taken to send messages to the fastest peer in the group exceeds the *threshold-value*, the local device identifies the former peer to be a slow one and removes it from the update peer-group. If this parameter is not specified, the default threshold (300s) is used.
   
   By default, slow peer detection is enabled.
4. (Optional) Enable slow peer detection in absolute mode.
   
   
   ```
   [slow-peer absolute-detection](cmdqueryname=slow-peer+absolute-detection+threshold) threshold threshold
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```