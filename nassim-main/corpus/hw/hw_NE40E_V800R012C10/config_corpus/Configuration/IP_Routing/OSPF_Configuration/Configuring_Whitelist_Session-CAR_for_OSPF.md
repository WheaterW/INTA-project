Configuring Whitelist Session-CAR for OSPF
==========================================

You can configure whitelist session-CAR for OSPF to isolate bandwidth resources by session for OSPF packets. This configuration prevents bandwidth preemption among OSPF sessions in the case of a traffic burst.

#### Context

In the case of an OSPF traffic burst, bandwidth may be preempted among different OSPF sessions. To resolve this problem, you can configure whitelist session-CAR for OSPF to isolate bandwidth resources by session. If the default parameters of whitelist session-CAR do not meet service requirements, you can adjust them as required.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**whitelist session-car ospf**](cmdqueryname=whitelist+session-car+ospf) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \*
   
   
   
   Parameters of whitelist session-CAR for OSPF are configured.
   
   In normal cases, you are advised to use the default values of these parameters.
3. (Optional) Run [**whitelist session-car ospf disable**](cmdqueryname=whitelist+session-car+ospf+disable)
   
   
   
   Whitelist session-CAR for OSPF is disabled.
   
   By default, whitelist session-CAR for OSPF is enabled. In normal cases, you are advised to keep this function enabled. Disable it if it becomes abnormal or adversely affects other services.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

* Run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car) **ospf** **statistics** **slot** *slot-id* command to check statistics about whitelist session-CAR for OSPF on a specified interface board.