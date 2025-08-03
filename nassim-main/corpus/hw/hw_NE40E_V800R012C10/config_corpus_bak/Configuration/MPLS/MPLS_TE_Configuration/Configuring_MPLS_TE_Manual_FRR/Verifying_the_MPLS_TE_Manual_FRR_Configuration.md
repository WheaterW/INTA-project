Verifying the MPLS TE Manual FRR Configuration
==============================================

After configuring MPLS TE manual FRR, you can view detailed information about the bypass tunnel.

#### Prerequisites

The MPLS TE manual FRR function has been configured.


#### Procedure

* Run the [**display mpls lsp**](cmdqueryname=display+mpls+lsp) command to check information about the primary tunnel.
* Run the [**display mpls te tunnel-interface**](cmdqueryname=display+mpls+te+tunnel-interface) command to check information about the tunnel interface on the ingress of a primary or bypass tunnel.
* Run the [**display mpls te tunnel path**](cmdqueryname=display+mpls+te+tunnel+path) command to check information about paths of a primary or bypass tunnel.