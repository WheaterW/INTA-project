(Optional) Configuring UNI-Side PRBS Testing
============================================

After configuring UNI-side PRBS testing, you can check the service connectivity on the UNI side in one-click mode, thereby determining whether the services between a PE and a CE are running properly.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0172364444__fig_dc_ne_cfg_prbs_000101), a PRBS bit stream is sent from PE1 and PRBS remote loopback is configured on the base station to test the service connectivity between PE1 and the base station.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Before initiating UNI-side PRBS testing on a local device, you must manually configure remote loopback on the remote device interface connected to the local device. In this case, services on the remote device interface are interrupted. As such, after the testing is complete, you need to manually restore services on the remote device interface.


**Figure 1** UNI-side PRBS testing

  
![](images/fig_dc_ne_cfg_prbs_000101.png "Click to enlarge")  


![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, the CE and PE1 are both NE40E devices.




#### Procedure

1. Configure remote loopback on the E1 interface of the CE.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**controller cpos**](cmdqueryname=controller+cpos) *cpos-number* command to enter the CPOS interface view.
   3. Run the [**e1**](cmdqueryname=e1) *e1-number* **set** **loopback** **remote** command to configure remote loopback.
2. Configure PRBS testing on PE1.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**test connectivity**](cmdqueryname=test+connectivity) **interface** { *interface-name* | *interface-type* *interface-number* } **uni-direction** **pattern** *pattern-list* **interval** { **hour** *hour-value* | **minute** *minute-value* | **second** *second-value* } **interval-repeat** *repeat-count* command to start UNI-side enhanced PRBS connectivity testing on the specified low-speed channel.
   3. (Optional) Run the [**test connectivity**](cmdqueryname=test+connectivity) **error-insert** **interface** { *interface-name* | *interface-type* *interface-name* } { **single-bit** | **insert-ratio** *ratio-list* } command to inject bit errors into the bit stream during enhanced PRBS testing.
   4. (Optional) Run the [**test connectivity**](cmdqueryname=test+connectivity) **abort** **interface** { *interface-name* | *interface-type* *interface-number* } command to stop enhanced PRBS testing on the low-speed channel.
3. After PRBS testing is complete, cancel the remote loopback configuration on the E1 interface of the CE.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**controller cpos**](cmdqueryname=controller+cpos) *cpos-number* command to enter the CPOS interface view.
   3. Run the [**undo e1**](cmdqueryname=undo+e1) *e1-number* **set** **loopback** command to cancel the remote loopback configuration on the device.