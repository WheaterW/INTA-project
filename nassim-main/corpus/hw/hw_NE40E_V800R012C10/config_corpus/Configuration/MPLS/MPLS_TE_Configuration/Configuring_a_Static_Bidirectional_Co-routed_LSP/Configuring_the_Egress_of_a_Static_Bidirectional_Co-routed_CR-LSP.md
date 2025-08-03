Configuring the Egress of a Static Bidirectional Co-routed CR-LSP
=================================================================

The egress of a static bidirectional co-routed CR-LSP needs to be manually specified.

#### Context

Perform the following steps on the egress of a static bidirectional co-routed CR-LSP:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bidirectional static-cr-lsp**](cmdqueryname=bidirectional+static-cr-lsp) **egress** *lsp-name*
   
   
   
   A static bidirectional CR-LSP is created, and its egress view is displayed.
3. Run [**forward**](cmdqueryname=forward) **in-label** *in-label-value* [ **lsrid** *ingress-lsr-id* **tunnel-id** *ingress-tunnel-id* ]
   
   
   
   A forward CR-LSP is configured on the egress.
   
   
   
   If **lsrid** *ingress-lsr-id* **tunnel-id** *ingress-tunnel-id* is specified in this command, the system checks whether the tunnel destination IP address on the egress and the specified value of *ingress-lsr-id* are consistent. If the specified value of *ingress-lsr-id* is different from the tunnel destination IP address on the egress, the tunnel cannot go up. As a result, the forward and reverse CR-LSPs configured on the egress cannot go up.
4. Run [**backward**](cmdqueryname=backward) { **nexthop** *next-hop-address* | **outgoing-interface** *interface-type* *interface-number* } \* **out-label** *out-label-value* [ **bandwidth** **ct0** *bandwidth* | **pir** *pir* ] \*
   
   
   
   A reverse CR-LSP is configured on the egress.
   
   
   
   The *bandwidth* parameter specifies the reserved bandwidth for a reverse CR-LSP. The *bandwidth* value cannot be higher than the maximum reservable link bandwidth. If the specified bandwidth is higher than the maximum reservable link bandwidth, the CR-LSP cannot go up.
5. (Optional) Run [**description**](cmdqueryname=description) *text*
   
   
   
   A description is configured for the static bidirectional co-routed CR-LSP.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.