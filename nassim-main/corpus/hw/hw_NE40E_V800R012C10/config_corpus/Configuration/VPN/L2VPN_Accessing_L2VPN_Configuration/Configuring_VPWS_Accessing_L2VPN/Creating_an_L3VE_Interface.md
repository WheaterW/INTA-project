Creating an L3VE Interface
==========================

This section describes how to configure an L3VE interface to access an L2VPN and bind the L3VE interface to a VE group.

#### Context

Perform the following steps on NPEs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface virtual-ethernet**](cmdqueryname=interface+virtual-ethernet) *interface-number*
   
   
   
   A VE interface is created, and its view is displayed.
3. Run [**ve-group**](cmdqueryname=ve-group) *ve-group-id* **l3-access**
   
   
   
   The VE interface is configured as an L3VE interface that provides access to L2VPN and bound to a VE group.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A VE group can contain only one L2VE interface and one L3VE interface. The two VE interfaces in a VE group must be on the same board. Only the L3VE interface can work in QinQ or dot1q VLAN tag termination mode.
   
   If the two VE interfaces in a VE group are created using the [**interface global-ve**](cmdqueryname=interface+global-ve) command, they can be on different boards.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.