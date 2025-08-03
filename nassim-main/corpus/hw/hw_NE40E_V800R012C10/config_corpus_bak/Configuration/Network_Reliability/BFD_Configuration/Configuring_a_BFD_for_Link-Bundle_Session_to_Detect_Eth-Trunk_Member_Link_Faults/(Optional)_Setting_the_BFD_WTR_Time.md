(Optional) Setting the BFD WTR Time
===================================

Setting a wait to restore (WTR) time for a BFD session can prevent applications from being frequently switched between the master and backup devices due to BFD session flapping.

#### Context

If a BFD session flaps, master/backup switchovers are frequently performed on the application associated with the BFD session. To resolve this issue, you can set the WTR time for the BFD session. When the BFD session changes from down to up, BFD reports the change to the upper-layer application after the WTR time expires.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd) *session-name*
   
   
   
   The BFD session view is displayed.
3. Perform either of the following operations to set the WTR time of the BFD session:
   
   
   * To set the WTR time of the BFD session in minutes, run the [**wtr**](cmdqueryname=wtr) *wtr-value* command.
   * To set the WTR time of the BFD session in seconds, run the [**wtr seconds**](cmdqueryname=wtr+seconds) *wtr-value-seconds* command.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A BFD session is unidirectional, and therefore you must configure the same WTR time at both ends. Otherwise, when the BFD session state changes at one end, applications at both ends detect different BFD session states.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.