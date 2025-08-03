Configuring Traffic Suppression Associated with MAC Address Flapping
====================================================================

Configuring Traffic Suppression Associated with MAC Address Flapping

#### Context

If the device enabled with MAC address flapping detection detects MAC address flapping on an interface, traffic suppression is triggered on the interface. When traffic suppression associated with MAC address flapping is configured, the device can use the CIR or the percentage of bandwidth occupied as the traffic suppression threshold and forcibly forward packets based on the threshold.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the threshold for traffic suppression associated with MAC address flapping.
   
   
   
   Configure the threshold for traffic suppression associated with MAC address flapping on interfaces.
   
   
   
   ```
   [storm suppression mac-address flapping](cmdqueryname=storm+suppression+mac-address+flapping) { percent-value | cir cir-value [ kbps | mbps | gbps ] } [ force ]
   ```
   
   By default, the threshold for traffic suppression associated with MAC address flapping is the percentage of bandwidth occupied, and its value is 1%.
   
   ![](public_sys-resources/note_3.0-en-us.png) When MAC address flapping occurs on an interface configured with traffic suppression:
   * If this command is configured and **force** is specified, traffic suppression associated with MAC address flapping takes effect.
   * If this command is not configured or **force** is not specified, traffic suppression takes effect on the interface.
   Traffic suppression associated with MAC address flapping does not take effect in the following scenarios:
   * If MAC address flapping occurs on a peer-link interface, traffic suppression does not take effect on the peer-link interface.
   * If storm control is configured on an interface, traffic suppression associated with MAC address flapping does not take effect on the interface.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```