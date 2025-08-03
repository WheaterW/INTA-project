Understanding Active-Route-Advertise
====================================

Understanding Active-Route-Advertise

#### Context

Active-route-advertise allows a device to advertise only optimal routes in the IP routing table to its BGP peers.

This feature prevents changes in selected routes to be advertised that may occur after independent BGP route selection is implemented. Currently, BGP uses independent route selection policies for route advertisement by default, allowing the optimal routes selected in the BGP routing table to be advertised to BGP peers, regardless of whether these routes are optimal in the IP routing table. However, in earlier versions that do not support independent route selection, a BGP route can be advertised to a peer only if the route is optimal in the IP routing table. Once a device is upgraded to support independent BGP route selection, the selected routes to be advertised to a peer may change, causing the data forwarding paths to be different from those used before the upgrade. To prevent these changes, you can configure active-route-advertise on the device.


#### Related Concepts

IP routing table: stores routes that are optimal in each available protocol-specific routing table. The route management module selects optimal routes from the stored routes and delivers those selected to the forwarding information base (FIB) table.

Independent BGP route selection: enables a device to advertise optimal routes selected in the BGP routing table to BGP peers, regardless of whether these routes are optimal in the IP routing table.


#### Implementation

On the network shown in [Figure 1](#EN-US_CONCEPT_0000001130783912__fig_dc_vrp_bgp_feature_003101), DeviceA and DeviceB are connected through a route reflector (RR), and DeviceA and the RR establish an OSPF neighbor relationship. DeviceB and DeviceC establish an EBGP peer relationship, and DeviceA and DeviceC are not directly connected.

**Figure 1** Network diagram of active-route-advertise  
![](figure/en-us_image_0000001130783984.png)

The route 10.0.0.0/8 is imported to the BGP and OSPF routing tables on DeviceA, and the RR learns both the BGP route 10.0.0.0/8 and OSPF route 10.0.0.0/8. By default, the OSPF route 10.0.0.0/8 is selected as an optimal route in the IP routing table through route preference comparison. [Table 1](#EN-US_CONCEPT_0000001130783912__table_active-route01) describes the changes after the RR is upgraded to support independent BGP route selection, including the changes in optimal route selection, route advertisement, and data forwarding path.

**Table 1** Change description
| Item | Source Version | Target Version Without Active-Route-Advertise | Target Version with Active-Route-Advertise |
| --- | --- | --- | --- |
| **Optimal route selection** | The BGP route 10.0.0.0/8 is optimal in the RR's BGP routing table, but not optimal in the IP routing table. | | |
| **Route advertisement** | Because independent BGP route selection is not supported, the RR does not advertise the BGP route 10.0.0.0/8 to DeviceB. As a result, DeviceC learns only the routes advertised by DeviceE and not by DeviceB. | Because independent BGP route selection is supported, the RR advertises the BGP route 10.0.0.0/8 to DeviceB. As a result, DeviceC learns the routes advertised by both DeviceB and DeviceE. | Because the BGP route 10.0.0.0/8 is not an optimal route in the RR's IP routing table, the RR does not advertise this route to DeviceB. As a result, DeviceC learns only the routes advertised by DeviceE and not by DeviceB. |
| **Available data forwarding paths** | Link B | Link A and Link B | Link B |
| **Actually selected data forwarding path** | DeviceC selects Link B to send data to 10.0.0.0/8. | DeviceC selects Link A to send data to 10.0.0.0/8. | DeviceC selects Link B to send data to 10.0.0.0/8. |

As described in [Table 1](#EN-US_CONCEPT_0000001130783912__table_active-route01), after active-route-advertise is configured on the RR after the upgrade, data sent by DeviceC to 10.0.0.0/8 is still forwarded through Link B.

![](public_sys-resources/note_3.0-en-us.png) 

Before you configure active-route-advertise, check whether BGP routes are optimal in the IP routing table. If all BGP routes are optimal in the IP routing table, data forwarding paths do not change after active-route-advertise is configured. If only some BGP routes are optimal in the IP routing table, analyze the impacts of active-route-advertise upon traffic forwarding and determine whether to configure this feature.



#### Benefits

Active-route-advertise prevents changes to data forwarding paths that may occur after a device is upgraded to support independent BGP route selection.