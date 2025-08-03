Configuring the Alarm Function in Case the Number of Bytes of Error Packets That an Interface Receives Exceeds an Alarm Threshold
=================================================================================================================================

You can configure the alarm function in case the number of bytes of error packets exceeds a threshold. If such an alarm is generated, the link is in a poor condition.

#### Context

If an interface receives a large number of bytes of error packets, the link is in a poor condition, affecting service transmission. In this situation, you can configure the alarm function, alarm threshold, and detection interval on an interface. The system then detects the number of bytes of error packets that the interface receives at the configured interval. If the number of bytes of error packets exceeds the configured alarm threshold, the system generates an alarm and sends it to the NMS, prompting the administrator to perform maintenance on the interface and troubleshoot the fault. When the number of bytes of error packets falls below the alarm threshold, the system generates a clear alarm and sends it to the NMS, notifying the administrator that the alarm has been cleared.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**snmp-agent trap enable port bad-bytes**](cmdqueryname=snmp-agent+trap+enable+port+bad-bytes)
   
   
   
   The alarm function is configured in case the number of bytes of error packets exceeds an alarm threshold.
3. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
4. Run [**trap-threshold bad-bytes**](cmdqueryname=trap-threshold+bad-bytes) *trap-threshold* **interval-second** *interval*
   
   
   
   An alarm threshold is configured for the number of bytes of error packets that the interface receives, and an interval is configured for the system to detect the number of bytes of error packets.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.