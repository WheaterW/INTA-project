Configuring Whitelist Session-CAR for PIM
=========================================

You can configure whitelist session-CAR for PIM to isolate bandwidth resources by session for PIM messages. This configuration prevents bandwidth preemption among PIM sessions in the case of a traffic burst.

#### Usage Scenario

When PIM messages suffer a traffic burst, bandwidth may be preempted among PIM sessions. To resolve this problem, you can configure whitelist session-CAR for PIM to isolate bandwidth resources by session. If the default bandwidth parameters of whitelist session-CAR do not meet service requirements, you can adjust them as required.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**whitelist session-car pim**](cmdqueryname=whitelist+session-car+pim) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \* command to set parameters of whitelist session-CAR for PIM.
3. (Optional) Run the [**whitelist session-car pim disable**](cmdqueryname=whitelist+session-car+pim+disable) command to disable whitelist session-CAR for PIM.
   
   
   
   In normal cases, you are advised to keep whitelist session-CAR for PIM enabled. Disable this function if it becomes abnormal or adversely affects other services.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.