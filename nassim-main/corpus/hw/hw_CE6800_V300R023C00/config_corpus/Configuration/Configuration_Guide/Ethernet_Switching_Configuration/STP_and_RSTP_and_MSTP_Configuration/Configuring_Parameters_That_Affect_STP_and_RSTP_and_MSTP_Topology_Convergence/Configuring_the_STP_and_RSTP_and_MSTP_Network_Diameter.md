Configuring the STP/RSTP/MSTP Network Diameter
==============================================

Configuring the STP/RSTP/MSTP Network Diameter

#### Context

Any two terminals on a network are connected through a specific path, along which multiple devices reside. The maximum number of devices between any two terminals correlates with the network diameter. A larger network diameter indicates a larger network scale. For example, the diameter of the network shown in [Figure 1](#EN-US_TASK_0000001345478641__fig4495847115416) is 5.

* DeviceC â DeviceA â DeviceD â DeviceB â DeviceE
* DeviceD â DeviceA â DeviceC â DeviceB â DeviceE

**Figure 1** STP/RSTP/MSTP network diameter  
![](figure/en-us_image_0000001292238816.png)

Set the network diameter on all devices based on the network scale. An appropriate network diameter can facilitate network convergence, whereas an improper diameter may reduce the rate of network convergence and affect user communications.

It is recommended that the same network diameter be set for all network devices.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Enter the MSTP process view.
   
   
   
   Perform this step to set system parameters only when the MSTP process ID is not 0. Skip this step if the MSTP process ID is 0.
   
   ```
   [stp process](cmdqueryname=stp+process) process-id
   ```
3. Set the network diameter.
   
   
   ```
   [stp bridge-diameter](cmdqueryname=stp+bridge-diameter) diameter
   ```
   
   The default network diameter is 7.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Based on the set network diameter, the device will calculate the optimal Forward Delay, Hello Time, and Max Age timer values. You are recommended to set the network diameter to adjust the Forward Delay, Hello Time, and Max Age timers.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display stp global**](cmdqueryname=display+stp+global) command to check the Bridge-diameter field for the network diameter setting.