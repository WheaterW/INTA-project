Enabling LLDP
=============

Enabling LLDP

#### Prerequisites

Before configuring LLDP, complete the following tasks:

* Configure reachable routes between devices and the NMS, and set SNMP parameters.
* Configure an IP address for LLDP management on a device.

#### Context

When a device and its neighbors are all enabled with LLDP, the device notifies the neighbors of its status and obtains their status information by exchanging LLDP frames with them.

LLDP can be enabled globally or on an interface. The relationships are as follows:

* By default, LLDP is enabled on all interfaces that support LLDP after LLDP is enabled globally.
* After LLDP is disabled globally, this function is disabled on all interfaces that support it.
* An interface can send and receive LLDP packets only when LLDP is enabled globally and on the interface.
* The operation of enabling or disabling LLDP on an interface does not take effect when LLDP is disabled globally.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable LLDP globally.
   
   
   ```
   [lldp enable](cmdqueryname=lldp+enable)
   ```
3. (Optional) Enable the interface mode of the LLDP management address.
   
   
   ```
   [lldp management-address interface-mode](cmdqueryname=lldp+management-address+interface-mode)
   ```
4. (Optional) Enable LLDP on an interface.
   
   
   1. Enter the interface view.
      ```
      [interface](cmdqueryname=interface) interface-type interface-number
      ```
   2. Enable LLDP on the interface.
      ```
      [undo lldp disable](cmdqueryname=undo+lldp+disable)
      ```
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * To enable LLDP on some interfaces and disable LLDP on other interfaces, enable LLDP globally and run the [**lldp disable**](cmdqueryname=lldp+disable) command in the views of the interfaces on which LLDP needs to be disabled.
   * LLDP can be configured only on physical interfaces. Logical interfaces do not support LLDP. For Eth-Trunk interfaces, LLDP can be configured only on Eth-Trunk member interfaces. Enabling or disabling LLDP on an Eth-Trunk member interface does not affect other member interfaces.
5. (Optional) Configure the LLDP working mode on an interface.
   
   
   1. Enter the interface view.
      ```
      [interface](cmdqueryname=interface) interface-type interface-number
      ```
   2. Configure the LLDP working mode on the interface.
      ```
       [lldp admin-status](cmdqueryname=lldp+admin-status) { tx | rx | txrx }
      ```
   
   This configuration allows the interface to work only in a specified mode, reducing the number of LLDP frames exchanged on the network. In this way, the system load is reduced, and other services are not affected.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```