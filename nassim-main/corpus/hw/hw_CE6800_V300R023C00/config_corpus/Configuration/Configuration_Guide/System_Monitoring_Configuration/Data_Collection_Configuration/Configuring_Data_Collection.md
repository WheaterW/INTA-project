Configuring Data Collection
===========================

Configuring Data Collection

#### Context

You can enable the data collection function to help locate faults based on device data (such as the number of packets on an interface or the CPU usage).

![](../public_sys-resources/note_3.0-en-us.png) 

* You can quickly locate faults by analyzing the data collected using this function, which does not involve user data.
* The data collection period cannot be manually adjusted.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the data collection function.
   
   
   ```
   [metrics enable](cmdqueryname=metrics+enable) 
   ```
   
   By default, this function is enabled.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

By default, the data collection function is enabled on a device. You can run the [**display this include-default**](cmdqueryname=display+this+include-default) command in the system view to check whether the data collection function is enabled.