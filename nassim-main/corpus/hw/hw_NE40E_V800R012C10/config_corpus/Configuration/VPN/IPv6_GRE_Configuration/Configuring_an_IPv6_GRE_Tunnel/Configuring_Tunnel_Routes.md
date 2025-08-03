Configuring Tunnel Routes
=========================

Routes for a tunnel must be available on both the source
and destination devices so that packets encapsulated with GRE can
be forwarded correctly.

#### Context

Packets can be properly forwarded over an IPv6 GRE tunnel
only if the local and remote devices both have routes that are advertised
over the tunnel. Currently, only static routes can be advertised over
an IPv6 GRE tunnel. A static route must be configured on both the
source and destination devices. The destination address of the static
route is neither the destination address of the tunnel nor the address
of the destination tunnel interface. Instead, it is the destination
address of the packet that is not encapsulated using IPv6 GRE. The
outbound interface must be the tunnel interface at the local end.

Perform the following steps on the Routers at both ends of the tunnel:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Choose either of the following methods to configure static
   routes to be advertised over the IPv6 GRE tunnel:
   
   
   * If an IPv4 address is configured for the tunnel interface:
     
     Run the [**ip route-static**](cmdqueryname=ip+route-static) *dest-ip-address* { *mask* | *mask-length* } **tunnel** *interface-number* [ **description** *text* ] command to configure
     an IPv4 static route.
   * If an IPv6 address is configured for the tunnel interface:
     
     Run the [**ipv6 route-static**](cmdqueryname=ipv6+route-static) *dest-ipv6-address* *prefix-length* { *interface-type* *interface-number* [ *nexthop-ipv6-address* ] | **vpn-instance** *vpn-instance-name* *nexthop-ipv6-address* | *nexthop-ipv6-address* } [ **description** *text* ] command to configure an IPv6 static route.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.