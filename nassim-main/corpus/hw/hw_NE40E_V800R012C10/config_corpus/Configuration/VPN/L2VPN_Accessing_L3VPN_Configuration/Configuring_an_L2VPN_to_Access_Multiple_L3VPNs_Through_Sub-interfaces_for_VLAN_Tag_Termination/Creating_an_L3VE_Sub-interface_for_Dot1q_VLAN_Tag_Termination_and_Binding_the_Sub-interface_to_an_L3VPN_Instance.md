Creating an L3VE Sub-interface for Dot1q VLAN Tag Termination and Binding the Sub-interface to an L3VPN Instance
================================================================================================================

If an L3VE sub-interface receives single-tagged service data packets from the UPE, configure the L3VE sub-interface as a dot1q VLAN tag termination sub-interface for L3VPN access.

#### Context

Perform the following steps on NPEs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface virtual-ethernet**](cmdqueryname=interface+virtual-ethernet) *interface-number* *interface-number*
   
   
   
   An L3VE sub-interface is created, and its view is displayed.
3. Run [**control-vid**](cmdqueryname=control-vid) *vid* **dot1q-termination**
   
   
   
   The encapsulation type of the sub-interface is configured as dot1q VLAN tag termination.
4. Run [**dot1q termination vid**](cmdqueryname=dot1q+termination+vid) *low-pe-vid* [ **to** *high-pe-vid* ]
   
   
   
   The dot1q VLAN tag termination function is configured for the L3VE sub-interface.
5. Run [**arp broadcast enable**](cmdqueryname=arp+broadcast+enable)
   
   
   
   ARP broadcast is enabled for the VLAN tag termination sub-interface.
   
   
   
   When ARP broadcast is enabled or disabled on the sub-interface, the routing status on the sub-interface alternates between down and up. This may result in route flapping on the entire network, affecting the normal operation of services.
6. Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
   
   
   
   The L3VE sub-interface is bound to a VPN instance.
7. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
   
   
   
   An IP address is configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The IP address is a private network address of the MPLS L3VPN.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.