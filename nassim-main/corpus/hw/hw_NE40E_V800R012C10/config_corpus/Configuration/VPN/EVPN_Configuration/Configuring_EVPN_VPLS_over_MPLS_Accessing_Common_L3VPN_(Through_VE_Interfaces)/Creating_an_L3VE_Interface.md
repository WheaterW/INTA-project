Creating an L3VE Interface
==========================

This section describes how to configure an L3VE interface to access an L3VPN and bind the L3VE interface to a VE-Group.

#### Context

Perform the following steps on each NPE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface)**virtual-ethernet** *interface-number* or **[**interface**](cmdqueryname=interface)** **global-ve** *interface-number*
   
   
   
   A VE interface or a global VE interface is created, and the VE interface view or global VE interface view is displayed.
3. Run [**ve-group**](cmdqueryname=ve-group) *ve-group-id* **l3-access**
   
   
   
   The VE interface or global VE interface is configured as an L3VE interface to access an L3VPN and is bound to a VE-Group.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * A VE-Group contains only one L2VE interface and one L3VE interface. Two VE interfaces in a VE-Group cannot reside on different boards.
   * Two global VE interfaces in a VE-Group can reside on different boards.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.