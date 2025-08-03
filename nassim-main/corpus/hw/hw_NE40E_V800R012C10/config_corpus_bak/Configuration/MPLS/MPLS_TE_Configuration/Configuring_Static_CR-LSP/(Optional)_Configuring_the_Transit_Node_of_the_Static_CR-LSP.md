(Optional) Configuring the Transit Node of the Static CR-LSP
============================================================

This section describes how to configure the transit nodes of a static CR-LSP. Before you set up a static CR-LSP, specify the transit nodes of the CR-LSP. This procedure is optional because the CR-LSP may have no transit node.

#### Context

If the static CR-LSP has only the ingress and egress, configuring a transit node is not needed. If the static CR-LSP has one or more transit nodes, perform the following steps on each transit node:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**static-cr-lsp transit**](cmdqueryname=static-cr-lsp+transit) *lsp-name* **incoming-interface** *interface-type* *interface-number* **in-label** *in-label* { **nexthop** *next-hop-address* | **outgoing-interface** *interface-type* *interface-number* } \* **out-label** *out-label* [ **ingress-lsrid** *ingress-lsrid* **egress-lsrid** *egress-lsrid* **tunnel-id** *tunnel-id* ] [ **bandwidth** [ **ct0** ] *bandwidth* ]
   
   
   
   The transit node of the static CR-LSP is configured.
   
   
   
   If you need to modify parameters except *lsp-name*, run the [**static-cr-lsp transit**](cmdqueryname=static-cr-lsp+transit) command without the need for running the [**undo static-cr-lsp transit**](cmdqueryname=undo+static-cr-lsp+transit) command first. This means that these parameters can be updated.
   
   The value of *lsp-name* on the transit node and the egress node cannot be the same as the existing names on the nodes. There are no other restrictions on the value.
   
   If an Ethernet interface is used as the outbound interface of an LSP, the **nexthop** *next-hop-address* parameter must be configured to ensure proper traffic forwarding along the LSP.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.