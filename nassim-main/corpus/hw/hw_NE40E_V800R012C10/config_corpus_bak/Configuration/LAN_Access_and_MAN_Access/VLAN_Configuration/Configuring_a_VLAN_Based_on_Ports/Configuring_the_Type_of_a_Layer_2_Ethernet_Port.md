Configuring the Type of a Layer 2 Ethernet Port
===============================================

On a Layer 2 switching device, some ports identify frames with VLAN tags, whereas the others do not. Configure ports types for Layer 2 Ethernet ports as needed.

#### Context

[Table 1](#EN-US_TASK_0172363088__tab_dc_vrp_vlan_cfg_000701) lists Layer 2 Ethernet port types.

**Table 1** Port types
| Port Type | Method for Processing a Received Untagged Frame | Method for Processing a Received Tagged Frame | Method for Sending a Frame | Application |
| --- | --- | --- | --- | --- |
| Access port | Accepts the frame and adds a tag with the default VLAN ID to the frame. | * Accepts the frame if the VLAN ID carried in the frame is the same as the default VLAN ID. * Discards the frame if the VLAN ID carried in the frame is different from the default VLAN ID. | Removes the tag from the frame and sends the frame. | An access port connects a switch to a PC and can be added to only one VLAN. |
| Trunk port | Discards the frame. | * Accepts the frame if the port permits the VLAN ID carried in the frame. * Discards the frame if the port denies the VLAN ID carried in the frame. | * Directly sends the frame if the port permits the VLAN ID carried in the frame. * Discards the frame if the port denies the VLAN ID carried in the frame. | A trunk port can be added to multiple VLANs to send and receive frames for these VLANs. A trunk port connects a switch to another switch or to a router. |
| Hybrid port | * If only the **port default vlan** command is run on a hybrid port, the hybrid port receives the frame and adds the default VLAN tag to the frame. * If only the **port trunk allow-pass** command is run on a hybrid port, the hybrid port discards the frame. * If both the **port default vlan** and **port trunk allow-pass** commands are run on a hybrid port, the hybrid port receives the frame and adds the VLAN tag with the default VLAN ID specified in the **port default vlan** command to the frame. | * If only the **port default vlan** command is run on a hybrid port:   + The hybrid port accepts the frame if the frame's VLAN ID is the same as the default VLAN ID of the port.   + The hybrid port discards the frame if the frame's VLAN ID is different from the default VLAN ID of the port. * If only the **port trunk allow-pass** command is run on a hybrid port:   + The hybrid port accepts the frame if the frame's VLAN ID is in the permitted range of VLAN IDs.   + The hybrid port discards the frame if the frame's VLAN ID is not in the permitted range of VLAN IDs. * If both the **port default vlan** and **port trunk allow-pass** commands are run on a hybrid port:   + The hybrid port accepts the frame if the frame's VLAN ID is in the permitted range of VLAN IDs specified in the **port trunk allow-pass** command or is the same as the default VLAN ID specified in the **port default vlan** command.   + The hybrid port discards the frame if the frame's VLAN ID is not in the permitted range of VLAN IDs specified in the **port trunk allow-pass** command or is different from the default VLAN ID specified in the **port default vlan** command. | * If only the **port default vlan** command is run on the hybrid port and the frame's VLAN ID is the same as the default VLAN ID, the hybrid port removes the VLAN tag and forwards the frame. Otherwise, the hybrid port discards the frame. * If only the **port trunk allow-pass** command is run on a hybrid port:   + The hybrid port forwards the frame if the frame's VLAN ID is in the permitted range of VLAN IDs.   + The hybrid port discards the frame if the frame's VLAN ID is not in the permitted range of VLAN IDs. * If both the **port default vlan** and **port trunk allow-pass** commands are run on a hybrid port:   + The hybrid port removes the VLAN tag and forwards the frame if the frame's VLAN ID is the same as the default VLAN ID of the port.   + The hybrid port forwards the frame if the frame's VLAN ID is different from the default VLAN ID of the port but in the permitted range of VLAN IDs specified in the **port trunk allow-pass** command. Otherwise, the hybrid port discards the frame.    NOTE:  The hybrid port removes the VLAN tag and forwards the frame if the frame's VLAN ID is the same as the default VLAN ID configured using the **port default vlan** command and the default VLAN ID is in the permitted range of VLAN IDs specified in the **port trunk allow-pass** command. | A hybrid port can be added to multiple VLANs to send and receive frames of these VLANs. A hybrid port can be used to connect network devices or connect user devices. |
| QinQ port | QinQ ports are enabled with the IEEE 802.1QinQ protocol. A QinQ port adds a tag to a single-tagged frame, and thus supports a maximum of 4094 x 4094 VLANs, which meets the requirement of a Metropolitan Area Network (MAN) for the number of VLANs. | | | |



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The view of a Layer 3 Ethernet interface to be added to a VLAN is displayed.
3. Run [**portswitch**](cmdqueryname=portswitch)
   
   
   
   The Layer 3 interface is switched to a Layer 2 interface.
   
   
   
   * If an interface borrows the IP address of an Ethernet, GE, or Eth-Trunk interface, the **portswitch** command cannot be run on the latter interface.
   * If an Ethernet, GE, or Eth-Trunk interface has any Layer 3 configuration, the **portswitch** command cannot be run on the interface. Before running the **portswitch** command on the interface, clear all Layer 3 configurations first.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If many Layer 3 Ethernet interfaces need to be added to the VLAN, run the [**portswitch batch**](cmdqueryname=portswitch+batch) *interface-type* { *interface-number1* [ **to** *interface-number2* ] } &<1-10> command in the system view to switch the working mode of these Ethernet interfaces in batches.
4. Run [**port link-type**](cmdqueryname=port+link-type) { **access** | **dot1q-tunnel** | **hybrid** | **trunk** }The port type is configured.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If you have specified a Dot1q-tunnel interface, run the [**port dot1q-tunnel discard untag-frame**](cmdqueryname=port+dot1q-tunnel+discard+untag-frame) command to enable this Dot1q-tunnel interface to discard incoming untagged packets to ensure network security.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.