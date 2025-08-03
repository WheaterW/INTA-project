Verifying the GMPLS UNI Tunnel Configuration
============================================

After configuring a GMPLS UNI tunnel, you can view information about the GMPLS UNI tunnel and the tunnel status.

#### Prerequisites

A GMPLS UNI tunnel has been configured.


#### Procedure

* Run the [**display lmp peer**](cmdqueryname=display+lmp+peer) command to check information about LMP neighbors.
* Run the [**display explicit-path**](cmdqueryname=display+explicit-path+verbose) [ *path-name* ] [ **verbose** ] command to check information about the configured explicit path.
* Run the [**display mpls te gmpls tunnel path**](cmdqueryname=display+mpls+te+gmpls+tunnel+path+verbose) [ *path-name* ] [ **verbose** ] command to check GMPLS UNI tunnel path information.
* Run the [**display mpls te gmpls tunnel c-hop**](cmdqueryname=display+mpls+te+gmpls+tunnel+c-hop+tunnel-name+lsp-id) [ **tunnel-name** *tunnel-name* ] [ **lsp-id** *ingress-lsr-id* *egress-lsr-id* *tunnel-id* *lsp-id* ] command to check information about the calculated path for a GMPLS UNI tunnel.
* Run the [**display mpls gmpls lsp**](cmdqueryname=display+mpls+gmpls+lsp+in-label+incoming-interface+lsr-role) [ **in-label** *in-label* | **incoming-interface** *interface-type* *interface-number* | **lsr-role** { **egress** | **ingress** } | **out-label** *out-label* | **outgoing-interface** *interface-type* *interface-number* ] \* [ **verbose** ] command to check GMPLS UNI LSP information.
* Run the [**display mpls te gmpls tunnel**](cmdqueryname=display+mpls+te+gmpls+tunnel+name+verbose) [ **name** *gmpls-tunnel-name* ] [ **verbose** ] command to check information about a GMPLS UNI tunnel.
* Run the [**display mpls te gmpls tunnel-interface**](cmdqueryname=display+mpls+te+gmpls+tunnel-interface+name) [ **name** *gmpls-tunnel-name* ] command to check information about GMPLS UNI tunnel interfaces on the ingress EN and egress EN.