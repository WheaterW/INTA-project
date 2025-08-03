Suppressing IS-IS
=================

You can disable an IS-IS process temporarily by suppressing IS-IS without affecting IS-IS configurations.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   An IS-IS process is started, and the IS-IS view displayed.
3. Run [**shutdown**](cmdqueryname=shutdown)
   
   
   
   The IS-IS process is disabled temporarily.
   
   After the IS-IS process is disabled temporarily, you can still perform IS-IS configurations but the configurations do not take effect. You can run the [**undo shutdown**](cmdqueryname=undo+shutdown) command to cancel the suppression.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.