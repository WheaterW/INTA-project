An Interface Fails to Learn MAC Address Entries
===============================================

An Interface Fails to Learn MAC Address Entries

#### Fault Symptom

An interface cannot learn MAC address entries, causing Layer 2 forwarding failures.


#### Procedure

1. Check device configuration.
   
   
   
   | Check Item | Check Method | Follow-up Procedure |
   | --- | --- | --- |
   | Whether the VLAN that the interface belongs to has been created | Run the [**display vlan**](cmdqueryname=display+vlan) *vlan-id* command in any view. If the system displays the message "Error: The VLAN does not exist.", the VLAN has not been created. | Run the [**vlan**](cmdqueryname=vlan) *vlan-id* command in the system view to create a VLAN. |
   | Whether the interface transparently transmits packets from the VLAN | Run the [**display vlan**](cmdqueryname=display+vlan) *vlan-id* command in any view to check whether the interface name exists. If not, the interface does not transparently transmit packets from the VLAN. | For a trunk interface, run the [**port trunk allow-pass vlan**](cmdqueryname=port+trunk+allow-pass+vlan) command to add the interface to the VLAN.  For a hybrid interface, run the [**port hybrid tagged vlan**](cmdqueryname=port+hybrid+tagged+vlan) or [**port hybrid untagged vlan**](cmdqueryname=port+hybrid+untagged+vlan) command to add the interface to the VLAN.  For an access interface, run the [**port default vlan**](cmdqueryname=port+default+vlan) command to add the interface to the VLAN. |
   | Whether a blackhole MAC address entry is configured | Run the [**display mac-address blackhole**](cmdqueryname=display+mac-address+blackhole) command in any view to check whether a blackhole MAC address entry is configured. | If a blackhole MAC address entry is displayed, run the [**undo mac-address blackhole**](cmdqueryname=undo+mac-address+blackhole) command in the system view to delete the blackhole MAC address entry. |
   | Whether MAC address learning is disabled on the interface or in the VLAN | Run the [**display this | include learning**](cmdqueryname=display+this+%7C+include+learning) command in the interface view and VLAN view to check whether the **mac-address learning disable** configuration exists. If so, MAC address learning is disabled on the interface or in the VLAN. | Run the [**undo mac-address learning disable**](cmdqueryname=undo+mac-address+learning+disable) command in the interface view or VLAN view to enable MAC address learning. |
   | Whether MAC address learning is disabled in a BD | Run the [**display this | include learning**](cmdqueryname=display+this+%7C+include+learning) command in the BD view to check whether the **mac-address learning disable** configuration exists. If so, MAC address learning is disabled in the BD. | Run the [**undo mac-address learning disable**](cmdqueryname=undo+mac-address+learning+disable) command in the BD view to enable MAC address learning. |
   | Whether the numbers of MAC address entries that can be learned on the interface and in the VLAN are limited | Run the [**display this | include mac-address limit**](cmdqueryname=display+this+%7C+include+mac-address+limit) command in the interface view and VLAN view to check whether the number of learned MAC address entries is limited. If so, the maximum number of learned MAC address entries is set. | * Run the [**mac-address limit**](cmdqueryname=mac-address+limit) command in the interface view or VLAN view to increase the maximum number of learned MAC address entries. * Run the [**undo mac-address limit**](cmdqueryname=undo+mac-address+limit) command in the interface view or VLAN view to remove the MAC address learning limit. |
   | Whether the number of MAC addresses that can be learned in a BD is limited | Run the [**display this | include mac-address limit**](cmdqueryname=display+this+%7C+include+mac-address+limit) command in the BD view to check whether the number of learned MAC addresses is limited. If so, the maximum number of learned MAC addresses is set. | * Run the [**mac-address limit**](cmdqueryname=mac-address+limit) command in the BD view to increase the maximum number of learned MAC addresses. * Run the [**undo mac-address limit**](cmdqueryname=undo+mac-address+limit) command in the BD view to remove the MAC address learning limit. |
   
   If the fault persists, go to Step 2.
2. Check whether a loop causes MAC address entry flapping.
   
   
   1. Run the [**mac-address flapping detection**](cmdqueryname=mac-address+flapping+detection) command in the system view to configure MAC address flapping detection.
   2. The system checks for MAC address flapping among all MAC addresses in the VLAN.
   
   If no loop is detected, go to Step 3.
3. Check whether the number of learned MAC address entries has reached the maximum value. If so, the device cannot learn new MAC address entries.
   
   
   * If the number of MAC address entries learned on the interface is less than or equal to the number of hosts connected to the interface, the device is connected to more hosts than it supports. Adjust your network plan accordingly.
   * If the interface has learned much more MAC address entries than the number of hosts connected to the interface, the interface may be experiencing a MAC address attack from the attached network.
     
     | Category | Solution |
     | --- | --- |
     | The interface connects to another network device. | Run the [**display mac-address**](cmdqueryname=display+mac-address) command on the connected device to view MAC address entries. Use the displayed MAC address entries to locate the interface connected to the malicious host. If the located interface is connected to another network device, repeat this step until you locate the malicious host. |
     | The interface connects to a host. | + Disconnect the host after obtaining permission from the administrator. After the attack stops, reconnect the host to the network. + Run the [**mac-address limit**](cmdqueryname=mac-address+limit) command on the interface to set the maximum number of MAC addresses learned on the interface to 1. |