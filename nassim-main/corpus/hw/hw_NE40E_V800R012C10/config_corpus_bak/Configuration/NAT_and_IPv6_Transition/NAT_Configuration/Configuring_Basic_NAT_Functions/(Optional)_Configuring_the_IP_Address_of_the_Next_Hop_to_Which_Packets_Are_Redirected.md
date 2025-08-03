(Optional) Configuring the IP Address of the Next Hop to Which Packets Are Redirected
=====================================================================================

This section describes how to configure the IP address of the next hop to which packets are redirected.

#### Context

A NAT instance is used for configuring NAT attributes. After NAT is performed for user traffic entering a NAT instance, a forwarding path is selected based on the IP address of the next hop to which packets are redirected.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat instance**](cmdqueryname=nat+instance) *instance-name* **id** *id*
   
   
   
   A NAT instance is created, and its view is displayed.
3. You can use either of the following methods to configure NAT redirection:
   
   
   * To specify a next-hop IP address to which all user traffic is redirected, run the [**redirect ip-nexthop**](cmdqueryname=redirect+ip-nexthop) *ip-address* { **inbound** | **outbound** } command.
     
     In this situation, only one **redirect ip-nexthop** command can be configured in each instance, either in inbound or outbound direction.
   * To specify a next-hop IP address to which specific user traffic is redirected, run the [**redirect ip-nexthop**](cmdqueryname=redirect+ip-nexthop) *ip-address* { **inbound** | **outbound** } *redirect-id* [ **tcp** | **udp** | *protocol-id* ] [ **source-ip** *ip-address* { *ip-mask* | *mask-length* } [ **source-port** *port-number* ] [ **vpn-instance** *vpn-instance-name* ] | **destination-ip** *ip-address* { *ip-mask* | *mask-length* } [ **destination-port** *port-number* ] [ **vpn-instance** *vpn-instance-name* ] ] \* command.
     
     In this situation, a maximum of 16 **redirect ip-nexthop** commands can be configured in each instance, either in inbound or outbound direction. You can specify different *redirect-id* to differentiate the commands. In addition, inbound and outbound directions can be configured at the same time.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.