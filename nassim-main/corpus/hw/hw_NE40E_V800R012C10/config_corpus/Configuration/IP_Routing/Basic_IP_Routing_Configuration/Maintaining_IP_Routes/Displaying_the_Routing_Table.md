Displaying the Routing Table
============================

Viewing information about the routing table helps locate faults on the network.

#### Context

It is necessary to check the information in the routing table using display commands in order to locate routing problems. The display commands can be used in all views. Common commands for displaying routing information are listed as follows:


#### Procedure

* To check brief information about activated routes in the IP routing table, run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command.
* To check detailed information about the IP routing table, run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) **verbose** command.
* To check limits on the number of routes and prefixes, run the [**display ip routing-table limit**](cmdqueryname=display+ip+routing-table+limit) [ **all-vpn-instance** | **vpn-instance** *vpn-instance-name* ] command.
* To check the number of routes, run the [**display ip routing-table route-number**](cmdqueryname=display+ip+routing-table+route-number) command.
* To check the route to the specified destination IP address, run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) *ip-address* [ *mask* | *mask-length* ] [ **longer-match** ] [ **verbose** ] command.
* To check routes to the specified range of destination IP addresses, run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) *ip-address1* { *mask1* | *mask-length1* } *ip-address2* { *mask2* | *mask-length2* } [ **verbose** ] command.
* To check the routes discovered by the specified protocol, run the [**display ip routing-table protocol**](cmdqueryname=display+ip+routing-table+protocol) { **direct** | **ospf** | **isis** | **static** | **rip** | **bgp** | **unr** } [ **inactive** | **verbose** ] command.
* To check general information about the routing table, run the [**display ip routing-table statistics**](cmdqueryname=display+ip+routing-table+statistics) command.
* To check brief information about the VPN routing table, run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) **vpn-instance** *vpn-instance-name* command.
* To check detailed information about the VPN routing table, run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) **vpn-instance** *vpn-instance-name* **verbose** command.
* To check detailed information about the route to the specified destination IP address in the VPN routing table, run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) **vpn-instance** *vpn-instance-name* *ip-address* [ *mask* | *mask-length* ] [ **longer-match** ] [ **verbose** ] command.
* To check detailed information about the routes to the specified network segment in the VPN routing table, run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) **vpn-instance** *vpn-instance-name* *ip-address1* { *mask1* | *mask-length1* } *ip-address2* { *mask2* | *mask-length2* } [ **verbose** ] command.
* To check brief information about activated routes in the IPv6 routing table, run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) command.
* To check detailed information about the IPv6 routing table, run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) **verbose** command.
* To check brief information about the IPv6 routing table, run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) [ **vpn-instance** *vpn-instance-name* ] **simple** command.
* To check limits on the number of IPv6 routes and prefixes, run the [**display ipv6 routing-table limit**](cmdqueryname=display+ipv6+routing-table+limit) [ **all-vpn-instance** | **vpn-instance** *vpn-instance-name* ] command.
* To check the number of IPv6 routes, run the [**display ipv6 routing-table route-number**](cmdqueryname=display+ipv6+routing-table+route-number) command.
* To check the route to the specified destination IPv6 address, run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) *ipv6-address* [ *prefix-length* ] [ **longer-match** ] [ **verbose** ] command.
* To check routes to the specified range of destination IPv6 addresses, run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) *ipv6-address1* [ *prefix-length1* ] *ipv6-address2* *prefix-length2* [ **verbose** ] command.
* To check the IPv6 routes discovered by the specified protocol, run the [**display ipv6 routing-table protocol**](cmdqueryname=display+ipv6+routing-table+protocol) { **bgp** | **direct** | **isis** | **ospfv3** | **ripng** | **static** | **unr** } [ **inactive** | **verbose** ] command.
* To check general information about the IPv6 routing table, run the [**display ipv6 routing-table statistics**](cmdqueryname=display+ipv6+routing-table+statistics) command.
* To check brief information about the VPN routing table, run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) **vpn-instance** *vpn-instance-name* command.
* To check detailed information about the VPN routing table, run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) **vpn-instance** *vpn-instance-name* **verbose** command.
* To check detailed information about the route to the specified destination IPv6 address in the VPN routing table, run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) **vpn-instance** *vpn-instance-name* *ipv6-address* [ *prefix-length* ] [ **longer-match** ] [ **verbose** ] command.
* To check detailed information about the routes to the specified IPv6 network segment in the VPN routing table, run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) **vpn-instance** *vpn-instance-name* *ipv6-address1* [ *prefix-length1* ] *ipv6-address2* *prefix-length2* [ **verbose** ] command.