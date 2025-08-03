(Optional) Configuring Global Dynamic BandwidthPre-verification
===============================================================

Global dynamic bandwidth pre-verification enables a device to check dynamic bandwidth usage before a static CR-LSP, or a static bidirectional co-routed LSP is established.

#### Context

When dynamic services or both static and dynamic services are configured, a device only checks static bandwidth usage when a static CR-LSP or a static bidirectional co-routed LSP is configured. The configuration is successful even if the interface bandwidth is insufficient, and the interface status is down. To prevent such an issue, global dynamic bandwidth pre-verification can be configured. With this function enabled, the device can prompt a message indicating that the configuration fails in the preceding situation.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   MPLS is enabled globally, and the MPLS view is displayed.
3. Run [**mpls te**](cmdqueryname=mpls+te)
   
   
   
   MPLS TE is enabled globally.
   
   
   
   Global dynamic bandwidth pre-verification can only be configured after MPLS TE is enabled globally.
4. Run [**mpls te static-cr-lsp bandwidth-check deduct-rsvp-bandwidth**](cmdqueryname=mpls+te+static-cr-lsp+bandwidth-check+deduct-rsvp-bandwidth)
   
   
   
   Global dynamic bandwidth pre-verification is enabled.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.