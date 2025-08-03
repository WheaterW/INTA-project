Monitoring the IPv6 Multicast Routing and Forwarding Status
===========================================================

Monitoring the IPv6 Multicast Routing and Forwarding Status

#### Context

During the routine maintenance of IPv6 multicast route management, you can run the required display commands in any view to learn information about the IPv6 multicast routing table and forwarding table.


#### Procedure

* Run the [**display multicast ipv6 routing-table**](cmdqueryname=display+multicast+ipv6+routing-table) command to check information about the multicast routing table.
* Run the [**display multicast ipv6 rpf-info**](cmdqueryname=display+multicast+ipv6+rpf-info) *ipv6-source-address* [ *ipv6-group-address* ] [ **rpt** | **spt** ] [ **verbose** ] command to check RPF routing information of a specified IPv6 multicast source.
* Run the [**display multicast ipv6 fib**](cmdqueryname=display+multicast+ipv6+fib) [ [ **vpn-instance** *vpn-instance-name* ] [ **group** *ipv6-group-address* | **source** *ipv6-source-address* | **incoming-interface** { *interface-type* *interface-name* | **register** } ]\* | **all-vpn-instance** ] [ **slot** *slot-id* [ **cpu** *cpu-id* ] ] command to check the IPv6 multicast forwarding table.