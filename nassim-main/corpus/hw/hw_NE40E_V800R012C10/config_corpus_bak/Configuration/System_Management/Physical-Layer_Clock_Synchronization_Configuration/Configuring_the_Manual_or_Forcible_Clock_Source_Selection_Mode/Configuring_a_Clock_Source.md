Configuring a Clock Source
==========================

Configuring_a_Clock_Source

#### Context

By default, the NE40E determines the clock source to trace through automatic clock source selection. You can also manually or forcibly specify a clock source to be traced based on the quality level of each clock source.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

The [automatic clock source selection](dc_ne_clock_cfg_5005.html) mode is recommended. Manual and forcible clock source selection modes do not support automatic protection switching of clock sources.

If the status of a forcibly specified clock source is not normal or its SSM level is **dnu**, the system clock works in the hold state.

If the status of a manually specified clock source is neither normal nor holdoff, or its SSM level is not the highest, this manually specified clock source does not take effect.

The device can use PTP, BITS, and line clock sources. The characteristics of the three clock sources are as follows:

* Line clock source: The performance is stable and the transmission distance is long. Many interfaces can be used.
* BITS clock source: External clock interfaces (also known as BITS interfaces) are used to provide higher performance. However, the transmission distance is short. Source switching cannot be performed in case of an SSM quality level decrease in 2mhz mode.
* PTP clock source: Physical interfaces are not mandatory and the transmission distance is long. However, the performance is poor and depends on packet transmission. Source switching cannot be performed in case of an SSM quality level decrease.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* It is recommended that the line clock source be used on the entire network, followed by the BITS clock source. Use the PTP clock source only if a link does not support the line or BITS clock source.
* If the peer has only a BITS interface but no synchronous Ethernet interface, using the BITS clock source is recommended.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This section uses the external clock source with the BITS0 interface as an example. The actual types and numbers of external clock interfaces vary with the hardware configuration. You need to set them based on the actual situation.

Perform one of the following configurations based on the clock source to be used on a clock synchronization network:


#### Procedure

* (Mandatory) Configure global manual or forcible clock source selection.
  
  
  
  Before configuring a clock source, configure global manual or forcible clock source selection.
  
  
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run either of the following commands to manually or forcibly specify the clock source to be traced for the system clock.
     
     
     1. Run the [**clock**](cmdqueryname=clock) { **manual** | **force** } **source** **bits0** command to manually or forcibly specify the BITS clock source as the clock source to be traced.
     2. Run the [**clock**](cmdqueryname=clock) { **manual** | **force** } **source** **ptp** command to manually or forcibly specify the PTP clock source as the clock source to be traced.
     3. Run the [**clock**](cmdqueryname=clock) { **manual** | **force** } **source** **interface** { **interface-name**| **interface-type** **interface-number**} command to manually or forcibly specify an interface as the clock source to be traced.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     After the [**clock manual source**](cmdqueryname=clock+manual+source) command is run, this command is not saved in the configuration file. To view the configuration results, run the [**display clock config**](cmdqueryname=display+clock+config) command. If the reference clock source fails, the clock selection mode is automatically switched to automatic clock source selection. After a device is restarted, the [**clock manual source**](cmdqueryname=clock+manual+source) command is not restored, and the default automatic clock source selection mode takes effect. After the device is upgraded to the target version from an earlier version, the [**clock manual source**](cmdqueryname=clock+manual+source) command run in the earlier version no longer takes effect, and the system uses the default automatic clock source selection mode.
  3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* (Optional) Configure a line clock source.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  It is recommended that two line clock sources be configured on different subcards.
  
  
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
  3. Run the [**clock synchronization enable**](cmdqueryname=clock+synchronization+enable) command to enable clock synchronization for the line clock source.
  4. Run the [**clock**](cmdqueryname=clock) **priority** *priority-value* command to configure a priority for the line clock source.
     
     
     
     A smaller value indicates a higher priority.
  5. (Optional) Run the [**clock ssm**](cmdqueryname=clock+ssm) { **dnu** | **prc** | **sec** | **ssua** | **ssub** | **unk** | **prtc** | **eprtc** | **esec** | **eprc** } command to configure an SSM level for the line clock source.
  6. (Optional) Run the [**clock**](cmdqueryname=clock) **clock-id** *clockid-value* command to configure a clock ID for the line clock source.
  7. (Optional) Run the [**clock bundle**](cmdqueryname=clock+bundle) *bundle-value* command to configure a bundle ID for the line clock source and add the line clock source to the bundle group. This command can be run to prevent a clock loop when two or more clock links exist between two devices.
  8. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* (Optional) Configure a BITS clock source.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**clock bits-type**](cmdqueryname=clock+bits-type) **bits0** { **2mhz** | **2mbps** } command to configure a signal type for the BITS clock source.
  3. (Optional) Run the [**clock sa-bit**](cmdqueryname=clock+sa-bit) { **sa4** | **sa5** | **sa6** | **sa7** | **sa8** } **source** [ **chassis** *chassis-id* ] **bits0** command to configure a timeslot from which the BITS clock source extracts SSM level information.
     
     
     
     When the type of the input BITS clock signal is **2mbps**, you can manually configure the SA timeslot from which the SSM level information is extracted. By default, the SSM level information is extracted from the **2mbps** clock signals in timeslot **sa4**.
  4. (Optional) Run the [**clock source**](cmdqueryname=clock+source) **bits0****ssm** { **prc** | **ssua** | **ssub** | **sec** | **dnu** | **unk** | **prtc** | **eprtc** | **esec** | **eprc** } command to configure an SSM level for the BITS clock source.
  5. (Optional) Run the [**clock bits output-threshold**](cmdqueryname=clock+bits+output-threshold) { **prc** | **ssua** | **ssub** | **sec** | **dnu** } command to configure an output quality threshold for the external clock source.
     
     
     
     If the SSM level of the clock signals output by the BITS port is lower than the set threshold, the BITS port stops outputting clock signals.
  6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* (Optional) Configure a PTP clock source.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**ptp device-type**](cmdqueryname=ptp+device-type) { ****oc****| ****bc****| ****e2etcoc****| ****p2ptcoc****| ****tcandbc****} command to configure a device type for the device.
  3. Run the [**ptp enable**](cmdqueryname=ptp+enable) command to enable PTP on the device.
  4. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
  5. Run the [**ptp enable**](cmdqueryname=ptp+enable) command to enable PTP on the interface.
  6. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
  7. Run the [**clock**](cmdqueryname=clock) **source** **ptp** **priority** *priority-value* command to configure a priority for the PTP clock source.
     
     
     
     A smaller value indicates a higher priority.
  8. Run the [**clock**](cmdqueryname=clock) **source** **ptp** **synchronization** **enable** command to enable clock synchronization for the PTP clock source.
  9. Run the [**clock source**](cmdqueryname=clock+source) **ptp** **ssm** { **dnu** | **prc** | **sec** | **ssua** | **ssub** | **unk** | **prtc** | **eprtc** | **esec** | **eprc** } command to configure an SSM level for the PTP clock source.
  10. (Optional) Run the [**clock source**](cmdqueryname=clock+source) **ptp** **clock-id** **clockid-value** command to configure a clock ID for the PTP clock source.
  11. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.