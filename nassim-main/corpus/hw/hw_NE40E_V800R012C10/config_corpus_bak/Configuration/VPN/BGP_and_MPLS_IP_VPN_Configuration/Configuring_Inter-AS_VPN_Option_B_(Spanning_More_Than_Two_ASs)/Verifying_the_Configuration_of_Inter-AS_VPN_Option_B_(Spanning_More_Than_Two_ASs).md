Verifying the Configuration of Inter-AS VPN Option B (Spanning More Than Two ASs)
=================================================================================

After configuring inter-AS VPN Option B (spanning more
than two ASs), you can view the status of all BGP peer relationships
and VPNv4 routing information on PEs or ASBRs.

#### Prerequisites

Inter-AS VPN Option B (spanning more than two ASs) has been
configured.
#### Procedure

* Run the [**display bgp**](cmdqueryname=display+bgp) **vpnv4** **all** **peer** command
  on the PE or ASBR to check the status of all BGP peer relationships.
* Run the [**display bgp vpnv4**](cmdqueryname=display+bgp+vpnv4) **all** **routing-table** command on the PE or ASBR to check information about VPNv4 routes.
* Run the [**display
  ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* command on the PE to check information about the VPN routing table.