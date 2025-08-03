Configuring a Dragonfly Profile
===============================

Configuring a Dragonfly Profile

#### Context

The adaptive routing relies on the dragonfly profile.

Currently, the device supports only the default dragonfly profile. You can enable adaptive routing globally and on an interface in sequence to make the configuration in the default dragonfly profile take effect.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the dragonfly profile view.
   
   
   ```
   [dragonfly profile](cmdqueryname=dragonfly+profile) default
   ```
   
   By default, a dragonfly profile exists on the device. Currently, the device supports only the default dragonfly profile.
3. Set the upper and lower thresholds for the bandwidth utilization level.
   
   
   ```
   [adaptive-routing bandwidth](cmdqueryname=adaptive-routing+bandwidth) high-threshold high-threshold-value low-threshold low-threshold-value
   ```
   
   By default, the upper and lower thresholds for the bandwidth utilization level are 6 and 3, respectively.
4. Set the upper and lower thresholds for the queue depth level.
   
   
   ```
   [adaptive-routing buffer](cmdqueryname=adaptive-routing+buffer) high-threshold high-threshold-value low-threshold low-threshold-value
   ```
   
   By default, the upper and lower thresholds for the queue depth level are 6 and 3, respectively.
5. Set the interval for sending an ARN message about congestion.
   
   
   ```
   [adaptive-routing congestion notification](cmdqueryname=adaptive-routing+congestion+notification) tx-interval tx-interval-value
   ```
   
   By default, the interval for sending an ARN message about congestion is 500 ms.
6. For the CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K and CE8850-HAM: Configure dragonfly antilocking PFC on interface queues. (The CE8855 and CE8851-32CQ4BQ do not support this command and need to be configured with PFC.)
   
   
   ```
   [abs-pfc priority](cmdqueryname=abs-pfc+priority) { prioritynumber } &<1-3> enable [ threshold threshold-value ]
   ```
   
   By default, dragonfly antilocking PFC is disabled on interface queues.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * If dragonfly antilocking PFC is enabled in the dragonfly profile, this function is enabled on the interface where the adaptive routing function is enabled.
   * If dragonfly antilocking PFC is enabled in the dragonfly profile and adaptive routing is enabled on an interface, you need to run the **[**qos hpc enhanced**](cmdqueryname=qos+hpc+enhanced)** command to ensure that the packets in queues 6 and 7 are not discarded.
   * If dragonfly antilocking PFC is enabled in the dragonfly profile, the interfaces where adaptive routing is enabled must have the same bandwidth.
   * Dragonfly antilocking PFC can be enabled for a maximum of three queues on an interface.
   * A maximum of 90 queues on all the interfaces of a device can have dragonfly antilocking PFC enabled.
   * If dragonfly deadlock prevention has been enabled for a priority queue, disable it before disabling dragonfly antilocking PFC in the queue.
7. Enable dragonfly deadlock prevention and adjust the queue priority and DSCP value of packets in hook-shaped flows.
   
   
   ```
   [adjust original-dscp](cmdqueryname=adjust+original-dscp) original-dscpvalue to priority prioritynumber dscp dscpvalue
   ```
   
   By default, dragonfly deadlock prevention is disabled, and there are no configurations for hook-shaped flows.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * PFC deadlock prevention and dragonfly deadlock prevention cannot both be enabled.
   * The **adjust original-dscp** command can be run twice at most, with different values configured for *original-dscpvalue*, *prioritynumber*, and *dscpvalue* the second time. To modify the configuration, run the **undo adjust original-dscp** command to delete the original configuration first.
   
   For the CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, and CE8850-HAM:
   
   * Before running the **[**adjust original-dscp**](cmdqueryname=adjust+original-dscp)** command to enable dragonfly deadlock prevention, you must run the **[**abs-pfc priority enable**](cmdqueryname=abs-pfc+priority+enable)** command to enable dragonfly antilocking PFC. In addition, the priority queue that **original-dscp** is mapped to and the priority queue specified by **priority** in the **[**adjust original-dscp**](cmdqueryname=adjust+original-dscp)** command must be within the range specified by **priority** in the **[**abs-pfc priority enable**](cmdqueryname=abs-pfc+priority+enable)** command.
   * If the priority queue that the **original-dscp** parameter is mapped to changes to a queue for which dragonfly antilocking PFC is not enabled due to the mapping change between DSCP values and priority queues, dragonfly deadlock prevention does not take effect for the priority queue that the **original-dscp** parameter is mapped to before and after the mapping change.
   * You need to enable dragonfly antilocking PFC for a specified queue and then enable dragonfly deadlock prevention.
   
   For the CE8855 and CE8851-32CQ4BQ:
   
   * If the role of an interface has been configured for adaptive routing, you must enable PFC on the interface before running the **[**adjust original-dscp**](cmdqueryname=adjust+original-dscp)** command to enable dragonfly deadlock prevention. In addition, the priority queue that **original-dscp** is mapped to and the priority queue specified by **priority** in the **[**adjust original-dscp**](cmdqueryname=adjust+original-dscp)** command must be within the range of the priority queues where PFC has been enabled.
   * Before configuring the role of an interface for adaptive routing, you must enable PFC for the priority queue that **original-dscp** is mapped to and the priority queue specified by **priority** in the **[**adjust original-dscp**](cmdqueryname=adjust+original-dscp)** command.
   * If the priority queue that the **original-dscp** parameter is mapped to changes to a queue for which PFC is not enabled due to the mapping change between DSCP values and priority queues, dragonfly deadlock prevention does not take effect for the priority queue that the **original-dscp** parameter is mapped to before and after the mapping change.
8. Exit the dragonfly profile view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```