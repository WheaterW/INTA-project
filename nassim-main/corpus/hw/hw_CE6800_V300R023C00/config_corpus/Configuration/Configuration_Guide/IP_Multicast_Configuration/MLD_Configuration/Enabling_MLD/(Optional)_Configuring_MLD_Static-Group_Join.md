(Optional) Configuring MLD Static-Group Join
============================================

(Optional) Configuring MLD Static-Group Join

#### Context

If IPv6 users on a user network segment frequently request multicast data, configure a multicast device's interface connected to the user network segment to statically join an IPv6 multicast group. The multicast device then rapidly responds to the users' requests, shortening the channel switching delay.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of the interface connected to the user network segment.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   
   
   Determine whether to perform this step based on the current interface working mode.
4. Add the interface to a multicast group statically.
   
   
   ```
   [mld static-group](cmdqueryname=mld+static-group) ipv6-group-address [ inc-step-mask ipv6-group-mask-length number group-number ] [ source ipv6-source-address ]
   ```
   
   
   
   After an interface is statically added to a multicast group, the multicast forwarding entries created by the device do not have a timer and never expire. As such, the device continuously forwards data to receivers. If receivers no longer require data from the multicast group, run the [**undo mld static-group**](cmdqueryname=undo+mld+static-group) command to manually delete the static multicast group configuration.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```