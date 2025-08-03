Verifying the Configuration
===========================

After configuring EVPN L3VPN over SRv6 TE Policy and L3VPN over MPLS to interwork in Option B mode, check information about all BGP peer relationships, EVPN routes on PEs or ASBRs, and BGP VPNv4/v6 routes on PEs or ASBRs.

#### Prerequisites

Interworking between EVPN L3VPN over SRv6 TE Policy and L3VPN over MPLS in Option B mode has been configured.


#### Procedure

* Run the [**display bgp vpnv4**](cmdqueryname=display+bgp+vpnv4) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table** [ *network* [ *prefix-length* ] ] command to check BGP VPN route information.
* Run the [**display bgp vpnv6**](cmdqueryname=display+bgp+vpnv6) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table** [ *network* [ *prefix-length* ] ] command to check BGP VPNv6 route information.
* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) **all** **routing-table** **prefix-route** *prefix* command to check EVPN IP prefix route information. Run the [**display ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* or [**display ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* command to check information about the VPN routes received from the remote device.