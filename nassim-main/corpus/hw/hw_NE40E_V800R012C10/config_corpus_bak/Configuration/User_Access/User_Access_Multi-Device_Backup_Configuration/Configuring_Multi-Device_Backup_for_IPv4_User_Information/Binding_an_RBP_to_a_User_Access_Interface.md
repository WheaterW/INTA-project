Binding an RBP to a User Access Interface
=========================================

Only an RBP that has been created in the system view can be bound to a user access interface. The binding needs to be configured on both devices that back up each other.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number.[ sub-interface ]*
   
   
   
   The view of the user access interface is displayed.
3. Run [**remote-backup-profile**](cmdqueryname=remote-backup-profile) *profile-name*
   
   
   
   An RBP is bound to the interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   An RBP can be bound to multiple sub-interfaces on the same main interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.