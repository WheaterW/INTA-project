Configuring Routes
==================

DSVPN routes need to be configured appropriately to ensure the correct forwarding of mGRE-encapsulated packets.

#### Context

The routes forwarded by a tunnel must be available on Spokes and the Hub so that mGRE-encapsulated packets can be forwarded correctly. These routes can be static routes or dynamic routes.

DSVPN supports the following route learning modes:

* Route learning between Spokes (non-shortcut)
  
  The next-hop address of the route from the source Spoke to the destination Spoke is the tunnel address of the destination Spoke, and each Spoke needs to learn the route to the remote end. This consumes many CPU and memory resources and requires large routing tables and high performance on Spokes. In practice, the Spokes have low performance and store a limited number of routes. The route learning solution applies to small- and medium-sized networks where there are fewer network nodes and a small number of routes.
  
  mGRE tunnels between Spokes are set up in non-shortcut mode.
* Spoke routes summarized to the Hub (shortcut mode)
  
  The next-hop address of the route from the source Spoke to the destination Spoke is the tunnel address of the Hub, and Spokes only need to store routes to the Hub. The number of routes of Spokes is reduced, so the route learning solution applies to large-sized networks with many Spokes.
  
  mGRE tunnels between Spokes are set up in shortcut mode.

Static routes and dynamic routing protocols can be deployed in the preceding two route learning modes. DSVPN supports OSPF and BGP.

Perform the following configurations on the Hub and Spokes.


#### Procedure

* **Configure a static route.**
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip route-static**](cmdqueryname=ip+route-static) *ip-address* { *mask* | *mask-length* } *nexthop-address* [ **description** *text* ]
     
     
     
     A static route is configured.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + When Spokes learn routes from each other, the next-hop address of the static route from a Spoke to the Hub or another Spoke is the tunnel address of the remote device.
     + When routes of Spokes are summarized to the Hub, the next-hop address of the static route from a Spoke to the Hub or another Spoke is the tunnel address of the Hub.
* **Configuring a dynamic route**
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Configure a dynamic route.
     
     
     
     Dynamic routes can be implemented using OSPF, or BGP. For the configuration of a dynamic routing protocol, see *Configuration Guide - IP Routing*.
     
     
     
     When configuring dynamic routing protocols, pay attention to the following points:
     
     | Scenario and Routing Protocol | OSPF | BGP |
     | --- | --- | --- |
     | Non-Shortcut Scenario of DSVPN | Configure the OSPF network type to multicast using the [**ospf network-type**](cmdqueryname=ospf+network-type) **broadcast** command on the Hub and Spokes. | Route aggregation cannot be configured on the Hub. |
     | Shortcut Scenario of DSVPN | Configure the OSPF network type to Point-to-Multipoint (P2MP) using the [**ospf network-type**](cmdqueryname=ospf+network-type) **p2mp** command on the Hub and Spokes. | Configure route aggregation on the Hub. |