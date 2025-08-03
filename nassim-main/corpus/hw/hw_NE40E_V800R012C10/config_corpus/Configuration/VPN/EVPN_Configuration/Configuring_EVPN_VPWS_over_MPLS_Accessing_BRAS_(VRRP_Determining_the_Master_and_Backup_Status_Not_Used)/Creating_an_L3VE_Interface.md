Creating an L3VE Interface
==========================

Configure an L3VE interface on each BNG for BRAS service access and bind the L3VE interface to a VE group.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface virtual-ethernet**](cmdqueryname=interface+virtual-ethernet) *interface-number* or [**interface global-ve**](cmdqueryname=interface+global-ve) *interface-number*
   
   
   
   A VE or global VE interface is created, and its view is displayed.
3. Run [**ve-group**](cmdqueryname=ve-group) *ve-group-id* **l3-access**
   
   
   
   The VE interface or global VE interface is configured as an L3VE interface for BRAS service access and bound to a VE group.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The VE group contains only one L2VE interface and one L3VE interface. The two VE interfaces in a VE group must be on the same board.
   * The two global VE interfaces in a VE group can reside on different boards.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.