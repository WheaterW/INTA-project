Configuring FRR for IPv6 Static Routes
======================================

Fast ReRoute (FRR) is applicable to services that are sensitive to packet delay and packet loss. FRR can be configured for IPv6 static routes to protect traffic using backup links.

#### Usage Scenario

FRR is applicable to IP services that are sensitive to delay and packet loss. FRR minimizes the impact of link faults on services.

If two static routes with the same prefix but different priorities are configured, they can implement FRR. The route with the higher priority is the primary route, and the route with the lower priority is the backup route. If the link that the primary route passes fails, traffic is rapidly switched to the backup route, thereby reducing the number of lost packets. On the network shown in [Figure 1](#EN-US_TASK_0172365488__fig107934316293), two static routes with different priorities from DeviceA to DeviceC work in primary/backup mode. The two routes are both delivered to the forwarding table. When the primary link A is normal, traffic is transmitted through link A. If link A fails, FRR allows traffic to be quickly switched to link B.

**Figure 1** FRR for IPv6 static routes  
![](figure/en-us_image_0237117043.png)

#### Pre-configuration Tasks

Before configuring FRR for IPv6 static routes, complete the following tasks:

* Configure parameters of the link layer protocol and IPv6 addresses for interfaces and ensure that the link layer protocol on the interfaces is up.
* [Configure dynamic BFD for IPv6 static routes](dc_vrp_static-route_disjoin_cfg_0023.html) or [configure static BFD for IPv6 static routes](dc_vrp_static-route_disjoin_cfg_0028.html) to speed up fault detection.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 route-static frr**](cmdqueryname=ipv6+route-static+frr) [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   FRR is enabled for public or VPN IPv6 static routes.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To implement route backup by configuring FRR for static routes, you need to specify different priorities for these static routes.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring FRR for IPv6 static routes, verify the configuration.

* Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) **verbose** command to check detailed information about the backup outbound interface and the backup next hop in the routing table.
* Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) *ipv6-address* [ *prefix-length* ] [ **longer-match** ] **verbose** command to check detailed information about the backup outbound interface and the backup next hop in the routing table.