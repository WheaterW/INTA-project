(Optional) Disabling DHCP Snooping on an Interface
==================================================

(Optional) Disabling DHCP Snooping on an Interface

#### Context

If DHCP snooping is enabled in a VLAN, DHCP snooping is enabled on all interfaces in the VLAN. To disable DHCP snooping on an interface, run the [**dhcp snooping disable**](cmdqueryname=dhcp+snooping+disable) command. After DHCP snooping is disabled on an interface, users can go online through this interface, but dynamic DHCP snooping binding entries are not generated for them.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Disable DHCP snooping on the interface.
   
   
   ```
   [dhcp snooping disable](cmdqueryname=dhcp+snooping+disable)
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```