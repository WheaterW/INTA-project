Configuring the Access to the Public Network or an L3VPN
========================================================

This section describes how to configure an IP address for an L3VE sub-interface and bind the sub-interface to a VPN for public network or L3VPN access.

#### Context

Perform the following steps on NPEs.


#### Procedure

* Configure a network-side user to access the public network.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface virtual-ethernet**](cmdqueryname=interface+virtual-ethernet) *interface-number interface-number*
     
     
     
     The L3VE sub-interface view is displayed.
  3. Run [**vlan-type**](cmdqueryname=vlan-type) **dot1q** *vlan-id*
     
     
     
     The VLAN ID of the L3VE sub-interface is configured.
  4. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
     
     
     
     An IP address is configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The IP address is a public network IP address.
  5. Configure a routing protocol for route exchange with devices accessing the MPLS L2VPN.
     
     
     
     For details, see NE40E Configuration Guide > IP Routing.
  6. (Optional) Run [**mpls l2vpn l3ve delay-up**](cmdqueryname=mpls+l2vpn+l3ve+delay-up) *time*
     
     
     
     A delay for the L3VE interface to go up after the faulty L2VPN service recovers is configured.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configuring a user to access the MPLS L3VPN network
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface virtual-ethernet**](cmdqueryname=interface+virtual-ethernet) *interface-number* *interface-number*
     
     
     
     The L3VE interface view is displayed.
  3. Run [**vlan-type**](cmdqueryname=vlan-type) **dot1q** *vlan-id*
     
     
     
     The VLAN ID of the L3VE sub-interface is configured.
  4. Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
     
     
     
     The L3VE interface is bound to a VPN instance.
  5. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
     
     
     
     An IP address is configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The IP address is a private network address of the MPLS L3VPN.
  6. (Optional) Run [**mpls l2vpn l3ve delay-up**](cmdqueryname=mpls+l2vpn+l3ve+delay-up) *time*
     
     
     
     A delay for the L3VE interface to go up after the faulty L2VPN service recovers is configured.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.