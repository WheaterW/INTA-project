Creating IPv6 Static Routes
===========================

To create an IPv6 static route, configure its destination IP address, outbound interface, and next hop.

#### Context

When creating a static route, you can specify an outbound interface, a next hop address, or both of them, depending on actual requirements.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure an IPv6 static route.
   
   
   * Run one of the following commands to configure an IPv6 static route for the public network:
     + [**ipv6 route-static**](cmdqueryname=ipv6+route-static) *dest-ipv6-address* *prefix-length* *interface-type* *interface-number* [ *nexthop-ipv6-address* ] [ **preference** *preference* | **tag** *tag* ] \* [ **description** *text* ]
     + [**ipv6 route-static**](cmdqueryname=ipv6+route-static) *dest-ipv6-address* *prefix-length* *nexthop-ipv6-address* [ **preference** *preference* | **tag** *tag* ] \* [ **description** *text* ]
     + [**ipv6 route-static**](cmdqueryname=ipv6+route-static) *dest-ipv6-address* *prefix-length* **vpn-instance** *vpn-instance-name* *nexthop-ipv6-address* [ **preference** *preference* | **tag** *tag* ] \* [ **description** *text* ]
     + [**ipv6 route-static**](cmdqueryname=ipv6+route-static) *dest-ipv6-address* *prefix-length* **vpn-instance** *vpn-instance-name* [ **preference** *preference* | **tag** *tag* ] \* [ **description** *text* ]
   * Run one of the following commands to configure an IPv6 static route for a VPN instance:
     + [**ipv6 route-static vpn-instance**](cmdqueryname=ipv6+route-static+vpn-instance) *vpn-source-name* *dest-ipv6-address* *prefix-length* { *interface-name* | *interface-type* *interface-number* } [ *nexthop-ipv6-address* ] [ **preference** *preference* | **tag** *tag* ] \* [ **description** *text* ]
     + [**ipv6 route-static vpn-instance**](cmdqueryname=ipv6+route-static+vpn-instance) *vpn-source-name* *dest-ipv6-address* *prefix-length* *nexthop-ipv6-address* [ **preference** *preference* | **tag** *tag* ] \* [ **description** *text* ]
     + [**ipv6 route-static vpn-instance**](cmdqueryname=ipv6+route-static+vpn-instance) *vpn-source-name* *dest-ipv6-address* *prefix-length* { **vpn-instance** *vpn-instance-name* *nexthop-ipv6-address* | *nexthop-ipv6-address* [ **public** ] } [ **preference** *preference* | **tag** *tag* ] \* [ **description** *text* ]
     + [**ipv6 route-static vpn-instance**](cmdqueryname=ipv6+route-static+vpn-instance) *vpn-source-name* *dest-ipv6-address* *prefix-length* { **vpn-instance** *vpn-instance-name* | **public** } [ **preference** *preference* | **tag** *tag* ] \* [ **description** *text* ]
   * To configure an IPv6 static route in the topology instance, run the [**ipv6 route-static topology**](cmdqueryname=ipv6+route-static+topology) *topology-name* *dest-ipv6-address* *prefix-length* { *interface-type* *interface-number* [ *nexthop-ipv6-address* ] | *nexthop-ipv6-address* } [ **preference** *preference* | **tag** *tag* ] \* [ **no-advertise** | **no-install** ] [ **description** *text* ] command.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.