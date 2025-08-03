Configuring STP/RSTP/MSTP Timers
================================

Configuring STP/RSTP/MSTP Timers

#### Context

Spanning tree calculation involves the Forward Delay, Hello Time, and Max Age timers.

* Forward Delay: specifies the delay before a state transition. After the topology of a ring network changes, the new configuration BPDUs take time to propagate across the entire network. As a result, blocking a new port may unblock a blocked port, which may cause a network loop. To help prevent such loops from occurring, set an appropriate Forward Delay timer. When the topology changes, all ports will be temporarily blocked during the Forward Delay timer.
* Hello Time: is used for detecting link failures. A device sends configuration BPDUs at an interval of the Hello Time to detect link failures. If the device does not receive any BPDUs within the timeout period (timeout period = Hello Time x 3 x Timer Factor), the device will recalculate the spanning tree.
* Max Age: determines when BPDUs expire. A device determines that a received configuration BPDU times out based on the Max Age timer value. If the received BPDU expires, the spanning tree will be recalculated.

Devices on a ring network must use the same Forward Delay, Hello Time, and Max Age timer values.

You are advised not to change the values of the preceding timers as they are related to the network scale. The spanning tree protocol will automatically adjust these timers if you set the network diameter. When the default network diameter is used, the three timers also use their default values.

![](public_sys-resources/notice_3.0-en-us.png) 

To prevent frequent network flapping, ensure that the Hello Time, Forward Delay, and Max Age timer values conform to the following formulas:

* 2 x (Forward Delay â 1.0 second) â¥ Max Age
* Max Age >= 2 Ã (Hello Time + 1.0 second)


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
3. Set the Forward Delay timer.
   
   
   ```
   [stp timer forward-delay](cmdqueryname=stp+timer+forward-delay) forward-delay
   ```
   
   The default Forward Delay timer for a device is 1500 centiseconds (15 seconds).
4. Set the Hello Time timer.
   
   
   ```
   [stp timer hello](cmdqueryname=stp+timer+hello) hello-time
   ```
   
   The default Hello Time timer for a device is 200 centiseconds (2 seconds).
5. Set the Max Age timer.
   
   
   ```
   [stp timer max-age](cmdqueryname=stp+timer+max-age) max-age
   ```
   
   
   
   The default Max Age timer for a device is 2000 centiseconds (20 seconds).
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display stp**](cmdqueryname=display+stp) [ **process** *process-id* ] [ **instance** *instance-id* ] [ **interface** *interface-type* *interface-number* | **slot** *slot-id* ] command and check the Config Times field for the STP timer settings.