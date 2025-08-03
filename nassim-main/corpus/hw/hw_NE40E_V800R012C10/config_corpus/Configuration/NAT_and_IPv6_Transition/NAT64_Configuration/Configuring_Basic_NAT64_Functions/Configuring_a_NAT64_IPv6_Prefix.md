Configuring a NAT64 IPv6 Prefix
===============================

A device identifies a network type based on a NAT64 prefix and sends each type of packet to a DNS64 server for processing.

#### Context

The destination address of IPv6 user data packets sent to a NAT64 CGN device is an IPv6 address, regardless of whether the packets are sent to the IPv4 or IPv6 network. In this situation, the NAT64 CGN device identifies packets based on IPv6 prefixes that have been defined for NAT64 processing.

* If a device receives an IPv6 packet with a prefix defined on the NAT64 device, the packet is destined for an IPv4 network. After NAT64 processes the packet, the packet is forwarded to the IPv4 network.
* If a device receives an IPv6 packet with a prefix different from that defined on the NAT64 device, the packet is destined for an IPv6 network. This packet is forwarded to the IPv6 network without being processed by NAT64.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat64 instance**](cmdqueryname=nat64+instance) *instance-name* **id** *id*
   
   
   
   The NAT64 instance view is displayed.
3. Run [**nat64 prefix**](cmdqueryname=nat64+prefix) *ipv6-prefix* **prefix-length** *prefix-length* *prefix-id* [ **no-pat** ]
   
   
   
   A NAT64 IPv6 prefix length is set.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The prefix configured on a DNS64 server must be the same as the NAT64 prefix, and the suffix must be 0.
   
   A NAT64 prefix in PAT mode can be associated with a NAT64 address pool only in PAT mode, and a NAT64 prefix in No-PAT mode can be associated with a NAT64 address pool only in No-PAT mode.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.