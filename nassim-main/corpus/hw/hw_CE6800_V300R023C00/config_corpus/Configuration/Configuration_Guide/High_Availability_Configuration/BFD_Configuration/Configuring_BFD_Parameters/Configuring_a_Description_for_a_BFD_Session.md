Configuring a Description for a BFD Session
===========================================

Configuring a Description for a BFD Session

#### Context

You can configure a description for a BFD session to identify this session.


#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BFD session view.
   ```
   [bfd](cmdqueryname=bfd) session-name
   ```
   
   The BFD session specified by *session-name* must have been created before you run this command.
3. Configure a description for the BFD session.
   ```
   [description](cmdqueryname=description) description
   ```
   
   By default, no description is configured for a BFD session.
4. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```