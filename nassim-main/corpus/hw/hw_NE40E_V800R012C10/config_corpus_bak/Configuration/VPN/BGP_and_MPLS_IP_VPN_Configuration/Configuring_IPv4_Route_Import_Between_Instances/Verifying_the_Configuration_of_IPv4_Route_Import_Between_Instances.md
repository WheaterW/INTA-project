Verifying the Configuration of IPv4 Route Import Between Instances
==================================================================

After configuring IPv4 route import between instances on
a device, you can check imported IPv4 routes on the device.

#### Prerequisites

IPv4 route import between instances has been configured.
#### Procedure

* Run the [**display
  ip routing-table vpn-instance**](cmdqueryname=display+ip+routing-table+vpn-instance) *vpn-instance-name* command to check IPv4 routes imported to a specific VPN instance.
* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command to check IPv4 public network routes.
* Run the [**display bgp vpnv4**](cmdqueryname=display+bgp+vpnv4) { **all** | **vpn-instance** *vpn-instance-name* } **routing-table** *ipv4-address* [ *mask* | *mask-length* ] command to check IPv4 VPN BGP routes.
* Run the [**display bgp routing-table**](cmdqueryname=display+bgp+routing-table) *ipv4-address* [ *mask* | *mask-length* ] command to check IPv4 public
  network BGP routes.