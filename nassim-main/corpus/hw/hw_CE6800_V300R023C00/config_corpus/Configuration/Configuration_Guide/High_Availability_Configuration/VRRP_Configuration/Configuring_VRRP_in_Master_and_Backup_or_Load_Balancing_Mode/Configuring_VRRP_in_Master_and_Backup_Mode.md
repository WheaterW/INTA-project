Configuring VRRP in Master/Backup Mode
======================================

Configuring VRRP in Master/Backup Mode

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
4. Create a VRRP group and configure a virtual IP address for it.
   ```
   [vrrp vrid](cmdqueryname=vrrp+vrid) virtual-router-id virtual-ip virtual-address
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   * The virtual IP addresses of VRRP groups must be unique.
   * Two devices in a VRRP group must be configured with the same VRID.
   * VRRP groups on different interfaces of a device can be configured with the same VRID.
   
   Multiple virtual IP addresses can be configured for a VRRP group to serve different user groups, whereas a single virtual IP address serves a separate user group in which users have the same reliability requirements. This configuration facilitates user management and prevents the default gateway address on the user side from changing with VRRP configurations.
   
   You can specify a virtual IP address for a VRRP group when you create the VRRP group. If another virtual IP address is specified for the VRRP group later, the system adds the virtual IP address to the virtual IP address list for the VRRP group.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Direct routes destined for virtual IP addresses of a VRRP group can be imported to OSPF, IS-IS, and RIP. By default, such routes can be advertised to neighbors through these protocols. On a live network, there may be a large number of routes destined for virtual IP addresses of VRRP groups; therefore, if OSPF, IS-IS, or RIP imports and advertises these routes to neighbors, some devices on the network may be overloaded, and network performance may be impacted. To resolve this issue, run the **[**vrrp virtual-ip route-advertise disable**](cmdqueryname=vrrp+virtual-ip+route-advertise+disable)** { **isis** | **ospf** | **rip** }\* command to disable OSPF, IS-IS, and RIP from advertising the routes destined for virtual IP addresses of VRRP groups to neighbors.
5. Configure a priority for each device in the VRRP group.
   ```
   [vrrp vrid](cmdqueryname=vrrp+vrid) virtual-router-id priority priority-value
   ```
   
   The default value of *priority-value* is 100.
   
   VRRP assigns roles to devices in a VRRP group according to their priorities. A device with a higher priority is more likely to be elected as the master device. Therefore, you can specify a device as the master device to forward traffic by configuring a higher priority for the device.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * The master device's priority must be higher than the priority of a backup device. It is recommended that you use the default priority on a backup device.
   * If devices in a VRRP group have the same VRRP priority, the device that enters the Master state the earliest becomes the master device. In addition, the other devices become backup devices and no longer preempt the master role.
6. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```