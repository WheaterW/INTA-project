Verifying the P2MP TE Tunnel Configuration
==========================================

After configuring a P2MP TE tunnel, you can view information about the tunnel when it is in the Up state.

#### Prerequisites

A P2MP TE tunnel has been configured.


#### Procedure

* Run the [**display mpls te p2mp tunnel-interface**](cmdqueryname=display+mpls+te+p2mp+tunnel-interface) command to check information about the P2MP TE tunnel interface on the ingress and all sub-LSPs.
* Run the [**display mpls te p2mp-template**](cmdqueryname=display+mpls+te+p2mp-template) command to check P2MP TE tunnel template configurations and information about P2MP TE tunnels established using this template.
* Run the [**display mpls te leaf-list**](cmdqueryname=display+mpls+te+leaf-list) command to check information about the leaf list configured on the ingress.
* Run the [**display mpls te p2mp tunnel path**](cmdqueryname=display+mpls+te+p2mp+tunnel+path) command to check the path attributes of the P2MP TE tunnel.
* Run the [**display mpls multicast-lsp protocol p2mp-te**](cmdqueryname=display+mpls+multicast-lsp+protocol+p2mp-te) command to check the sub-LSP status and MPLS forwarding entries, including the incoming label, outgoing label, inbound interface, and outbound interface of each sub-LSP.
* Run the [**display mpls multicast-lsp statistics protocol p2mp-te**](cmdqueryname=display+mpls+multicast-lsp+statistics+protocol+p2mp-te) command to check statistics about sub-LSPs that pass through a local node.
* Run the [**display mpls rsvp-te p2mp lsp**](cmdqueryname=display+mpls+rsvp-te+p2mp+lsp) command to check information about RSVP signaling of the P2MP LSP.
* Run the [**display mpls rsvp-te p2mp session**](cmdqueryname=display+mpls+rsvp-te+p2mp+session) command to check statistics about the RSVP signaling packets sent and received over the P2MP TE tunnel.
* Run the [**display mpls rsvp-te p2mp statistics**](cmdqueryname=display+mpls+rsvp-te+p2mp+statistics) command to check information about RSVP signaling packets.

#### Follow-up Procedure

If errors occur in tunnel services, perform the following to quickly restore the services if no other workarounds are available.

* Run the [**reset mpls te auto-tunnel p2mp name**](cmdqueryname=reset+mpls+te+auto-tunnel+p2mp+name)*tunnel-name* command in the user view to reestablish the P2MP TE tunnel.
* Run the [**reset mpls rsvp-te p2mp sub-lsp**](cmdqueryname=reset+mpls+rsvp-te+p2mp+sub-lsp)*tunnel-id* *lsp-id* *ingress-lsr-id* *sub-group-id* *sub-group-origin-id* *s2l-destination* command in the user view to restart the sub-LSP of the P2MP TE tunnel.