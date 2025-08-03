(Optional) Configuring ND Fast Reply
====================================

(Optional) Configuring ND Fast Reply

#### Context

If a large number of NS messages are sent to a main control board, the CPU usage of the main control board may be high. To resolve this issue, run the [**nd fast-reply enable**](cmdqueryname=nd+fast-reply+enable) command to enable ND fast reply. After the command is run, NS messages are sent to an interface board instead of a main control board, and the interface board responds with NA messages.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. Run [**slot**](cmdqueryname=slot) *slot-id*
   
   The slot view is displayed.
3. Run [**nd fast-reply enable**](cmdqueryname=nd+fast-reply+enable)
   
   ND fast reply is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.