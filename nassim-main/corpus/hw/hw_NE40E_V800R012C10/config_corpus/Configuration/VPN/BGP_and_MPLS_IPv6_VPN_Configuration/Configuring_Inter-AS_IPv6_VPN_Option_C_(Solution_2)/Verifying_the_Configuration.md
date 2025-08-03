Verifying the Configuration
===========================

After configuring inter-AS IPv6 VPN Option C (solution 2), check the establishment status of all BGP peer relationships, VPNv6 and IPv6 VPN routes on PEs, IPv4 route labels on ASBRs, and LDP LSP information on ASBRs.

#### Prerequisites

Inter-AS IPv6 VPN Option C (solution 2) has been configured.


#### Procedure

* Run the [**display bgp**](cmdqueryname=display+bgp) **vpnv6** **all** **peer** command to check BGP peer relationships on a PE.
* Run the [**display bgp vpnv6**](cmdqueryname=display+bgp+vpnv6) **all** **routing-table** command to check information about the VPNv6 routing table on a PE.
* Run the [**display bgp routing-table label**](cmdqueryname=display+bgp+routing-table+label) command to check IPv4 route labels on an ASBR.
* Run the [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* command to check the IPv6 VPN routing table on a PE.
* Run the [**display mpls route-state**](cmdqueryname=display+mpls+route-state) [ **vpn-instance** *vpn-instance-name* ] [ { **exclude** | **include** } { **idle** | **ready** | **settingup** } \* | *destination-address* *mask-length* ] [ **verbose** ] command to check the matching relationship between routes and an LSP on an ASBR.
* Run the [**display mpls lsp**](cmdqueryname=display+mpls+lsp) command to check whether LDP LSPs have been set up on an ASBR.