Binding an Interface to a VPN Instance
======================================

By binding an interface to a VPN instance, you can change
the interface to be a VPN interface. Then, packets entering this interface
are forwarded according to the forwarding information of the VPN instance.

#### Context

The configuration on the Hub-PE involves two interfaces
or sub-interfaces:

* One is bound to VPN-in for receiving the routes advertised
  by Spoke-PEs.
* One is bound to VPN-out for advertising the routes of all the
  hub sites and spoke sites.

If a Hub-PE and a Hub-CE are connected through a single link, one interface or sub-interface on the Hub-PE is bound to the VPN instance vpnhub.

Perform the following steps on the Hub-PE and all the Spoke-PEs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
   
   
   
   The interface
   is bound to the VPN instance.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the [**ip binding
   vpn-instance**](cmdqueryname=ip+binding+vpn-instance) command is run on an interface, the
   Layer 3 features such as the IP address and routing protocol configured
   on the interface are deleted.
4. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
   
   
   
   An IP address is configured for the interface.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is
   committed.