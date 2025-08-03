(Optional) Disabling a Device from Generating Dynamic Binding Entries on Interfaces
===================================================================================

(Optional) Disabling a Device from Generating Dynamic Binding Entries on Interfaces

#### Context

After DHCP snooping is enabled on a device, the device generates DHCP snooping binding entries for users by default. If the number of binding entries on the device reaches the upper limit, new users cannot go online. If you do not want to limit the number of online users but want to record user location information, you can disable the device from generating DHCP snooping binding entries on interfaces.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Disable the device from generating binding entries. If this function is configured in the interface view, it takes effect for all DHCP users on the interface. If this function is configured in the VLAN view, it takes effect for all DHCP users belonging to the VLAN on all interfaces. If this function is configured in the system view, it takes effect in the same way as if it were configured in the VLAN view, except that multiple VLANs can be specified.
   
   
   * Disable the device from generating binding entries in the system view.
     ```
     [dhcp snooping enable no-user-binding](cmdqueryname=dhcp+snooping+enable+no-user-binding) vlan { vlan-id1 [ [to](cmdqueryname=to) vlan-id2 ] } &<1-10>
     ```
   * Enter the VLAN view and disable the device from generating binding entries for the specified VLAN.
     ```
     [vlan](cmdqueryname=vlan) vlan-id
     [dhcp snooping enable no-user-binding](cmdqueryname=dhcp+snooping+enable+no-user-binding)
     [quit](cmdqueryname=quit)
     ```
   * Enter the interface view and disable the device from generating binding entries for the specified interface.
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     portswitch
     [dhcp snooping enable no-user-binding](cmdqueryname=dhcp+snooping+enable+no-user-binding)
     [quit](cmdqueryname=quit)
     ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```