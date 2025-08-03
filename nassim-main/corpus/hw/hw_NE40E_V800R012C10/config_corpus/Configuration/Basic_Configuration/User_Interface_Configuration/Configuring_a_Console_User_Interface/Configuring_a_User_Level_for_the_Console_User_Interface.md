Configuring a User Level for the Console User Interface
=======================================================

You can configure a user level for the console user interface to manage users based on their levels.

#### Context

User levels correspond to command levels. After a user logs in to a router, the user can use only commands of the corresponding level or lower.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**user-interface**](cmdqueryname=user-interface){ *ui-type* | **console***first-ui-number* }
   
   
   
   The console user interface view is displayed.
3. Run [**user privilege level**](cmdqueryname=user+privilege+level) *level*
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the user level configured for a user interface conflicts with the user level configured for a user, the user level configured for the user takes precedence.
   
   For example, user 001 can use commands at Level 3, and the user level configured for the user in the user interface view Console 0 is 2. After user 001 logs in through Console 0, the user can use commands at Level 3 or lower.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.