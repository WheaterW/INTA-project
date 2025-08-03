(Optional) Configuring SR on a PCC
==================================

The SR capability is configured on a PCC. After a controller calculates a path and delivers path information to a forwarder (PCC), the SR-enabled PCC can establish an SR-MPLS TE tunnel.

#### Context

SR can be configured on a PCC (forwarder). Path computation is then delegated to the controller. After the controller calculates a path, the controller sends a PCEP message to deliver path information to the PCC (forwarder).![](../../../../public_sys-resources/note_3.0-en-us.png) 

The path information can also be delivered by a third-party adapter to the forwarder. In this situation, SR does not need to be configured on the PCC, and the following operation can be skipped.




#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pce-client**](cmdqueryname=pce-client)
   
   
   
   A PCE client is configured, and the PCE client view is displayed.
3. Run [**capability segment-routing**](cmdqueryname=capability+segment-routing)
   
   
   
   SR is enabled for the PCE client.
4. Run [**connect-server**](cmdqueryname=connect-server) *ip-address*
   
   
   
   A candidate PCE server is configured for the PCE client.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.