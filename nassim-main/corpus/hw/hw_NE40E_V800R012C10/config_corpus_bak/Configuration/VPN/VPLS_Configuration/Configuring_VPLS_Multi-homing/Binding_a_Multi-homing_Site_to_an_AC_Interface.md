Binding a Multi-homing Site to an AC Interface
==============================================

Configure an AC interface and bind a multi-homing site to the AC interface to implement VPLS multi-homing.

#### Context

After a multi-homing site is configured, bind it to an AC interface so that it can establish a PW with the PE housing the AC interface for carrying end-to-end services.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The AC interface view is displayed.
3. (Optional) Run either of the following commands to configure Ethernet OAM:
   
   
   * To associate CFM with an AC interface's blocked state, run the [**mpls l2vpn multi-homing trigger cfm**](cmdqueryname=mpls+l2vpn+multi-homing+trigger+cfm) **md** *md-name* **ma** *ma-name* command.
     
     CFM applies only to sub-interfaces. Run this command when CFM runs between a CE and a PE.
   * To associate EFM with an AC interface's blocked state, run the [**mpls l2vpn multi-homing trigger efm**](cmdqueryname=mpls+l2vpn+multi-homing+trigger+efm) command.
     
     EFM applies only to main interfaces. Run this command when EFM runs between a CE and a PE.
4. Run either of the following commands to configure binding:
   
   
   * In VPLS multi-homing scenarios where a CE is single-homed to a PE, run:
     
     Run the [**l2 binding**](cmdqueryname=l2+binding) [**vsi**](cmdqueryname=vsi) *vsi-name* command to bind the AC interface to a VSI.
   * In VPLS multi-homing scenarios where a CE is multi-homed to PEs, run:
     
     Run the [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name* **multi-homing-site** *site-name* command to bind the AC interface to a multi-homing site.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.