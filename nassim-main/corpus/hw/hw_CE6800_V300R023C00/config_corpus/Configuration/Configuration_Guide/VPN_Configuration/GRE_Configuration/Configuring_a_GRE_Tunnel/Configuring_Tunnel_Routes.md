Configuring Tunnel Routes
=========================

Configuring Tunnel Routes

#### Context

Routes with GRE tunnel interfaces as the outbound interfaces must exist on both the local and remote devices of a GRE tunnel, so that GRE-encapsulated packets can be properly forwarded. These routes can be either static or dynamic routes. When configuring GRE tunnel routes, note the following:

* If you configure a static route, it must be configured on both the local and remote devices. Additionally, the destination address of the route must be that of the original packet which is not encapsulated using GRE and the outbound interface of the route must be the local tunnel interface. The destination address cannot be the tunnel destination address or the remote tunnel interface address.
* If you configure a dynamic routing protocol to generate a dynamic route, the protocol must be enabled on both tunnel interfaces and the interfaces connected to private networks. If you configure a route to the IP address of a physical interface on the tunnel destination, ensure that the next-hop address of the route is a physical interface address instead of a tunnel interface address. Otherwise, packets cannot be properly forwarded.
  
  For example, in [Figure 1](#EN-US_TASK_0000001130782616__fig_dc_vrp_gre_cfg_200501), the source physical interface of Tunnel 1 is interface 1 on DeviceA, and the destination physical interface of Tunnel 1 is interface 2 on DeviceB. When configuring a dynamic routing protocol to generate a dynamic route, you need to enable the protocol on both the tunnel interfaces and the interfaces connected to the PCs. In the IP routing table of DeviceA, the outbound interface for the route to the subnet where interface 2 on DeviceB resides cannot be Tunnel 1.
  
  In real-world configurations, different routing protocols or different processes of the same routing protocol need to be used on tunnel interfaces and public network physical interfaces. This prevents a tunnel interface from being selected as the outbound interface of routes to the tunnel destination, and ensures that packets are forwarded through the GRE tunnel instead of the physical interfaces.
  
  **Figure 1** Configuring a dynamic routing protocol for GRE  
  ![](figure/en-us_image_0000001176742333.png)

Perform the following steps on the devices at both ends of a GRE tunnel.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Choose either of the following methods to configure a GRE tunnel route:
   
   
   * Configure an IPv4 static route.
     
     ```
     [ip route-static](cmdqueryname=ip+route-static) dest-ip-address { mask | mask-length } tunnel interface-number [ description text ]
     [commit](cmdqueryname=commit)
     ```
   * Configure an IPv6 static route.
     ```
     [ipv6 route-static](cmdqueryname=ipv6+route-static) dest-ipv6-address prefix-length tunnel interface-number [ description text ]
     [commit](cmdqueryname=commit)
     ```
   * Configure an IPv4 or IPv6 dynamic routing protocol. The dynamic routing protocol can be IGP or BGP. For details about how to configure a dynamic routing protocol, see the  *Configuration Guide**-IP Routing Configuration*.