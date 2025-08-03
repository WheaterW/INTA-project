Enabling BFD Globally
=====================

BFD must be enabled globally before configurations relevant to BFD are performed.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   BFD is enabled globally on the local node, and the BFD view is displayed.
   
   Configurations relevant to BFD can be performed only after the [**bfd**](cmdqueryname=bfd) command is run globally.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.