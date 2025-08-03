(Optional) Enabling the Device to Record Logs and Generate Alarms About Potential Attacks
=========================================================================================

To locate and resolve potential attacks, you can enable
the device to record logs and generate alarms about potential attacks.

#### Background Information

After Address Resolution
Protocol (ARP) Miss message rate limit is configured, the device counts
the number of received ARP Miss messages. If the number of ARP Miss
messages received in a specified period exceeds a specified limit,
the device discards additional ARP Miss messages. The device considers
this problem as a potential attack. The device records logs and generates
alarms about potential attacks.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**arp anti-attack log-trap-timer**](cmdqueryname=arp+anti-attack+log-trap-timer) *timer*
   
   
   
   The device is enabled
   to record logs and generate alarms about potential attacks.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.