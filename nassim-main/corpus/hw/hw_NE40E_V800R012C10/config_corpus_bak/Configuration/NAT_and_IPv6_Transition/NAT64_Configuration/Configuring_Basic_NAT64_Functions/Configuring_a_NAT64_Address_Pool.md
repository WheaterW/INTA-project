Configuring a NAT64 Address Pool
================================

You can create a NAT64 address pool and assign available public IPv4 address segments to a specified NAT64 instance to translate between private IPv6 addresses and public IPv4 addresses.

#### Context

A NAT64 address pool is essential to NAT64 implementation. When IPv6 user data packets are sent to a NAT64 CGN device, an IPv4 address must be allocated from the NAT64 address pool to the packets so that the packets are transmitted over an IPv4 network. NAT64 supports the following address translation methods:

* Port address translation (PAT): NAT64 translates both IP addresses and port numbers between private and public networks. PAT implements more efficient IP address sharing and is the most commonly used mode in address translation.
* No-Port Address Translation (No-PAT): Only the IP address in a packet is replaced.

The following address translation modes are supported based on NAT64 address translation methods:

* Symmetric mode: also called the 5-tuple mode. A 5-tuple entry contains a source IP address, source port number, protocol type, destination IP address, and destination port number and is used to allocate addresses and filter packets. If packets carrying the same source IP address and port number but different destination IP addresses and port numbers are translated by a device using NAT64, the source IP address and port number in the packets are translated into different external IP addresses and port numbers. In addition, the device allows only the external network hosts with these destination IP addresses to use the translated IP addresses and port numbers to visit internal network hosts.
* Full-cone mode: also known as the 3-tuple mode that is not concerned with destination addresses or destination port numbers. In this mode, a device assigns IP addresses and filters packets based on the source address, source port number, and protocol type. If packets carrying the same source IP address and port number are translated by a device using NAT64, the source IP address and port number in the packets are translated into the same external IP address and port number. In addition, the device allows external network hosts to use the translated IP addresses and port numbers to visit internal network hosts.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat64 instance**](cmdqueryname=nat64+instance) *instance-name* [ **id** *id* ]
   
   
   
   The NAT64 instance view is displayed.
3. Create a NAT64 address pool and specify the mode of assigning address ranges. Perform either of the following operations:
   
   
   * Run the [**nat64 address-group**](cmdqueryname=nat64+address-group) *address-group-name* **group-id** *group-id* *start-address* { **mask** { *mask-length* | *mask-ip* } | *end-address* } [ **vpn-instance** *vpn-instance-name* ] [ **no-pat** ] command to create an address pool by specifying an address range in the NAT64 instance view.
   * Run the [**nat64 address-group**](cmdqueryname=nat64+address-group) *address-group-name* **group-id** *group-id* [ **vpn-instance** *vpn-instance-name* ] [ **no-pat** ] command to enter the NAT64 address pool view and run the [**section**](cmdqueryname=section) *section-id* *start-address* { **mask** { *mask-length* | *mask-ip* } | *end-address* } command to specify an address range in the NAT64 address pool view.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A NAT64 address pool cannot contain a DHCP server address. You need to properly allocate address segments. Otherwise, NAT traffic cannot be forwarded.
4. (Optional) Exclude a specific IP address or a range of IP addresses in an address range from NAT64 translation.
   
   
   * If the **[**nat64 address-group**](cmdqueryname=nat64+address-group)** command is used to allocate addresses from an address pool, run the **[**nat64 address-group**](cmdqueryname=nat64+address-group)** **address-group-name****[**exclude-ip-address**](cmdqueryname=exclude-ip-address)** **start-address** [ **end-address** ] command.
   * If the **[**section**](cmdqueryname=section)** command is used to allocate addresses from an address pool, run the **[**section**](cmdqueryname=section)** **section-id** **[**exclude-ip-address**](cmdqueryname=exclude-ip-address)****start-address**[ **end-address** ] command.
5. (Optional) Run [**nat64 filter mode full-cone**](cmdqueryname=nat64+filter+mode+full-cone)
   
   
   
   The full-cone mode (3-tuple mode) is configured for all addresses in the NAT64 instance.
   
   
   
   By default, the address translation mode is the symmetric (5-tuple) mode.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.