Configuring Whitelist Session-CAR for RSVP-TE
=============================================

You can configure whitelist session-CAR for RSVP-TE to isolate bandwidth resources by session for RSVP-TE packets. This configuration prevents bandwidth preemption among RSVP-TE sessions in the case of a traffic burst.

#### Context

When the RSVP-TE service suffers a traffic burst, bandwidth may be preempted among RSVP-TE sessions. To resolve this problem, you can configure whitelist session-CAR for RSVP-TE to isolate bandwidth resources by session. If the default parameters of whitelist session-CAR for RSVP-TE do not meet service requirements, you can adjust them as required.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**whitelist session-car ospf disable**](cmdqueryname=whitelist+session-car+ospf+disable)
   
   
   
   Whitelist session-CAR for RSVP-TE is disabled.
3. (Optional) Run [**whitelist session-car rsvp-te**](cmdqueryname=whitelist+session-car+rsvp-te) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \*
   
   
   
   Parameters of whitelist session-CAR for RSVP-TE are configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring whitelist session-CAR for RSVP-TE, you can verify the configuration.

Run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car) **rsvp-te** **statistics** **slot** *slot-id* command to check whitelist session-CAR statistics about RSVP-TE packets on a specified interface board.

To check the statistics in a coming period of time, you can run the [**reset cpu-defend whitelist session-car**](cmdqueryname=reset+cpu-defend+whitelist+session-car) **rsvp-te** **statistics** **slot** *slot-id* command to clear the existing whitelist session-CAR statistics about RSVP-TE packets first. Then, after the period elapses, run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car) **rsvp-te** **statistics** **slot** *slot-id* command. In this case, all the statistics are newly generally, facilitating statistics query.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Cleared whitelist session-CAR statistics cannot be restored. Exercise caution when running the reset command.