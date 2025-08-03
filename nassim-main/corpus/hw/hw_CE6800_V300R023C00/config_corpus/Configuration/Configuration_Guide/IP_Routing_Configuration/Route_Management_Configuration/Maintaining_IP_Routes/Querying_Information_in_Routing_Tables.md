Querying Information in Routing Tables
======================================

Querying Information in Routing Tables

#### Context

Viewing routing table information is a basic requirement for locating routing problems. The following lists common commands for displaying routing table information.

The **display** commands can be used in any view.

**Table 1** Commands used to display routing table information
| Operation | Command |
| --- | --- |
| Check brief information about active routes in the IPv4 routing table. | [**display ip routing-table**](cmdqueryname=display+ip+routing-table) |
| Check detailed information about routes in the IPv4 routing table. | [**display ip routing-table**](cmdqueryname=display+ip+routing-table) **verbose** |
| Check the limit on the number of routes and prefixes. | [**display ip routing-table limit**](cmdqueryname=display+ip+routing-table+limit) [ **all-vpn-instance** | **vpn-instance** *vpn-instance-name* ] |
| Check the number of routes. | [**display ip routing-table route-number**](cmdqueryname=display+ip+routing-table+route-number) |
| Check information about routes with a specified destination address. | [**display ip routing-table**](cmdqueryname=display+ip+routing-table) *ip-address* [ *mask* | *mask-length* ] [ **longer-match** ] [ **verbose** ] |
| Check information about routes destined for addresses in a specified destination IPv4 address range. | [**display ip routing-table**](cmdqueryname=display+ip+routing-table) *ip-address1* { *mask1* | *mask-length1* } *ip-address2* { *mask2* | *mask-length2* } [ **verbose** ] |
| Check information about the routes discovered by a specified protocol. | [**display ip routing-table protocol**](cmdqueryname=display+ip+routing-table+protocol) { **direct** | **ospf** | **isis** | **static** | **rip** | **bgp** } [ **inactive** | **verbose** ] |
| Check comprehensive information about the routing table. | [**display ip routing-table statistics**](cmdqueryname=display+ip+routing-table+statistics) |
| Check brief information about the VPN routing table. | [**display ip routing-table**](cmdqueryname=display+ip+routing-table) **vpn-instance** *vpn-instance-name* |
| Check detailed information about the VPN routing table. | [**display ip routing-table**](cmdqueryname=display+ip+routing-table) **vpn-instance** *vpn-instance-name* **verbose** |
| Check detailed information about routes with a specified destination address in the VPN routing table. | [**display ip routing-table**](cmdqueryname=display+ip+routing-table) **vpn-instance** *vpn-instance-name* *ip-address* [ *mask* | *mask-length* ] [ **longer-match** ] [ **verbose** ] |
| Check detailed information about routes to a specified IPv4 network segment in the IPv4 routing table of a specified VPN instance. | [**display ip routing-table**](cmdqueryname=display+ip+routing-table) **vpn-instance** *vpn-instance-name* *ip-address1* { *mask1* | *mask-length1* } *ip-address2* { *mask2* | *mask-length2* } [ **verbose** ] |
| Check brief information about active routes in the IPv6 routing table. | [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table)  NOTE:  The CE6885-LL in low latency mode does not support this command. |
| Check detailed information about routes in the IPv6 routing table. | [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) **verbose**  NOTE:  The CE6885-LL in low latency mode does not support this command. |
| Check brief information about routes in the IPv6 routing table. | [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) [ **vpn-instance** *vpn-instance-name* ] **simple**  NOTE:  The CE6885-LL in low latency mode does not support this command. |
| Check the limit on the number of IPv6 routes and prefixes. | [**display ipv6 routing-table limit**](cmdqueryname=display+ipv6+routing-table+limit) [ **all-vpn-instance** | **vpn-instance** *vpn-instance-name* ]  NOTE:  The CE6885-LL in low latency mode does not support this command. |
| Check the number of IPv6 routes. | [**display ipv6 routing-table route-number**](cmdqueryname=display+ipv6+routing-table+route-number)  NOTE:  The CE6885-LL in low latency mode does not support this command. |
| Check information about routes with a specified destination IPv6 address. | [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) *ipv6-address* [ *prefix-length* ] [ **longer-match** ] [ **verbose** ]  NOTE:  The CE6885-LL in low latency mode does not support this command. |
| Check information about routes destined for addresses in a specified destination IPv6 address range. | [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) *ipv6-address1* [ *prefix-length1* ] *ipv6-address2* *prefix-length2* [ **verbose** ]  NOTE:  The CE6885-LL in low latency mode does not support this command. |
| Check information about IPv6 routes discovered by a specified protocol. | [**display ipv6 routing-table protocol**](cmdqueryname=display+ipv6+routing-table+protocol) { **bgp** | **direct** | **isis** | **ospfv3** | **ripng** | **static** } [ **inactive** | **verbose** ]  NOTE:  The CE6885-LL in low latency mode does not support this command. |
| Check comprehensive information about the IPv6 routing table. | [**display ipv6 routing-table statistics**](cmdqueryname=display+ipv6+routing-table+statistics)  NOTE:  The CE6885-LL in low latency mode does not support this command. |
| Check brief information about the VPN routing table. | [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) **vpn-instance** *vpn-instance-name*  NOTE:  The CE6885-LL in low latency mode does not support this command. |
| Check detailed information about the VPN routing table. | [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) **vpn-instance** *vpn-instance-name* **verbose**  NOTE:  The CE6885-LL in low latency mode does not support this command. |
| Check detailed information about routes with a specified IPv6 destination address in the VPN routing table. | [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) **vpn-instance** *vpn-instance-name* *ipv6-address* [ *prefix-length* ] [ **longer-match** ] [ **verbose** ]  NOTE:  The CE6885-LL in low latency mode does not support this command. |
| Check detailed information about routes to a specified IPv6 network segment range in the VPN routing table. | [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) **vpn-instance** *vpn-instance-name* *ipv6-address1* [ *prefix-length1* ] *ipv6-address2* *prefix-length2* [ **verbose** ]  NOTE:  The CE6885-LL in low latency mode does not support this command. |