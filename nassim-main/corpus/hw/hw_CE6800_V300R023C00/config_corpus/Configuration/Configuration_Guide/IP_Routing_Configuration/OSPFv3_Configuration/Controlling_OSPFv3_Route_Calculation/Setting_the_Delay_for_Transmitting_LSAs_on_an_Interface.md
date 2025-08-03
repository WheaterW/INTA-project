Setting the Delay for Transmitting LSAs on an Interface
=======================================================

Setting the Delay for Transmitting LSAs on an Interface

#### Prerequisites

Before setting the delay for transmitting LSAs on an interface, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

#### Context

Because it takes time to transmit OSPFv3 packets on a link, a certain delay is added to the aging time carried in an LSA before a device interface sends this LSA. Setting the delay for transmitting LSAs on OSPFv3 interfaces is recommended on low-speed links.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Set the delay for transmitting LSAs on the interface.
   
   
   ```
   [ospfv3 trans-delay](cmdqueryname=ospfv3+trans-delay) interval [ instance instance-id ]
   ```
   
   By default, the delay for transmitting LSAs is 1 second.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **interface** [ **area** *area-id* ] [ *interface-type* *interface-number* ] command to check OSPFv3 interface information. The **Transmit Delay** field in the command output indicates the delay for transmitting LSAs.