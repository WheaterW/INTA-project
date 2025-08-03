Configuring the Egress of a Static LSP
======================================

A static LSP needs to be manually configured on the egress.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**static-lsp egress**](cmdqueryname=static-lsp+egress+incoming-interface+in-label) *lsp-name* [ **incoming-interface** *interface-type* *interface-number* ] **in-label** *in-label*
   
   
   
   The local node is configured as the egress of a specified LSP.
   
   To modify the **incoming-interface** *interface-type* *interface-number* and **in-label** *in-label* parameter settings, run the [**static-lsp egress**](cmdqueryname=static-lsp+egress) command to set new values, not requiring you to clear previous settings using the [**undo static-lsp egress**](cmdqueryname=undo+static-lsp+egress) command.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.