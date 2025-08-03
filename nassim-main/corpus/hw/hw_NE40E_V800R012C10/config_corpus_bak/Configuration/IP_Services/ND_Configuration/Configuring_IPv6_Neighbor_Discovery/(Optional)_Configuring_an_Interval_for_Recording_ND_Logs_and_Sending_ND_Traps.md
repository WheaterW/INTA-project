(Optional) Configuring an Interval for Recording ND Logs and Sending ND Traps
=============================================================================

Through logs and traps for potential attacks, administrators can obtain ND running in real time, taking measures on the attacks.

#### Context

After a rate limit is configured for ND or ND Miss messages, the device counts the number of received ND or ND Miss messages. If the number of ND or ND Miss messages received in a specified period exceeds the configured limit, the device discards excess ND or ND Miss messages. The device considers this is a potential attack, and records ND logs for the potential attack and sends the corresponding ND traps to the NMS.

If potential attacks frequently occur, the device generates a large number of logs and traps. To resolve this issue, configure a large interval for recording ND logs and sending ND traps.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 nd anti-attack log-trap-timer**](cmdqueryname=ipv6+nd+anti-attack+log-trap-timer) *time-value*
   
   
   
   An interval for recording ND logs and sending ND traps is configured.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.