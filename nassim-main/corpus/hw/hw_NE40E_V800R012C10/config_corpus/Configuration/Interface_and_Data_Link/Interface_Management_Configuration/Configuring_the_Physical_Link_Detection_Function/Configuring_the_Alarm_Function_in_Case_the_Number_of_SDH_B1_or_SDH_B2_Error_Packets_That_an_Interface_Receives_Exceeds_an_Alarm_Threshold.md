Configuring the Alarm Function in Case the Number of SDH B1 or SDH B2 Error Packets That an Interface Receives Exceeds an Alarm Threshold
=========================================================================================================================================

You can configure the alarm function in case the number of SDH B1 or SDH B2 error packets exceeds an alarm threshold. If such an alarm is generated, the link is in a poor condition.

#### Context

If an interface receives a large number of SDH B1 or SDH B2 error packets, the link is in a poor condition, affecting service transmission. In this situation, you can configure the alarm function, alarm threshold, and detection interval on an interface. The system then detects the number of SDH B1 or SDH B2 error packets that the interface receives at the configured interval. If the number of SDH B1 or SDH B2 error packets exceeds the configured alarm threshold, the system generates an alarm and sends it to the NMS, prompting the administrator to perform maintenance on the interface and troubleshoot the fault. When the number of SDH B1 or SDH B2 error packets falls below the alarm threshold, the system generates a clear alarm and sends it to the NMS, notifying the administrator that the alarm has been cleared.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
3. Run [**trap-threshold**](cmdqueryname=trap-threshold) { **sdh-b1-error** | **sdh-b2-error** } *threshold* **interval-second** *interval*
   
   
   
   A threshold and detection interval for the SDH B1 or SDH B2 error alarm on an interface are set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.