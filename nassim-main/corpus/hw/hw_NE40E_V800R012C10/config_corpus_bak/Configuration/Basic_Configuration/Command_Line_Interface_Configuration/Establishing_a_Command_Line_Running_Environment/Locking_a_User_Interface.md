Locking a User Interface
========================

To prevent unauthorized users' access to a user interface, lock the user interface.

#### Procedure

1. Run [**configuration exclusive**](cmdqueryname=configuration+exclusive)
   
   
   
   The configuration is locked and accessible only to the current user.
   
   After the configuration is locked, the current user can individually has unshared configuration rights.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You can run the [**display configuration-occupied user**](cmdqueryname=display+configuration-occupied+user) command to view the current user that has the unshared configuration rights.
2. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
3. Run [**configuration-occupied timeout**](cmdqueryname=configuration-occupied+timeout) *timeout-value*
   
   
   
   The interval after which the configuration is unlocked is set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.