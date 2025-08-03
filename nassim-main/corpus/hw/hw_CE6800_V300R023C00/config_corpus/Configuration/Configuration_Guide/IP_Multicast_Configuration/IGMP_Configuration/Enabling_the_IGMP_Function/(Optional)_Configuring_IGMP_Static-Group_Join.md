(Optional) Configuring IGMP Static-Group Join
=============================================

(Optional) Configuring IGMP Static-Group Join

#### Context

To implement fast and stable multicast data forwarding or direct multicast traffic to an interface, configure a static multicast group on the user-side interface of the multicast device. After a static multicast group is configured on an interface, the multicast device considers that the multicast group always has members on the network segment of the interface, and forwards multicast data of the multicast group to the interface. This function applies to the following scenarios:

* There are stable multicast group members on a network.
* Hosts on a network segment cannot send Report messages, but multicast data needs to be forwarded to the network segment.

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
   [igmp static-group](cmdqueryname=igmp+static-group) group-address [ inc-step-mask { group-mask | group-mask-length } number group-number ] [ source source-address ] [ dot1q vid lowVidValue  ]
   ```
   
   
   
   After an interface is statically added to a multicast group, the multicast forwarding entries created by the device do not have a timer and never expire. As such, the device continuously forwards data to receivers. If receivers no longer require data from the multicast group, run the [**undo igmp static-group**](cmdqueryname=undo+igmp+static-group) command to manually delete the static multicast group configuration.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```