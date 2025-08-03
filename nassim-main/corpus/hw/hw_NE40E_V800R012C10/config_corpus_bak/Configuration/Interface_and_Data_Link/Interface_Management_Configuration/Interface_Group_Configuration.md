Interface Group Configuration
=============================

An interface group can be used to perform interface configuration in batches, simplifying interface configurations and reducing management costs.

#### Context

Interface groups are classified into permanent and temporary interface groups. Multiple interfaces can be added to the same permanent or temporary interface group to enable batch command configurations for the interfaces. The differences between permanent and temporary interface groups are described as follows:

* After a user exits the view of a temporary interface group, the system automatically deletes the temporary interface group. A permanent interface group, however, can be deleted only by using the [**undo port-group**](cmdqueryname=undo+port-group) command.
* Information about a permanent interface group can be viewed using the [**display port-group**](cmdqueryname=display+port-group) command, whereas information about a temporary interface group cannot.
* After a permanent interface group is configured, a configuration file is generated. However, no configuration file is generated after a temporary interface group is configured.


#### Procedure

* Configure a permanent interface group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**port-group**](cmdqueryname=port-group) *port-group-name*
     
     
     
     A permanent interface group is created and the view of the permanent interface group is displayed.
  3. Run [**group-member**](cmdqueryname=group-member) { *interface-type interface-number1* [ **to** *interface-type interface-number2* ] } &<1-10>
     
     
     
     Specified interfaces are added to the permanent interface group.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a temporary interface group.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**port-group group-member**](cmdqueryname=port-group+group-member) { *interface-type-start* *interface-number-start* [ **to** *interface-type-end* *interface-number-end* ] } &<1-10>
     
     
     
     A temporary interface group is created, and specified interfaces are added to the group.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If the [**shutdown**](cmdqueryname=shutdown) or [**undo shutdown**](cmdqueryname=undo+shutdown) command is run for a permanent interface group and the configuration is committed, the configuration is not recorded in the configuration file.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, run the [**display port-group**](cmdqueryname=display+port-group) [ **all** | *port-group-name* ] command to view information about a specified permanent interface group or all permanent interface groups.