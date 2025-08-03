Verifying the Configuration
===========================

After configuring inter-AS seamless MPLS, you can check established LSPs and the connectivity of BGP LSPs between a CSG and an MASG.

#### Prerequisites

Inter-AS seamless MPLS has been configured.


#### Procedure

* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command on a CSG or an MASG to check the routes to the peer end.
* Run the [**display mpls lsp**](cmdqueryname=display+mpls+lsp) command to check LSP information.
* Run the [**ping lsp**](cmdqueryname=ping+lsp+-a+-c+-exp+-h+-m+-r+-s+-t+-v+bgp) [ **-a** *source-ip* | **-c** *count* | **-exp** *exp-value* | **-h** *ttl-value* | **-m** *interval* | **-r** *reply-mode* | **-s** *packet-size* | **-t** *time-out* | **-v** ] \* **bgp** *destination-iphost* *mask-length* [ *ip-address* ] command on a CSG or MASG to check the BGP LSP connectivity.
* Run the [**display mpls lsp protocol bgp traffic-statistics inbound**](cmdqueryname=display+mpls+lsp+protocol+bgp+traffic-statistics+inbound) command to check the incoming traffic statistics of BGP LSPs.
* Run the [**display mpls lsp protocol bgp traffic-statistics**](cmdqueryname=display+mpls+lsp+protocol+bgp+traffic-statistics+outbound) **outbound** [ *ipv4-address* *mask-length* ] **verbose** command to check the outgoing traffic statistics of BGP LSPs.
* Run the [**display mpls lsp protocol bgp traffic-statistics outbound aggregated**](cmdqueryname=display+mpls+lsp+protocol+bgp+traffic-statistics+outbound+aggregated) command to check the traffic statistics of BGP LSPs aggregated by FEC.