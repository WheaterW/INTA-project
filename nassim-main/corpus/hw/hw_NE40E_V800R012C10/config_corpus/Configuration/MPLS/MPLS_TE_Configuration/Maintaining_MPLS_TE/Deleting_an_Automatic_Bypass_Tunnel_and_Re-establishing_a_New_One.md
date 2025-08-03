Deleting an Automatic Bypass Tunnel and Re-establishing a New One
=================================================================

If MPLS TE Auto FRR is enabled, a command is used to instruct a node to tear down an automatic bypass tunnel and reestablish a new one.

#### Procedure

1. Run the [**reset mpls te auto-frr**](cmdqueryname=reset+mpls+te+auto-frr) { **lsp-id** *ingress-lsrid tunnel-id* | **name** *bypass-tunnel-name* } command to tear down an automatic bypass tunnel and re-establish a new one.