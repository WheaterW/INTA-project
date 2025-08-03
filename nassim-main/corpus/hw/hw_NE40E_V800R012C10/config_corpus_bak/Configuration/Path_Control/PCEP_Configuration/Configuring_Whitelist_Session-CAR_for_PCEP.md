Configuring Whitelist Session-CAR for PCEP
==========================================

You can configure whitelist session-CAR for PCEP to limit the session rate of PCEP packets. This configuration prevents bandwidth preemption among PCEP sessions in the case of a traffic burst.

#### Context

When the PCEP service suffers a traffic burst, bandwidth may be preempted among PCEP sessions. To resolve this problem, you can configure whitelist session-CAR for PCEP to isolate bandwidth resources by session. If the default bandwidth parameters of whitelist session-CAR do not meet service requirements, you can adjust them as required.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**whitelist session-car pcep-ipv4**](cmdqueryname=whitelist+session-car+pcep-ipv4) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \*
   
   
   
   Whitelist session-CAR parameters are configured for PCEP.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring whitelist session-CAR for PCEP, verify the configuration.

Run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car) **pcep** **statistics** **slot** *slot-id* command to check whitelist session-CAR statistics about PCEP packets on a specified interface board.

To check the statistics collected in a specified period, you can run the [**reset cpu-defend whitelist session-car**](cmdqueryname=reset+cpu-defend+whitelist+session-car) **pcep** **statistics** **slot** *slot-id* command to clear the existing whitelist session-CAR statistics about PCEP packets on the specified interface board, and then run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car) **pcep** **statistics** **slot** *slot-id* command after a certain period of time.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Cleared whitelist session-CAR statistics cannot be restored. Exercise caution when running the reset command.



#### Exception Handling

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**whitelist session-car pcep-ipv4 disable**](cmdqueryname=whitelist+session-car+pcep-ipv4+disable) command to disable whitelist session-CAR for PCEP.
   
   
   
   Disable this function only if it encounters an exception. In normal cases, you are advised to keep whitelist session-CAR enabled for PCEP.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.