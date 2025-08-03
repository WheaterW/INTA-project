Binding an Interface to an IPv4 VPN Instance
============================================

Binding an Interface to an IPv4 VPN Instance

#### Prerequisites

A VPN instance has been created and the IPv4 address family has been enabled for the VPN instance.


#### Context

If the interface belonging to the VPN is not bound to the VPN instance, the interface functions as a public network interface and cannot forward VPN data.

An interface bound to a VPN instance becomes a VPN interface on a PE and must be assigned an IP address so that the PE can exchange routes with its connected CE.

After an interface is bound to a VPN instance, Layer 3 features, such as the IP address and routing protocol configured on the interface, are deleted.

When an address family in a VPN instance is disabled, the configuration of this address family on the interface is deleted; if no address family is configured for a VPN instance, the interface is unbound from the VPN instance.

![](public_sys-resources/note_3.0-en-us.png) 

Binding a VPN instance to a loopback interface is usually used to test whether VPNs can communicate with each other. The prerequisite is that the VPN instance has been bound to a VLANIF interface or physical interface. In actual service applications, a VPN instance must be bound to a VLANIF interface, physical interface, or tunnel interface.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of the interface to be bound to the VPN instance.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
4. Bind the interface to a VPN instance.
   
   
   ```
   [ip binding vpn-instance](cmdqueryname=ip+binding+vpn-instance) vpn-instance-name
   ```
   
   By default, an interface functions as a public network interface and is not bound to any VPN instance.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Running the [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) command deletes Layer 3 (including IPv4 and IPv6) configurations, such as IP address and routing protocol configurations, on the involved interface. If needed, reconfigure them after running the command.
5. Configure an IP address for the interface.
   
   
   ```
   [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length }
   ```
   
   After an IP address is configured for the VPN interface, certain Layer 3 features, such as route exchange, can be configured between the PE and CE.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```