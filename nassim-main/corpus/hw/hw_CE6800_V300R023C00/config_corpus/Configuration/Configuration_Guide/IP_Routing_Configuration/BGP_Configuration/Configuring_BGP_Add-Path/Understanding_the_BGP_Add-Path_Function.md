Understanding the BGP Add-Path Function
=======================================

Understanding the BGP Add-Path Function

#### Context

In a scenario where a route reflector (RR) and clients are configured, if the RR has multiple routes to the same destination (with the same prefix), the RR selects an optimal route from these routes and then sends only the optimal route to its clients. Therefore, the clients have only one route to the destination. If a link along this route fails, route convergence is performed and is time-consuming, which cannot meet high reliability requirements.

To address this issue, deploy the BGP Add-Path function on the RR. With the BGP Add-Path function, the RR can send two or more routes with the same prefix to its clients. After reaching the clients, these routes can load-balance traffic or back up each other, which ensures high reliability of data transmission.

![](public_sys-resources/note_3.0-en-us.png) 

* The BGP Add-Path function is mainly deployed on RRs even though this function can be configured on any device and take effect.
* With the BGP Add-Path function configured, you can set the maximum number of routes with the same prefix that an RR can send to its clients. The actual number of routes with the same prefix and destination that an RR can send to its clients is the smaller value between the configured maximum number and the number of available routes with the same prefix and destination.


#### Related Concepts

An Add-Path route is a preferred route that is selected by BGP after the BGP Add-Path function is configured.


#### Typical Networking

On the network shown in [Figure 1](#EN-US_CONCEPT_0000001130624146__fig_dc_vrp_bgp_feature_003501), DeviceA, DeviceB, and DeviceC are clients of the RR. DeviceB and DeviceC learn a route 1.1.1.1/32 from their EBGP peer DeviceD.

DeviceB and DeviceC advertise the route 1.1.1.1/32 to the RR. The two routes have the same destination address but different next hops. The RR selects an optimal route (the route learned from DeviceB for example) based on BGP route selection rules and advertises the optimal route to DeviceA. Therefore, DeviceA has only one route to 1.1.1.1/32.

**Figure 1** Typical network with BGP Add-Path deployed  
![](figure/en-us_image_0000001130624218.png)

BGP Add-Path can be configured on the RR to control the maximum number of routes with the same prefix that the RR can send to DeviceA. Assume that the configured maximum number of routes with the same prefix that the RR can send to DeviceA is 2. [Table 1](#EN-US_CONCEPT_0000001130624146__table_dc_vrp_bgp_feature_003501) describes differences between route convergence scenarios with and without the BGP Add-Path function configured.

**Table 1** Differences with and without the BGP Add-Path function configured
| Whether Add-Path Is Enabled | Route Advertisement | Route Convergence in Case of a Link Fault |
| --- | --- | --- |
| No | An RR advertises a single route to 1.1.1.1/32 with 10.1.1.1/24 as a next-hop IP address to DeviceA. | Only one link is available. A new route must be selected to take over traffic after routes converge. |
| Yes | The RR advertises two routes to 1.1.1.1/32, one with 10.1.1.1/24 and the other with 10.1.2.1/24 as a next-hop IP address to DeviceA. | If the two routes back up each other and a link fault occurs, the standby link takes over traffic.  If the two routes load-balance traffic and one link fails, the other link takes over all the traffic. |



#### Application Scenarios

BGP Add-Path applies to scenarios in which an RR is deployed and needs to send multiple routes with the same prefix to clients to ensure data transmission reliability.BGP Add-Path supports route attribute-or prefix-based filtering to control Add-Path route advertisement in a refined manner.

BGP Add-Path is used in traffic optimization scenarios and allows multiple routes to be sent to the controller.


#### Benefits

Deploying the BGP Add-Path function can improve network reliability.