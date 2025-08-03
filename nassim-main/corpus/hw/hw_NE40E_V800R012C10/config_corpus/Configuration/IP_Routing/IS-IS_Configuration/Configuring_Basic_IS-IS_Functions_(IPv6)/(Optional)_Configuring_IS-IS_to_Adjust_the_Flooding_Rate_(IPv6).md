(Optional) Configuring IS-IS to Adjust the Flooding Rate (IPv6)
===============================================================

(Optional) Configuring IS-IS to Adjust the Flooding Rate (IPv6)

#### Context

In a scenario where a large number of LSPs need to be flooded at a time, for example, in a large-scale network, because the maximum number of LSPs that can be sent by IS-IS per second is limited, the time needed to complete the LSP flooding at a time may exceed the expected time, which affects the convergence efficiency on the entire network. In this case, you can increase the maximum IS-IS LSP flooding rate by increasing the maximum number of LSPs that can be sent per second during IS-IS LSP flooding. This speeds up IS-IS LSP flooding and network convergence. When the flooding pressure on the network is heavy and flow control is required, you can reduce the maximum number of LSPs that can be sent by IS-IS per second to slow down the IS-IS LSP flooding rate and relieve the flooding pressure on nodes.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis lsp flood-control max-count**](cmdqueryname=isis+lsp+flood-control+max-count) *max-count-value*
   
   
   
   The maximum number of LSPs that IS-IS sends every second is set.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.