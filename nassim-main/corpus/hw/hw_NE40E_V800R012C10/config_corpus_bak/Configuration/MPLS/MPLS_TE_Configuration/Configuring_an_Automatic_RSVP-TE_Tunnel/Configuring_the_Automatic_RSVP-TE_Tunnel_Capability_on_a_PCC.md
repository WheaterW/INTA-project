Configuring the Automatic RSVP-TE Tunnel Capability on a PCC
============================================================

The PCE Initiated LSP protocol needs to be configured for automatic RSVP-TE tunnels. A controller runs this protocol to deliver tunnel and path information to the ingress on which a forwarder resides. Upon receipt of the information, the ingress automatically establishes an RSVP-TE tunnel.

#### Context

The PCE Initiated LSP protocol is used to implement the automatic RSVP-TE tunnel function. A PCE client (PCC) (ingress) establishes a PCE link to a PCE server (controller). The controller delivers tunnel and path information to a forwarder configured on the ingress. The ingress uses the information to automatically establish a tunnel and reports LSP status information to the controller along the PCE link.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pce-client**](cmdqueryname=pce-client)
   
   
   
   A PCE client is configured, and the PCC client view is displayed.
3. Run [**capability**](cmdqueryname=capability) **segment-routing**
   
   
   
   The initiated-LSP capability and RSVP-TE are enabled.
4. Run [**connect-server**](cmdqueryname=connect-server) *ip-address*
   
   
   
   A candidate PCE server is specified for the PCE client.
5. (Optional) Configure a PCC to delete LSPs whose establishment is triggered by a controller if the PCE fails.
   1. Run the [**quit**](cmdqueryname=quit) command to return to the PCE client view.
   2. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   3. Run the [**mpls**](cmdqueryname=mpls) command to enter the MPLS view.
   4. Run the [**mpls te pce cleanup initiated-lsp**](cmdqueryname=mpls+te+pce+cleanup+initiated-lsp) command to enable a PCC to delete LSPs whose establishment is triggered by a controller if the PCE fails.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.