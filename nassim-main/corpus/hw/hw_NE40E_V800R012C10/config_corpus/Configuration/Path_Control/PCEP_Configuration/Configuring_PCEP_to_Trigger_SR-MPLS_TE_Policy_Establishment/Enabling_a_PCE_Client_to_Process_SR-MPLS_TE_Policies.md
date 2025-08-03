Enabling a PCE Client to Process SR-MPLS TE Policies
====================================================

Configure a PCE client and establish a session between the PCE client and server so that the PCE client can receive SR-MPLS TE Policy information delivered by the PCE server.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pce-client**](cmdqueryname=pce-client)
   
   
   
   The device is configured as a PCE client, and the PCE client view is displayed.
3. Run [**capability segment-routing**](cmdqueryname=capability+segment-routing)
   
   
   
   The PCE client is enabled to process SR-MPLS TE Policies.
4. (Optional) Run [**stateless-bringup**](cmdqueryname=stateless-bringup)
   
   
   
   The PCE client is enabled to send PCReq messages to the PCE server to request path computation.
   
   
   
   With the [**stateless-bringup**](cmdqueryname=stateless-bringup) command configured, after synchronization between the PCE client and server is complete, the PCE client sends a PCReq message to request path computation for a newly configured LSP of an SR-MPLS TE Policy. After receiving the request, the PCE server returns a path computation result using a PCRep message. This function can be configured in PCE delegation scenarios. If the returned path computation result meets service requirements, delegation can be started. However, if a no-path message or an error is returned, rectify faults before starting delegation.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.