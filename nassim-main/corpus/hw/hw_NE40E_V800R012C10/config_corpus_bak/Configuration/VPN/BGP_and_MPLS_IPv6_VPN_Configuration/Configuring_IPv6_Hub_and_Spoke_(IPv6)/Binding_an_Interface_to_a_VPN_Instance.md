Binding an Interface to a VPN Instance
======================================

By binding an interface to a VPN instance, you can change the interface to a VPN interface. Then, packets entering this interface are forwarded according to the forwarding information of the VPN instance.

#### Context

The configuration on the Hub-PE involves two interfaces or sub-interfaces:

* One is bound to VPN-in for receiving the routes advertised by Spoke-PEs.
* One is bound to VPN-out for advertising the routes of all the Hub sites and Spoke sites.

Perform the following steps on the Hub-PE and all the Spoke-PEs:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface to be bound to the VPN instance is displayed.
3. Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
   
   The interface is bound to a VPN instance.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) command is run on an interface, the Layer 3 features such as the IP address and routing protocol configured on the interface are deleted.
4. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is enabled on the interface.
5. Run [**ipv6 address**](cmdqueryname=ipv6+address) { *ipv6-address* *prefix-length* | *ipv6-address* *prefix-length* }
   
   
   
   An IPv6 address is configured for the interface.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.