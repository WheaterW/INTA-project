Checking Network Connectivity and Reachability
==============================================

This section describes how to use the **ping** command to check the network connectivity between the source and destination, and how to use the **tracert** command to check the devices through which data packets are sent from the source to the destination.

#### Procedure

* Run the [**ping**](cmdqueryname=ping) command to check whether the network between the source and destination is properly connected. You can run a different command to display detailed or brief information.
  
  
  + Detailed information: [**ping**](cmdqueryname=ping) [ **ip** ] { [ **-c** *count* | { [ **-i** { *interface-name* | *interface-type* *interface-number* } | **-nexthop** *nexthop-address* ] \* | **-si** { *interface-name* | *interface-type* *interface-number* } } | { **-s** *packetsize* | **-range** [ [ **min** *min-value* | **max** *max-value* | **step** *step-value* ] \* ] } | **-t** *timeout* | **-m** *time* | **-a** *source-ip-address* | **-h** *ttl-value* | **-p** *pattern* | { **-tos** *tos-value* | **-dscp** *dscp-value* } | { **-f** | **ignore-mtu** } | **-q** | **-r** | **-vpn-instance** *vpn-instance-name* | **-v** | **-system-time** | **-ri** | **-8021p** *8021p-value*| | **-name** | **-detail** ] \* *host* [ **ip-forwarding** ] } [ **bypass** **-si** { *interface-name* | *interface-type* *interface-number* } ]
  + Brief information: [**ping**](cmdqueryname=ping) [ **ip** ] { [ **-c** *count* | { [ **-i** { *interface-name* | *interface-type* *interface-number* } | **-nexthop** *nexthop-address* ] \* | **-si** { *interface-name* | *interface-type* *interface-number* } } | { **-s** *packetsize* | **-range** [ [ **min** *min-value* | **max** *max-value* | **step** *step-value* ] \* ] } | **-t** *timeout* | **-m** *time* | **-a** *source-ip-address* | **-h** *ttl-value* | **-p** *pattern* | { **-tos** *tos-value* | **-dscp** *dscp-value* } | { **-f** | **ignore-mtu** } | **-vpn-instance** *vpn-instance-name* | **-ri** | **-8021p** *8021p-value*| | **-name** | **-brief** ] \* *host* [ **ip-forwarding** ] } [ **bypass** **-si** { *interface-name* | *interface-type* *interface-number* } ]
* To check the gateway that a packet passes when being transmitted from the source to the destination, run the [**tracert**](cmdqueryname=tracert) [ **-a** *source-ip-address* | **-f** *first-TTL* | **-m** *max-TTL* | **-p** *port* | **-q** *nqueries* | **-vpn-instance** *vpn-instance-name* | **-w** *timeout* ]\* *host* command.
* To check the connectivity of the L3VPN LSP, run the [**ping lsp**](cmdqueryname=ping+lsp) [ **-a** *source-ip* | **-c** *count* | **-exp** *exp-value* | **-h** *ttl-value* | **-m** *interval* | **-r** *reply-mode* | **-s** *packet-size* | **-t** *time-out* | **-v** ] \* **ip** *destination-iphost* *mask-length* [ *ip-address* ] [ **nexthop** *nexthop-address* ] command.
* To check the gateways that the packet passes through from the source host to the destination on the LSP, run the [**tracert lsp**](cmdqueryname=tracert+lsp) [ **-a** *source-ip* | **-exp** *exp-value* | **-h** *ttl-value* | **-r** *reply-mode* | **-t** *time-out* ] \* **ip** *destination-iphost* *mask-length* [ *ip-address* ] **detail** command.

#### Example

After completing VPN configurations, you can:

* Run the [**ping**](cmdqueryname=ping) command on a local CE. The command output shows whether the local and remote CEs in the same VPN can communicate with each other. If the ping fails, you can run the [**tracert**](cmdqueryname=tracert) command to locate the faulty node.
* Alternatively, run the [**ping**](cmdqueryname=ping) command with the -**vpn-instance** *vpn-instance-name* parameter on the PE. The command output shows whether the PE and CE in the same VPN as the PE can communicate with each other. If the ping fails, you can run the [**tracert**](cmdqueryname=tracert) command with the **vpn-instance** *vpn-instance-name* parameter to locate the faulty node.

If multiple interfaces on the PE are bound to the same VPN, you need to specify the source IP address, that is, the **-a** *source-ip-address*, when you [**ping**](cmdqueryname=ping) or [**tracert**](cmdqueryname=tracert) the remote CE that accesses the peer PE. If no source IP address is specified, the PE selects the lowest IP address from the IP addresses of the interfaces on the PE bound to this VPN as the source address of the Internet Control Message Protocol (ICMP) messages. If the CE has no route to the selected IPv4 route, the CE discards the returned ICMP message.