Creating an L2VE Interface
==========================

Configure an L2VE interface on each PE to terminate EVPN VPWS and bind the L2VE interface to a VE group.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface virtual-ethernet**](cmdqueryname=interface+virtual-ethernet) *interface-number*
   
   
   
   A VE interface is created, its view is displayed.
3. Run [**ve-group**](cmdqueryname=ve-group) *ve-group-id* **l2-terminate**
   
   
   
   The VE interface is configured as an L2VE interface that terminates EVPN VPWS and bound to a VE group.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A VE group contains only one L2VE interface and one L3VE interface. The two VE interfaces in a VE group must be on the same board.
4. Run [**esi**](cmdqueryname=esi) *esi*
   
   
   
   An ESI is configured.
   
   
   
   After an ESI is configured for PEs' L2VE interfaces connected to M-AGGs, PE1 and PE2 can obtain each other's ESI through route advertisement and detect that M-AGGs are dual-homed to them.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.