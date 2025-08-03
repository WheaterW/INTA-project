Configuring a User Level for a VTY User Interface
=================================================

To improve security, configure user levels for user interfaces to manage users based on their levels. This section describes how to configure a user level for a VTY user interface.

#### Context

User levels correspond to command levels. After a user logs in to a router, the user can use only commands of the corresponding level or lower.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**user-interface**](cmdqueryname=user-interface) **vty** *first-ui-number* [ *last-ui-number* ]
   
   
   
   One or more VTY user interface views are displayed.
3. Run [**user privilege**](cmdqueryname=user+privilege) **level** *level*
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the user level configured for a user interface conflicts with the user level configured for a user, the user level configured for the user takes precedence.
   
   For example, user 001 can use commands at Level 3, and the user level configured for the user in the user interface view VTY 0 is 2. After user 001 logs in through VTY 0, the user can use commands at Level 3 or lower.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.