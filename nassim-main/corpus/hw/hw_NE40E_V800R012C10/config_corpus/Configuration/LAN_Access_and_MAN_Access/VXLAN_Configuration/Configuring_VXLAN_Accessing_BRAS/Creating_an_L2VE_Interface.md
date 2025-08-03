Creating an L2VE Interface
==========================

Configure an L2VE interface on the pUP to terminate VXLAN services and bind the interface to a VE group.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface virtual-ethernet**](cmdqueryname=interface+virtual-ethernet) *ve-number* or [**interface global-ve**](cmdqueryname=interface+global-ve) *ve-number*
   
   
   
   A VE or global VE interface is created, and its view is displayed.
3. Run [**ve-group**](cmdqueryname=ve-group) *ve-group-id* **l2-terminate**
   
   
   
   The VE or global VE interface is configured as an L2VE interface that terminates VXLAN services and bound to a VE group.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * A VE group can contain only one L2VE interface and one L3VE interface. The two VE interfaces in a VE group must reside on the same board.
   * The two global VE interfaces in a VE group can reside on different boards.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.