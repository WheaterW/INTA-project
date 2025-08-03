Creating the L3VE Sub-interface Terminated by QinQ
==================================================

If an L3VE sub-interface receives double-tagged service data packets from the UPE, configure the L3VE sub-interface as a sub-interface for QinQ VLAN tag termination to access the L3VPN.

#### Context

Do as follows on NPEs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface virtual-ethernet**](cmdqueryname=interface+virtual-ethernet) *interface-number interface-number*
   
   
   
   A L3VE sub-interface is created the sub-interface view is displayed.
   
   You can create sub-interfaces only on the L3VE interface that operates in user termination mode.
3. Run [**control-vid**](cmdqueryname=control-vid) *vid* **qinq-termination**
   
   
   
   The sub-interface is encapsulated into the QinQ termination mode.
4. Run [**qinq termination pe-vid**](cmdqueryname=qinq+termination+pe-vid) *pe-vid* [ **to** *high-pe-vid* ] **ce-vid** *ce-vid* [ **to** *high-ce-vid* ] [ **vlan-group** *group-id* ]
   
   
   
   The QinQ termination is configured for the L3VE sub-interface.
   
   When the L3VE sub-interface receives packets with double tags from users, it will terminate the packets whose inner tag is in the range specified by the **ce-vid**.
5. Run [**arp broadcast enable**](cmdqueryname=arp+broadcast+enable)
   
   
   
   The ARP broadcast function is enabled for the sub-interface for QinQ VLAN tag termination.
   
   When you enable or disable the ARP broadcast function on a termination sub-interface, the routing status of the sub-interface becomes Down and then Up. This may result in a flapping of routes on the entire network, affecting the normal operation of services.
6. Run [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name*
   
   
   
   The L3VE sub-interface is associated with a VPN instance.
7. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
   
   
   
   The IP address is configured.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The IP address is a private network address of MPLS L3VPN.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.