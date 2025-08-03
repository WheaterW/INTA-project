Associating an L2VE Interface with a BD
=======================================

Associate an L2VE interface with a BD on a vBRAS-pUP so that E-LAN services can be terminated on the L2VE interface.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run either of the following commands:
   
   
   * To enter the VE Layer 2 sub-interface view, run the [**interface virtual-ethernet**](cmdqueryname=interface+virtual-ethernet) *interface-number*.*subinterface-number* command.
   * To enter the global VE Layer 2 sub-interface view, run the [**interface global-ve**](cmdqueryname=interface+global-ve) *interface-number*.*subinterface-number* command.
3. Run [**encapsulation**](cmdqueryname=encapsulation) { **dot1q** [ **vid** *low-pe-vid* [ **to** *high-pe-vid* ] ] | **untag** | **qinq** [ **vid** *pe-vid* **ce-vid** { *low-ce-vid* [ **to** *high-ce-vid* ] | **default** } ] }
   
   
   
   The encapsulation type of packets allowed to pass through the Layer 2 sub-interface is specified.
4. Run [**rewrite pop**](cmdqueryname=rewrite+pop) { **single** | **double**}
   
   
   
   The vBRAS-pUP is configured to remove VLAN tags from received packets.
   
   
   
   If the flow encapsulation type of packets is set to **dot1q**, specify **single** for the sub-interface to remove the tag from each received single-tagged packet.
   
   If the flow encapsulation type of packets is set to QinQ, specify **double** in this step for the sub-interface to remove double VLAN tags from each received double-tagged packet.
5. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
   
   
   
   The Layer 2 sub-interface is associated with a BD so that the sub-interface can forward packets through the BD.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.