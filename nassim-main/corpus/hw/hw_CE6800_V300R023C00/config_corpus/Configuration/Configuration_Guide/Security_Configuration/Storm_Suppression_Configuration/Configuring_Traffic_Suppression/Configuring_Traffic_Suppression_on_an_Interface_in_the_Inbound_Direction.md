Configuring Traffic Suppression on an Interface in the Inbound Direction
========================================================================

Configuring Traffic Suppression on an Interface in the Inbound Direction

#### Context

To prevent broadcast storms, you can configure traffic suppression on an interface in the inbound direction. The device supports traffic suppression for broadcast packets, unknown multicast packets, or unknown unicast packets by percentage of bandwidth occupied or packet rate. When the traffic volume of any of these packet types exceeds the threshold, the system discards excess packets to reduce the traffic volume to within an appropriate range.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Configure traffic suppression on an interface in the inbound direction.
   
   
   ```
   [storm suppression](cmdqueryname=storm+suppression) { broadcast | multicast | unknown-unicast } { percent-value | cir cir-value [ gbps | kbps | mbps ] [ cbs cbs-value [ bytes | kbytes | mbytes ] ] | packets packets-per-second }
   ```
   
   If traffic suppression is configured for packets of the same type on an interface in the inbound direction for multiple times and parameters of *percent-value* and **cir** *cir-value* are specified, only the latest configuration takes effect.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display storm suppression**](cmdqueryname=display+storm+suppression) { ****broadcast**** | ****multicast**** | ****unknown-unicast**** } [ **interface** *interface-type* *interface-number* ] command to check the configured and actual traffic suppression thresholds on an interface in the inbound direction.

![](public_sys-resources/note_3.0-en-us.png) 

The rate limit threshold of traffic suppression and the actual rate limit may differ, in which case the actual rate limit of packets is used.