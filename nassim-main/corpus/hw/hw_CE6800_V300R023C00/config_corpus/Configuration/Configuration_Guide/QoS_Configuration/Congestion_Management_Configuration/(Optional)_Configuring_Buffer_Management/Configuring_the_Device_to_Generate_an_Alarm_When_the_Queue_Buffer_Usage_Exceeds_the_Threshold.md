Configuring the Device to Generate an Alarm When the Queue Buffer Usage Exceeds the Threshold
=============================================================================================

Configuring the Device to Generate an Alarm When the Queue Buffer Usage Exceeds the Threshold

#### Context

The supported bandwidth on each interface is fixed. Once the traffic rate exceeds the interface bandwidth and the used queue buffer exceeds the configured threshold, the device starts discarding excess traffic. Run the [**qos buffer overrun threshold**](cmdqueryname=qos+buffer+overrun+threshold) command to set the threshold of the queue buffer usage, and run the [**qos buffer overrun alarm enable**](cmdqueryname=qos+buffer+overrun+alarm+enable) command to enable the device to generate an alarm when the queue buffer usage exceeds the threshold.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Set the threshold of the queue buffer usage.
   
   
   ```
   [qos buffer overrun threshold](cmdqueryname=qos+buffer+overrun+threshold) percent
   ```
3. Configure the device to generate an alarm when the queue buffer usage exceeds the threshold.
   
   
   ```
   [qos buffer overrun alarm enable](cmdqueryname=qos+buffer+overrun+alarm+enable)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```