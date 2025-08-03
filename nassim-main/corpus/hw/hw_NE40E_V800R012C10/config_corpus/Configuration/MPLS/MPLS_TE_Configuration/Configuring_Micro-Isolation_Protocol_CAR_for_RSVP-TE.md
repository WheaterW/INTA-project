Configuring Micro-Isolation Protocol CAR for RSVP-TE
====================================================

Configuring Micro-Isolation Protocol CAR for RSVP-TE

#### Context

Micro-isolation CAR for RSVP-TE is enabled by default to implement micro-isolation protection for RSVP-TE connection establishment packets. If a device is attacked, messages of one RSVP-TE session may preempt bandwidth of other sessions. Therefore, you are advised to keep this function enabled.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**micro-isolation protocol-car rsvp-te**](cmdqueryname=micro-isolation+protocol-car+rsvp-te) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \*
   
   
   
   Micro-isolation CAR parameters are configured for RSVP-TE.
   
   
   
   In normal cases, you are advised to use the default values of these parameters. *pir-value* must be greater than or equal to *cir-value*, and *pbs-value* must be greater than or equal to *cbs-value*.
3. (Optional) Run [**micro-isolation protocol-car rsvp-te disable**](cmdqueryname=micro-isolation+protocol-car+rsvp-te+disable)
   
   
   
   Micro-isolation CAR is disabled for RSVP-TE.
   
   
   
   Micro-isolation CAR for RSVP-TE is enabled by default. To disable micro-isolation for RSVP-TE packets, run the [**micro-isolation protocol-car rsvp-te disable**](cmdqueryname=micro-isolation+protocol-car+rsvp-te+disable) command. In normal cases, you are advised to keep micro-isolation CAR enabled for RSVP-TE.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.