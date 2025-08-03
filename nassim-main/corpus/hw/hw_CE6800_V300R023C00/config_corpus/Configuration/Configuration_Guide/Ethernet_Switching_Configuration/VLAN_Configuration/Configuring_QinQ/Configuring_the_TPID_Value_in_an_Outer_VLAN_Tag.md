Configuring the TPID Value in an Outer VLAN Tag
===============================================

Configuring the TPID Value in an Outer VLAN Tag

#### Context

The Tag Protocol Identifier (TPID) field in a VLAN tag specifies the protocol type, whose value is defined as 0x8100 in IEEE 802.1Q. As devices from different vendors or in different network plans may use different TPID values in the outer VLAN tag of packets, to ensure that the device can properly communicate with a non-Huawei device or work properly on a specific network, configure the TPID of the device to a value that can be identified accordingly.

* Ensure that the configured TPID value can be identified by non-Huawei devices.
* A device identifies incoming packets based on the TPID value, and adds or changes the TPID value of outgoing packets.
* The TPID value in the outer VLAN tag cannot be configured on dot1q-tunnel interfaces.

![](public_sys-resources/note_3.0-en-us.png) 

The CE6885-LL (low latency mode) does not support this function.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the Ethernet interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   
   
   Determine whether to perform this step based on the current interface working mode.
4. Configure the TPID value in the outer VLAN tag.
   
   
   ```
   [qinq protocol](cmdqueryname=qinq+protocol) ethertype-value
   ```
   
   You can set the TPID value to 0x8100, 0x9100, or 0x88a8. By default, the TPID value in the outer VLAN tag is 0x8100.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```