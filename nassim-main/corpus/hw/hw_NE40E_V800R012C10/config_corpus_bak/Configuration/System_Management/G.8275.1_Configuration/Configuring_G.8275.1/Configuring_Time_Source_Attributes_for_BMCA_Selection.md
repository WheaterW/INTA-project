Configuring Time Source Attributes for BMCA Selection
=====================================================

After BITS signal input is configured on multiple T-BCs, you can configure the time source attributes of the T-BCs to allow them to participate in BMCA source selection. You can also configure the local clocks of T-BCs to participate in BMCA source selection. The BMCA helps devices to dynamically select a master clock. The master clock provides time signals for the entire G.8275.1 network. T-BCs use G.8275.1 to achieve time synchronization with the grandmaster clock.

#### Context

Perform the following steps on the Routers connected to external BITS time sources (including PTP interfaces and external time interfaces) on the G.8275.1 network.

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
5. (Optional) Run the [**ptp clock-source**](cmdqueryname=ptp+clock-source) { **local** | **bits1** } **clock-class** *clock-class-value* command to configure a clock source level.
6. (Optional) Run the [**ptp clock-source**](cmdqueryname=ptp+clock-source) { **local** | **bits1** } **local-priority** *local-priority-value* command to configure a local priority for the clock source.
7. (Optional) Run the [**ptp clock-source**](cmdqueryname=ptp+clock-source) **bits1 grandmaster-clockid** *clockid-value* command to configure a grandmaster clock ID for the clock source.
8. (Optional) Run the [**ptp clock-source**](cmdqueryname=ptp+clock-source) **bits1 offsetscaled-logvariance** *offsetscaled-logvariance-value* command to configure a stability value for the clock source.
9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.