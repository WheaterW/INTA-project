Configuring a Clock Source
==========================

Configuring_a_Clock_Source

#### Context

Before configuring clock synchronization on the NE40E, you need to configure the global automatic clock source selection function and a clock source.

In automatic clock source selection mode, the following reference factors may affect the final clock source selection: synchronous status message (SSM) levels, priorities, types, interface IDs, enhanced SSM levels, and clock IDs of clock sources.

* By default, the automatic clock source selection algorithm selects a clock source based on the priorities, types, and interface IDs of clock sources in sequence.
* If clock source selection based on SSM levels is enabled, the automatic clock source selection algorithm preferentially selects a clock source based on the SSM levels of clock sources. If there are two or more clock sources with the same SSM level, the automatic clock source selection algorithm selects a clock source based on the priorities, types, and interface IDs of clock sources in sequence. For details about the automatic clock source selection modes, see [Clock Source Selection Modes](feature_0003995108.html#EN-US_CONCEPT_0000001779759164__section2005378490214007).
* If the extended SSM function is enabled, clock IDs of clock sources also participate in clock source selection. The participation of clock IDs prevents clock loops.
* After the enhanced SSM function is enabled, the system uses the enhanced SSM level as the clock source selection control information.

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

* (Mandatory) Configure global automatic clock source selection.
  
  
  
  Before configuring a clock source, configure global automatic clock source selection.
  
  
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. (Optional) Run the [**clock clear**](cmdqueryname=clock+clear) command to restore the clock source selection mode to automatic.
     
     
     
     This step is required if a clock source has been manually or forcibly specified for the system clock through the [**clock**](cmdqueryname=clock) { **manual** | **force**} **source** { **bits0** | **ptp** | **interface** *interface-type* *interface-number* } command.
  3. Run the [**clock ssm-control**](cmdqueryname=clock+ssm-control) { **on** | **off** } command to enable clock source selection based on SSM levels.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + Specifying **on** to enable clock source selection based on SSM levels is recommended. If clock source selection based on SSM quality levels is not enabled, the system does not select a clock source based on SSM quality levels. If the SSM quality level decreases, the system does not perform source switching or send clock source signals that contain SSM quality level information.
     + If **off** is specified, the SSM quality level of sent clock source signals is dnu.
  4. (Optional) Run the [**clock extend-ssm-control**](cmdqueryname=clock+extend-ssm-control) { **on** | **off** } command to enable the extended SSM function so that automatic clock source selection can be performed based on clock IDs.
  5. (Optional) Run the [**clock enhanced-ssm-control**](cmdqueryname=clock+enhanced-ssm-control) { **on** | **off** } command to enable enhanced SSM.
  6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* (Optional) Configure a line clock source.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  It is recommended that two line clock sources be configured on different subcards.
  
  
  
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
  3. Run the [**clock synchronization enable**](cmdqueryname=clock+synchronization+enable) command to enable clock synchronization for the line clock source.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     When a device functions as a master clock and transmits frequency information to downstream devices, you need to run this command to enable the device to transmit ESMC packets.
  4. Run the [**clock**](cmdqueryname=clock) **priority** *priority-value* command to configure a priority for the line clock source.
     
     
     
     A smaller value indicates a higher priority.
  5. (Optional) Run the [**clock ssm**](cmdqueryname=clock+ssm) { **dnu** | **prc** | **sec** | **ssua** | **ssub** | **unk** | **prtc** | **eprtc** | **esec** | **eprc** } command to configure an SSM level for the line clock source.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     This function is static SSM quality configuration. If the SSM quality is degraded, source switching cannot be performed. Therefore, this function is not recommended.
  6. (Optional) Run the [**clock**](cmdqueryname=clock) **clock-id** *clockid-value* command to configure a clock ID for the line clock source.
  7. (Optional) Run the [**clock bundle**](cmdqueryname=clock+bundle) *bundle-value* command to configure a bundle group ID for the line clock source and add the line clock source to the bundle group.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     This function can prevent a clock loop when two or more clock links exist between two devices.
  8. (Optional) Run the [**clock freq-deviation-detect enable**](cmdqueryname=clock+freq-deviation-detect+enable) command to enable frequency deviation detection.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + After frequency deviation detection is enabled, the detection result is used as the reference for automatic clock source selection, which may affect the final clock source selection result. If the frequency deviation of the clock source relative to the stratum-3 crystal oscillator of the local device is too large, switching to a normal clock source can be performed.
     + If the frequency deviation of a clock source relative to the stratum-3 crystal oscillator of the local device exceeds 9.2 ppm, the clock source cannot function as a clock synchronization source. If the frequency deviation of the clock source relative to the stratum-3 crystal oscillator of the local device falls below 8.7 ppm, the clock source can function as a clock synchronization source again.
  9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* (Optional) Configure a BITS clock source.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**clock bits-type**](cmdqueryname=clock+bits-type) **bits0** { **2mhz** | **2mbps** } command to configure a signal type for the BITS clock source.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The **2mbps** mode is recommended. If the **2mhz** mode is configured, the device cannot transmit the SSM quality level through the external clock interface. As such, source switching cannot be performed in case of an SSM quality level decrease.
  3. Run the [**clock source**](cmdqueryname=clock+source) **bits0** **synchronization enable** command to enable clock synchronization on the BITS clock source.
  4. Run the [**clock source**](cmdqueryname=clock+source) **bits0** **priority** *priority-value* command to configure a priority for the BITS clock source.
     
     
     
     A smaller value indicates a higher priority.
  5. (Optional) Run the [**clock sa-bit**](cmdqueryname=clock+sa-bit) { **sa4** | **sa5** | **sa6** | **sa7** | **sa8** } **source** [ **chassis** *chassis-id* ] **bits0** command to configure a timeslot from which the BITS clock source extracts SSM level information.
     
     
     
     When the type of the input BITS clock signal is **2mbps**, you can manually configure the SA timeslot from which the SSM level information is extracted. By default, the SSM level information is extracted from the **2mbps** clock signals in timeslot **sa4**.
  6. (Optional) Run the [**clock source**](cmdqueryname=clock+source) **bits0****ssm** { **prc** | **ssua** | **ssub** | **sec** | **dnu** | **unk** | **prtc** | **eprtc** | **esec** | **eprc** } command to configure an SSM level for the BITS clock source.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If the signal type of the BITS clock source is set to **2mhz**, the BITS clock source cannot directly extract SSM level information from clock signals. If clock source selection based on SSM levels is enabled, you need to run this command to manually configure an SSM level for the clock source.
     + If the signal type of the BITS clock source is set to **2mbps**, you are advised not to run this command because source switching cannot be performed in case of an SSM quality level decrease.
  7. (Optional) Run the [**clock source**](cmdqueryname=clock+source) **bits0** **clock-id** *clockid-value* command to configure a clock ID for the BITS clock source.
     
     
     
     If you have enabled the extended SSM function, configure a clock ID for the BITS clock source.
  8. (Optional) Run the [**clock bits output-threshold**](cmdqueryname=clock+bits+output-threshold) { **prc** | **ssua** | **ssub** | **sec** | **dnu** } command to configure an output quality threshold for the external clock source.
     
     
     
     If the SSM level of the clock signals output by the BITS port is lower than the set threshold, the BITS port stops outputting clock signals.
  9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
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
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If clock source selection based on SSM levels is enabled, you need to run this command to manually configure an SSM level for the PTP clock source. If clock source selection based on SSM levels is not enabled, you do not need to run this command.
     + This function is static SSM quality configuration. Source switching is not performed in case of an SSM quality level decrease, but depends on the PTP time source.
  10. (Optional) Run the [**clock source**](cmdqueryname=clock+source) **ptp** **clock-id** **clockid-value** command to configure a clock ID for the PTP clock source.
  11. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.