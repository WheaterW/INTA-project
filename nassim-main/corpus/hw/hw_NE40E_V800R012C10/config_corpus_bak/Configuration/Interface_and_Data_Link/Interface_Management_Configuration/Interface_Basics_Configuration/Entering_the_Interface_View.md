Entering the Interface View
===========================

The command for entering the view of an interface varies with the physical attribute of the interface.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
   
   
   
   In this command, *interface-type* specifies the type of the interface, and *interface-number* specifies the number of the interface.
3. (Optional) Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
   
   
   
   If the interface of the specified type and number exists in the preceding step, you do not need to run the [**commit**](cmdqueryname=commit) command.