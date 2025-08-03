(Optional) Configuring Errored Frame Detection
==============================================

If the number of errored frames detected on the local interface reaches or exceeds a configured threshold within a specified interval, the local device reports the fault to the remote device.

#### Context

If a device's interface has been enabled to report detected errored frames and the number of errored frames detected on the interface reaches or exceeds a configured threshold within a specified interval, the device generates a threshold-crossing event of errored frames and reports the event to the remote device.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface at one end of a link is displayed.
3. Run [**efm error-frame period**](cmdqueryname=efm+error-frame+period) *period*
   
   
   
   The interval at which errored frames are checked is set.
4. Run [**efm error-frame threshold**](cmdqueryname=efm+error-frame+threshold) *threshold*
   
   
   
   The threshold for the number of detected errored frames is set.
5. Run [**efm error-frame notification enable**](cmdqueryname=efm+error-frame+notification+enable)
   
   
   
   The interface is enabled to detect and report the detected errored frames.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.