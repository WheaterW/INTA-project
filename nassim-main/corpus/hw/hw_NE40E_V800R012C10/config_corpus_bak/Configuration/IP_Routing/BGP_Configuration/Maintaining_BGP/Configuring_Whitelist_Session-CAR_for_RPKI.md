Configuring Whitelist Session-CAR for RPKI
==========================================

You can configure whitelist session-CAR for RPKI to isolate bandwidth resources by session for RPKI messages.

#### Context

The function of whitelist session-CAR for RPKI sets an independent CAR channel for each RPKI session to ensure that the bandwidth of each RPKI session is not preempted by other traffic (including traffic of other sessions of the same protocol and traffic of other protocols). When RPKI messages form a traffic burst, you can adjust the bandwidth for each RPKI session in whitelist session-CAR for RPKI to ensure that RPKI messages can be sent to the CPU properly.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If the function becomes abnormal or affects other services, you can run the [**whitelist session-car rpki disable**](cmdqueryname=whitelist+session-car+rpki+disable) command to disable whitelist session-CAR for RPKI. In normal cases, you are advised to keep whitelist session-CAR for RPKI enabled.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**whitelist session-car rpki**](cmdqueryname=whitelist+session-car+rpki+cir+cbs+pir+pbs) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \*
   
   
   
   Parameters of whitelist session-CAR for RPKI are configured.
   
   
   
   In normal cases, you are advised to use the default values.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car+rpki+statistics+slot) **rpki** **statistics** **slot** *slot-id* command to check statistics about IPv4 whitelist session-CAR for RPKI on a specified interface board. To check the statistics within a specific period of time, run the [**reset cpu-defend whitelist session-car**](cmdqueryname=reset+cpu-defend+whitelist+session-car+rpki+statistics+slot) **rpki** **statistics** **slot** *slot-id* command to clear the existing statistics about IPv4 whitelist session-CAR for RPKI on the specified interface board; after a certain period of time, run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car+rpki+statistics+slot) **rpki** **statistics** **slot** *slot-id* command.![](../../../../public_sys-resources/note_3.0-en-us.png) 

The statistics about whitelist session-CAR for RPKI on a specified interface board cannot be restored after being cleared. Therefore, exercise caution before clearing them.