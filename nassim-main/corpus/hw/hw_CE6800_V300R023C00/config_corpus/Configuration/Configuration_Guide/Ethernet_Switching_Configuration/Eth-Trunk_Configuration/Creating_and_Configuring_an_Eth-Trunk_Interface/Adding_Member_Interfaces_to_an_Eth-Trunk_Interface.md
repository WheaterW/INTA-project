Adding Member Interfaces to an Eth-Trunk Interface
==================================================

Adding Member Interfaces to an Eth-Trunk Interface

#### Context

Physical interfaces can be added to an Eth-Trunk interface in either of the following modes:

* Add physical interfaces either in batches or one by one to an Eth-Trunk interface in the view of the Eth-Trunk interface.
* Add a physical interface to a specific Eth-Trunk interface in the view of the physical interface.

**Before Link Aggregation Is Configured**

* When adding an interface to an Eth-Trunk interface, ensure that the interface is of the default type. In addition, the member interface cannot be configured with certain services, such as a static MAC address. Otherwise, the device displays an error message. (Because the services supported by interfaces are different, the types of services that cannot be configured on an interface added to an Eth-Trunk interface cannot be listed. For details, see the error message displayed on the device.)
* Devices at both ends of an Eth-Trunk link must use the same number of physical interfaces and the same interface rate, duplex mode, and flow control mode.
* It is recommended that the same jumbo frame length be configured for the physical interfaces connecting the devices at both ends of an Eth-Trunk link.
* If an interface of the local device is added to an Eth-Trunk interface, the directly connected interface on the peer device must also be added to an Eth-Trunk interface. Otherwise, communication between the two devices will fail.
* Both devices of an Eth-Trunk link must use the same link aggregation mode.
* Interfaces operating at different rates and in different duplex modes can be added to the same Eth-Trunk interface. In addition, optical and electrical interfaces can be added to a single Eth-Trunk interface.
* A member interface of an Eth-Trunk interface cannot also be an Eth-Trunk interface.
* Interfaces operating at different rates, in different duplex modes, and on different boards can be added to the same Eth-Trunk interface working in LACP mode. However, member interfaces working at different rates cannot forward data at the same time, and member interfaces working in half-duplex mode cannot forward traffic. As such, before the configuration, check the boards where member interfaces reside, interface rates, and duplex modes.

![](public_sys-resources/note_3.0-en-us.png) 

If you run the [**shutdown**](cmdqueryname=shutdown) command on an Eth-Trunk interface, the physical status of both the Eth-Trunk interface and its member interfaces becomes **Administratively DOWN**, and the **shutdown** command is visible in the configuration file under each member interface.



#### Procedure

* Add one or more member interfaces in the Eth-Trunk interface view.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the view of an Eth-Trunk interface.
     
     
     ```
     [interface](cmdqueryname=interface) eth-trunk trunk-id
     ```
  3. Run either of the following commands as required.
     
     
     + Add physical interfaces to the Eth-Trunk interface in batches.
       
       ```
       [trunkport](cmdqueryname=trunkport) interface-type { interface-number1 [ to interface-number2 ] } &<1-16>
       ```
     + Add a single physical interface to the Eth-Trunk interface.
       
       ```
       [trunkport](cmdqueryname=trunkport) interface-type interface-number
       ```
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Add a physical interface to an Eth-Trunk interface in the view of the physical interface.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the view of an Eth-Trunk interface.
     
     
     ```
     [interface](cmdqueryname=interface) eth-trunk trunk-id
     ```
  3. Enter the view of the physical interface that needs to be added to an Eth-Trunk interface.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  4. Add the physical interface to an Eth-Trunk interface.
     
     
     ```
     [eth-trunk](cmdqueryname=eth-trunk) trunk-id
     ```
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Follow-up Procedure

An Eth-Trunk interface functions properly after you complete configurations described in [Creating an Eth-Trunk Interface and Configure a Link Aggregation Mode for It](vrp_eth-trunk_cfg_0012.html) and [Adding Member Interfaces to an Eth-Trunk Interface](vrp_eth-trunk_cfg_0013.html) on the local and peer devices. You can then configure services on the Eth-Trunk interface. To modify Eth-Trunk interface parameters, see [(Optional) Configuring Parameters for an Eth-Trunk Interface in Manual Mode](vrp_eth-trunk_cfg_0014.html) or [(Optional) Configuring Parameters for an Eth-Trunk Interface in LACP Mode](vrp_eth-trunk_cfg_0016.html).

**After Link Aggregation Is Configured**

* An Ethernet interface can be added to only one Eth-Trunk interface. To add the Ethernet interface to another Eth-Trunk interface, delete it from the original one first.
* After an interface is added to an Eth-Trunk interface, MAC address entries and ARP entries are learned based on the entire Eth-Trunk interface, not according to individual member interfaces.

* Before you remove an interface from or add a physical interface to an Eth-Trunk interface, run the **shutdown** command for this interface. After this interface is removed or added, run the **undo shutdown** command.
* Before deleting an Eth-Trunk interface, delete all of its member interfaces.