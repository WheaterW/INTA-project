Enabling a Multicast RBS
========================

An RBS is enabled for multicast services.

#### Context

Perform the following steps on the devices that back up each other.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
   
   
   
   The RBP view is displayed.
3. Run [**service-type**](cmdqueryname=service-type) **multicast**
   
   
   
   A multicast RBS is enabled.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After the [**undo service-type multicast**](cmdqueryname=undo+service-type+multicast) command is run, the system does not back up new IGMP messages. The IGMP messages that have been backed up are not affected.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.