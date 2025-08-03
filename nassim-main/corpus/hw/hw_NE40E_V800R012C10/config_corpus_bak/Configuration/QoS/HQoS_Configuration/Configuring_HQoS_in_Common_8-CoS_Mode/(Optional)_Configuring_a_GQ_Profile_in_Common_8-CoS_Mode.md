(Optional) Configuring a GQ Profile in Common 8-CoS Mode
========================================================

After a user group queue (GQ) profile in common 8-CoS mode is configured and applied, the device can send traffic at an even rate.

#### Context

You can configure a shaping value, weight, CIR, and PIR for a GQ profile in common 8-CoS mode to limit the volume of GQ traffic and prevent its burst, as well as ensure that the GQ is scheduled based on the configured weight.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**user-group-queue**](cmdqueryname=user-group-queue) *group-name*
   
   
   
   The GQ view is displayed.
3. Run [**mode template**](cmdqueryname=mode+template)
   
   
   
   Users in the user group corresponding to the GQ are enabled to share QoS resources.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After a GQ is created, users in the user group corresponding to the GQ can share QoS resources only when the GQ is bound to a QoS profile. If the **mode template** command has been run, users in the user group corresponding to the GQ share QoS resources. If the **mode template** command is not run, users in all user groups share QoS resources.
4. Run [**shaping**](cmdqueryname=shaping) *shaping-value* [ **pbs** *pbs-value* ] { **inbound** | **outbound** }
   
   
   
   A shaping value is configured for the GQ.
5. Run [**weight**](cmdqueryname=weight) *weight-value* **outbound**
   
   
   
   A weight is configured for the GQ.
6. Run [**cir**](cmdqueryname=cir) *cir-value* [ **cbs** *cbs-value* ] [ **pir** *pir-value* [ **pbs** *pbs-value* ] ] **outbound**
   
   
   
   Scheduling parameters are configured for the GQ.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.