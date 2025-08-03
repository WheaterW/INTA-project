Configuring a WTR Time for a BFD Session
========================================

Configuring a WTR Time for a BFD Session

#### Context

If a BFD session flaps, the applications associated with BFD will be frequently switched between devices. To resolve this problem, configure a WTR time for the BFD session. When the BFD session status changes from down to up, BFD reports the change to the upper-layer applications after the WTR time expires.


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
3. Configure a WTR time for the BFD session.
   ```
   [wtr](cmdqueryname=wtr) wtr-value
   ```
   
   The default value is 0, indicating that the state change of a BFD session is reported immediately.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   A BFD session is unidirectional, and therefore you need to configure the same WTR time at both ends. Otherwise, when the BFD session state changes at one end, applications at both ends detect different BFD session states.
4. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```