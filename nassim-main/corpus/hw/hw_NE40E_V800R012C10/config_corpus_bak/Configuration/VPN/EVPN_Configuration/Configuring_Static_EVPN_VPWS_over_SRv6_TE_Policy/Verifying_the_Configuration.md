Verifying the Configuration
===========================

After configuring static EVPN VPWS over SRv6 TE Policy, verify EVPL instance information.

#### Prerequisites

Static EVPN VPWS over SRv6 TE Policy has been configured.


#### Procedure

* Run the [**display bgp evpn evpl**](cmdqueryname=display+bgp+evpn+evpl) command to check all EVPL instance information.
* Run the [**display bgp evpn**](cmdqueryname=display+bgp+evpn) { **all** | **route-distinguisher** *route-distinguisher* } **routing-table** [ { **ad-route** | **es-route** | **inclusive-route** | **mac-route** | **prefix-route** } *prefix* ] command to check BGP EVPN route information. The command output shows that the value of **Relay Tunnel Out-Interface** is **SRv6 TE Policy**.
* Run the [**display evpn vpn-instance**](cmdqueryname=display+evpn+vpn-instance) [ **name** *vpn-instance-name* ] **tunnel-info** command to check information about the tunnel associated with the specified EVPN instance.
* Run the [**display evpn vpn-instance name**](cmdqueryname=display+evpn+vpn-instance+name)*vpn-instance-name* **tunnel-info** **nexthop** *nexthopIpv6Addr* command to check information about the tunnel that is associated with the specified EVPN instance and matches the specified next hop.