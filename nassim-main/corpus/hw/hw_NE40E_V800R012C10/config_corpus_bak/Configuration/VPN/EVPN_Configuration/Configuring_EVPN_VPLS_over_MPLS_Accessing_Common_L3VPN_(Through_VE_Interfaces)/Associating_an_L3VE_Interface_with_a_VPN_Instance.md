Associating an L3VE Interface with a VPN Instance
=================================================

This section describes how to configure an IP address for an L3VE sub-interface and bind it to a VPN instance to access L3VPN.

#### Context

Perform the following steps on each NPE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface)**virtual-ethernet** *interface-number*.*subinterface-number* or **[**interface**](cmdqueryname=interface)** **global-ve** *interface-number*.*subinterface-number*
   
   
   
   The L3VE sub-interface or global L3VE sub-interface view is displayed.
3. Run [**vlan-type dot1q**](cmdqueryname=vlan-type+dot1q) *vlan-id*
   
   
   
   A VLAN to be associated with the sub-interface is specified, and the VLAN encapsulation type is set to dot1q.
4. Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
   
   
   
   The sub-interface is bound to a VPN instance.
5. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
   
   
   
   A private network IP address is configured for the MPLS L3VPN.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.