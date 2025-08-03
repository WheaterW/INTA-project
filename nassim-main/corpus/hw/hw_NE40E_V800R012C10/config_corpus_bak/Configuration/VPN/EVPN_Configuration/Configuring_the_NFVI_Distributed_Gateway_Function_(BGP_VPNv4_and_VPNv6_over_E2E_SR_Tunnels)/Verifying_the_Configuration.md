Verifying the Configuration
===========================

After configuring the NFVI distributed gateway function, verify the configuration. On DC GWs, you can view the VPN peer relationships between DC GWs and VNFs and information about the UE routes received from VNFs.

#### Prerequisites

The NFVI distributed gateway function has been configured.


#### Procedure

* Run the [**display bgp**](cmdqueryname=display+bgp) { **vpnv4** | **vpnv6** } **vpn-instance** *vpn-instance-name* **peer** command on each DC GW to check whether the VPN BGP peer relationships between the DC GW and VNFs are **Established**.
* Run the [**display bgp vpnv4 vpn-instance**](cmdqueryname=display+bgp+vpnv4+vpn-instance) *vpn-instance-name* **routing-table** or [**display bgp vpnv6 vpn-instance**](cmdqueryname=display+bgp+vpnv6+vpn-instance) *vpn-instance-name* **routing-table** command on each DC GW to check whether the DC GW has received UE routes from VNFs and whether the next hop addresses of these routes are VNF addresses.
* Run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* or [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* command on each PE to check the VPN routing table of the PE. The command output shows UE and VNF route information.