Solution to the Low Equal-Cost Route Specification on the Remote Device Without Interrupting Services
=====================================================================================================

Solution_to_the_Low_Equal-Cost_Route_Specification_on_the_Remote_Device_Without_Interrupting_Services

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_CONCEPT_0172365040__fig_load-balance_feature_05601), the two egresses of AS 100 are Huawei NE40Es. Each of the two egresses was connected to AS 200 through six links, and then the number of links was doubled for expansion. However, the two egresses received traffic along only eight links from the remote device after the expansion because the remote device supports only eight equal-cost routes to the same network segment. It is required that services run uninterrupted. Therefore, the six links cannot be added to a trunk.

**Figure 1** Link expansion  
![](images/fig_load-balance_feature_05601.png)

#### Solution

No more links can be added for load balancing because of the equal-cost route specification of the remote device. In this situation, deploy a BGP route-policy. The EBGP peer address of egress 1 is 1.1.1.1. A new loopback interface with IP address 1.1.1.2 is configured on the remote device, and a new EBGP peer relationship is established between the new loopback interface and egress 1. Perform the following operations:

1. Configure a pair of loopback interfaces at both ends and establish EBGP peer relationships.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**interface loopback**](cmdqueryname=interface+loopback) *interface-number* command to create a loopback interface.
   3. Run the [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } command to configure an IP address for the loopback interface.
   4. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   5. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   6. Run the [**bgp**](cmdqueryname=bgp) **1.1.1.2** **as-number** *as-number* command to set the IP address of the EBGP peer to the new loopback interface IP address on the remote end.
   7. Run the [**bgp**](cmdqueryname=bgp) **1.1.1.2** **connect-interface loopback** *interface-number* command to configure the new loopback interface as the source interface of the TCP session used by the BGP connection.
2. Configure two groups of static routes for the EBGP peers, with six static routes to each EBGP peer.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**ip route-static**](cmdqueryname=ip+route-static) **1.1.1.1** { *mask* | *mask-length* } { *nexthop-address* | *interface-type interface-number* [ *nexthop-address* ] } command to configure six static routes to 1.1.1.1, with the same outbound interfaces and next hops as those of the original links.
   3. Run the [**ip route-static**](cmdqueryname=ip+route-static) **1.1.1.2** { *mask* | *mask-length* } { *nexthop-address* | *interface-type interface-number* [ *nexthop-address* ] } command to configure six static routes to 1.1.1.2, with the same outbound interfaces and next hops as those of the new links.
   
   Therefore, BGP routes can recurse to the two groups of equal-cost routes to both EBGP peers.
3. Configure a route-policy and set the next hops of some routes to the new loopback interface of the remote device for load balancing.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**ip ip-prefix**](cmdqueryname=ip+ip-prefix) **prefix1** **index** *index-number* *ipv4-address* *mask-length* [ **greater-equal** *greater-equal-value* ] [ **less-equal** *less-equal-value* ] command to configure an IP prefix list to match the destinations of routes to be switched to the new links.
   3. Run the [**route-policy**](cmdqueryname=route-policy) **new-policy** **permit node 10** command to configure a route-policy and create node 10 for it.
   4. Run the [**if-match ip-prefix**](cmdqueryname=if-match+ip-prefix) **prefix1** command to apply the IP prefix list to the route-policy.
   5. Run the [**apply ip-address next-hop**](cmdqueryname=apply+ip-address+next-hop) **1.1.1.2** command to set the next hops of the routes that match the route-policy to the new loopback interface of the remote device.
4. Configure a route-policy so that the original six links carry the rest traffic.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**route-policy**](cmdqueryname=route-policy) **old-policy** **deny node 10** command to configure a route-policy and create node 10 for it.
   3. Run the [**if-match ip-prefix**](cmdqueryname=if-match+ip-prefix) **prefix1** command to apply the IP prefix list to the route-policy.
   4. Run the [**route-policy**](cmdqueryname=route-policy) **old-policy** **permit node 20** command to configure node 20 for the route-policy.
   5. Run the [**apply ip-address next-hop**](cmdqueryname=apply+ip-address+next-hop) **1.1.1.1** command to set the next hops of the routes that match the route-policy to the original loopback interface of the remote device.
5. Apply the route-policy to the routes to be advertised to the EBGP peer.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
   3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **unicast** command to enter the BGP IPv4 unicast address family view.
   4. Run the [**peer**](cmdqueryname=peer) **1.1.1.1 route-policy old-policy export** command to apply the route-policy to the original EBGP peer.
   5. Run the [**peer**](cmdqueryname=peer) **1.1.1.2 route-policy new-policy export** command to apply the route-policy to the new EBGP peer.
6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, an IP prefix list is configured to filter routes. You can also configure an ACL, AS\_Path filter, community filter, extcommunity filter, or RD filter. The extcommunity filter and RD filter take effect only on VPNv4 and VPNv6 routes, and the rest filters take effect on both VPN and public routes.



#### Follow-up Procedure

Run the [**save**](cmdqueryname=save) command to save the current configuration to the configuration file when a set of configuration is finished and the expected functions have been achieved.