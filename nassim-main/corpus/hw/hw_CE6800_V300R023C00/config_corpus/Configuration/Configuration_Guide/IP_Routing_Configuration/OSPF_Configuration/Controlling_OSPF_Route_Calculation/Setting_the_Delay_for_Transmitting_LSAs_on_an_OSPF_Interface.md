Setting the Delay for Transmitting LSAs on an OSPF Interface
============================================================

Setting the Delay for Transmitting LSAs on an OSPF Interface

#### Prerequisites

Before setting the delay for transmitting LSAs on an OSPF interface, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Context

Setting the delay for transmitting LSAs on OSPF interfaces is recommended on low-speed networks.


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
   [ospf trans-delay](cmdqueryname=ospf+trans-delay) delayvalue
   ```
   
   An LSA ages by 1 each second in the LSDB on the local device, but it does not increase during transmission. Therefore, an LSA transmission delay needs to be set before LSAs are sent.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **interface** [ **all** | **no-peer** | *interface-type* *interface-number* ] [ **verbose** ] command to check OSPF interface information. The **Transmit Delay** field in the command output indicates the delay for transmitting LSAs.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **brief** command to check brief OSPF information. The **Timers** field in the command output indicates the delay for transmitting LSAs.