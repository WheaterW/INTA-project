Configuring an Alarm Threshold for TM Bandwidth Overflow
========================================================

This section describes how to configure an alarm threshold for TM bandwidth overflow. After such an alarm threshold is configured, an alarm is triggered when bandwidth overflow occurs.

#### Context

You can configure an alarm threshold for TM bandwidth overflow based on network traffic and network running status. When the TM bandwidth overflow threshold is reached, an alarm is triggered to notify maintenance personnel to rectify the fault.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**set tm bandwidth alarm-threshold**](cmdqueryname=set+tm+bandwidth+alarm-threshold) *value*
   
   
   
   An alarm threshold for TM bandwidth overflow is configured.
   
   
   
   The default alarm threshold for TM bandwidth overflow is 95%. When the bandwidth usage of services reaches the default alarm threshold, the device automatically triggers an hwTmPerformanceALarm alarm. You can run this command to change the alarm threshold.
3. (Optional) Run [**set tm bandwidth alarm disable**](cmdqueryname=set+tm+bandwidth+alarm+disable)
   
   
   
   The TM bandwidth overflow alarm function is disabled.
   
   
   
   By default, the alarm function for TM bandwidth overflow is enabled. If you do not want to receive this alarm, run this command to disable the alarm function. Service packets may be lost if TM bandwidth overflow occurs, so you are advised to keep the alarm function enabled. Exercise caution when running this command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.