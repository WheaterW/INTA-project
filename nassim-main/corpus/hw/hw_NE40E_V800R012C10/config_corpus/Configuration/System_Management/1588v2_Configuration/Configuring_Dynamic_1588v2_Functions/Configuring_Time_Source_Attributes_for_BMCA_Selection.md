Configuring Time Source Attributes for BMCA Selection
=====================================================

This section describes how to configure time source attributes used for BMCA selection. The devices configured with time source attributes can participate in BMCA selection. A local clock on a 1588v2 device can also participate in BMCA selection. The BMCA helps 1588v2 devices select a grandmaster clock. The grandmaster clock provides time signals for other devices over a 1588v2 network. 1588v2 devices obtain time synchronization information from the grandmaster.

#### Context

A 1588v2 Router runs the BMCA to use the following parameters in sequence to select a grandmaster clock:

* **priority1**
* **clock-class**
* **clock-accuracy**
* **priority2**

For example, the Router compares **priority1** values of two candidates. If the two candidates have the same **priority1** value, the Router compares clock classes of the two candidates. The process repeats until the Router selects a grandmaster clock.

Perform the following steps on the Routers connected to external BITS time sources (including PTP interfaces and external time interfaces) on the 1588v2 network.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* When a time server is interconnected with a device (through a PTP interface or external time interface), it is recommended that the local priority2 (*priority2-value*) be configured for the device and other parameters take the default values. When a device is interconnected with a time server or third-party device through an external time interface, you need to set priority2 (*priority2-value*) for the external time interface and retain the default values for other parameters.
* You are advised to retain the default values of *time-source-value*, *clock-accuracy-value*, *clock-class-value*, *priority1-value*, *clockid-value*, and *offsetscaled-logvariance-value* for the time source.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This section uses the BITS1 external time interface as an example. The actual quantity of external time interfaces and their types and numbers vary with the hardware configuration. You need to set them based on the actual situation.



#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Configure priority2 of the time source.
   
   
   ```
   [ptp clock-source](cmdqueryname=ptp+clock-source) { local | bits1 } priority2 priority2-value
   ```
3. (Optional) Configure the time source type.
   
   
   ```
   [ptp clock-source](cmdqueryname=ptp+clock-source) { local | bits1 } time-source time-source-value 
   ```
   
   For the mapping between the *time-source-value* parameter and time source types, see [**ptp clock-source**](cmdqueryname=ptp+clock-source) in the *NE40E Command Reference*.
4. (Optional) Configure the accuracy of the time source.
   
   
   ```
   [ptp clock-source](cmdqueryname=ptp+clock-source) { local | bits1 } clock-accuracy clock-accuracy-value 
   ```
   
   
   
   For the mapping between the *clock-accuracy-value* parameter and clock precision, see [**ptp clock-source**](cmdqueryname=ptp+clock-source) in the *NE40E Command Reference*.
5. (Optional) Configure the clock class of the time source.
   
   
   ```
   [ptp clock-source](cmdqueryname=ptp+clock-source) { local | bits1 } clock-class clock-class-value
   ```
   
   For the mapping between the *clock-class-value* parameter and the clock source class, see [**ptp clock-source**](cmdqueryname=ptp+clock-source) in the *NE40E Command Reference*. If the *clock-class-value* value is less than 128, the device cannot function as a slave clock.
6. (Optional) Configure priority1 of the time source.
   
   
   ```
   [ptp clock-source](cmdqueryname=ptp+clock-source) { local | bits1 } priority1 priority1-value
   ```
7. (Optional) Configure the grandmaster clock ID of the time source.
   
   
   ```
   [ptp clock-source](cmdqueryname=ptp+clock-source) bits1 grandmaster-clockid clockid-value
   ```
8. (Optional) Configure the stability value of the time source.
   
   
   ```
   [ptp clock-source](cmdqueryname=ptp+clock-source) bits1 offsetscaled-logvariance offsetscaled-logvariance-value
   ```
9. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.