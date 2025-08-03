Monitoring the Running Status of a BGP/MPLS IP VPN
==================================================

Monitoring the running status of a BGP/MPLS IP VPN involves checking VPN instance, VPNv4 peer, and BGP peer log information.

#### Context

In routine maintenance, you can run any of the following commands in all views to check the running status of a BGP/MPLS IP VPN.


#### Procedure

* Run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* [ [ *filter-option* ] [ **verbose** ] | **statistics** ] command to check the IP routing table of a VPN instance.
* Run the [**display ip vpn-instance**](cmdqueryname=display+ip+vpn-instance) [ **verbose** ] [ *vpn-instance-name* ] command to check VPN instance information.
* Run the [**display mpls lsp**](cmdqueryname=display+mpls+lsp) command to check LSP information.
* Run the [**display bgp vpnv4**](cmdqueryname=display+bgp+vpnv4) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table** *destination-address* [ *mask* | *mask-length* ] command to check information about a specific BGP VPNv4 routing entry.
* Run the [**display bgp vpnv4**](cmdqueryname=display+bgp+vpnv4) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table** **statistics** [ *match-options* ] command to check statistics about the BGP VPNv4 routing table.
* Run the [**display bgp vpnv4**](cmdqueryname=display+bgp+vpnv4) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table** [ *match-options* ] command to check information about the BGP VPNv4 routing table.
* Run the [**display bgp vpnv4**](cmdqueryname=display+bgp+vpnv4) { **all** | **vpn-instance** *vpn-instance-name* } **group** [ *group-name* ] command to check information about VPNv4 BGP peer groups.
* Run the [**display bgp vpnv4 peer**](cmdqueryname=display+bgp+vpnv4+peer) command to check information about BGP VPNv4 peers.
* Run the [**display bgp**](cmdqueryname=display+bgp) **vpnv4** { **all** | **vpn-instance** *vpn-instance-name* } **network** command to check the VPNv4 routes imported into the BGP routing table using the [**network**](cmdqueryname=network) command.
* Run the [**display bgp**](cmdqueryname=display+bgp) **vpnv4** **vpn-instance** *vpn-instance-name* { **peer** *ipv4-address* | **peer-group** *group-name* } **log-info** command to check the log information about BGP peers in the VPN instance IPv4 address family.