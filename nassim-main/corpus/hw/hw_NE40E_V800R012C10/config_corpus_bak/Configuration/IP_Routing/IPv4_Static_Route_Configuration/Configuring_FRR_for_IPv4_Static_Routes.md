Configuring FRR for IPv4 Static Routes
======================================

Fast reroute (FRR) is applicable to services that are sensitive to packet delay and packet loss. FRR can be configured for IPv4 static routes to protect traffic using backup links.

#### Usage Scenario

FRR is applicable to IP services that are sensitive to delay and packet loss. FRR minimizes the impact of link faults on services.

You can specify different priorities for different static routes to implement FRR for static routes. Routes with the same destination IP address but different priorities can back up each other.


#### Pre-configuration Tasks

Before configuring FRR for IPv4 static routes, complete the following tasks:

* Configure parameters of the link layer protocol and IP addresses for interfaces and ensure that the link layer protocol on the interfaces is Up.
* Configure multiple routes with the same destination IP address but different priorities.
* [Configure dynamic BFD for IPv4 static routes](dc_vrp_static-route_disjoin_cfg_0012.html) or [configure static BFD for IPv4 static routes](dc_vrp_static-route_disjoin_cfg_0027.html) to speed up fault detection.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip route-static frr**](cmdqueryname=ip+route-static+frr) [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   FRR is enabled for public or VPN IPv4 static routes.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To implement route backup by configuring FRR for static routes, specify different priorities for these static routes.
   
   If FRR for static routes and BFD are both configured and a static route has an Ethernet interface as its outbound interface but has no next hop address, FRR cannot be implemented between this static route and those with next hop addresses. To implement FRR between them, specify a next hop address for this route.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

Run the following commands to check the previous configuration.

* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) **verbose** command to check detailed information about the backup outbound interface and the backup next hop in the routing table.
* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) *ip-address* [ *mask* | *mask-length* ] [ **longer-match** ] **verbose** command to check detailed information about the backup outbound interface and the backup next hop in the routing table.
* Run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) *ip-address1* { *mask1* | *mask-length1* } *ip-address2* { *mask2* | *mask-length2* } **verbose** command to check detailed information about the backup outbound interface and the backup next hop in the routing table.