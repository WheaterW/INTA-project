Verifying the Configuration of Inter-AS IPv6 VPN-Option C (Solution 1)
======================================================================

After inter-AS IPv6 VPN Option C is configured, you can
view information about all BGP peer relationships, VPNv6 routing information
and IPv6 VPN routing information on the PE, and information about
labeled IPv4 routes on the ASBR.

#### Prerequisites

The Inter-AS IPv6 VPN-Option C function has been configured.
#### Procedure

* Run the [**display bgp**](cmdqueryname=display+bgp) **vpnv6** **all** **peer** command
  to check the BGP peers on the PE.
* Run the [**display bgp vpnv6**](cmdqueryname=display+bgp+vpnv6) **all** **routing-table** command to check the VPNv6 routing table on the PE.
* Run the [**display bgp routing-table
  label**](cmdqueryname=display+bgp+routing-table+label) command to check information about the labels
  of the IPv4 routes on the ASBR.
* Run the [**display
  ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) [ *vpn-instance-name* ] command to check the VPN-IPv6 routing table on the PE.