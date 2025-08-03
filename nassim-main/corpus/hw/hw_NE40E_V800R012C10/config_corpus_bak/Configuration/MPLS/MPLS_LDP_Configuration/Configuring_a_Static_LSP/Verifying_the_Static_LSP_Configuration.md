Verifying the Static LSP Configuration
======================================

After configuring the static LSP, verify its information on a local node.

#### Prerequisites

The configurations of a static LSP are complete.


#### Procedure

* Run the [**display mpls static-lsp**](cmdqueryname=display+mpls+static-lsp+include+exclude+verbose) [ *lsp-name* ] [ { **include** | **exclude** } *ip-address* *mask-length* ]
  [ **verbose** ] command to check information about local static LSPs.
* Run the [**display mpls lsp protocol static**](cmdqueryname=display+mpls+lsp+protocol+static+include+exclude) [ { **include** | **exclude** } *destaddr* *masklen* ] [ **incoming-interface** *in-port-type* *in-port-num* ][ **outgoing-interface** *out-port-type* *out-port-num* ] [ **in-label** *in-label-value* ] [ **out-label** *out-label-value* ] [ **nexthop** *nexthopaddr* ] [ **lsr-role**{ **ingress** | **transit** | **egress** } ] [ **verbose** ] command to check information about static LSPs.