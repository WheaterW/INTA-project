Creating a DS-Lite Tunnel
=========================

This section describes how to configure a DS-Lite tunnel. A DS-Lite tunnel allows users with private IPv4 addresses to pass through IPv6-only carrier networks.

#### Context

A DS-Lite device uses a remote IPv6 address and a local IPv6 address to establish an IPv4-in-IPv6 tunnel to a CPE. Perform the following steps on a DS-Lite device:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ds-lite instance**](cmdqueryname=ds-lite+instance) *instance-name* [ **id** *id* ]
   
   
   
   The DS-Lite instance view is displayed.
3. Run [**local-ipv6**](cmdqueryname=local-ipv6) *ipv6-address* **prefix-length** *prefix-length*
   
   
   
   A local IPv6 address of a DS-Lite tunnel is set.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The local IPv6 address of a DS-Lite tunnel on the DS-Lite device must be the same as the IP address mapped to the address family transition router (AFTR) name configured on a DNS server.
   
   A single local IPv6 network address can be configured in each DS-Lite instance and must be different from interface IP addresses. The identical address causes the DS-Lite service to conflict with other services. A local IPv6 address can be configured in multiple DS-Lite instances.
4. Run [**remote-ipv6**](cmdqueryname=remote-ipv6) *ipv6-address* **prefix-length** *prefix-length*
   
   
   
   A remote IPv6 address of a DS-Lite tunnel is set.
5. (Optional) Run [**ds-lite tunnel prefix-length**](cmdqueryname=ds-lite+tunnel+prefix-length) *prefix-length*
   
   
   
   The length of a CPE IPv6 address prefix of packets transmitted on a DS-Lite tunnel is set.
   
   
   
   Upon receipt of the packet, the DS-Lite device identifies a tunnel based on a 128-bit source IPv6 address. When a BRAS only assigns a prefix, not an IPv6 address, to the CPE, the DS-Lite device can only use the IPv6 prefix to identify the tunnel. In this situation, run the [**ds-lite tunnel prefix-length**](cmdqueryname=ds-lite+tunnel+prefix-length) command to set the length of an IPv6 address prefix on a CPE of a DS-Lite tunnel.
6. (Optional) Run [**ds-lite mtu**](cmdqueryname=ds-lite+mtu) *mtu-value*
   
   
   
   The MTU on the outbound interface of a DS-Lite tunnel to the CPE is set.
   
   
   
   * If the size of packets is greater than the configured MTU value, the packets are broken into a great number of fragments.
   * If the MTU is set too large, packets may be transmitted at a low speed.
7. (Optional) Run [**set ds-lite inbound ipv4-tos**](cmdqueryname=set+ds-lite+inbound+ipv4-tos) *tos-value*
   
   
   
   The IPv4 ToS is set for packets transmitted along a DS-Lite tunnel.
8. (Optional) Run [**ds-lite dscp-copy enable**](cmdqueryname=ds-lite+dscp-copy+enable)
   
   
   
   The device is enabled to copy an IPv6 DSCP value in packets to the IPv4 DSCP field when the packets are sent out of a DS-Lite tunnel.
9. (Optional) Run [**ds-lite traffic-class**](cmdqueryname=ds-lite+traffic-class) *class-value*
   
   
   
   The traffic class of IPv6 packets that are sent to a DS-Lite tunnel is set.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.