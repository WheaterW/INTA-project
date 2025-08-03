Verifying the Static CR-LSP Configuration
=========================================

After the configuration of a static CR-LSP, you can view the static CR-LSP status.

#### Prerequisites

The static CR-LSP has been configured.


#### Procedure

* Run the [**display mpls static-cr-lsp**](cmdqueryname=display+mpls+static-cr-lsp) [ *lsp-name* ] [ **verbose** ] command to check information about the static CR-LSP.
* Run the [**display mpls te tunnel**](cmdqueryname=display+mpls+te+tunnel) [ **destination** *ip-address* ] [ **lsp-id** *ingress-lsr-id* *session-id* *local-lsp-id* ] [ **lsr-role** { **all** | **egress** | **ingress** | **remote** | **transit** } ] [ **name** *tunnel-name* ] [ { **incoming-interface** | **interface** | **outgoing-interface** } *interface-type* *interface-number* ] [ **verbose** ] command to check information about the tunnel.
* Run the [**display mpls te tunnel statistics**](cmdqueryname=display+mpls+te+tunnel+statistics) or [**display mpls lsp statistics**](cmdqueryname=display+mpls+lsp+statistics) command to check the tunnel statistics.
* Run the [**display mpls te tunnel-interface**](cmdqueryname=display+mpls+te+tunnel-interface) command to check information about the tunnel interface on the ingress.