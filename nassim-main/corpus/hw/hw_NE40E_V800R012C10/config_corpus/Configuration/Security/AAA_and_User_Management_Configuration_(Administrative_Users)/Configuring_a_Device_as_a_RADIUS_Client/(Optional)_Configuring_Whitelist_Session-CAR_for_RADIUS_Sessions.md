(Optional) Configuring Whitelist Session-CAR for RADIUS Sessions
================================================================

(Optional) Configuring Whitelist Session-CAR for RADIUS Sessions

#### Context

When packets sent to the RADIUS server form a traffic burst, RADIUS sessions may preempt bandwidth. To resolve this problem, you can configure whitelist session-CAR for RADIUS sessions to isolate bandwidth resources by session. If the default parameters of whitelist session-CAR for RADIUS do not meet service requirements, you can adjust them as required.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**whitelist session-car radius**](cmdqueryname=whitelist+session-car+radius) { **cir** *cir-value* | **pir** *pir-value* | **cbs** *cbs-value* | **pbs** pbs-value } \*
   
   
   
   Bandwidth parameters are configured for whitelist session-CAR of RADIUS.
3. (Optional) Run [**whitelist session-car radius disable**](cmdqueryname=whitelist+session-car+radius+disable)
   
   
   
   Whitelist session-CAR for RADIUS sessions is disabled.
   
   
   
   Whitelist session-CAR for RADIUS sessions can be disabled only when this function is abnormal. Under normal circumstances, enabling whitelist session-CAR for RADIUS sessions is recommended.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.