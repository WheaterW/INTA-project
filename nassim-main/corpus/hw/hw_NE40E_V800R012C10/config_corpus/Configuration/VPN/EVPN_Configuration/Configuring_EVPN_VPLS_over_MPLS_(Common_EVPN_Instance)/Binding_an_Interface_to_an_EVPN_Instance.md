Binding an Interface to an EVPN Instance
========================================

After an interface is bound to an EVPN instance, the interface becomes a part of the EVPN. Packets entering the interface will then be forwarded based on forwarding entries in the EVPN instance.

#### Context

After an EVPN instance is configured on a device, the device's interface that belongs to the EVPN must be bound to the EVPN instance. Otherwise, the interface functions as a public network interface and cannot forward VPN traffic.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface to be bound to the EVPN instance is displayed. In a CE dual-homing scenario, the interface type is Eth-Trunk.
3. Run [**evpn binding vpn-instance**](cmdqueryname=evpn+binding+vpn-instance) *vpn-instance-name*
   
   
   
   The interface is bound to the EVPN instance.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.