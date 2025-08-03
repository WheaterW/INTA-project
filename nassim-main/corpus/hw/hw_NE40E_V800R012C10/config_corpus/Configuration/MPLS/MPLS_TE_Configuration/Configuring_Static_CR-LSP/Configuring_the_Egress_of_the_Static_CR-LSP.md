Configuring the Egress of the Static CR-LSP
===========================================

This section describes how to configure the egress of a static CR-LSP. Before you set up a static CR-LSP, specify the egress of the CR-LSP.

#### Context

Perform the following steps on the egress of the static CR-LSP:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**static-cr-lsp egress**](cmdqueryname=static-cr-lsp+egress) *lsp-name-val* **incoming-interface** *interface-type* *interface-number* **in-label** *in-label* [ **lsrid** *ingress-lsr-id* **tunnel-id** *tunnel-id* ]
   
   
   
   The egress is configured for a specified static CR-LSP.
   
   
   
   To modify the **incoming-interface** *interface-type* *interface-number* and **in-label** *in-label-value* values, run the [**static-cr-lsp egress**](cmdqueryname=static-cr-lsp+egress) command to set new values. There is no need to run the [**undo static-cr-lsp egress**](cmdqueryname=undo+static-cr-lsp+egress) command to delete the original settings. This means that these parameters can be changed.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.