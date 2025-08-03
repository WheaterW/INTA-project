Adding an L2VE Interface to a BD
================================

You can add an L2VE interface to the BD so that EVPN VPLS services are terminated on the L2VE interface.

#### Context

Perform the following steps on each NPE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface)**virtual-ethernet** *interface-number*.*subinterface-number* **mode l2** or **[**interface**](cmdqueryname=interface)** **global-ve** *interface-number*.*subinterface-number* **mode l2**
   
   
   
   The L2VE sub-interface or global L2VE sub-interface view is displayed.
3. Run [**encapsulation**](cmdqueryname=encapsulation) { **dot1q** [ **vid** *low-pe-vid* [ **to** *high-pe-vid* ] ] | **untag** | **qinq** [ **vid** *pe-vid* **ce-vid** { *low-ce-vid* [ **to** *high-ce-vid* ] | **default** } ] }
   
   
   
   An encapsulation type of packets allowed to pass through the Layer 2 sub-interface is specified.
4. Run [**rewrite**](cmdqueryname=rewrite) **pop** { **single** | **double** }
   
   
   
   The traffic behavior is set to **pop** so that the Ethernet sub-interface removes VLAN tags from received packets.
   
   If the received packets each carry a single VLAN tag, specify **single**.
   
   If the encapsulation type of packets has been set to QinQ, specify **double** in this step to remove double VLAN tags from the received packets.
5. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
   
   
   
   The Layer 2 sub-interface is added to a BD so that the sub-interface can transmit data packets only through this BD.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.