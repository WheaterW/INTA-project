(Optional) Disabling Location Transition for DHCP Snooping Users
================================================================

(Optional) Disabling Location Transition for DHCP Snooping Users

#### Context

If a mobile user goes online through interface A, goes offline, and then goes online through interface B, the user sends a DHCPDISCOVER message to apply for an IP address. By default, if DHCP snooping is enabled on the device, the device allows the user to go online and updates the DHCP snooping binding table. However, this brings security risks in some scenarios. For example, if an attacker pretends to be an authorized user and sends a DHCPDISCOVER message, the device updates the DHCP snooping binding and the authorized user can no longer access the network. In this case, you need to disable location transition for DHCP snooping users. After this function is disabled, the device discards DHCPDISCOVER messages sent by a user who has an entry in the DHCP snooping binding table (the user's MAC address exists in the table) through another interface.

![](../public_sys-resources/note_3.0-en-us.png) 

Interface A and interface B must belong to the same VLAN.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Disable location transition for DHCP snooping users.
   
   
   ```
   [undo dhcp snooping user-transfer enable](cmdqueryname=undo+dhcp+snooping+user-transfer+enable)
   ```
   
   By default, location transition is enabled for DHCP snooping users.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```