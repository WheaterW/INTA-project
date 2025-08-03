Configuring a Route for a Tunnel
================================

A route for a tunnel must be available on both the source and destination devices so that packets encapsulated with GRE can be forwarded correctly. A route passing through a tunnel interface can be either a static or dynamic route.

#### Context

A route for a tunnel must be available on both the local and remote devices so that packets encapsulated by GRE can be forwarded properly. The route can be either a static or dynamic route. When configuring a route for a tunnel, note the following:

* If the route is a static route, it must be configured on both the source and destination devices. The destination address of the route is the original destination address of the packet before GRE encapsulation, rather than the destination address of the tunnel or the address of the peer tunnel interface. The outbound interface is the local tunnel interface.
* When configuring a dynamic routing protocol, you need to enable the protocol on both the tunnel interface and the Router interface connected to the VPN. When configuring a route to the actual destination interface address of a tunnel, ensure that the next hop is not the tunnel interface address. Otherwise, GRE-encapsulated packets cannot be forwarded properly.
  
  As shown in [Figure 1](#EN-US_TASK_0172369081__fig_dc_vrp_gre_cfg_200501), the source interface of Tunnel1 is interface1 on DeviceA, and the destination physical interface of Tunnel1 is interface2 on DeviceC. When configuring a dynamic routing protocol, you need to enable the protocol on both the tunnel interface and the interface connected to the PC. In the routing table, the outbound interface for the route to interface2 on DeviceC cannot be Tunnel1.
  
  In practical configurations, different routing protocols or different processes of the same routing protocol need to be used for tunnel interfaces and public network physical interfaces. This prevents a tunnel interface from being selected as an outbound interface of routes to the destination of the tunnel. In addition, this also ensures that users packets are forwarded through the tunnel instead of the physical interface.
  
  **Figure 1** Configuring a GRE dynamic routing protocol![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Interfaces 1 through 4 in this example represent GE0/1/0, GE0/2/0, Tunnel1, and Tunnel2, respectively.
  
  
    
  ![](figure/en-us_image_0000001571737800.png)

Perform the following steps on the endpoint Routers of a tunnel.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Choose one of the following methods to configure routes passing through the tunnel interface.
   
   
   * Run the [**ip route-static**](cmdqueryname=ip+route-static) *dest-ip-address* { *mask* | *mask-length* } **tunnel** *interface-number* [ **description** *text* ] command to configure a static route.
   * Configure a dynamic routing protocol, which can be IGP or BGP. The detailed configuration is not provided here. For the configuration of dynamic routes, see the *NE40E Configuration Guide - IP Routing*.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

To implement millisecond-level fault detection for a GRE tunnel, configure the following BFD functions on the GRE tunnel interface:

* [Configure dynamic BFD for RIP](dc_vrp_rip_cfg_0055.html)
* [Configure BFD for OSPF on a specified interface](dc_vrp_ospf_cfg_2048.html)
* [Configure dynamic BFD for IS-IS](dc_vrp_isis_cfg_0043.html)