(Optional) Configuring IPv6 IS-IS to Adjust the Flooding Rate
=============================================================

(Optional) Configuring IPv6 IS-IS to Adjust the Flooding Rate

#### Context

In a scenario where a large number of LSPs need to be flooded at a time, for example, in a large-scale network, because the maximum number of LSPs that can be sent by IS-IS per second is limited, the time needed to complete the LSP flooding at a time may exceed the expected time, which affects the convergence efficiency on the entire network. In this case, you can increase the maximum IS-IS LSP flooding rate by increasing the maximum number of LSPs that can be sent per second during IS-IS LSP flooding. This speeds up IS-IS LSP flooding and network convergence. When the flooding pressure on the network is heavy and flow control is required, you can reduce the maximum number of LSPs that can be sent by IS-IS per second to slow down the IS-IS LSP flooding rate and relieve the flooding pressure on nodes.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Set the maximum number of LSPs that can be sent by IS-IS per second.
   
   
   ```
   [isis lsp flood-control max-count](cmdqueryname=isis+lsp+flood-control+max-count) max-count-value
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```