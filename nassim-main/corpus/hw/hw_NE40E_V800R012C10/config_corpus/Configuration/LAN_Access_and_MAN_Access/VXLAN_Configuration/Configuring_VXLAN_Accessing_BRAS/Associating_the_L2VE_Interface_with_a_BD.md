Associating the L2VE Interface with a BD
========================================

Associate the L2VE interface with a BD on the pUP, so that VXLAN services can be terminated on the L2VE interface.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface virtual-ethernet**](cmdqueryname=interface+virtual-ethernet) *ve-number*.*subinterface-number* **mode l2** or [**interface global-ve**](cmdqueryname=interface+global-ve) *ve-number*.*subinterface-number* **mode l2**
   
   
   
   The VE or global VE Layer 2 sub-interface view is displayed.
3. Run [**encapsulation**](cmdqueryname=encapsulation) { **dot1q** [ **vid** *low-pe-vid* [ **to** *high-pe-vid* ] ] | **untag** | **qinq** [ **vid** *pe-vid* **ce-vid** { *low-ce-vid* [ **to** *high-ce-vid* ] | **default** } ] }
   
   
   
   A packet encapsulation type is configured, so that a specific type of interface can transmit data packets of the specified encapsulation type.
4. Run [**rewrite pop**](cmdqueryname=rewrite+pop) { **single** | **double** }
   
   
   
   The function to remove VLAN tags from received packets is enabled.
   
   
   
   For single-tagged packets received by the Layer 2 sub-interface, specify **single** to enable the sub-interface to remove the VLAN tag from each packet.
   
   If the packet encapsulation type is set to QinQ in the previous step, specify **double** to enable the sub-interface to remove double VLAN tags from each double-tagged packet received.
5. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
   
   
   
   The Layer 2 sub-interface is associated with a BD, so that the sub-interface can forward packets through the BD.
   
   
   
   The BD must have been associated with a VNI in the VXLAN configuration.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.