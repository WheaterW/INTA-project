(Optional) Configuring a Description for a BFD Session
======================================================

You can configure a description for a BFD session to identify this session.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd) *session-name*
   
   
   
   The BFD session view is displayed.
3. Run [**description**](cmdqueryname=description) *description*
   
   
   
   A description is configured for the BFD session.
   
   
   
   *description* is a string of 1 to 64 case-sensitive characters, spaces not supported.
   
   You can run the [**undo description**](cmdqueryname=undo+description) command to delete the description of the BFD session.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.