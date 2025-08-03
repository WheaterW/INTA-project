Configuring the Ingress of a Static LSP
=======================================

A static LSP must be manually configured on the ingress.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**static-lsp ingress**](cmdqueryname=static-lsp+ingress+destination+nexthop+outgoing-interface) *lsp-name* **destination** *ip-address* { *mask-length* | *mask* } { **nexthop** *next-hop-address* | **outgoing-interface** *interface-type* *interface-number* } **out-label** *out-label*
   
   
   
   The local node is configured as the ingress of a specified LSP.
   
   
   
   To modify the **destination** *destination-address*, **nexthop** *next-hop-address*, **outgoing-interface** *interface-type interface-number*, and **out-label** *out-label* parameter settings, run the [**static-lsp ingress**](cmdqueryname=static-lsp+ingress) command to set new values directly, not requiring you to clear previous settings using the [**undo static-lsp ingress**](cmdqueryname=undo+static-lsp+ingress) command.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You are advised to specify a next hop for a static LSP. Ensure that the local routing table contains a routing entry that exactly matches the specified destination IP address and next-hop IP address.
   
   If an Ethernet interface is used as an outbound interface of an LSP, you must specify the **nexthop** *next-hop-address* parameter to ensure normal traffic forwarding on the LSP.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.