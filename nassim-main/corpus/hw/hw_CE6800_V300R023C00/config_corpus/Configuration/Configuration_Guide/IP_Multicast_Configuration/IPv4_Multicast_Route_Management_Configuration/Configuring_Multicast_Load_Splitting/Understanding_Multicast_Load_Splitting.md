Understanding Multicast Load Splitting
======================================

Understanding Multicast Load Splitting

#### Definition

Load splitting is different from load balancing. Load splitting provides a way to distribute data flows destined for the same destination to multiple equal-cost paths. The data traffic loads forwarded on each path may vary according to the load splitting mode. Load balancing is a special form of load splitting and distributes even data traffic loads on multiple equal-cost paths. In this context, multicast load splitting refers to distributing multicast traffic to multiple equal-cost optimal paths based on the configured multicast load splitting mode, instead of following the RPF check rules to select only the route with the largest next-hop address.


#### Fundamentals

By default, if multiple equal-cost optimal paths exist during multicast packet forwarding, equal-cost optimal routes are treated as follows during an RPF check:

* If the equal-cost routes are from the same routing table, for example, all from the unicast routing table or multicast static routing table, the route with the largest next-hop address is selected as the RPF route.
* If the equal-cost routes are from different routing tables, the route preferences are compared first, and then the mask matching lengths are compared. If they are the same, the device selects a route as the RPF route after a function-based calculation.

In either of the preceding situations, the device selects only one route as the RPF route to forward multicast packets. After multicast load splitting is configured, if multiple equal-cost routes exist on the network, multicast data flows can be split according to different policies to optimize network traffic transmission.

In [Figure 1](#EN-US_CONCEPT_0000001176742435__fig_dc_fd_mrm_000701), the multicast source (Source) sends multicast flows to multicast group G. An IGP (for example, OSPF) runs between DeviceA and DeviceD. Two equal-cost paths are available: DeviceA -> DeviceB -> DeviceD and DeviceA -> DeviceC -> DeviceD. By default, multicast traffic is forwarded through interface0 according to the RPF check rules because it has a larger IP address than interface1. After multicast load splitting is configured, forwarding paths are not selected according to the next-hop addresses. Rather, multicast flows are forwarded through both DeviceA -> DeviceB -> DeviceD and DeviceA -> DeviceC ->DeviceD.**Figure 1** Multicast forwarding without and with multicast load splitting  
![](figure/en-us_image_0000001176662559.png)


#### Multicast Load Splitting Modes

Multicast load splitting provides varied load splitting modes for the data flows from any-source multicast (\*, G) or source-specific multicast (S, G) to meet the requirements of different applications.

**Multicast group G-based load splitting**

The multicast group-based load splitting policy is mainly used when a large number of different multicast groups exist on a network. In [Figure 2](#EN-US_CONCEPT_0000001176742435__fig_02), for the data flows sent from the source to different multicast groups (G1 to G10), two equal-cost routes from the source exist on Device7, Device6 and Device5. Using a series of algorithms, the multicast devices select a proper route from the equal-cost routes for each multicast group (G) as the packet forwarding route. After load splitting is implemented, flows transmitted on different paths are sent to different groups (G).

**Figure 2** Multicast group G-based load splitting  
![](figure/en-us_image_0000001130623004.png)

**Multicast source S-based load splitting**

The multicast source-based load splitting policy is mainly used when a large number of different multicast sources exist on a network. In [Figure 3](#EN-US_CONCEPT_0000001176742435__fig_03), for the data flows sent from different sources (S1 to S10) to the same multicast group (G), two equal-cost routes from the sources exist on Device7, Device6 and Device5. Using a series of algorithms, the multicast devices select a proper route from the equal-cost routes for each multicast source (S) as the packet forwarding route. After load balancing is implemented, flows transmitted on different paths belong to different sources (S).

**Figure 3** Multicast source S-based load splitting  
![](figure/en-us_image_0000001176742449.png)

**Load splitting based on multicast source-group (S, G)**

This load splitting policy applies to scenarios where a large number of different multicast groups and multicast sources exist on a network. In [Figure 4](#EN-US_CONCEPT_0000001176742435__fig_04), for the data flows sent from different sources (S1 to S10) to different multicast groups (G1 to G10), two equal-cost routes from the sources exist on Device7, Device6 and Device5. Using a series of algorithms, the multicast devices select a proper route from the equal-cost routes for each multicast source-group (S, G) as the packet forwarding route. After load splitting is implemented, flows transmitted on different paths belong to different multicast source-groups (S, G).

**Figure 4** Load splitting based on multicast source-group (S, G)  
![](figure/en-us_image_0000001130782794.png)

**Stable-preferred load splitting**

This policy can be applied to the preceding three load splitting scenarios. In [Figure 5](#EN-US_CONCEPT_0000001176742435__fig_05), if route flapping occurs on the multicast network, frequent load adjustment on a multicast device will aggravate route flapping. After stable-preferred load splitting is configured on the device, the device â instead of immediately adjusting the load â adjusts the load only after route flapping ends. When the network topology becomes stable, routing entries on the device from the same multicast source are evenly distributed on equal-cost paths. Stable-preferred load splitting is implemented based on entries instead of traffic. As a result, when there are entries that do not forward multicast traffic, the number of entries on each outbound interface may be balanced, but the multicast traffic sent by each outbound interface may not be balanced.

**Figure 5** Stable-preferred load splitting  
![](figure/en-us_image_0000001130782786.png)

**Link bandwidth-based load splitting**

This policy applies to networks where links have different load bandwidths. In [Figure 6](#EN-US_CONCEPT_0000001176742435__fig15585182515482), the load capabilities of paths on the network are different. If routing entries are evenly distributed to equal-cost paths, the load bandwidth of each path cannot be fully used. After link bandwidth-based load splitting is configured, routing entries can be unevenly distributed to paths based on link bandwidth. When a new entry is generated, the multicast devices calculate a value (Interface bandwidth/Number of current interface entries) for each equal-cost route and select the route with the largest calculation result as the forwarding route of the entry. If entries are deleted, load imbalance occurs. In this case, loads are not automatically adjusted with link bandwidth-based load splitting configured.

**Figure 6** Link bandwidth-based load splitting  
![](figure/en-us_image_0000001130623012.png)