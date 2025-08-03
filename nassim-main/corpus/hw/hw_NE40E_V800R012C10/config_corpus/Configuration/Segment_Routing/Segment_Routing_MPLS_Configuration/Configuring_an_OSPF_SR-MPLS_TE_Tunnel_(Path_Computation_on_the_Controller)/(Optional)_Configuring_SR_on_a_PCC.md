(Optional) Configuring SR on a PCC
==================================

Configure SR on a PCE client (PCC), so that a controller can deliver path information to the PCC (forwarder) after path computation.

#### Context

SR is configured on a PCC (forwarder). Path computation is delegated to the controller. After the controller computes a path, the controller sends a PCEP message to deliver path information to the PCC.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The path information can also be delivered by a third-party adapter to the forwarder. In this situation, SR does not need to be configured on the PCC, and the associated step can be skipped.




#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pce-client**](cmdqueryname=pce-client)
   
   
   
   A PCE client is configured, and the PCE client view is displayed.
3. Run [**capability segment-routing**](cmdqueryname=capability+segment-routing)
   
   
   
   SR is enabled for the PCE client.
4. Run [**connect-server**](cmdqueryname=connect-server) *ip-address*
   
   
   
   A candidate PCE server is specified for the PCE client.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.