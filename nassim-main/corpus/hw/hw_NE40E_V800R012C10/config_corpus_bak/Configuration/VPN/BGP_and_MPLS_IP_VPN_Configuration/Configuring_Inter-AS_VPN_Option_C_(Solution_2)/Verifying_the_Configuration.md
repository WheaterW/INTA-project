Verifying the Configuration
===========================

After configuring inter-AS VPN Option C (solution 2), check information about all BGP peer relationships, VPNv4 routes on PEs, and labels of IPv4 routes on ASBRs.

#### Prerequisites

Inter-AS VPN Option C (solution 2) has been configured.


#### Procedure

* Run the [**display bgp**](cmdqueryname=display+bgp) **vpnv4** **all** **peer** command to check information about the specified VPNv4 peer on a PE.
* Run the [**display bgp vpnv4**](cmdqueryname=display+bgp+vpnv4) **all** **routing-table** command to check the VPN-IPv4 routing table on a PE.
* Run the [**display bgp routing-table label**](cmdqueryname=display+bgp+routing-table+label) command to check information about IPv4 route labels on an ASBR.
* Run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* command to check the VPN routing table on a PE.
* Run the [**display mpls route-state**](cmdqueryname=display+mpls+route-state) command to check the mapping between routes and LSPs on an ASBR.
* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command to check information about the routing table on an ASBR.
* Run the [**display mpls lsp**](cmdqueryname=display+mpls+lsp) command to check LDP LSP establishment status on an ASBR.