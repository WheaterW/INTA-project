(Optional) Configuring a Device to Record ARP Logs for Potential Attacks and Send the Corresponding ARP Traps
=============================================================================================================

(Optional) Configuring a Device to Record ARP Logs for Potential Attacks and Send the Corresponding ARP Traps

#### Context

After a rate limit is configured for ARP or ARP Miss messages, the device counts the number of received ARP or ARP Miss messages. If the number of ARP or ARP Miss messages received in a specified period exceeds the configured limit, the device discards excess ARP or ARP Miss messages. The device considers this is a potential attack, and records ARP logs for the potential attack and sends the corresponding ARP traps to the NMS.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure an interval for recording ARP logs for potential attacks and sending the corresponding ARP traps.
   
   
   ```
   [arp anti-attack log-trap-timer](cmdqueryname=arp+anti-attack+log-trap-timer) timer
   ```
   
   The default interval is 0s. That is, a device does not record ARP logs for potential attacks or send the corresponding ARP traps.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```