Configuring Dynamic BFD For Initiated RSVP-TE LSP
=================================================

LSPs that a controller runs the PCE Initiated LSP protocol to establish can only be monitored by dynamic BFD.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Configuring dynamic BFD to monitor RSVP-TE Initiated LSPs is recommended. If no BFD session is configured, the LSP goes Up by default, but its actual status cannot be determined.




#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
3. Run [**mpls te bfd enable auto-primary-tunnel**](cmdqueryname=mpls+te+bfd+enable+auto-primary-tunnel) **pce-initiated-lsp**
   
   
   
   BFD for TE LSP is enabled globally.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.