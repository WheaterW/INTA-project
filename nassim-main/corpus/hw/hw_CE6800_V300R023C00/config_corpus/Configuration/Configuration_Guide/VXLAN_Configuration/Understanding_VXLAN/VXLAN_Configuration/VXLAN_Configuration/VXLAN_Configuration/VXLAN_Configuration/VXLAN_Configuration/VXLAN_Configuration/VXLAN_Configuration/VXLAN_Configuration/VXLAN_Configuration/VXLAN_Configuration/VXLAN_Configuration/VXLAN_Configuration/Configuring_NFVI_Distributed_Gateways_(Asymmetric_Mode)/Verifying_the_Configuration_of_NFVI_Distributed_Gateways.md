Verifying the Configuration of NFVI Distributed Gateways
========================================================

Verifying the Configuration of NFVI Distributed Gateways

#### Procedure

1. Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) **vpn-instance** *vpn-instance-name* or [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) **vpn-instance** *vpn-instance-name* command on each L2GW/L3GW to check whether the L2GW/L3GW has received loopback routes from the peer DC gateway and whether the next hop addresses of these routes are the anycast VTEP address.
2. Run the [**display bgp evpn all routing-table**](cmdqueryname=display+bgp+evpn+all+routing-table) **peer** *peer-address* **advertised-routes** **prefix-route** command on each L2GW/L3GW to check whether the L2GW/L3GW has advertised locally imported VPN static routes, including Add-Path routes, to the peer DC gateway.