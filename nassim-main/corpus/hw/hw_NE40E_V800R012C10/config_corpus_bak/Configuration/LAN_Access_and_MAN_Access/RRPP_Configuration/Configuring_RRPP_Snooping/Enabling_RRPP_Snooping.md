Enabling RRPP Snooping
======================

After being enabled with RRPP Snooping, an interface can detect the RRPP ring status through RRPP control packets. In addition, when the RRPP ring status changes, the interface notifies the bound virtual switch instance (VSI) to update the MAC address table.

#### Context

Perform the following steps on the NPEs at the border of the RRPP ring and the VPLS network:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Choose one of the following commands to enter the view of the interface to be enabled with RRPP snooping.
   
   
   * Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number.subinterface-number* command to enter the sub-interface view.
     
     The sub-interface in this step must be configured with the control VLAN of RRPP using the [**vlan-type dot1q**](cmdqueryname=vlan-type+dot1q) or [**dot1q termination vid**](cmdqueryname=dot1q+termination+vid) *low-pe-vid* command.
   * Run the [**interface**](cmdqueryname=interface) **vlanif** *vlan-id* command to enter the specified VLANIF interface view.
     
     The number of the VLANIF interface must be consistent with to the control VLAN ID of RRPP.
3. Run [**l2 binding**](cmdqueryname=l2+binding) [**vsi**](cmdqueryname=vsi) *vsi-name*
   
   
   
   The sub-interface or VLANIF interface is bound to the VSI.
4. Run [**rrpp snooping enable**](cmdqueryname=rrpp+snooping+enable)
   
   
   
   RRPP snooping is enabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.