Link Switchover Fails in a Smart Link Group
===========================================

Link Switchover Fails in a Smart Link Group

#### Possible Causes

Data flow locking has been enabled in the Smart Link group.


#### Procedure

1. Check whether data flow locking has been enabled in the Smart Link group.
   
   
   ```
   [display smart-link group](cmdqueryname=display+smart-link+group) group-id
   ```
   
   If **Link status** is **lock** or **force**, data flow locking has been enabled in the Smart Link group. In this case, go to Step 2.
2. Disable data flow locking in the Smart Link group.
   1. Enter the Smart Link group view.
      
      
      ```
      [smart-link group](cmdqueryname=smart-link+group) group-id
      ```
   2. Disable data flow locking in the Smart Link group.
      
      
      ```
      undo smart-link { force | lock }
      ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```