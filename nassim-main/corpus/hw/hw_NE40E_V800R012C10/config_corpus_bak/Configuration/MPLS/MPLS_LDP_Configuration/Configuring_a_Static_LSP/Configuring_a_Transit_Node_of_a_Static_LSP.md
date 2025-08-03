Configuring a Transit Node of a Static LSP
==========================================

A static LSP needs to be manually configured on each transit node.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**static-lsp transit**](cmdqueryname=static-lsp+transit+incoming-interface+in-label+nexthop) *lsp-name* [ **incoming-interface** *interface-type* *interface-number* ] **in-label** *in-label* { **nexthop** *next-hop-address* | **outgoing-interface** *interface-type* *interface-number* } \* **out-label** *out-label*
   
   
   
   The local node is configured as a transit node of a specified LSP.
   
   
   
   To modify the **incoming-interface** *interface-type* *interface-number*, **in-label** *in-label*, **nexthop** *next-hop-address*, **outgoing-interface** *interface-type* *interface-number*, or **out-label** *out-label* value, run the [**static-lsp transit**](cmdqueryname=static-lsp+transit) command to set a new value. You do not need to run the [**undo static-lsp transit**](cmdqueryname=undo+static-lsp+transit) command to cancel the original setting.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You are advised to specify the next hop when configuring a static LSP, so that the local routing table will contain the routing entry that exactly matches the specified next hop IP address.
   
   If an Ethernet interface is used as an outbound interface, the **nexthop** *next-hop-address* parameter must be configured to ensure normal traffic forwarding on the LSP.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.