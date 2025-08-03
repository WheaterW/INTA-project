(Optional) Configuring the VSI Associated with RRPP Snooping
============================================================

This part describes how to associate the sub-interface or VLANIF interface enabled with RRPP Snooping with other virtual switch instances (VSIs) related to the device. Therefore, the interface can inform the associated VSIs of the change in the RRPP ring status so that the VSIs can upgrade their MAC address tables accordingly.

#### Context

Perform the following steps on the NPE nodes at the border of an RRPP ring and a VPLS network:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run either of the following commands:
   
   
   * To enter the sub-interface view, run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number.subinterface-number* command.
     
     RRPP snooping must have been enabled on the sub-interface using the [**rrpp snooping enable**](cmdqueryname=rrpp+snooping+enable) command.
   * To enter the specified VLANIF interface view, run the [**interface**](cmdqueryname=interface) **vlanif** *vlan-id* command.
     
     The number of the VLANIF interface must be consistent with the control VLAN ID of RRPP.
3. Run either of the following commands:
   
   
   * To enter the sub-interface or VLANIF interface view and associate a VSI with RRPP snooping, run the [**rrpp snooping vsi**](cmdqueryname=rrpp+snooping+vsi) *vsi-name* command.
   * To enter the sub-interface and associate the VSIs of all the other sub-interfaces on the same main interface as the existing sub-interface with RRPP snooping, run the [**rrpp snooping all-vsi**](cmdqueryname=rrpp+snooping+all-vsi) command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.