Indirect Next Hop
=================

Indirect Next Hop

#### Definition

The indirect next hop technology changes a direct association between route prefixes and next-hop information to an indirect association, speeding up route convergence. Indirect next hop allows next-hop information mapped to a prefix to be refreshed separately from other prefixes of the same next hop, which speeds up route convergence.


#### Purpose

In a scenario requiring route recursion, when IGP route or tunnel switching occurs, the indirect next hop function helps a device rapidly refresh forwarding entries, which implements fast route convergence and minimizes the impact of route or tunnel switching on services.


#### Next-Hop Information

Mapping between route prefixes and next-hop information is the basis of indirect next hop. Next-hop information includes the address family, original next-hop IP address, and tunnel policy, which meets various route and tunnel recursion requirements. A device assigns an index to each piece of next-hop information, performs route recursion, notifies the recursive route to a routing protocol, and delivers a forwarding entry to the forwarding table.


#### On-Demand Route Recursion

Devices forward packets over dependent routes. Route recursion refers to the process of finding a dependent route based on a next-hop IP address, which is called route recursion.

On-demand route recursion indicates that once a dependent route changes, recursion is performed only for the next hop associated with the dependent route. If the destination address of the dependent route is an original next-hop IP address or network segment address contained in next-hop information, a dependent route change affects the recursion for the next-hop information. In other situations, dependent route changes do not affect the recursion for next-hop information. Therefore, if a dependent route changes, re-recursion is performed only for the next-hop information associated with the corresponding destination address of the changed route. For example, if the original next-hop IP address of a route to 10.2.2.2/32 is 10.1.1.1, the dependent route may be 10.1.1.1/32 or 10.1.0.0/16. If the route to 10.1.1.1/32 or 10.1.0.0/16 changes, the recursion of the original next hop 10.1.1.1 is affected.

With respect to tunnel recursion, when a tunnel alternates between up and down, a device merely needs to re-recurse the next-hop information whose original next-hop address is the same as the destination address of the tunnel.


#### Indirect Next Hop Implementation

Without indirect next hop, forwarding information and prefixes are in one-to-one mapping. Subsequently, the total convergence time is in direct proportion to the number of prefixes. With indirect next hop enabled, in the case of mapping between numerous prefixes and the same next hop, only the next hop-specific forwarding information needs to be added to the forwarding table, so that traffic related to the route prefixes can be switched simultaneously, speeding up route convergence.

**Figure 1** Implementation without indirect next hop used  
![](figure/en-us_image_0000001176742235.png)

In [Figure 1](#EN-US_CONCEPT_0000001176742209__fig_dc_vrp_ip-route_feature_001401), without indirect next hop, prefixes are independent, and each prefix is separately mapped to its next hop and forwarding information. If a dependent route changes, recursion is performed for the next-hop information mapped to each prefix, and forwarding information is updated based on the prefix. In this case, the convergence time is in direct proportion to the number of prefixes.

Note that prefixes of the same BGP peer have the same next hop, forwarding information, and refreshed forwarding information.

**Figure 2** Implementation with indirect next hop used  
![](figure/en-us_image_0000001176662323.png)

As shown in [Figure 2](#EN-US_CONCEPT_0000001176742209__fig_dc_vrp_ip-route_feature_001402), with indirect next hop, prefixes of routes from the same BGP peer share the next hop. When a dependent route changes, only the shared next hop participates in recursion and forwarding information mapped to the next hop is updated. In this case, routes of all prefixes can converge simultaneously, and the convergence time is irrelevant to the number of prefixes.


#### Comparison Between Route Recursion and Tunnel Recursion

[Table 1](#EN-US_CONCEPT_0000001176742209__tab_dc_vrp_ip-route_feature_001401) describes the differences between route recursion and tunnel recursion.

**Table 1** Comparison between route recursion and tunnel recursion
| Recursion Type | Characteristics |
| --- | --- |
| Route recursion | * Applies to BGP public network routes. * Is triggered by route changes. * Supports next hop recursion based on a specified route-policy. |
| Tunnel recursion | * Applies to BGP VPN routes. * Is triggered by tunnel or tunnel policy changes. * Uses tunnel policies to control recursion behaviors to meet requirements in different scenarios. |



#### IBGP Route Recursion to an IGP Route

**Figure 3** Network diagram of IBGP route recursion  
![](figure/en-us_image_0000001130782566.png)

As shown in [Figure 3](#EN-US_CONCEPT_0000001176742209__fig_dc_vrp_ip-route_feature_001403), an IBGP peer relationship is established between DeviceA and DeviceD. The IBGP peer relationship is usually established between two loopback interfaces on the routing devices. As the next hop of the IBGP route is not directly reachable, it cannot be used to guide packet forwarding. Therefore, to refresh the forwarding table and guide packet forwarding, a device needs to search for an eligible outbound interface and directly connected next hop based on the original IBGP next hop.

DeviceD receives 100,000 routes, which have the same original BGP next hop, from DeviceA. After recursion is performed, these routes follow the same IGP path (DeviceA -> DeviceB -> DeviceD). If the IGP path (DeviceA -> DeviceB -> DeviceD) fails, recursion does not need to be performed to each of these IBGP routes, and the relevant forwarding entries do not need to be refreshed one by one. Note that only the shared next hop participates in recursion and needs to be refreshed. Consequently, these IBGP routes converge to the path (DeviceA -> DeviceC -> DeviceD) on the forwarding plane. Therefore, the convergence time depends on only the number of next hops, not the number of prefixes.

If DeviceA and DeviceD establish a multi-hop EBGP peer relationship, the convergence procedure is the same as the preceding one. Indirect next hop also applies to the recursion of a multi-hop EBGP route.