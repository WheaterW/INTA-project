Enabling a PCE Client to Process SRv6 TE Policies
=================================================

Configure a PCE client and establish a session between the PCE client and server so that the PCE client can receive SRv6 TE Policy information delivered by the PCE server.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pce-client**](cmdqueryname=pce-client)
   
   
   
   The device is configured as a PCE client, and the PCE client view is displayed.
3. Run [**capability segment-routing-ipv6**](cmdqueryname=capability+segment-routing-ipv6)
   
   
   
   The PCE client is enabled to process SRv6 TE Policies.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.