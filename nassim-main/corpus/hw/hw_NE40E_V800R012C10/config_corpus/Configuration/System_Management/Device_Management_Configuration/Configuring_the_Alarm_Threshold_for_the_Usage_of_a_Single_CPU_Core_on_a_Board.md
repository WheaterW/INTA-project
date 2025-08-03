Configuring the Alarm Threshold for the Usage of a Single CPU Core on a Board
=============================================================================

This section describes how to configure the alarm threshold for the usage of a single CPU core on a multi-core CPU-equipped board.

#### Context

When the usage of a single CPU core on a multi-core CPU-equipped board is high, measures such as expanding board capacity or adjusting services need to be taken in a timely manner to ensure proper service running.

In VS mode, this configuration process is supported only by the admin VS.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the NE40E-M2K/-M2F/-M2H/-M2K-B supports this function.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**forward alarm vcpu-usage multi-core threshold**](cmdqueryname=forward+alarm+vcpu-usage+multi-core+threshold) *threshold-value*
   
   
   
   The alarm threshold for the usage of a single CPU core on a multi-core CPU-equipped board is configured.
3. **Optional:** Run [**undo forward alarm vcpu-usage multi-core threshold**](cmdqueryname=undo+forward+alarm+vcpu-usage+multi-core+threshold) *threshold-value*
   
   
   
   The default alarm threshold for the usage of a single CPU core on a multi-core CPU-equipped board is restored.
4. **Optional:** Run [**forward alarm vcpu-usage multi-core**](cmdqueryname=forward+alarm+vcpu-usage+multi-core) { **log** | **trap** } **disable**
   
   
   
   The function of reporting alarms or generating logs when the usage of a single CPU core on a multi-core CPU-equipped board reaches the threshold is disabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.