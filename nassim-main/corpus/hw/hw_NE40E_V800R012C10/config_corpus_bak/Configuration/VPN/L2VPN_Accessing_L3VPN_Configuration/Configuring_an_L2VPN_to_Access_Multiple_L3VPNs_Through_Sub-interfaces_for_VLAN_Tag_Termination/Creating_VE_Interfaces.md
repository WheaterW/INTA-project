Creating VE Interfaces
======================

This section describes how to configure an L2VE interface for L2VPN termination and an L3VE interface for L3VPN access and bind the two VE interfaces to the corresponding VE group.

#### Context

Perform the following steps on NPEs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **virtual-ethernet** *interface-number* or [**interface**](cmdqueryname=interface) **global-ve** *ve-number*
   
   
   
   The VE interface view or Global-VE interface view is displayed.
3. Run either of the following commands based on required interface functions:
   
   
   * L2VE interface: Run the [**ve-group**](cmdqueryname=ve-group) *ve-group-id* **l2-terminate** command to configure the VE interface as an L2VE interface for L2VPN termination and bind it to the corresponding VE group.
   * L3VE interface: Run the [**ve-group**](cmdqueryname=ve-group) *ve-group-id* **l3-access** command to configure the VE interface as an L3VE interface for MPLS L3VPN access and bind it to the corresponding VE group.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The L2VPN can access the L3VPN only if the L2VE and L3VE interfaces are bound to the same VE group and reside on the same board.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.