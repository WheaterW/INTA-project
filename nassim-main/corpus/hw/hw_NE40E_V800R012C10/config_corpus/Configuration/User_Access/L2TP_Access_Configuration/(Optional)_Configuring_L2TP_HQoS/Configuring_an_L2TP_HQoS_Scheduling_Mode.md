Configuring an L2TP HQoS Scheduling Mode
========================================

In an L2TP service wholesale scenario, an LNS is the actual service control point. Therefore, an L2TP HQoS scheduling mode needs to be configured on an NE40E that functions as an LNS.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**l2tp-group**](cmdqueryname=l2tp-group) *group-name*
   
   
   
   An L2TP group is created, and its view is displayed.
   
   The L2TP group must be of the LNS type.
3. Run [**qos scheduling-mode**](cmdqueryname=qos+scheduling-mode) { **session** | **tunnel** }
   
   
   
   An L2TP HQoS scheduling mode is configured.
   
   L2TP HQoS has the following scheduling modes:
   
   * Scheduling by tunnel: User services are not differentiated. As a result, user queues are not allocated to users but to tunnels.
   * Scheduling by session: User queues with priorities ranging from 1 to 8 are allocated to each user, and group queues are allocated to tunnels. SP or WFQ scheduling can be performed between any of the user queues.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.