Verifying the Configuration
===========================

After configuring inter-AS seamless MPLS+HVPN, you can check all BGP peer relationships, VPNv4 routing information on AGGs and MASGs, and the connectivity of the BGP LSP between each pair of an AGG and MASG.

#### Prerequisites

Inter-AS seamless MPLS+HVPN has been configured.


#### Procedure

* Run the [**display bgp**](cmdqueryname=display+bgp+vpnv4+all+peer) **vpnv4** **all** **peer** command on an AGG or MASG to check BGP peer relationship information.
* Run the [**display bgp vpnv4**](cmdqueryname=display+bgp+vpnv4+all+routing-table) **all** **routing-table** command to check the VPNv4 routing table on an AGG or MASG.
* Run the [**display bgp routing-table label**](cmdqueryname=display+bgp+routing-table+label) command on an AGG, AGG ASBR, core ASBR, or MASG to check label information of IPv4 routes.
* Run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* command to check the VRF table on an AGG or MASG.
* Run the [**display mpls lsp protocol bgp traffic-statistics inbound**](cmdqueryname=display+mpls+lsp+protocol+bgp+traffic-statistics+inbound) command to check the incoming traffic statistics of BGP LSPs.
* Run the [**display mpls lsp protocol bgp traffic-statistics**](cmdqueryname=display+mpls+lsp+protocol+bgp+traffic-statistics+outbound) **outbound** [ *ipv4-address* *mask-length* ] **verbose** command to check the outgoing traffic statistics of BGP LSPs.
* Run the [**display mpls lsp protocol bgp traffic-statistics outbound aggregated**](cmdqueryname=display+mpls+lsp+protocol+bgp+traffic-statistics+outbound+aggregated) command to check the traffic statistics of BGP LSPs aggregated by FEC.