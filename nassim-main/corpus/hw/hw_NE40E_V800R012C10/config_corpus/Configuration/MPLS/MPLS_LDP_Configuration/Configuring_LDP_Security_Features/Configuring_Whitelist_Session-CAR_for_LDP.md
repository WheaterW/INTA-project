Configuring Whitelist Session-CAR for LDP
=========================================

You can configure whitelist session-CAR for LDP to isolate bandwidth resources by session for LDP packets. This configuration prevents bandwidth preemption among LDP sessions in the case of a traffic burst.

#### Context

When traffic bursts occur in the LDP service, bandwidth may be preempted among LDP sessions. To resolve this problem, you can configure whitelist session-CAR for LDP to isolate bandwidth resources by session. If the default parameters of whitelist session-CAR for LDP do not meet service requirements, you can adjust them as required.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**whitelist session-car**](cmdqueryname=whitelist+session-car+ldp-tcp+ldp-udp-local+ldp-udp-remote+cir) { **ldp-tcp** | **ldp-udp-local** | **ldp-udp-remote** } { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \*
   
   
   
   Parameters of whitelist session-CAR for LDP are configured.
3. (Optional) Run [**whitelist session-car ldp disable**](cmdqueryname=whitelist+session-car+ldp+disable)
   
   
   
   Whitelist session-CAR is disabled for LDP.
   
   
   
   In normal cases, you are advised to keep whitelist session-CAR enabled for LDP.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.