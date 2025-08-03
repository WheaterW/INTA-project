Verifying the Configuration
===========================

After configuring an mLDP P2MP LSP, verify mLDP P2MP LSP information on each node along the LSP and mLDP P2MP LSP connectivity on the root node.

#### Prerequisites

An mLDP P2MP LSP has been configured.


#### Procedure

* Run the [**ping**](cmdqueryname=ping+multicast-lsp+mldp+p2mp+root-ip+lsp-id+opaque-value) **multicast-lsp** **mldp** **p2mp** **root-ip** *root-ip-address* { **lsp-id** *lsp-id* | **opaque-value** *opaque-value* } command to check mLDP P2MP LSP connectivity on the root node.
* Run the [**display
  mpls mldp lsp**](cmdqueryname=display+mpls+mldp+lsp+p2mp+root-ip+lsp-id+opaque-value) **p2mp** [ **root-ip** *root-ip-address* { **lsp-id** *lsp-id* | **opaque-value** *opaque-value* } ] command to check P2MP LSP signaling information on the local node.
* Run the [**display
  mpls multicast-lsp protocol mldp**](cmdqueryname=display+mpls+multicast-lsp+protocol+mldp+p2mp+root-ip+lsp-id) **p2mp** [ **root-ip** *root-ip-address* { **lsp-id** *lsp-id* | **opaque-value** *opaque-value* } ] [ **lsr-role** { **bud** | **ingress** | **transit** | **egress** } ] command to check P2MP LSP forwarding information on the local node.