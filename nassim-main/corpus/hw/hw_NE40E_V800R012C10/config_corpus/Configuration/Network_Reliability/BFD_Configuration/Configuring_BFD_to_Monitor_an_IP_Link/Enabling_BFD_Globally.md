Enabling BFD Globally
=====================

BFD must be enabled globally before BFD is configured.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   BFD is enabled globally on the local node, and the BFD view is displayed.
   
   BFD can be configured only after the [**bfd**](cmdqueryname=bfd) command has been run globally.
3. (Optional) Run [**default-ip-address**](cmdqueryname=default-ip-address) *default-ip-value*
   
   
   
   The default multicast address is configured for a BFD session.
   
   In VS mode, this command is supported only by the admin VS.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.