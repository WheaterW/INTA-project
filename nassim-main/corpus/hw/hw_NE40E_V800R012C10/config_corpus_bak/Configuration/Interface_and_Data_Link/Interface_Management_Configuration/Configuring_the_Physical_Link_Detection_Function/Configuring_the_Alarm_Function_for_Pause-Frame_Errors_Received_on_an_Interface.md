Configuring the Alarm Function for Pause-Frame Errors Received on an Interface
==============================================================================

This section describes how to configure the alarm function for pause-frame errors received on an interface.

#### Context

A device generates an alarm and sends it to an NMS only when the number of pause-frame error packets sent or received by the device reaches the upper threshold for three consecutive detection intervals. The device sends a clear alarm to the NMS only when the number of pause-frame error packets sent or received by the device falls below the lower threshold for three consecutive detection intervals.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The view of an interface is displayed.
3. Run [**trap-threshold pause-frame**](cmdqueryname=trap-threshold+pause-frame) **high-threshold** *high-threshold* **low-threshold** *low-threshold* **interval-second** *interval*
   
   
   
   The upper threshold, lower threshold, and detection interval for the pause-frame error alarm are set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.