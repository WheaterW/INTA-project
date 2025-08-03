Configuring Tunnel Interfaces
=============================

This section describes how to create tunnel interfaces to implement communication between IPv4 networks over the tunnel established.

#### Context

An IPv4 over IPv6 tunnel is established between tunnel interfaces on two devices. As such, you need to configure a tunnel interface on both devices. For an IPv4 over IPv6 tunnel interface, you must specify a protocol type, source IPv6 address/source interface, and destination IPv6 address/destination domain name.

A tunnel interface is a logical interface and its status is Down in the following situations:

* The destination address configured for the tunnel interface is unreachable or is the address of the tunnel interface.
* The status of the source interface configured for the tunnel interface is Down.
* The IP address configured on the tunnel interface is invalid.

Perform the following steps on the devices at both ends of a tunnel:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
   
   
   
   A tunnel interface is created, and the tunnel interface view is displayed.
3. Run [**tunnel-protocol**](cmdqueryname=tunnel-protocol) **ipv4-ipv6**
   
   
   
   The tunnel protocol is set to IPv4 over IPv6.
4. Run [**source**](cmdqueryname=source) { *ipv6-address* | *interface-type* *interface-number* }
   
   
   
   A source IPv6 address or source interface is specified for the tunnel interface.
   
   
   
   You can only specify a loopback interface as the source interface for a tunnel interface. Likewise, you can only specify the IPv6 address of a loopback interface as the source IPv6 address for a tunnel interface.
5. Configure a destination IPv6 address or destination domain name for the tunnel as required:
   
   
   * Configure a destination IPv6 address.
     
     Run the [**destination**](cmdqueryname=destination) [ **vpn-instance** *vpn-instance-name* ] *ipv6-address* command to specify a destination IPv6 address for the tunnel.
     
     The destination IPv6 address specified for the tunnel can only be the IPv6 address of the loopback interface on the peer end.
   * Configure a destination domain name.
     
     Run the [**dns resolve**](cmdqueryname=dns+resolve) command to enable dynamic DNS resolution.
     
     Run the [**destination**](cmdqueryname=destination) [ **vpn-instance** *vpn-instance-name* ] **domain** *domain-name* command to specify a destination domain name for the tunnel.
   
   
   
   In VPN scenarios, the VPN instance to which the peer device is bound must be specified.
6. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ]
   
   
   
   An IPv4 address is configured for the tunnel interface.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.