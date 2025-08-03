Verifying the Configuration
===========================

After configuring the DCI solution, check the VPN instance, EVPN instance, VXLAN tunnel, and other configurations.

#### Prerequisites

A DCI solution has been configured.


#### Procedure

* Run the [**display ip vpn-instance**](cmdqueryname=display+ip+vpn-instance) *vpn-instance-name* command to check brief information about a specified VPN instance.
* Run the [**display ip vpn-instance**](cmdqueryname=display+ip+vpn-instance) **verbose** *vpn-instance-name* command to check detailed information about a specified VPN instance, including information in the IPv4 address family of the VPN instance.
* Run the [**display ip vpn-instance**](cmdqueryname=display+ip+vpn-instance) [ *vpn-instance-name* ] **interface** command to view information about the interfaces bound to a specified VPN instance.
* Run the [**display evpn vpn-instance**](cmdqueryname=display+evpn+vpn-instance) [ **name** *vpn-instance-name* ] command to check EVPN instance information.
* Run the [**display vxlan tunnel**](cmdqueryname=display+vxlan+tunnel) [ *tunnel-id* ] [ **verbose** ] command to check VXLAN tunnel information.
* Run the [**display evpn mac routing-table**](cmdqueryname=display+evpn+mac+routing-table) { **all-evpn-instance** | **mac-address** *mac-address* } command to check information about MAC routes of a specified EVPN instance.
* Run the [**display bgp evpn peer**](cmdqueryname=display+bgp+evpn+peer) [ [ *ipv4-address* ] **verbose** ] command to check information about BGP EVPN peers.
* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table** **mac-route** command to check MAC route information.
* Run the [**display bgp vpnv4**](cmdqueryname=display+bgp+vpnv4) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table** command to check BGP VPNv4 route information.
* Run the [**display bgp vpnv6**](cmdqueryname=display+bgp+vpnv6) { **all** | **route-distinguisher** *route-distinguisher* | **vpn-instance** *vpn-instance-name* } **routing-table** command to check BGP VPNv6 route information.