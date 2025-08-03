Verifying the Configuration of MPLS OAM for an Associated Bidirectional LSP
===========================================================================

After configuring MPLS OAM for an associated bidirectional LSP, verify the configurations.

#### Prerequisites

MPLS OAM has been configured for an associated bidirectional LSP.


#### Procedure

* Run the [**display mpls oam ingress**](cmdqueryname=display+mpls+oam+ingress) { **all** | *t*unnel-type** **tunnel-number** | **tunnel-name** } [ **verbose** ] command to check MPLS OAM information on the ingress.
* Run the [**display mpls oam egress**](cmdqueryname=display+mpls+oam+egress) { **all** | **lsp-name** *lsp-name-value* | **lsr-id** *ip\_addr* **tunnel-id** *tunnelIdValue* } [ **verbose** ] command to check MPLS OAM information on the egress.