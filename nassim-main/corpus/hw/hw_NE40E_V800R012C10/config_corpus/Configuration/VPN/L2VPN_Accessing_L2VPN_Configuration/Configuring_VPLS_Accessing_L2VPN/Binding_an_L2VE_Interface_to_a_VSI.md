Binding an L2VE Interface to a VSI
==================================

After an L2VE interface is bound to a VSI, the L2VE interface can be considered as an attachment circuit (AC) interface.

#### Context

Perform the following steps on NPEs.


#### Procedure

1. Configure a VLAN for an L2VE sub-interface and bind the sub-interface to a VSI.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**interface**](cmdqueryname=interface) **virtual-ethernet** *interface-number.subinterface-number* command to enter the L2VE sub-interface view.
   3. Run the [**vlan-type**](cmdqueryname=vlan-type) **dot1q** *vlan-id* command to configure a VLAN ID for the L2VE sub-interface.
   4. Run the [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name* command to bind the L2VE interface to a VSI.
   5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
2. Configure a VLAN range for an L2VE sub-interface and bind the sub-interface to a VSI.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**interface**](cmdqueryname=interface) **virtual-ethernet** *interface-number.subinterface-number* command to enter the L2VE sub-interface view.
   3. Run the [**encapsulation**](cmdqueryname=encapsulation) **dot1q-termination** [ **rt-protocol** ] command to configure a VLAN tag termination type for the sub-interface.
   4. Run the [**vlan-group**](cmdqueryname=vlan-group) *group-id* command to create a user VLAN group.
   5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   6. Run the [**quit**](cmdqueryname=quit) command to exit the VLAN group view.
   7. If the L2VE sub-interface is associated with multiple VLANs, run the [**dot1q termination vid**](cmdqueryname=dot1q+termination+vid) *low-pe-vid* [ **to** *high-pe-vid* ] [ **vlan-group** *group-id* ] command to configure a VLAN range for the L2VE sub-interface.
   8. Run the [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name* command to bind the L2VE interface to a VSI.
   9. (Optional) Run the [**dot1q termination client-mode single**](cmdqueryname=dot1q+termination+client-mode+single) command to enable a dot1q VLAN tag termination sub-interface to deliver only one leaf for the replication of one copy of broadcast traffic when the sub-interface provides access for qualify-mode VPLS services.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) Before running the [**dot1q termination client-mode single**](cmdqueryname=dot1q+termination+client-mode+single) command, ensure that:
      * A dot1q VLAN tag termination sub-interface has been configured.
      * The dot1q VLAN tag termination sub-interface has been bound to a qualify-mode VSI (namely, the [**mac-learn-style qualify**](cmdqueryname=mac-learn-style+qualify) command has been run for the VSI).
   10. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.