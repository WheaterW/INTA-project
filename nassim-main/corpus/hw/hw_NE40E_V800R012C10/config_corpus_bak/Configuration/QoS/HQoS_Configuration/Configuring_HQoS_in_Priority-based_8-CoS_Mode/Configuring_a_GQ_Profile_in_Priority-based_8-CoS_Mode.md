Configuring a GQ Profile in Priority-based 8-CoS Mode
=====================================================

You can configure a shaping value and token bucket depth for a priority-based GQ.

#### Context

In GQ service scenarios, you can configure a shaping value for a priority-based GQ to implement traffic shaping.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**user-group-queue**](cmdqueryname=user-group-queue) *group-name* **priority-mode**
   
   
   
   The priority-based GQ view is displayed.
3. Run [**priority**](cmdqueryname=priority) *priority-value* **shaping** *shaping-value* [ **pbs** *pbs-value* ] **outbound**
   
   
   
   A shaping value and token bucket depth are configured for the priority-based GQ.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.