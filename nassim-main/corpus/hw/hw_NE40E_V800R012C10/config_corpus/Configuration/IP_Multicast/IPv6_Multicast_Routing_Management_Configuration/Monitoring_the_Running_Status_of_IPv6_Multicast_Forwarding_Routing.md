Monitoring the Running Status of IPv6 Multicast Forwarding Routing
==================================================================

During the routine maintenance of IPv6 multicast routing management, you can run the display commands in any view to know the running of the multicast forwarding table.

#### Context

In routine maintenance, you can run the following commands in any view to check the running status of IPv6 multicast forwarding.


#### Procedure

* Run the [**display multicast ipv6 forwarding-table**](cmdqueryname=display+multicast+ipv6+forwarding-table) [ *ipv6-source-address* | *ipv6-group-address* | **incoming-interface** { *interface-type* *interface-number* | **register** } | **outgoing-interface** { { **exclude** | **include** | **match** } { *interface-type* *interface-number* | **register** | **none** } } | **slot** *slot-number* | **statistics** ] \* command in any view to check the IPv6 multicast forwarding table.