Configuring IPv4 over IPv6 Tunnel Routes
========================================

Packets can be forwarded correctly only when Routers at two ends of a tunnel are configured with forwarding routes.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Choose one of the following methods to configure the route with the outgoing interface as the tunnel interface:
   
   
   * Run the [**ip route-static**](cmdqueryname=ip+route-static) *ip-address* { *mask* | **mask-length** } [**tunnel**](cmdqueryname=tunnel) *interface-number* command to configure a static route.
     
     When configuring a static route, you must configure both ends of the tunnel. Note that the destination address is the destination IPv4 address of the packet before IPv4 over IPv6 encapsulation is performed; the outbound interface is the local tunnel interface.
     
     In VPN scenarios, you must also specify the VPN instance to which the next-hop address belongs.
   * Configure dynamic routes. You can use the Border Gateway Protocol (BGP) or the Interior Gateway Protocol (IGP), excluding Intermediate System-to-Intermediate System (IS-IS). Detailed configurations are not mentioned here.
     
     When configuring a dynamic routing protocol, you must enable the dynamic routing protocol on tunnel interfaces and the IPv4 network-side interfaces.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.