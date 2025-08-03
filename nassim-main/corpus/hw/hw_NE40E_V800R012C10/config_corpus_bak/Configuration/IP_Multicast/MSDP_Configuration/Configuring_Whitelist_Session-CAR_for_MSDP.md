Configuring Whitelist Session-CAR for MSDP
==========================================

Configuring_Whitelist_Session-CAR_for_MSDP

#### Usage Scenario

When MSDP messages suffer a traffic burst, bandwidth may be preempted among MSDP sessions. To resolve this problem, you can configure whitelist session-CAR for MSDP to isolate bandwidth resources by session. If the default parameters of whitelist session-CAR do not meet service requirements, you can adjust them as required.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**whitelist session-car msdp**](cmdqueryname=whitelist+session-car+msdp) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \*
   
   
   
   Parameters of whitelist session-CAR for MSDP are configured.
   
   
   
   In normal cases, you are advised to use the default values. The value of **PIR** must be greater than or equal to that of [**CIR**](cmdqueryname=CIR), and the value of [**PBS**](cmdqueryname=PBS) must be greater than or equal to that of **CBS**.
3. (Optional) Run [**whitelist session-car msdp disable**](cmdqueryname=whitelist+session-car+msdp+disable)
   
   
   
   Whitelist session-CAR for MSDP is disabled.
   
   
   
   In normal cases, you are advised to keep whitelist session CAR for MSDP enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Result

Run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car) **msdp** **statistics** **slot** *slot-id* command to check statistics about whitelist session-CAR for MSDP on a specified interface board.