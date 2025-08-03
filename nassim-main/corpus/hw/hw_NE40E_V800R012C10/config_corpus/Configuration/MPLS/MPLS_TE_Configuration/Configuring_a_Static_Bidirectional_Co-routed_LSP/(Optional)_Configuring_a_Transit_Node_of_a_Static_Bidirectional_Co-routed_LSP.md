(Optional) Configuring a Transit Node of a Static Bidirectional Co-routed LSP
=============================================================================

The transit node of a static bidirectional co-routed LSP needs to be manually specified. This configuration is optional because a static bidirectional co-routed LSP may have no transit node.

#### Context

Skip this procedure if a static bidirectional co-routed LSP has only an ingress and an egress. If a static bidirectional co-routed LSP has a transit node, perform the following steps on this transit node:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bidirectional static-cr-lsp**](cmdqueryname=bidirectional+static-cr-lsp) **transit** *lsp-name*
   
   
   
   A static bidirectional CR-LSP is created, and its transit view is displayed.
   
   
   
   The value of *lsp-name* cannot be the same as an existing LSP name on the device.
3. Run [**forward**](cmdqueryname=forward) **in-label** *in-label-value* { **nexthop** *next-hop-address* | **outgoing-interface** *interface-type* *interface-number* } \* **out-label** *out-label-value* [ **ingress-lsrid** *ingress-lsrid* **egress-lsrid** *egress-lsrid* **tunnel-id** *tunnel-id* ] [ **bandwidth** **ct0** *bandwidth* | **pir** *pir* ] \*
   
   
   
   A forward CR-LSP is configured on the transit node.
4. Run [**backward**](cmdqueryname=backward) **in-label** *in-label-value* { **nexthop** *next-hop-address* | **outgoing-interface** *interface-type* *interface-number* } \* **out-label** *out-label-value* [ **bandwidth** **ct0** *bandwidth* | **pir** *pir* ] \*
   
   
   
   A reverse CR-LSP is configured on the transit node.
5. (Optional) Run [**description**](cmdqueryname=description) *text*
   
   
   
   A description is configured for the static bidirectional co-routed CR-LSP.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.