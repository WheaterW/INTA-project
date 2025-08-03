Configuring Clock Source Attributes for BMCA Selection
======================================================

After multiple T-BCs are configured with the input of BITS signals, clock source attributes for BMCA selection can be configured on the T-BCs to allow the T-BCs to participate in BMCA selection. The local clocks of T-BCs can also be configured to participate in BMCA selection. BMCA can be used to dynamically determine the T-GM. The T-GM provides time signals for the entire CU-106 network. T-BCs use CU-106 to obtain time synchronization information from the T-GM.

#### Context

Perform the following steps on the devices connected to external BITS time sources (including PTP interfaces and external time interfaces) on the CU-106 network.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* When a time server is interconnected with a device (through a PTP interface or external time interface), it is recommended that the local priority2 (*priority2-value*) be configured for the device and other parameters take the default values. When a device is interconnected with a time server or third-party device through an external time interface, you need to set priority2 (*priority2-value*) for the external time interface and retain the default values for other parameters.
* You are advised to retain the default values of *time-source-value*, *clock-accuracy-value*, *clock-class-value*, *priority1-value*, *clockid-value*, and *offsetscaled-logvariance-value* for the time source.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This section uses the BITS1 external time interface as an example. The actual quantity of external time interfaces and their types and numbers vary with the hardware configuration. You need to set them based on the actual situation.



#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**ptp clock-source**](cmdqueryname=ptp+clock-source) { **local** | **bits1** } **priority2** *priority2-value* command to configure a priority2 value for the clock source.
3. (Optional) Run the [**ptp clock-source**](cmdqueryname=ptp+clock-source) { **local** | **bits1** } **time-source** *time-source-value* command to configure a type for the clock source traced by the device.
4. (Optional) Run the [**ptp clock-source**](cmdqueryname=ptp+clock-source) { **local** | **bits1** } **clock-accuracy** *clock-accuracy-value* command to configure the accuracy of the clock source.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In T-BC mode, the local clock accuracy defaults to 0xFE and cannot be configured.
5. (Optional) Run the [**ptp clock-source**](cmdqueryname=ptp+clock-source) { **local** | **bits1** } **clock-class** *clock-class-value* command to configure a clock source level.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   In T-BC mode, the local clock class defaults to 248 and cannot be configured. If the locked clock class is less than 135, after the clock is unlocked, the local clock class automatically changes to 165.
6. (Optional) Run the [**ptp clock-source { local | bits1 } local-priority**](cmdqueryname=ptp+clock-source+local-priority) *local-priority-value* command to configure a local priority of the local time source.
7. (Optional) Run the [**ptp clock-source**](cmdqueryname=ptp+clock-source) **bits1** **grandmaster-clockid** *clockid-value* command to configure a grandmaster clock ID for the BITS time source. The BITS time source then uses the configured clock ID to participate in time source selection.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The *clockid-value* value needs to be the actual clock ID obtained from the BITS external time source and configured for the BITS time source. Otherwise, time synchronization path calculation is affected when the BITS external time source and PTP source are deployed on the same network.
   * In addition, when the clock ID of the BITS source changes due to factors such as BITS device replacement, you need to change the grandmaster clock ID of the BITS source on the device.
8. (Optional) Run the [**ptp clock-source**](cmdqueryname=ptp+clock-source) **bits1 offsetscaled-logvariance** *offsetscaled-logvariance-value* command to configure a stability value for the clock source.
9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.