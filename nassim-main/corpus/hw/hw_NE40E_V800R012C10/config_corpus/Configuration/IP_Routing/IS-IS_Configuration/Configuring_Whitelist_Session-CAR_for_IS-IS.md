Configuring Whitelist Session-CAR for IS-IS
===========================================

You can configure whitelist session-CAR for IS-IS to isolate bandwidth resources by session for IS-IS packets. This configuration prevents bandwidth preemption among IS-IS sessions in the case of a traffic burst.

#### Context

When IS-IS packets suffer a traffic burst, bandwidth may be preempted among different IS-IS sessions. To resolve this problem, you can configure whitelist session-CAR for IS-IS to isolate bandwidth resources by session. If the default parameters of whitelist session-CAR for IS-IS do not meet service requirements, you can adjust them as required.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**whitelist session-car isis**](cmdqueryname=whitelist+session-car+isis) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \*
   
   
   
   Parameters of whitelist session-CAR for IS-IS are configured.
   
   
   
   In normal cases, you are advised to use the default values of these parameters.
3. (Optional) Run [**whitelist session-car isis disable**](cmdqueryname=whitelist+session-car+isis+disable)
   
   
   
   Whitelist session-CAR for IS-IS is disabled.
   
   
   
   By default, whitelist session-CAR for IS-IS is enabled. In normal cases, you are advised to keep this function enabled. Disable it if it becomes abnormal or adversely affects other services.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

Run the [**display cpu-defend whitelist-l2 session-car**](cmdqueryname=display+cpu-defend+whitelist-l2+session-car) **isis** **statistics** **slot** *slot-id* command to check statistics about whitelist session-CAR for IS-IS on a specified interface board.

If you want to check such statistics within a specific period, first you can run the [**reset cpu-defend whitelist-l2 session-car**](cmdqueryname=reset+cpu-defend+whitelist-l2+session-car) **isis** **statistics** **slot***slot-id* command to clear statistics about whitelist session-CAR for IS-IS on the specified interface board. After some time, run the [**display cpu-defend whitelist-l2 session-car**](cmdqueryname=display+cpu-defend+whitelist-l2+session-car) **isis** **statistics** **slot** *slot-id* command again.