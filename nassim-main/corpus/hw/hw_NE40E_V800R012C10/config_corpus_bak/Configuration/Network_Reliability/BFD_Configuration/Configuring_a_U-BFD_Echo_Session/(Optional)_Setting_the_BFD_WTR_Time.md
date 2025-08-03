(Optional) Setting the BFD WTR Time
===================================

You can set the BFD wait to restore (WTR) time to prevent an application from switching between the master and slave devices due to BFD session flapping.

#### Context

If a BFD session flaps, master/slave switchovers are frequently performed on the application associated with BFD. To resolve this issue, set the WTR time for a BFD session. When the BFD session changes from Down to Up, BFD reports the change to the upper-layer application after the WTR time expires.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd) *session-name*
   
   
   
   The BFD session view is displayed.
3. Run [**wtr**](cmdqueryname=wtr) *wtr-value*
   
   
   
   The WTR time of the BFD session is set.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A BFD session is unidirectional. Therefore, if the WTR time is used, you must set the same WTR time on both ends of the BFD session. If the WTR times on both ends are different and the session status changes on one end, applications on both ends of the BFD session detect different BFD session statuses.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.