(Optional) Configuring the Shaping Value of a GQ
================================================

You can configure a shaping value for a GQ to limit the volume of GQ traffic and prevent its burst. In this case, traffic can be sent at an even rate.

#### Context

Perform the following configurations on the Router where HQoS needs to be configured.

If traffic shaping is not configured for a GQ, the system performs no traffic shaping by default.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**user-group-queue**](cmdqueryname=user-group-queue) *group-name*
   
   
   
   The GQ view is displayed.
3. Run [**shaping**](cmdqueryname=shaping) *shaping-value* [ **pbs** *pbs-value* ] { **inbound** | **outbound** }
   
   
   
   A shaping rate is set for the GQ.
4. (Optional) Run [**mode template**](cmdqueryname=mode+template)
   
   
   
   Users in the user group corresponding to the GQ are enabled to share QoS resources.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   After a GQ is created, it applies for QoS resources only when it is bound to a QoS profile. If the [**mode template**](cmdqueryname=mode+template) command is run, a GQ shares QoS resources with other GQs based on a group specified for the QoS profile. If the [**mode template**](cmdqueryname=mode+template) command is not run, a GQ shares QoS resources with other GQs based on all groups of a QoS profile.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.