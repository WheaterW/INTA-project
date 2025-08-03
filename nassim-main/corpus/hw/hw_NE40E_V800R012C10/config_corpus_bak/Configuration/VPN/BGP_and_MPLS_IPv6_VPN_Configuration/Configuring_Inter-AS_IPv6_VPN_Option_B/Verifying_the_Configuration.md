Verifying the Configuration
===========================

After configuring inter-AS IPv6 VPN Option B, you can view the status of all BGP peer relationships and VPNv6 routing information on PEs or ASBRs.

#### Prerequisites

Inter-AS IPv6 VPN Option B configurations are complete.


#### Procedure

* Run the [**display bgp**](cmdqueryname=display+bgp) **vpnv6** **all** **peer** command on a PE or ASBR to check the status of all BGP peer relationships.
* Run the [**display bgp vpnv6**](cmdqueryname=display+bgp+vpnv6) **all** **routing-table** command on a PE or ASBR to check VPNv6 route information.
* Run the [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* command on a PE to check VPN routing table information.
* Run the [**display mpls lsp asbr**](cmdqueryname=display+mpls+lsp+asbr) [ **nexthop** *nexthop-ipv6-address* [ **verbose** ] ] command on an ASBR to check information about LSPs created using BGP based on received BGP VPNv6 routes.
* Run the [**display mpls lsp protocol bgp**](cmdqueryname=display+mpls+lsp+protocol+bgp) [ **nexthop** *nexthop-ipv6-address* ] [ **lsr-role** { **egress** | **ingress** | **transit** } ] [ **verbose** ] command to check information about LSPs created using BGP based on received BGP IPv6 VPN routes.