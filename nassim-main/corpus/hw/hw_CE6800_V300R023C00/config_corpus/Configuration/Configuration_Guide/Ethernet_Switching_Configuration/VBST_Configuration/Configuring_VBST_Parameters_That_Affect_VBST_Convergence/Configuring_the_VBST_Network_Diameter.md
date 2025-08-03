Configuring the VBST Network Diameter
=====================================

Configuring the VBST Network Diameter

#### Context

Any two terminals on a network are connected through a specific path, along which multiple devices reside. The maximum number of devices between any two terminals correlates with the network diameter. A larger network diameter indicates a larger network scale. For example, the diameter of the network shown in [Figure 1](#EN-US_TASK_0000001512848790__en-us_task_0227126161_fig4495847115416) is 5.

* DeviceC-DeviceA-DeviceD-DeviceB-DeviceE
* DeviceD-DeviceA-DeviceC-DeviceB-DeviceE

**Figure 1** VBST network diameter  
![](figure/en-us_image_0000001513048378.png)

Set the network diameter on all devices based on the network scale. An appropriate network diameter can facilitate network convergence, whereas an improper diameter may reduce the rate of network convergence and affect user communications.

It is recommended that the same network diameter be set for all network devices.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Set the network diameter.
   
   
   ```
   [stp vlan](cmdqueryname=stp+vlan) vlan-id1 [ to vlan-id2 ] [ vlan-id3 [ to vlan-id4 ] ] &<1-9> bridge-diameter dbridge-diameter
   ```
   
   The default network diameter is 7.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Based on the set network diameter, the device will calculate the optimal Forward Delay, Hello Time, and Max Age timer values. You are recommended to set the network diameter to adjust the Forward Delay, Hello Time, and Max Age timers.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```