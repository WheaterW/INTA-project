Configuring a Layer 3 Eth-Trunk Sub-Interface
=============================================

Configuring a Layer 3 Eth-Trunk Sub-Interface

#### Prerequisites

Before creating a Layer 3 Eth-Trunk sub-interface, ensure that the corresponding Eth-Trunk interface has been created. You can add member interfaces to the Eth-Trunk interface in any sequence. For example, you can add member interfaces to the Eth-Trunk interface after creating a Layer 3 sub-interface.


#### Context

Layer 3 sub-interfaces can be configured on Layer 3 Eth-Trunk interfaces. When a Layer 3 device is connected to a Layer 2 device through a Layer 3 Eth-Trunk interface and the interfaces of the Layer 2 device are added to different VLANs, the Layer 3 Eth-Trunk interface needs to correctly identify packets from different VLANs to ensure normal communication between users in different VLANs. To support this, you need to create Layer 3 sub-interfaces on the Eth-Trunk interface.

![](public_sys-resources/note_3.0-en-us.png) 

The CE6885-LL (low latency mode) does not support this function.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of an Eth-Trunk interface.
   
   
   ```
   [interface eth-trunk](cmdqueryname=interface+eth-trunk) trunk-id
   ```
3. Configure the Eth-Trunk interface to work in Layer 3 mode and return to the system view.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   [quit](cmdqueryname=quit)
   ```
4. Create a Layer 3 Eth-Trunk sub-interface and enter the Eth-Trunk sub-interface view.
   
   
   ```
   [interface eth-trunk](cmdqueryname=interface+eth-trunk) trunk-id.subnumber
   ```
   
   *subnumber* specifies the number of a Layer 3 Eth-Trunk sub-interface.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   By default, a linkdown alarm (trap OID: 1.3.6.1.6.1.1.5.3) is generated when the status of a Layer 3 sub-interface changes. If there are a large number of Layer 3 sub-interfaces on a device, the linkdown alarm generated on the interface is reported to the NMS every several minutes. In this case, the NMS needs to process a large number of interface status alarms, increasing the burden on the NMS. To resolve this problem, run the **subinterface trap updown disable** command in the system view to disable the Layer 3 sub-interface from generating a linkdown alarm. After this command is run, no linkdown alarm is generated when the status of any sub-interface on the device changes. Exercise caution when running this command.
5. Configure the Eth-Trunk Layer 3 sub-interface to terminate single-tagged packets.
   
   
   ```
   [dot1q termination vid](cmdqueryname=dot1q+termination+vid) low-pe-vid
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Follow-up Procedure

After an Eth-Trunk Layer 3 sub-interface is created, you can configure an IP address, MTU, and related services on the sub-interface. You can also run the [**display interface eth-trunk**](cmdqueryname=display+interface+eth-trunk) *trunk-id.subnumber* command to view the status of the Eth-Trunk sub-interface.