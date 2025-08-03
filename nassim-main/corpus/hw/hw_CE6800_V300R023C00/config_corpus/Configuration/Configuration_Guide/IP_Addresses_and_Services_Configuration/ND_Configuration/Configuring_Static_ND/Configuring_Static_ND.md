Configuring Static ND
=====================

Configuring Static ND

#### Context

ND entries indicate the mappings between IPv6 and MAC addresses of neighbors. Devices obtain these mappings through ND messages. If a device is not enabled to send ND messages, it cannot obtain ND entries. To enable such a device to obtain ND entries, configure static ND on the device.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of the interface on which a static ND entry needs to be configured.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
4. Enable IPv6.
   
   
   ```
   [ipv6 enable](cmdqueryname=ipv6+enable)
   ```
5. Configure a static ND entry for the interface. The configuration command varies according to the interface type.
   
   
   
   **Table 1** Static ND entry configuration commands for different types of interfaces
   | Operation | Command |
   | --- | --- |
   | Configure a static ND entry for a common Layer 3 interface. | [**ipv6 neighbor**](cmdqueryname=ipv6+neighbor) *ipv6-address* *mac-address* |
   | Configure a static ND entry for a VLANIF interface. | [**ipv6 neighbor**](cmdqueryname=ipv6+neighbor) *ipv6-address* *mac-address* **vlan** *vlan-id* *interface-type* *interface-number* |
   | Configure a static ND entry for a Layer 3 sub-interface. | [**ipv6 neighbor**](cmdqueryname=ipv6+neighbor) *ipv6-address mac-address* **vlan** *pe-vlan-id* |
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```