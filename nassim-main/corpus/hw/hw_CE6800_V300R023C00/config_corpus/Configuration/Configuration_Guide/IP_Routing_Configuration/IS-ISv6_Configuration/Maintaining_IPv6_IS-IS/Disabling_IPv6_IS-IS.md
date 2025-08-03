Disabling IPv6 IS-IS
====================

Disabling IPv6 IS-IS

#### Context

If IPv6 IS-IS functions abnormally and needs to be temporarily disabled, you can disable the involved IPv6 IS-IS process. When this process is disabled, the system saves IPv6 IS-IS configurations, stops IPv6 IS-IS calculation, and deletes dynamic IPv6 IS-IS database information, including LSDB, neighbor, and routing information.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the IS-IS view.
   
   
   ```
   [isis](cmdqueryname=isis) [ process-id ]
   ```
3. Disable the IS-IS process.
   
   
   ```
   [shutdown](cmdqueryname=shutdown)
   ```
   
   
   
   After an IPv6 IS-IS process is disabled, IPv6 IS-IS configurations can still be performed but do not take effect. To enable the IPv6 IS-IS process again, run the [**undo shutdown**](cmdqueryname=undo+shutdown) command.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```