Monitoring the Running Status of a BGP/MPLS IPv6 VPN
====================================================

Monitoring the running status of a BGP/MPLS IPv6 VPN involves checking VPN instance information, VPNv6 peer information, and BGP peer log information.

#### Context

In routine maintenance, the following commands can be run in any view to display BGP/MPLS IPv6 VPN information.


#### Procedure

* Run the [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* [ [ *filter-option* ] [ **verbose** ] | **statistics** ] command to check the routing table of the VPN instance IPv6 address family on the PE.
* Run the [**display ip vpn-instance**](cmdqueryname=display+ip+vpn-instance) [ **verbose** | **brief** ] [ *vpn-instance-name* ] command to check information about the VPN instance IPv6 address family.
* Run the [**display mpls lsp**](cmdqueryname=display+mpls+lsp) command to check LSP information.
* Run the [**display bgp vpnv6**](cmdqueryname=display+bgp+vpnv6) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table** *destination-address* [ *mask-length* ] command to check entries in the routing table of the BGP-VPN instance IPv6 address family.
* Run the [**display bgp vpnv6**](cmdqueryname=display+bgp+vpnv6) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table statistics** [ *match-options* ] command to check statistics about the routing table of the BGP-VPN instance IPv6 address family.
* Run the [**display bgp vpnv6**](cmdqueryname=display+bgp+vpnv6) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table** [ *match-options* ] command to check information about the routing table of the BGP-VPN instance IPv6 address family.
* Run the [**display bgp**](cmdqueryname=display+bgp) **vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **group** [ *group-name* ] command to check VPNv6 BGP peer group information.
* Run the [**display bgp**](cmdqueryname=display+bgp) **vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **peer** [ [ *peer-address* ] **verbose** ] command to check VPNv6 BGP peer information.
* Run the [**display bgp**](cmdqueryname=display+bgp) **vpnv6** { **all** | **vpn-instance** *vpn-instance-name* } **network** command to check VPNv6 route information advertised by BGP.
* Run the [**display bgp**](cmdqueryname=display+bgp) **vpnv6** **vpn-instance** *vpn-instance-name* { **peer** *ipv6-address* | **peer-group** *group-name* } **log-info** command to check log information about the BGP peers in the BGP-VPN instance IPv6 address family.