(Optional) Configuring Errored Frame Second Detection
=====================================================

If the number of errored frame seconds detected on the local interface reaches or exceeds a configured threshold within a specified interval, the local device reports the fault to the remote device.

#### Context

An errored frame second is a 1-second interval during which at least one errored frame is detected.

If a device's interface has been enabled to report detected errored frame seconds and the number of errored frame seconds detected on the interface reaches or exceeds a configured threshold within a specified interval, the device generates a threshold-crossing event of errored frame seconds and reports the event to the remote device.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface at one end of a link is displayed.
3. Run [**efm error-frame-second period**](cmdqueryname=efm+error-frame-second+period) *period*
   
   
   
   The interval at which errored frame seconds are checked is set.
4. Run [**efm error-frame-second threshold**](cmdqueryname=efm+error-frame-second+threshold) *threshold*
   
   
   
   The threshold for the number of detected errored frame seconds is set.
5. Run [**efm error-frame-second notification enable**](cmdqueryname=efm+error-frame-second+notification+enable)
   
   
   
   The interface is enabled to detect and report the detected errored frame seconds.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.