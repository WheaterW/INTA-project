Enabling a Smart Link Group
===========================

Enabling a Smart Link Group

#### Context

After a Smart Link group is enabled, the slave interface in the group is blocked. After the Smart Link group is disabled, the blocked slave interface is unblocked.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the Smart Link group view.
   
   
   ```
   [smart-link group](cmdqueryname=smart-link+group) group-id
   ```
3. Enable the Smart Link group.
   
   
   ```
   [smart-link enable](cmdqueryname=smart-link+enable)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```