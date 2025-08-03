Configuring VRRP6 in Master/Backup Mode
=======================================

Configuring VRRP6 in Master/Backup Mode

#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Enable IPv6 on the interface.
   ```
   [ipv6 enable](cmdqueryname=ipv6+enable)
   ```
   
   By default, IPv6 is disabled.
5. Configure an IPv6 address for the interface.
   ```
   [ipv6 address](cmdqueryname=ipv6+address) { ipv6-address prefix-length | ipv6-address/prefix-length }
   ```
6. Create a VRRP6 group and configure the first virtual IPv6 address for it.
   ```
   [vrrp6 vrid](cmdqueryname=vrrp6+vrid) virtual-router-id virtual-ip virtual-ipv6-address link-local
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   * When you create a VRRP6 group on an interface, ensure that the first virtual IPv6 address configured for the group is a link-local address.
   * You can specify a virtual IPv6 address for a VRRP6 group when you create the VRRP6 group. If another virtual IPv6 address is specified for the VRRP6 group later, the system adds the virtual IPv6 address to the virtual IPv6 address list for the VRRP6 group.
7. Configure another virtual IPv6 address for the VRRP6 group.
   ```
   [vrrp6 vrid](cmdqueryname=vrrp6+vrid) virtual-router-id virtual-ip virtual-ipv6-address
   ```
   
   Multiple virtual IPv6 addresses can be assigned to a VRRP6 group. A single virtual IPv6 address serves a separate user group, in which users have the same reliability requirements. This setting helps prevent the default gateway addresses from varying according to changes in VRRP6 device locations.
8. Configure a priority for each device in the VRRP6 group.
   ```
   [vrrp6 vrid](cmdqueryname=vrrp6+vrid) virtual-router-id priority priority-value
   ```
   
   The default value of *priority-value* is 100. The value ranges from 1 to 254.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * The priority configured for the master device must be higher than that for a backup device.
   * If devices in a VRRP6 group have the same priority, the device that enters the Master state the earliest becomes the master device. In addition, the other devices become backup devices and no longer preempt the master role.
9. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```