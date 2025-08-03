Creating IPv4 Static Routes
===========================

To create an IPv4 static route, configure its destination address, outbound interface, and next hop.

#### Context

When creating an IPv4 static route, you need the following information:

* Destination address and mask
  
  In the [**ip route-static**](cmdqueryname=ip+route-static) command, the IPv4 address is expressed in dotted decimal notation, and the mask is expressed either in dotted decimal notation or represented by the mask length.
* Outbound interface and next hop address
  
  When creating a static route, you can specify *interface-type* *interface-name*, *nexthop-address*, or both. In addition, you can configure the Next-Table function, that is, only a VPN instance name (public in the case of the public network) is specified as the next hop of a static route, and no outbound interface or next hop address is specified. You can configure the parameters as required.
  
  Actually, each routing entry requires a next hop address. Before sending a packet, a device needs to search its routing table for the route matching the destination address in the packet based on the longest match rule. The device can find the associated link layer address to forward the packet only when the next hop address of the packet is available.
  
  When specifying an outbound interface, note the following rules:
  + For a Point-to-Point (P2P) interface, if the outbound interface is specified, the next hop address is the address of the remote interface connected to the outbound interface. For example, when a GE interface is encapsulated with Point-to-Point Protocol (PPP) and obtains the remote IP address through PPP negotiation, you need to specify only the outbound interface rather than the next hop address.
  + Non-Broadcast Multiple-Access (NBMA) interfaces are applicable to Point-to-Multipoint networks. Therefore, you need to configure IP routes and the mappings between IP addresses and link layer addresses. In this case, next hop IP addresses need to be configured.
  + An Ethernet interface is a broadcast interface and a virtual-template (VT) interface can be associated with multiple virtual access interfaces. If the Ethernet interface or the VT interface is specified as the outbound interface of a static route, the next hop cannot be determined because multiple next hops exist. Therefore, do not specify an Ethernet interface or a VT interface as the outbound interface unless necessary. If you need to specify a broadcast interface (such as an Ethernet interface), a VT interface, or an NBMA interface as the outbound interface, you are recommended to specify the associated next hop address at the same time.
* Other attributes
  
  You can configure different preferences for different static routes so that routing management policies can be flexibly applied. For example, when creating multiple routes to the same destination address, you can set the same preference for these routes to implement load balancing. You can also set different preferences to implement routing redundancy.
  
  By configuring different tag values, you can classify static routes to implement different routing policies. For example, other protocols can import static routes with specified tag values based on routing policies.
  
  If service traffic needs to be forwarded along a specified path, regardless of the link status, you can configure permanent advertisement of static routes by using **permanent**.
  
  In network maintenance scenarios, static routes are required to verify services. If you do not want these static routes to be imported by other protocols, specify **no-advertise** to prevent these static routes from being advertised.
  
  If you set the destination address and the mask to all 0s (0.0.0.0 0.0.0.0) in the [**ip route-static**](cmdqueryname=ip+route-static) command, a default route is configured.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure an IPv4 static route.
   
   
   * Run one of the following commands to configure an IPv4 static route for the public network:
     + [**ip route-static**](cmdqueryname=ip+route-static) *ip-address* { *mask* | *mask-length* } { *nexthop-address* | *nexthop6-address* } [ **preference** *preference* | **tag** *tag* ] \* [ **description** *text* ]
     + [**ip route-static**](cmdqueryname=ip+route-static) *ip-address* { *mask* | *mask-length* }{ *interface-name* | *interface-type* *interface-number*} [ { *nexthop-address* | *nexthop6-address* } ] [ **preference** *preference* | **tag** *tag* ] \* [ **description** *text* ]
     + [**ip route-static**](cmdqueryname=ip+route-static) *ip-address* { *mask* | *mask-length* } **vpn-instance** *vpn-instance-name* [ **preference** *preference* | **tag** *tag* ] \* **description** *text*
     + [**ip route-static**](cmdqueryname=ip+route-static) *ip-address* { *mask* | *mask-length* } **vpn-instance** *vpn-instance-name* { *nexthop-address* | *nexthop6-address* } [ **preference** *preference* | **tag** *tag* ] \* [ **description** *text* ]
   * Run one of the following commands to configure an IPv4 static route for a VPN instance:
     + [**ip route-static vpn-instance**](cmdqueryname=ip+route-static+vpn-instance) *vpn-source-name* *destination-address* { *mask* | *mask-length* }{ *interface-type* *interface-number* } [ *nexthop-address* ] [ **preference** *preference* | **tag** *tag* ] \* [ **description** *text* ]
     + [**ip route-static vpn-instance**](cmdqueryname=ip+route-static+vpn-instance) *vpn-source-name* *destination-address* { *mask* | *mask-length* } *nexthop-address*  [ **preference** *preference* | **tag** *tag* ] \* [ **description** *text* ]
     + [**ip route-static vpn-instance**](cmdqueryname=ip+route-static+vpn-instance) *vpn-source-name* *destination-address* { *mask* | *mask-length* } { **public** | **vpn-instance** *vpn-destination-name* } [ **preference** *preference* | **tag** *tag* ] \* [ **description** *text* ]
     + [**ip route-static vpn-instance**](cmdqueryname=ip+route-static+vpn-instance) *vpn-source-name* *destination-address* { *mask* | *mask-length* } **vpn-instance** *vpn-destination-name* *nexthop-address*  [ **preference** *preference* | **tag** *tag* ] \* [ **description** *text* ]
   * To configure an IPv4 static route in the topology instance, run the [**ip route-static topology**](cmdqueryname=ip+route-static+topology) *topology-name* *ip-address* { *mask* | *mask-length* } { *nexthop-address* | *interface-type* *interface-number* [ *nexthop-address* ] } [ **preference** *preference* | **tag** *tag* ] \* [ **no-advertise** | **no-install** ] [ **description** *text* ] command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the outbound interface of a static route is a broadcast interface or an NBMA interface, the next hop of the outbound interface must be specified.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.