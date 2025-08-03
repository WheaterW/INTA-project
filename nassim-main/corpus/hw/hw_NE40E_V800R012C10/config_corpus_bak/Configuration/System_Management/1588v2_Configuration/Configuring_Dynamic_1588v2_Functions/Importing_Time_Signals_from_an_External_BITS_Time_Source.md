Importing Time Signals from an External BITS Time Source
========================================================

On a 1588v2 network, time signals are typically imported from an external BITS time source. You can configure multiple Routers to import time signals from an external BITS time source. A master clock can be selected dynamically using the BMCA.

#### Context

The BITS time source can provide reference time signals for devices. 1588v2 devices can be configured to import time signals from BITSs and use the BMCA to select the grandmaster. The grandmaster clock provides time signals for other devices over a 1588v2 network. 1588v2 devices obtain time synchronization information from the grandmaster.

The device can import time signals from external BITS time sources through the following interfaces:

* PTP interface: a service interface (such as a GE interface) that supports 1588v2.
* External time interface: also called a BITS interface, is a dedicated interface for inputting or outputting time signals. It usually corresponds to the TOD or CLK/TOD interface on the front panel of a device. External time interfaces are numbered in the format of **BITS** + *X*. The most common external time interface number is BITS1. For details about external time interfaces, see the interface description in the Hardware Description.

If time signals of external BITS time sources are imported through PTP interfaces, skip this section. If time signals of external BITS time sources are imported through external time interfaces, perform the following steps on the device:

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This section uses the external time source with the BITS1 interface as an example. The actual quantity of external time interfaces and their types and numbers vary with the hardware configuration. You need to set them based on the actual situation.



#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Set the type of the time signals from the external time interface.
   
   
   ```
   [clock bits-type](cmdqueryname=clock+bits-type) bits1 1pps input
   ```
3. Configure the time signals input from the external time interface to participate in BMCA calculation.
   
   
   ```
   [ptp clock-source](cmdqueryname=ptp+clock-source) bits1 on
   ```
4. Configure the protocol type that the time signals from the external time interface comply with.
   
   
   ```
   [clock tod protocol](cmdqueryname=clock+tod+protocol) { g-8271 | ccsa | ubx | nmea }
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The same protocol type must be configured at both transmit and receive ends of signals on 1PPS+TOD external time interfaces. You are advised to set the protocol type of TOD signals to g-8271.
   * If the **ubx** or **nmea** parameter is configured, the device cannot obtain the clock class from an external time source. It cannot detect any clock class degrade on the upstream device or perform source switching when such degrade occurs.
   * After the **ccsa** parameter is configured, the PPS status of TOD input and output external time signals is converted into the clock class based on the CCSA standard.
5. Configure the correction for the delay in receiving time signals from the external time interface.
   
   
   ```
   [ptp clock-source](cmdqueryname=ptp+clock-source) bits1 receive-delay receive-delay-value
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You can perform this step to configure delay compensation for external time interfaces. The delay varies according to cables. The external time offset caused by cable length is 5 ns/m. When external time synchronization is implemented, you are advised to compensate for the external time offset based on the actual cable length.
6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.