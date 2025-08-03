Enabling LLDP
=============

When LLDP is enabled on a device, the device sends LLDP packets carrying its status information to its LLDP-capable neighbors and obtains their status information by receiving LLDP packets from them.

#### Context

LLDP can be enabled globally or on an interface. The relationships are as follows:

* LLDP is disabled on all interfaces that support LLDP after LLDP is disabled globally.
* An interface can send and receive LLDP packets only when LLDP is enabled globally and on the interface.
* The command to enable or disable LLDP on an interface is invalid when LLDP is disabled globally.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**lldp enable**](cmdqueryname=lldp+enable)
   
   
   
   LLDP is enabled globally.
3. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
4. (Optional) Run **[**lldp admin-status**](cmdqueryname=lldp+admin-status)** { ****tx**** | ****rx**** | ****txrx**** }
   
   
   
   The LLDP working mode is configured for the interface.
5. (Optional) Perform the following steps to enable LLDP on a sub-interface:
   
   
   1. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to create a sub-interface.
   2. Run the [**vlan-type dot1q**](cmdqueryname=vlan-type+dot1q) *vlan-id* command to associate the sub-interface with a VLAN.
   3. Run the **[**lldp enable**](cmdqueryname=lldp+enable)** command in the sub-interface view to enable LLDP on the sub-interface.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * To enable LLDP on some interfaces and disable LLDP on other interfaces on a device, enable LLDP globally on the device and run the [**undo lldp enable**](cmdqueryname=undo+lldp+enable) command on the interfaces that do not need LLDP.
   * For Eth-Trunk interfaces, LLDP can be configured only on Eth-Trunk member interfaces. Enabling or disabling LLDP on an Eth-Trunk member interface does not affect other member interfaces.
   * Interfaces that support LLDP must be physical interfaces. Logical interfaces such as VLANIF and Eth-Trunk interfaces do not support LLDP.
   * Interfaces do not support LLDP packets carrying the VLAN tag. If LLDP is used and the peer device is a non-Huawei router, configure the peer device not to carry the VLAN tag in sent LLDP packets.
   * Before enabling LLDP on a sub-interface, you need to enable LLDP on the corresponding main interface. To enable LLDP on an Eth-Trunk sub-interface, you only need to enable LLDP on all member interfaces of the Eth-Trunk.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.