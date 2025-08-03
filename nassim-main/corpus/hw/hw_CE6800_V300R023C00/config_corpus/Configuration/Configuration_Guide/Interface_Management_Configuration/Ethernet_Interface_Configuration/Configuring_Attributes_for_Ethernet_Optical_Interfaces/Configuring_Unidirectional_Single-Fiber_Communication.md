Configuring Unidirectional Single-Fiber Communication
=====================================================

Configuring Unidirectional Single-Fiber Communication

#### Context

Unidirectional single-fiber communication enables a device to send but not receive packets or, conversely, to receive but not send packets. A single fiber means that two optical modules are connected by only one fiber, and unidirectional communication means that packets can be sent in only one direction. For example, during network management and maintenance, the administrator needs to send traffic to a specified server for analysis. This may pose a security risk if the server is able to send the traffic to other devices. The unidirectional single-fiber communication function can address this issue.

An optical module typically consists of a transmit (TX) end and a receive (RX) end, which can be respectively connected to the RX and TX ends of another module using fibers. A device transmits and receives packets through two independent fibers. If the unidirectional single-fiber communication function is disabled, two devices cannot communicate with each other through a single fiber. After this function is configured, the devices can use one fiber to communicate with each other.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. (Optional) Pre-configure a medium type for the interface.
   
   
   ```
   [device transceiver](cmdqueryname=device+transceiver) transceiver-type
   ```
   
   You can configure single-fiber communication on an interface only after an optical module (not a single-fiber bidirectional optical module) is inserted into the interface. If no optical module is inserted into the interface, you can run this command to pre-configure the medium type of the interface as fiber.
4. Perform either of the following operations based on requirements: (The two commands cannot be used together. If both commands are configured, only the later one takes effect.)
   
   
   * Enable the unidirectional single-fiber communication function.
     ```
     [single-fiber enable](cmdqueryname=single-fiber+enable)
     ```
     
     By default, the unidirectional single-fiber communication function is disabled. After this command is run on an interface, the interface will be in down state if no optical module is inserted, or if a single-fiber bidirectional optical module, MPO optical module, or high-speed cable is inserted into the interface. This command enables the function of only sending or receiving packets based on the connection mode of the optical module.
   * Configure the single-fiber receiving function.
     ```
     [single-fiber rx](cmdqueryname=single-fiber+rx)
     ```
     
     By default, the single-fiber receiving function is disabled. After the command is run, the interface goes up only when the optical modules at both ends are present and can receive optical signals properly. The command takes effect only when the RX port of the optical module is connected on the local end.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```