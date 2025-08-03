Disabling IS-IS
===============

Disabling IS-IS

#### Context

If IS-IS functions abnormally and needs to be temporarily disabled, you can disable the involved IS-IS process. When this process is disabled, the system saves IS-IS configurations, stops IS-IS calculation, and deletes dynamic IS-IS database information, including LSDB, neighbor, and routing information.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ]
   ```
3. Disable the IS-IS process temporarily.
   
   
   ```
   [shutdown](cmdqueryname=shutdown)
   ```
   
   
   
   After an IS-IS process is disabled, IS-IS configurations can still be performed but do not take effect. To enable the IS-IS process again, run the [**undo shutdown**](cmdqueryname=undo+shutdown) command.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```