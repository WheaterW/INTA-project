Configuring the Ingress of a Static Bidirectional Co-routed LSP
===============================================================

The ingress of a static bidirectional co-routed LSP needs to be manually specified.

#### Context

Perform the following steps on the ingress of a static bidirectional co-routed LSP:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bidirectional static-cr-lsp**](cmdqueryname=bidirectional+static-cr-lsp) **ingress** *tunnel-name*
   
   
   
   A static bidirectional CR-LSP is created, and its ingress view is displayed.
3. Run [**forward**](cmdqueryname=forward) { **nexthop** *next-hop-address* | **outgoing-interface** *interface-type* *interface-number* } \* **out-label** *out-label-value* [ **bandwidth** **ct0** *bandwidth* | **pir** *pir* ] \*
   
   
   
   A forward CR-LSP is configured on the ingress. The *bandwidth* parameter specifies the reserved bandwidth for the forward CR-LSP. The *bandwidth* value cannot be higher than the maximum reservable link bandwidth. If the specified bandwidth is higher than the maximum reservable link bandwidth, the CR-LSP cannot go up.
4. Run [**backward**](cmdqueryname=backward) **in-label** *in-label-value* [ **lsrid** *ingress-lsr-id* **tunnel-id** *ingress-tunnel-id* ]
   
   
   
   A reverse CR-LSP is specified on the ingress.
5. (Optional) Run [**description**](cmdqueryname=description) *text*
   
   
   
   A description is configured for the static bidirectional co-routed CR-LSP.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.