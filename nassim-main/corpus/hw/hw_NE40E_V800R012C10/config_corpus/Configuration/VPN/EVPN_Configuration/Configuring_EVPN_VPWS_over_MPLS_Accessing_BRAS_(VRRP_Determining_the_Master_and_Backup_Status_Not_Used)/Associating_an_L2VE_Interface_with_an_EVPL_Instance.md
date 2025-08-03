Associating an L2VE Interface with an EVPL Instance
===================================================

After an L2VE interface is associated with an EVPL instance on a BNG, E-Line services can be terminated on the L2VE interface.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface virtual-ethernet**](cmdqueryname=interface+virtual-ethernet) *interface-number*.*subinterface-number* or [**interface global-ve**](cmdqueryname=interface+global-ve) *interface-number*.*subinterface-number*
   
   
   
   The VE or global VE Layer 2 sub-interface view is displayed.
3. Run [**encapsulation**](cmdqueryname=encapsulation) { **dot1q** [ **vid** *low-pe-vid* [ **to** *high-pe-vid* ] ] | **untag** | **qinq** [ **vid** *pe-vid* **ce-vid** { *low-ce-vid* [ **to** *high-ce-vid* ] | **default** } ] }
   
   
   
   The encapsulation type of packets allowed to pass through the Layer 2 sub-interface is specified.
4. Run [**rewrite pop**](cmdqueryname=rewrite+pop) { **single** | **double** }
   
   
   
   The function to remove VLAN tags from received packets is enabled.
   
   
   
   For single-tagged packets received by the Layer 2 sub-interface, specify **single** to enable the sub-interface to remove the VLAN tag from each packet.
   
   If the packet encapsulation type is set to QinQ in the previous step, specify **double** to enable the sub-interface to remove double VLAN tags from each double-tagged packet received.
5. Run [**evpl instance**](cmdqueryname=evpl+instance) *evpl-id*
   
   
   
   The Layer 2 sub-interface is bound to an EVPL instance.
6. (Optional) Run [**evpn-vpws ignore-ac-state**](cmdqueryname=evpn-vpws+ignore-ac-state)
   
   
   
   The Layer 2 sub-interface is enabled to ignore the AC status.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.