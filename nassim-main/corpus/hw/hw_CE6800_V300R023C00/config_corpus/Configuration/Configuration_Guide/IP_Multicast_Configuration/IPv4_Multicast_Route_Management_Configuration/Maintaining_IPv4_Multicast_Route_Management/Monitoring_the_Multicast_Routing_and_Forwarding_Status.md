Monitoring the Multicast Routing and Forwarding Status
======================================================

Monitoring the Multicast Routing and Forwarding Status

#### Context

During the routine maintenance of IPv4 multicast route management, you can run the required display commands in any view to learn information about a multicast routing table and MFIB.


#### Procedure

* Run the [**display multicast routing-table**](cmdqueryname=display+multicast+routing-table) command to check information about the multicast routing table.
* Run the [**display multicast ip fib**](cmdqueryname=display+multicast+ip+fib) [ [ **vpn-instance** *vpn-instance-name* ] [ **group** *group-address* | **source** *source-address* | **incoming-interface** { *interface-type* *interface-number* | **register** } ]\* | **all-vpn-instance** ] [ **slot** *slot-id* [ **cpu** *cpu-id* ] ] command to check the MFIB information.