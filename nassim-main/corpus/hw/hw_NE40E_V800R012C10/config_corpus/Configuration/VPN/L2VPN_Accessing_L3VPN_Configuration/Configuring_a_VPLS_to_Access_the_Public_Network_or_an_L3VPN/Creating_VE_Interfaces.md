Creating VE Interfaces
======================

This part describes how to configure an L2VE interface that terminates the L2VPN and configure an L3VE interface that access L3VPN, and how to bind the VE interfaces to the relevant VE-Group.

#### Context

Do as follows on NPEs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **virtual-ethernet** *interface-number* or [**interface**](cmdqueryname=interface) **global-ve** *ve-number*
   
   
   
   The VE interface view or Global-VE interface view is displayed.
3. Run either of the following commands as needed:
   
   
   * If the interface is an L2VE interface:
     
     ```
     [ve-group](cmdqueryname=ve-group) ve-group-id l2-terminate
     ```
     
     The VE interface is set to an L2VE interface that terminates L2VPN, and the interface is bound to a VE-Group.
   * If the interface is an L3VE interface:
     
     ```
     [ve-group](cmdqueryname=ve-group) ve-group-id l3-access
     ```
     
     The VE interface is set to an L3VE interface that accesses the MPLS L3VPN, and it is bound to a VE-Group.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The L2VE interface and L3VE interface in the same VE-Group must be on the same board.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.