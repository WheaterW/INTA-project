(Optional) Configuring a TOD Interface to Output Time Signals
=============================================================

TOD interfaces on T-BC devices can be configured to output time signals.

#### Context

Perform the following steps on the T-BC:


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Configure the type of output time signals on the TOD interface.
   
   
   
   In this example, the type of output time signals on the bits1 interface is set to **1pps**.
   
   ```
   [clock bits-type](cmdqueryname=clock+bits-type) bits1 1pps output
   ```
   
   The actual quantity of BITS interfaces and their numbers vary with the hardware configuration. You need to set them based on the actual situation. For details about clock interfaces, see *Hardware Description*.
   
   Generally, bits0 provides frequency signals for physical clock synchronization and corresponds to CLK or CLK/TOD0 on the interface panel; bits1 provides time signals and corresponds to TOD or CLK/TOD1 on the interface panel.
3. (Optional) Run the [**clock tod protocol**](cmdqueryname=clock+tod+protocol) { **g-8271** | **ubx** | **nmea** | **ccsa** } command to configure the protocol with which output time signals on the TOD interface comply.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The same protocol type must be configured at both transmit and receive ends of signals on 1PPS+TOD external time interfaces. You are advised to set the protocol type of TOD signals to g-8271.
   * If the **ubx** or **nmea** parameter is configured, the device cannot obtain the clock class from an external time source. It cannot detect any clock class degrade on the upstream device or perform source switching when such degrade occurs.
   * After the **ccsa** parameter is configured, the PPS status of TOD input and output external time signals is converted into the clock class based on the CCSA standard.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.