BGP Route Load Balancing in an RR Scenario
==========================================

BGP_Route_Load_Balancing_in_an_RR_Scenario

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_CONCEPT_0172365035__fig_load-balance_feature_05501), an RR is deployed in AS 100. The RR learns external routes from two egress routers and reflects the routing information to its clients (R1, R2, ..., Rn). All the clients have equal-cost upstream links to the egress routers. However, the RR selects an optimal route from those received from the two egress routers and reflects only the optimal route to its clients. Therefore, the external routing information received by each client has only one next hop (either egress 1 or 2). As a result, traffic cannot be load-balanced.

**Figure 1** Load balancing among BGP routes  
![](images/fig_load-balance_feature_05501.png)

#### Solution 1

Establish an IBGP peer relationship with the RR on egress 1 and egress 2, create Loopback1 interfaces, and set the same IP address for the interfaces. Configure a route-policy to change the next hop of routes advertised to the RR to the address of Loopback1.

After BGP routes recurse to IGP routes, traffic can be load-balanced between routes from each client to each egress router because of the same next hop addresses on the two egress routers.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

To maintain the stability of the entire network and prevent unpredictable problems, it is recommended that the loopback interfaces with the same IP address on egress 1 and egress 2 be configured only as the next hops of the routes for load balancing.



#### Solution 2

Configure a route-policy on the RR in AS 100 so that traffic destined for AS 300 passes through egress 1 and that traffic destined for AS 400 passes through egress 2, as shown in [Figure 2](#EN-US_CONCEPT_0172365035__fig_load-balance_feature_05502).

**Figure 2** Load balancing among BGP routes  
![](images/fig_load-balance_feature_05502.png)

Perform the following operations on the RR in AS 100:

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Configure AS\_Path filters in regular expression to differentiate routes destined for AS 300 and AS 400.
   1. Run the [**ip as-path-filter**](cmdqueryname=ip+as-path-filter) *ToAS300* **permit [ 300 ]** command to configure an AS\_Path filter for routes destined for AS 300.
   2. Run the [**ip as-path-filter**](cmdqueryname=ip+as-path-filter) *ToAS400* **permit [ 400 ]** command to configure an AS\_Path filter for routes destined for AS 400.
3. Configure node 10 for the route-policy to set the next hop of routes destined for AS 300 to egress 1.
   1. Run the [**route-policy**](cmdqueryname=route-policy) **policy1 permit node 10** command to create node 10 for the route-policy.
   2. Run the [**if-match as-path-filter**](cmdqueryname=if-match+as-path-filter) **ToAS300** command to configure an **if-match** clause to match routes destined for AS 300.
   3. Run the [**apply ip-address next-hop**](cmdqueryname=apply+ip-address+next-hop) *ipv4-address* command to set the next hop of routes destined for AS 300 to egress 1.
4. Configure node 20 for the route-policy to set the next hop of routes destined for AS 400 to egress 2.
   1. Run the [**route-policy**](cmdqueryname=route-policy) **policy1 permit node 20** command to create node 20 for the route-policy.
   2. Run the [**if-match as-path-filter**](cmdqueryname=if-match+as-path-filter) **ToAS400** command to configure an **if-match** clause to match routes destined for AS 400.
   3. Run the [**apply ip-address next-hop**](cmdqueryname=apply+ip-address+next-hop) *ipv4-address* command to set the next hop of routes destined for AS 400 to egress 2.
5. Reflect the BGP routes after the next hop modification to clients.
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**bgp**](cmdqueryname=bgp) **100** command to enter the BGP view.
   3. Run the [**ipv4-family**](cmdqueryname=ipv4-family) **unicast** command to enter the BGP IPv4 unicast address family view.
   4. Run the [**peer route-policy**](cmdqueryname=peer+route-policy) *group-name* **policy1** **export** command to configure an AS\_Path-based route-policy.
6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this instance, an AS\_Path-based filter is configured on the RR to filter routes. To implement more refined route filtering, you can configure a community filter or an ACL, IP prefix list, extcommunity filter, or RD filter, among which, the extcommunity filter and RD filter take effect only on VPNv4 and VPNv6 routes, and the rest filters take effect on both VPN routes and public routes.



#### Follow-up Procedure

Run the [**save**](cmdqueryname=save) command to save the current configuration to the configuration file when a set of configuration is finished and the expected functions have been achieved.