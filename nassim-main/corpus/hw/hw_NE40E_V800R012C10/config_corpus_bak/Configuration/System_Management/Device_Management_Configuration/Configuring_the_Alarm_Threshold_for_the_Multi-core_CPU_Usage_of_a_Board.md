Configuring the Alarm Threshold for the Multi-core CPU Usage of a Board
=======================================================================

This section describes how to configure the alarm threshold for the multi-core CPU usage of a board regardless of service types.

#### Context

Configuring the alarm threshold for the multi-core CPU usage of a board regardless of service types helps learn the CPU usage information. When the multi-core CPU usage is high, measures such as expanding board capacity or adjusting services need to be taken in a timely manner to ensure proper service running.

In VS mode, this configuration process is supported only by the admin VS.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the NE40E-M2K/-M2F/-M2H/-M2K-B supports this function.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**forward alarm cpu-usage multi-core threshold**](cmdqueryname=forward+alarm+cpu-usage+multi-core+threshold) *threshold-value*
   
   
   
   The alarm threshold for the average usage across a multi-core CPU of the board regardless of service types is configured.
3. **Optional:** Run [**forward alarm cpu-usage multi-core**](cmdqueryname=forward+alarm+cpu-usage+multi-core) { **log** | **trap** } **disable**
   
   
   
   The function of reporting alarms or generating logs when the multi-core CPU usage reaches the threshold regardless of service types is disabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.