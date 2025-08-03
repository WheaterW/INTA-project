Configuring Layer 3 Sub-interfaces to Implement Inter-VLAN Communication
========================================================================

Configuring Layer 3 Sub-interfaces to Implement Inter-VLAN Communication

#### Prerequisites

Before configuring Layer 3 sub-interfaces to implement inter-VLAN communication, you have completed the following tasks:

* Create VLANs. For details, see [Creating and Deleting a VLAN](vrp_vlan_cfg_0013.html).
* Run the [**undo portswitch**](cmdqueryname=undo+portswitch) command to switch the working mode of the physical interface where a sub-interface needs to be created to Layer 3.![](public_sys-resources/note_3.0-en-us.png) 
  
  Determine whether to switch the interface working mode to Layer 3 based on the current interface working mode.

#### Context

The most direct method for implementing inter-VLAN communication is connecting VLANs to different physical interfaces of a Layer 3 device to route the packets between VLANs. However, this method requires many physical interfaces. To solve this problem, you can configure Layer 3 sub-interfaces.

Layer 3 sub-interfaces are logical Layer 3 interfaces that can be configured on one physical interface, each corresponding to one VLAN. This means inter-VLAN communication can be achieved by using only one physical interface. Inter-VLAN communication through Layer-3 sub-interfaces applies only when the hosts in different VLANs are located in different network segments. For details, see [Inter-VLAN Communication Through a Single Device Using Layer 3 Sub-interfaces](vrp_vlan_cfg_0009.html#EN-US_CONCEPT_0000001176742329__section26271943217).


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a sub-interface and enter the sub-interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number.subinterface-number
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   By default, a Layer 3 sub-interface reports a linkdown alarm (Trap OID: 1.3.6.1.6.1.1.5.3) when its status changes. When there are a large number of Layer 3 sub-interfaces on a device, linkDown alarms may be reported every few minutes, burdening the NMS involved. To address this issue, run the [**subinterface trap updown disable**](cmdqueryname=subinterface+trap+updown+disable) command to ignore linkDown alarms. After this command is run, linkDown alarms are no longer generated on any of the device's sub-interfaces even when their status changes. Exercise caution when running this command.
3. Configure the encapsulation type for the sub-interface and VLAN ID associated with the sub-interface.
   
   
   ```
   [dot1q termination vid](cmdqueryname=dot1q+termination+vid) low-pe-vid
   ```
4. Assign an IP address to the sub-interface.
   
   
   ```
   [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length } [ sub ]
   ```
   
   
   
   The sub-interface and corresponding main interface can be on the same primary network segment but must use different subnet masks.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display vlan**](cmdqueryname=display+vlan) *vlan-id***verbose** command to check the sub-interface associated with a VLAN.