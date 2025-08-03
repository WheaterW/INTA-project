Associating an L3VE Interface with a VPN Instance
=================================================

Configure an IP address for the L3VE sub-interface on each PE and bind the L3VE sub-interface to the corresponding VPN instance for L3VPN access.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface)**virtual-ethernet** *interface-number*.*subinterface-number*
   
   
   
   The VE interface view is displayed.
3. Run [**vlan-type dot1q**](cmdqueryname=vlan-type+dot1q) *vlan-id*
   
   
   
   The sub-interface is associated with a VLAN, and the VLAN encapsulation type is set to dot1q.
4. Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
   
   
   
   The sub-interface is bound to a VPN instance.
5. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
   
   
   
   A private IP address is configured for MPLS L3VPN.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.