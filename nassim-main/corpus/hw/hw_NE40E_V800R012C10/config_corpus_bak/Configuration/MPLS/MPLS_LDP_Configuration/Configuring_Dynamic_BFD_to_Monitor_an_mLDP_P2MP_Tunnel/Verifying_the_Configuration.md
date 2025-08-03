Verifying the Configuration
===========================

After configuring dynamic BFD to monitor an mLDP P2MP tunnel, you can check BFD session information.

#### Prerequisites

Dynamic BFD has been configured to monitor an mLDP P2MP tunnel.


#### Procedure

* Run the [**display mpls bfd session protocol mldp p2mp**](cmdqueryname=display+mpls+bfd+session+protocol+mldp+p2mp+root-ip+lsp-id) [ **root-ip** *root-ip* { **lsp-id** *lsp-id* | **opaque-value** *opaque-value* } ] [ **bfd-type** **ldp-tunnel** ] command to check BFD session information.