Configuring the Management Address and Gateway of the Device
============================================================

Configuring the Management Address and Gateway of the Device

#### Context

Each device on a network must have a globally unique management address, enabling O&M personnel to easily locate and log in to the device.

You can configure a management IP address for a management interface or a common interface. The IP address can be an IPv4 or IPv6 address. The following uses an IPv4 address as an example.


#### Procedure

* Configure a management IP address for the management interface.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the management interface view.
     
     
     ```
     interface meth 0/0/0
     ```
  3. Configure an IP address and a mask for the management interface.
     
     
     ```
     [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length }
     ```
  4. Return to the system view.
     
     
     ```
     [quit](cmdqueryname=quit)
     ```
  5. Configure a route on the device. 
     
     
     ```
     [ip route-static](cmdqueryname=ip+route-static) ip-address { mask | mask-length } nexthop-address
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     Run the **display this** command in the management interface view to check whether the management interface is in **\_management\_vpn\_** by default. If so, run the [**ip route-static**](cmdqueryname=ip+route-static) **vpn-instance** **\_management\_vpn\_** *destination-address* { *mask* | *mask-length* } *nexthop-address* command to configure a route for the device.
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure a management IP address for a common interface.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create a VLAN for the management network.
     
     
     ```
     [vlan](cmdqueryname=vlan) vlan-id
     ```
  3. Return to the system view.
     
     
     ```
     [quit](cmdqueryname=quit)
     ```
  4. Enter the VLANIF interface view.
     
     
     ```
     [interface vlanif](cmdqueryname=interface+vlanif) vlan-id
     ```
  5. Configure an IP address and a mask for the VLANIF interface.
     
     
     ```
     [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length }
     ```
  6. Return to the system view.
     
     
     ```
     [quit](cmdqueryname=quit)
     ```
  7. Enter the view of the service interface used for management.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  8. Switch the interface working mode to Layer 2.
     
     
     ```
     [portswitch](cmdqueryname=portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  9. Set the link type of the interface to access.
     
     
     ```
     [port link-type](cmdqueryname=port+link-type) access
     ```
  10. Configure a VLAN as the default VLAN of the interface and add the interface to the VLAN.
      
      
      ```
      [port default vlan](cmdqueryname=port+default+vlan) vlan-id
      ```
  11. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
  12. Configure a route on the device.
      
      
      ```
      [ip route-static](cmdqueryname=ip+route-static) ip-address { mask | mask-length } nexthop-address
      ```
  13. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```