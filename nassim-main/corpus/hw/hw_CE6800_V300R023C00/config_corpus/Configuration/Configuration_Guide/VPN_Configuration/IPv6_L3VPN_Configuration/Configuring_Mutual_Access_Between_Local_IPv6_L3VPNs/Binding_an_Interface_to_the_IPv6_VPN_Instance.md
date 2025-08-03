Binding an Interface to the IPv6 VPN Instance
=============================================

Binding an Interface to the IPv6 VPN Instance

#### Prerequisites

A VPN instance has been created, and the IPv6 address family has been enabled for the VPN instance.


#### Context

If the interface belonging to a VPN instance is not bound to the VPN instance, the interface functions as a public network interface and cannot forward VPN data.

An interface becomes a VPN interface after being bound to a VPN instance. You must configure an IP address for the interface, so that the PE can exchange routing information with its connected CE through this interface.

After an interface is bound to a VPN instance, Layer 3 configurations, such as IP address and routing protocol configurations, are deleted from the interface.

After you disable an address family in the VPN instance, the corresponding address configuration is deleted from the interface. If no address family configuration exists in the VPN instance, the interface is unbound from the VPN instance.

![](public_sys-resources/note_3.0-en-us.png) 

Loopback interfaces can be bound to VPN instances for connectivity testing between VPNs, under the prerequisite that VLANIF or physical interfaces have been bound to the VPN instances prior to loopback interfaces. In actual service scenarios, a specific VLANIF, physical, or tunnel interface must be bound to a VPN instance.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of the interface to be bound to a VPN instance.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Bind the interface to a VPN instance.
   
   
   ```
   [ip binding vpn-instance](cmdqueryname=ip+binding+vpn-instance) vpn-instance-name
   ```
   
   By default, an interface functions as a public network interface that is not bound to any VPN instance.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Running the [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) command on an interface deletes Layer 3 (including IPv4 and IPv6) configurations, such as IP address and routing protocol configurations, on the interface. If needed, reconfigure them after running the command.
5. Enable IPv6 on the interface.
   
   
   ```
   [ipv6 enable](cmdqueryname=ipv6+enable)
   ```
6. Configure an IPv6 address for the interface.
   
   
   ```
   [ipv6 address](cmdqueryname=ipv6+address) { ipv6-address prefix-length | ipv6-address/prefix-length }
   ```
   
   Some Layer 3 features, such as route exchange between the PE and CE, can be configured only after an IPv6 address is configured for the VPN interface on the PE.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```