(Optional) Configuring an Alarm Threshold for the Outbound Bandwidth Usage of the Soft Pipe
===========================================================================================

After the hard pipe is configured on the network-side or AC-side interface, you can configure an alarm threshold for the soft pipe bandwidth usage to monitor the soft pipe load on the device. When the bandwidth usage exceeds the alert or alarm threshold, the device reports an alarm to prompt users to properly plan service traffic or expand device capacity. You can set the alarm threshold and clear alarm threshold as required.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The GE interface view is displayed.
3. Run [**qos soft-pipe trap-threshold output-rate**](cmdqueryname=qos+soft-pipe+trap-threshold+output-rate) *bandwidth-in-use* [ **resume-rate** *resume-threshold* ]
   
   
   
   The alarm and clear alarm thresholds for the outbound bandwidth usage of the soft pipe are configured.