Creating a VE Interface
=======================

This section describes how to configure an L2VE interface that terminates L2VPN and an L3VE interface that provides access to L2VPN, and how to bind the VE interfaces to the corresponding VE group.

#### Context

Perform the following steps on NPEs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **virtual-ethernet** *interface-number* or [**interface**](cmdqueryname=interface) **global-ve** *ve-number*
   
   
   
   A VE or global VE interface is created, and its view is displayed.
3. Perform either of the following operations based on required interface functions:
   
   
   * L2VE interface: Run the [**ve-group**](cmdqueryname=ve-group) *ve-group-id* **l2-terminate** command to configure the VE interface as an L2VE interface that terminates L2VPN and bind the interface to a VE group.
   * L3VE interface: Run the [**ve-group**](cmdqueryname=ve-group) *ve-group-id* **l3-access** command to configure the VE interface as an L3VE interface that provides access to MPLS L2VPN and bind the interface to a VE group.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The L2VE interface and L3VE interface must be in the same VE group and on the same board.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.