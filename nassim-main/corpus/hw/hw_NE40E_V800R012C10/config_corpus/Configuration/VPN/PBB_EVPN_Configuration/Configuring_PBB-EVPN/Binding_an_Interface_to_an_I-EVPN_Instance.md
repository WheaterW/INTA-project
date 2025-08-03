Binding an Interface to an I-EVPN Instance
==========================================

After an interface is bound to an I-EVPN instance, the
interface becomes a part of the provider backbone bridge (PBB-EVPN).
Packets entering the interface will then be forwarded based on PBB-EVPN
instance traffic forwarding entries.

#### Context

After an I-EVPN instance is configured on a provider edge
(PE), an interface that belongs to the I-EVPN instance must be bound
to the I-EVPN instance. Otherwise, the interface functions as a public
network interface and cannot forward PBB-EVPN traffic.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**evpn binding vpn-instance**](cmdqueryname=evpn+binding+vpn-instance) *vpn-instance-name*
   
   
   
   The interface is bound to an I-EVPN instance.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * In Single-Active mode, only an Eth-Trunk interface, Eth-Trunk
     VLAN-type Dot1q sub-interface, or Eth-Trunk VLAN tag termination sub-interface
     can be bound to an I-EVPN instance.
   * In Active-Active mode, only an Eth-Trunk interface with no sub-interfaces
     can be bound to an I-EVPN instance.
   * When a PE switches from the Active-Active mode to the Single-Active
     mode, the binding between the I-EVPN instance and interfaces remains
     unchanged.
   * If an Eth-Trunk has been bound to an I-EVPN instance on a PE,
     the PE cannot switch from the Single-Active mode to the Active-Active
     mode.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.