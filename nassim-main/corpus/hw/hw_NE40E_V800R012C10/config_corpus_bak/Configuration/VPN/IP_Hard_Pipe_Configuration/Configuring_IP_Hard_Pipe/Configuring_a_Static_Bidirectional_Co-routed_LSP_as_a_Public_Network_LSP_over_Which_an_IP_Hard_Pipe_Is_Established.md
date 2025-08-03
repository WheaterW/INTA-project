Configuring a Static Bidirectional Co-routed LSP as a Public Network LSP over Which an IP Hard Pipe Is Established
==================================================================================================================

A static bidirectional co-routed LSP can be configured to implement public network service isolation and label forwarding for PW packets transmitted along an IP hard pipe.

#### Usage Scenario

IP hard pipe is a pipe technology that establishes a static PW over a static bidirectional co-routed LSP to simulate an SDH private line. To enable the hard pipe function for a static bidirectional co-routed LSP so that this LSP is used as the public network LSP for IP hard pipe services, run the [**hard-pipe enable**](cmdqueryname=hard-pipe+enable) command.

A static bidirectional co-routed LSP involves three roles: ingress, transit node, and egress. The [**hard-pipe enable**](cmdqueryname=hard-pipe+enable) command must be configured on all nodes.


#### Procedure

* Configure the ingress node.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bidirectional static-cr-lsp**](cmdqueryname=bidirectional+static-cr-lsp) **ingress** *tunnel-name* command to enter the static bidirectional LSP view on the ingress node.
  3. Run the [**hard-pipe enable**](cmdqueryname=hard-pipe+enable) command to enable the IP hard pipe function for the static bidirectional LSP on the ingress node.
  4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure the transit node.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bidirectional static-cr-lsp**](cmdqueryname=bidirectional+static-cr-lsp) **transit** *lsp-name* command to enter the static bidirectional LSP view on the transit node.
  3. Run the [**hard-pipe enable**](cmdqueryname=hard-pipe+enable) command to enable the IP hard pipe function for the static bidirectional LSP on the transit node.
  4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure the egress node.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**bidirectional static-cr-lsp**](cmdqueryname=bidirectional+static-cr-lsp) **egress** *lsp-name* command to enter the static bidirectional LSP view on the egress node.
  3. Run the [**hard-pipe enable**](cmdqueryname=hard-pipe+enable) command to enable the IP hard pipe function for the static bidirectional LSP on the egress node.
  4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.