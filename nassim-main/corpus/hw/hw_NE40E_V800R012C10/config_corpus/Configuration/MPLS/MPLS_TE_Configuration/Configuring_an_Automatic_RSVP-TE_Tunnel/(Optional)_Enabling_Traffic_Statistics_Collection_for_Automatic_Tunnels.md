(Optional) Enabling Traffic Statistics Collection for Automatic Tunnels
=======================================================================

A device can be enabled to collect traffic statistics on RSVP-TE tunnels that are established by the PCE Initiated LSP protocol.

#### Context

To view traffic information about an automatic tunnel, perform the following steps to enable a device to collect traffic statistics on the automatic tunnel.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   MPLS is enabled, and the MPLS view is displayed.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**mpls traffic-statistics**](cmdqueryname=mpls+traffic-statistics)
   
   
   
   MPLS traffic statistics collection is enabled globally, and the traffic statistics view is displayed.
5. Run [**te auto-primary-tunnel**](cmdqueryname=te+auto-primary-tunnel) **pce-initiated-lsp**
   
   
   
   Traffic statistics collection for automatic tunnels is enabled.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.