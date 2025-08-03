Verifying the Configuration of Inter-AS VPN Option C in an Independent Labeled Address Family (Solution 1)
==========================================================================================================

After configuring inter-AS VPN Option C (solution 1), check
information about all BGP peer relationships, VPNv4 routes on PEs
or ASBRs, and labels of IPv4 routes on ASBRs.

#### Prerequisites

Inter-AS VPN Option C (solution 1) has been configured.
#### Procedure

* Run the [**display bgp**](cmdqueryname=display+bgp) **vpnv4** **all** **peer** command
  to check the BGP peers on the PE.
* Run the [**display bgp vpnv4**](cmdqueryname=display+bgp+vpnv4) **all** **routing-table** command to check the VPN IPv4 routing table on the PE or ASBR.
* Run the [**display bgp
  labeled routing-table label**](cmdqueryname=display+bgp+labeled+routing-table+label) command to check information
  about the labels of the IPv4 routes on the ASBR.
* Run the [**display
  ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* command to check the VPN routing table on the PE.