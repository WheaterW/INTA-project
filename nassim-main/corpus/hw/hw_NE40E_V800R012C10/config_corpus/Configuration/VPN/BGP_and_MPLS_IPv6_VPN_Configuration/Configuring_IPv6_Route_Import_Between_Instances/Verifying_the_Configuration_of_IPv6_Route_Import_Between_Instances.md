Verifying the Configuration of IPv6 Route Import Between Instances
==================================================================

After configuring IPv6 route import between instances,
you can check IPv6 route import results.

#### Prerequisites

IPv6 route import between instances has been configured.
#### Procedure

* Run the [**display
  ipv6 routing-table vpn-instance**](cmdqueryname=display+ipv6+routing-table+vpn-instance) *vpn-instance-name* command to check IPv6 routes imported to a specific VPN instance.
* Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) command to check IPv6 public network routes.
* Run the [**display bgp vpnv6**](cmdqueryname=display+bgp+vpnv6) { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** *ipv6-address* [ *prefix-length* ] command to check IPv6 VPN BGP routes.
* Run the [**display bgp ipv6
  routing-table**](cmdqueryname=display+bgp+ipv6+routing-table) *ipv6-address* [ *prefix-length* ] command to check IPv6 public network BGP
  routes.