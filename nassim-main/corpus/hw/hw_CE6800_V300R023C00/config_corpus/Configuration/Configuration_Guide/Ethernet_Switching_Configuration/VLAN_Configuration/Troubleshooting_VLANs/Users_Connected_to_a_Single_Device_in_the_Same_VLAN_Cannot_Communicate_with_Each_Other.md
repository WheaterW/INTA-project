Users Connected to a Single Device in the Same VLAN Cannot Communicate with Each Other
======================================================================================

Users Connected to a Single Device in the Same VLAN Cannot Communicate with Each Other

#### Fault Symptom

Users connected to a single device in the same VLAN cannot communicate with each other.

#### Possible Causes

* The interfaces connecting to other devices in the VLAN are down.
* The users in the VLAN are on different network segments.
* MAC address entries are incorrect.
* The VLAN configuration is incorrect.
* The port isolation function is enabled on the device.
* Incorrect static ARP entries are configured on user terminals.


#### Procedure

* Check whether the interfaces connected to user terminals are down.
  1. Check the running status of the interfaces connected to user terminals.
     
     
     ```
     [display interface](cmdqueryname=display+interface) interface-type interface-number
     ```
  2. If the interfaces are down, rectify the fault.
* Check whether the users in the VLAN are on the same network segment.
  
  
  
  Check whether the IP addresses of users in the same VLAN are on the same network segment. If not, reconfigure IP addresses for the users.
* Check whether MAC address entries on the device are correct.
  1. Check whether the MAC addresses, outbound interface, and VLANs learned by the device are correct.
     
     
     ```
     [display mac-address](cmdqueryname=display+mac-address)
     ```
  2. If not, delete these incorrect MAC address entries and enable the device to learn MAC addresses again.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     [undo mac-address all](cmdqueryname=undo+mac-address+all)
     [commit](cmdqueryname=commit)
     ```
     
     
     
     If only dynamic MAC address entries are incorrect, run the **[**reset mac-address**](cmdqueryname=reset+mac-address)** command in the user view to clear dynamic MAC address entries.
* Check whether the VLAN configuration is correct.
  
  
  
  Check whether the VLAN configuration is correct against the items in the following table.
  
  | Check Item | Method |
  | --- | --- |
  | Whether the VLAN has been created | Run the [**display vlan**](cmdqueryname=display+vlan) *vlan-id* command in any view to check whether the VLAN to which the interfaces connected to user terminals belong has been created. If not, run the [**vlan**](cmdqueryname=vlan) command in the system view to create the VLAN. |
  | Whether the interfaces are added to the VLAN | Run the [**display vlan**](cmdqueryname=display+vlan) *vlan-id* command in any view to check whether the interfaces connected to user terminals are added to the specified VLAN. If not, add the interfaces to the specified VLAN. For details, see [Configuring Interface-based VLAN Assignment](vrp_vlan_cfg_0018.html#EN-US_TASK_0000001130622850__cmd159334395817). |
  | Whether connections between the interfaces and user terminals are correct | Correctly connect user terminals to the device interfaces. |
* Check whether port isolation is configured on the device.
  1. Check whether port isolation is configured on the interfaces.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     [interface](cmdqueryname=interface) interface-type interface-number
     [display this](cmdqueryname=display+this)
     ```
  2. If so, disable port isolation on the interfaces.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     [interface](cmdqueryname=interface) interface-type interface-number
     [portswitch](cmdqueryname=portswitch)
     [undo port-isolate enable](cmdqueryname=undo+port-isolate+enable) [ group group-id ]
     [commit](cmdqueryname=commit)
     ```
* Check whether incorrect static ARP entries are configured on the user terminals. If so, correct the configuration.