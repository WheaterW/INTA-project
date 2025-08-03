Configuring Whitelist Session-CAR for OSPFv3
============================================

You can configure whitelist session-CAR for OSPFv3 to isolate bandwidth resources by session for OSPFv3 packets. This configuration prevents bandwidth preemption among OSPFv3 sessions in the case of a traffic burst.

#### Context

In the case of an OSPFv3 traffic burst, bandwidth may be preempted among different OSPFv3 sessions. To resolve this problem, you can configure whitelist session-CAR for OSPFv3, which isolates bandwidth resources by session. If the default bandwidth parameters of whitelist session-CAR do not meet service requirements, you can adjust them as required.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**whitelist session-car ospfv3**](cmdqueryname=whitelist+session-car+ospfv3) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \*
   
   
   
   Parameters of whitelist session-CAR for OSPFv3 are configured.
   
   In normal cases, you are advised to use the default values of these parameters.
3. (Optional) Run [**whitelist session-car ospfv3 disable**](cmdqueryname=whitelist+session-car+ospfv3+disable)
   
   
   
   Whitelist session-CAR for OSPFv3 is disabled.
   
   By default, whitelist session-CAR for OSPFv3 is enabled. In normal cases, you are advised to keep this function enabled. Disable it if it becomes abnormal or adversely affects other services.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring whitelist session-CAR for OSPFv3, verify the configuration.

* Run the [**display cpu-defend whitelist-v6 session-car**](cmdqueryname=display+cpu-defend+whitelist-v6+session-car) **ospfv3** **statistics** **slot** *slot-id* command to check statistics about whitelist session-CAR for OSPFv3 on a specified interface board.