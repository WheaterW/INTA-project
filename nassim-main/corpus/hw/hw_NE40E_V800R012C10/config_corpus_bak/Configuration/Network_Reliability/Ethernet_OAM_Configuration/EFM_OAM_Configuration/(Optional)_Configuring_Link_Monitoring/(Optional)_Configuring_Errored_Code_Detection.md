(Optional) Configuring Errored Code Detection
=============================================

If the number of errored codes detected on the local interface reaches or exceeds a configured threshold within a specified interval, the local device reports the fault to the remote device.

#### Context

If a device's interface has been enabled to report detected errored codes and the number of errored codes detected on the interface reaches or exceeds a configured threshold within a specified interval, the device generates a threshold-crossing event of errored codes and reports the event to the remote device.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface at one end of a link is displayed.
3. Run [**efm error-code period**](cmdqueryname=efm+error-code+period) *period*
   
   
   
   The interval at which errored codes are checked is set.
4. Run [**efm error-code threshold**](cmdqueryname=efm+error-code+threshold) *threshold*
   
   
   
   The threshold for the number of detected errored codes is set.
5. Run [**efm error-code notification enable**](cmdqueryname=efm+error-code+notification+enable)
   
   
   
   The interface is enabled to detect and report the detected errored codes.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.