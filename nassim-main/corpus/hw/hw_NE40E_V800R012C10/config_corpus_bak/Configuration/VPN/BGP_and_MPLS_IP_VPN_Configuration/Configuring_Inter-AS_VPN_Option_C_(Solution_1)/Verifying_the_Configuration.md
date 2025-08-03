Verifying the Configuration
===========================

After configuring inter-AS VPN Option C (solution 1), check information about all BGP peer relationships, VPNv4 routes on PEs, and IPv4 route labels on ASBRs.

#### Prerequisites

Inter-AS VPN Option C (solution 1) has been configured.


#### Procedure

* Run the [**display bgp**](cmdqueryname=display+bgp) **vpnv4** **all** **peer** command to check BGP peer relationships on the PE.
* Run the [**display bgp vpnv4**](cmdqueryname=display+bgp+vpnv4) **all** **routing-table** command to check the VPN-IPv4 routing table on the PE.
* Run the [**display bgp routing-table label**](cmdqueryname=display+bgp+routing-table+label) command to check information about IPv4 route labels on the ASBR.
* Run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* command to check the VPN routing table on the PE.