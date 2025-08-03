Creating an L2VE Interface
==========================

This section describes how to configure an L2VE interface for L2VPN termination and bind the L2VE interface to a VE group.

#### Context

Perform the following steps on NPEs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Perform either of the following operations:
   
   
   * To create a VE interface and access the VE interface view, run the [**interface virtual-ethernet**](cmdqueryname=interface+virtual-ethernet) *interface-number* command.
   * To create a global VE interface and access the global VE interface view, run the [**interface global-ve**](cmdqueryname=interface+global-ve) *ve-number* command.
3. Run [**ve-group**](cmdqueryname=ve-group) *ve-group-id* **l2-terminate**
   
   
   
   The VE interface is configured as an L2VE interface for L2VPN termination and bound to the corresponding VE group.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * A VE group has only one L2VE interface and one L3VE interface.
   * In the VE interface view, the two VE interfaces in a VE group must be on the same board.
   * In the global VE interface view, the two VE interfaces in a VE group can be on different boards.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.