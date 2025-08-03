(Optional) Configuring a PCE Client to Delegate TE LSPs to All PCE Servers
==========================================================================

A PCE client can be configured to delegate TE LSPs to all PCE servers. This configuration prevents a PCE server path calculation failure that occurs when forwarders select a master PCE server different from that configured on a controller.

#### Usage Scenario

In a PCEP scenario, forwarders (PCE clients) elect the master and backup PCE servers. Each PCE client delegates all TE LSPs to the selected or highest-priority PCE server. The PCE server can then calculate paths for the delegated TE LSPs. In geographical redundancy, the master and backup PCE servers are configured on controllers. In this situation, the forwarders may select a master PCE server different from that configured on a controller, causing a master PCE server inconsistency. After PCE clients delegate all TE LSPs to the selected PCE server, the master PCE server configured on the controller cannot calculate paths. To prevent a path calculation failure, run the [**multi-delegate enable**](cmdqueryname=multi-delegate+enable) command to enable a PCE client to delegate TE LSPs to all PCE servers that have established PCEP sessions to the PCE client.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pce-client**](cmdqueryname=pce-client)
   
   
   
   The PCE client view is displayed.
3. Run [**multi-delegate enable**](cmdqueryname=multi-delegate+enable)
   
   
   
   The PCE client is enabled to delegate all TE LSPs to all PCE servers that have established PCEP sessions with the client.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.