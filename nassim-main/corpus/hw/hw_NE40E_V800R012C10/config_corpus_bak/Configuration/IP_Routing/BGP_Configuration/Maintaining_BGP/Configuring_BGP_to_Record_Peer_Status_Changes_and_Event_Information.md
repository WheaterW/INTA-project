Configuring BGP to Record Peer Status Changes and Event Information
===================================================================

After BGP is configured to record peer status changes, BGP records logs when the BGP peer status changes.

#### Context

System log files serve as an important reference for locating network connectivity and stability problems. If an error occurs on a connection between BGP peers, a corresponding error code and subcode are generated. If the local device terminates the connection with a peer due to a received a Notification message from the peer, the local device records the error code carried in the received message, and the state machine on the local device changes. When the connection is interrupted due to an error on the local end, the local end changes its state machine and sends a Notification message to the peer end.

By default, BGP records peer status changes and event information in the system log files. The record includes BGP error codes and subcodes, BGP state machine changes, and whether BGP Notification messages are sent.

If you do not want BGP to record peer status changes or event information, run the [**undo peer log-change**](cmdqueryname=undo+peer+log-change) command. After you run the [**undo peer log-change**](cmdqueryname=undo+peer+log-change) command, BGP records only the last peer status change in the log file. To check this log, run the [**display bgp peer log-info**](cmdqueryname=display+bgp+peer+log-info) command.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } [**log-change**](cmdqueryname=log-change)
   
   
   
   BGP is configured to record peer status changes and event information.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.