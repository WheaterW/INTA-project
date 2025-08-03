Configuring an Idle-Cut Timer for a Tunnel
==========================================

To save bandwidth resources, you can set an idle-cut timer.

#### Context

An idle-cut timer specifies the period during which a tunnel continues to exist after the number of sessions in the tunnel reaches 0. When the timer expires, the tunnel is deleted.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**l2tp-group**](cmdqueryname=l2tp-group) *group-name*
   
   
   
   The L2TP group view is displayed.
3. Run [**tunnel idle-cut**](cmdqueryname=tunnel+idle-cut) *time-value*
   
   
   
   An idle-cut timer is configured.
   
   A tunnel with an idle-cut timer value 0 will never be actively deleted by the local end. However, the tunnel will not be set up again if the remote end deletes it.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.