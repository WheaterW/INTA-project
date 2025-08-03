Configuring Clock Source Attributes for Dynamic BMCA Selection
==============================================================

After multiple SMPTE-2059-2 devices are configured with time signal input, clock source attributes can be configured on these devices to allow them to participate in BMCA selection. The local clock of an SMPTE-2059-2 device can also participate in BMCA selection. The BMCA helps SMPTE-2059-2 devices dynamically determine the grandmaster clock which provides time signals for the entire SMPTE-2059-2 network. SMPTE-2059-2 devices can obtain time synchronization information from the grandmaster clock through the SMPTE-2059-2 protocol.

#### Context

When an SMPTE-2059-2-enabled Router uses the BMCA to dynamically select a time source, the Router compares the following parameters in sequence: **priority1** > **clock-class** > **clock-accuracy** > **priority2**. That is, the Router preferentially compares **priority1** of time sources. The time source with the largest value of **priority1** is selected as the grandmaster clock. If the **priority1** values are the same, the Router then compares **clock-class**.

Perform the following steps on the Routers connected to external BITS time sources (including PTP interfaces and external time interfaces) on the SMPTE-2059-2 network.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This section uses the BITS1 external time interface as an example. The actual quantity of external time interfaces and their types and numbers vary with the hardware configuration. You need to set them based on the actual situation.



#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Configure the type of the clock source to be traced.
   
   
   ```
   [ptp clock-source](cmdqueryname=ptp+clock-source) { local | bits1 } time-source time-source-value 
   ```
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command applies only to the grandmaster. The parameter settings vary according to the type of the clock source. For the mapping between the *time-source-value* parameter and the clock source type, see [**ptp clock-source**](cmdqueryname=ptp+clock-source) in the NE40E Command Reference.
3. Configure the accuracy of the clock source.
   
   
   ```
   [ptp clock-source](cmdqueryname=ptp+clock-source) { local | bits1 } clock-accuracy clock-accuracy-value 
   ```
   
   
   
   For the mapping between the *clock-accuracy-value* parameter and the clock precision, see [**ptp clock-source**](cmdqueryname=ptp+clock-source) in the *NE40E Command Reference*.
4. Configure the class of the clock source.
   
   
   ```
   [ptp clock-source](cmdqueryname=ptp+clock-source) { local | bits1 } clock-class clock-class-value
   ```
   
   For the mapping between the *clock-class-value* parameter and the clock source class, see [**ptp clock-source**](cmdqueryname=ptp+clock-source) in the *NE40E Command Reference*.
   
   If the *clock-class-value* value is less than 128, the device cannot function as a slave clock.
5. Configure priority1 of the clock source.
   
   
   ```
   [ptp clock-source](cmdqueryname=ptp+clock-source) { local | bits1 } priority1 priority1-value
   ```
6. Configure priority2 of the clock source.
   
   
   ```
   [ptp clock-source](cmdqueryname=ptp+clock-source) { local | bits1 } priority2 priority2-value
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