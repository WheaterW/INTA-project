Understanding Routing Loop Detection for Routes Imported to OSPFv3
==================================================================

Routes of an OSPFv3 process can be redistributed by another OSPFv3 process or the process of another protocol (such as IS-IS or BGP) through route import or default route distribution. However, if a device that performs such a route import or default route distribution is incorrectly configured, routing loops may occur. OSPFv3 can use the routing loop detection function to detect routing loops.

![](../public_sys-resources/note_3.0-en-us.png) 

When OSPFv3 is configured to import routes or distribute default routes, routing loop detection can be deployed to proactively detect whether routing loops exist in the topology and whether the routing loop prevention mechanism of the import route-policy takes effect. Routing loop alarms can be reported to locate configuration errors in time.

Generally, routing loop detection cannot eliminate routing loops. Increasing the metric value or adjusting the route preference value after a routing loop alarm is reported can temporarily prevent routing loops but may cause the traffic to be forwarded in an unexpected path. Therefore, routing loop detection can only be used temporarily. To eliminate routing loops in the long run, re-plan network configurations.


#### Related Concepts

**Redistribute ID**

IS-IS uses a system ID as a redistribution identifier, OSPF and OSPFv3 use a router ID + process ID as a redistribution identifier, and BGP uses a VrfID + random number as a redistribution identifier. For ease of understanding, the redistribution identifiers of different protocols are all called Redistribute IDs. When routes are distributed, the information carried in the routes contains Redistribute IDs.

**Redistribute List**

A Redistribute list may consist of multiple Redistribute IDs. Each Redistribute list of BGP contains a maximum of four Redistribute IDs, and each Redistribute list of any other routing protocol contains a maximum of two Redistribute IDs. When the number of Redistribute IDs exceeds the corresponding limit, the old ones are discarded according to the sequence in which Redistribute IDs are added.


#### OSPFv3 Redistribute ID Format

OSPFv3 Redistribute IDs are distributed through the sub-TLV of the OSPFv3 External-Prefix TLV carried in OSPFv3 E-AS-External-LSAs. [Figure 1](#EN-US_CONCEPT_0000001223706301__fig191609246418) shows the format of the Redistribute ID TLV.

**Figure 1** Redistribute ID TLV format  
![](figure/en-us_image_0000001831182341.png)

**Table 1** Fields in the Redistribute ID TLV format
| Field | Length | Description |
| --- | --- | --- |
| Type | 16 bits | TLV type. The value is 32770. |
| Length | 16 bits | Total length of the TLV (excluding the Type and Length fields). |
| Flags | 8 bits | Flags. Currently, the value is 0. |
| Reserved | 24 bits | Reserved field. |
| Redistribute ID1 | 64 bits | Device that imported the route last time and the Redistribute ID of a protocol on the device. |
| Redistribute ID2 | 64 bits | Device that imported the route last but one time and the Redistribute ID of a protocol on the device. This field is optional. |

Currently, OSPFv3 allows a TLV to carry a maximum of two Redistribute IDs. If more than two routes corresponding to a prefix are imported, only the latest two Redistribute IDs are retained. If the received TLV carries more than two Redistribute IDs, only the first two Redistribute IDs are processed.


#### Cause (OSPFv3 Inter-Process Mutual Route Import)

In [Figure 2](#EN-US_CONCEPT_0000001223706301__fig28588511242), DeviceA, DeviceB, and DeviceC run OSPFv3 process 1; DeviceF and DeviceG run OSPFv3 process 2; DeviceD and DeviceE run both of the processes. DeviceD imports routes from OSPFv3 process 1 to OSPFv3 process 2 for distribution. DeviceE imports the routes from OSPFv3 process 2 to OSPFv3 process 1. In this case, the routes are re-distributed back to OSPFv3 process 1. As the costs of the routes newly distributed by DeviceE are smaller, they are preferentially selected by OSPFv3 process 1, resulting in routing loops.

**Figure 2** Typical network diagram of OSPFv3 inter-process mutual route import  
![](figure/en-us_image_0000001187901616.png "Click to enlarge")

Take the route distributed by DeviceA as an example. A stable routing loop is formed through the following phases:

**Phase 1**

On the network shown in [Figure 3](#EN-US_CONCEPT_0000001223706301__fig32561325134118), OSPFv3 process 1 on DeviceA imports the static route 2001:DB8:1::1 and floods a Type 5 AS-External-LSA in OSPFv3 process 1. After receiving the LSA, OSPFv3 process 1 on DeviceD and OSPFv3 process 1 on DeviceE each calculate a route to 2001:DB8:1::1, with the outbound interfaces being interface1 on DeviceD and interface1 on DeviceE, respectively, and the cost being 102. At this point, the routes to 2001:DB8:1::1 in OSPFv3 process 1 in the routing tables of DeviceD and DeviceE are active.

**Figure 3** Phase 1  
![](figure/en-us_image_0000001233382691.png "Click to enlarge")

**Phase 2**

OSPFv3 process 2 on DeviceD is configured to import routes from OSPFv3 process 1, and no import route-policy is configured or the configured route-policy is improper. In [Figure 4](#EN-US_CONCEPT_0000001223706301__fig647512502514), DeviceD imports routes from OSPFv3 process 1 to OSPFv3 process 2, and the advertised Type 5 AS-External LSA is flooded in OSPFv3 process 2. After receiving the LSA, OSPFv3 process 2 on DeviceE calculates a route to 2001:DB8:1::1, with the cost being 2, which is smaller than that (102) of the route calculated by OSPFv3 process 1. As a result, the active route to 2001:DB8:1::1 in the routing table of DeviceE is switched from the one calculated by OSPFv3 process 1 to the one calculated by OSPFv3 process 2, and the outbound interface of the route is sub-interface2.1.

**Figure 4** Phase 2  
![](figure/en-us_image_0000001233581119.png "Click to enlarge")

**Phase 3**

In [Figure 5](#EN-US_CONCEPT_0000001223706301__fig191141331165910), DeviceE imports the route from OSPFv3 process 2 to OSPFv3 process 1 and floods a Type 5 AS-External LSA in OSPFv3 process 1. After receiving the LSA, OSPFv3 process 1 on DeviceE recalculates the route to 2001:DB8:1::1. The cost of the route becomes 2, which is smaller than that of the previously calculated route. Therefore, the route to 2001:DB8:1::1 in OSPFv3 process 1 on DeviceD is changed to the route distributed by DeviceE, and the outbound interface is interface 2.

**Figure 5** Phase 3  
![](figure/en-us_image_0000001188061528.png "Click to enlarge")

**Phase 4**

After the route to 2001:DB8:1::1 on DeviceD is updated, OSPFv3 process 2 still imports the route from OSPFv3 process 1 because the route remains active, and continues to distribute/update a Type 5 AS-External-LSA.

By now, a stable routing loop is formed. Assuming that traffic is injected from DeviceF, [Figure 6](#EN-US_CONCEPT_0000001223706301__fig850684615511) shows the traffic flow when the routing loop occurs.

**Figure 6** Traffic flow when the routing loop occurs  
![](figure/en-us_image_0000001233462637.png)

#### Implementation (OSPFv3 Inter-Process Mutual Route Import)

Routing loop detection for the routes imported between OSPFv3 processes can resolve the routing loops in the preceding scenario.

When distributing a Type 5 AS-External LSA for an imported route, OSPFv3 also uses an E-AS-External-LSA to distribute to other devices the Redistribute ID of the device that redistributes the imported route. If the route is redistributed by different protocols through multiple devices, all the Redistribute IDs of these protocols on the devices are distributed through an E-AS-External-LSA. When receiving the E-AS-External-LSA, a route calculation device saves the Redistribute ID and route information of the route redistribution device. When another process of a route calculation device imports the route, the device checks whether a routing loop occurs according to the route redistribution information. If a routing loop occurs, the device attaches a large route cost to the AS-External-LSA for the imported route so that other devices preferentially select other paths after learning the route. This prevents routing loops.

![](../public_sys-resources/note_3.0-en-us.png) 

* The prefixes distributed through Type 5 AS-External LSAs are used for route calculation. E-AS-External-LSAs are used to distribute extended TLVs for specified prefixes without affecting OSPFv3 route calculation results, and the device stores the information carried in the Redistribute ID TLV as route attributes in its routing table.
* When a routing loop is detected, if the original cost of the corresponding route is less than 10223715, the cost of the route is adjusted to 10223715; if the original cost is greater than or equal to 10223715, the cost of the route is adjusted to 16777214. For ease of understanding, the following section assumes that the original route cost is less than 10223715.
* After the cost of a route distributed through an LSA is increased, the device does not proactively withdraw the routing loop state. Instead, it keeps distributing the new route cost. To manually exit the routing loop state, you need to run the clear command.

**Figure 7** Typical network diagram for routing loop detection when routes are imported between OSPFv3 processes  
![](figure/en-us_image_0000001187743052.png "Click to enlarge")

On the network shown in [Figure 7](#EN-US_CONCEPT_0000001223706301__fig18981473557), assume that the router ID of OSPFv3 process 2 on DeviceD is 4.4.4.2 (the Redistribute ID is 0x0404040200000002) and that the router ID of OSPFv3 process 1 on DeviceE is 5.5.5.1 (the Redistribute ID is 0x0505050100000001).

Routing loops are detected and resolved as follows:

1. Through OSPFv3 process 1, DeviceD learns the route 2001:DB8:1::1/128 distributed by DeviceB, imports the route from OSPFv3 process 1 to OSPFv3 process 2, and adds Redistribute ID information to the route to be distributed through an E-AS-External-LSA.
2. Through OSPFv3 process 2, DeviceE learns the route distributed by DeviceD and saves the Redistribute list distributed by DeviceD through OSPFv3 process 2 to the routing table when calculating routes. At this point, the next hop of the route 2001:DB8:1::1 in OSPFv3 process 2 on DeviceE is DeviceD.
3. DeviceE imports the route from OSPFv3 process 2 to OSPFv3 process 1 and redistributes the route through OSPFv3 process 1. The corresponding E-AS-External-LSA contains the Redistribute ID of OSPFv3 process 1 on DeviceE and the Redistribute ID of OSPFv3 process 2 on DeviceD.
4. OSPFv3 process 1 on DeviceD learns the Redistribute List corresponding to the route distributed by DeviceE and saves the Redistribute List in the routing table. At this point, the next hop of the route 2001:DB8:1::1 in OSPFv3 process 1 on DeviceD is DeviceE, indicating that a routing loop occurs.
5. When importing the route from OSPFv3 process 1 to OSPFv3 process 2, DeviceD finds that the Redistribute List of the route contains its own Redistribute ID, considers that a routing loop is detected, and reports an alarm. When re-distributing the route, OSPFv3 process 2 on DeviceD attaches a large cost to the route in the AS-External LSA.
6. After learning the route, OSPFv3 process 2 on DeviceE does not preferentially select it because of the large cost. Therefore, the route is not optimal in the IP routing table.
7. DeviceE fails to import the route from OSPFv3 process 2 to OSPFv3 process 1 and therefore withdraws the route through OSPFv3 process 1.
8. Unable to learn the route 2001:DB8:1::1 distributed by DeviceE, OSPFv3 process 1 on DeviceD updates the next hop of the route to DeviceB, indicating that the routing loop is resolved.![](../public_sys-resources/note_3.0-en-us.png) 
   
   In the preceding typical networking:
   
   * Routing loop detection is performed randomly. In the preceding process, it is assumed that DeviceD distributes a Redistribute ID and detects a routing loop first. In this case, DeviceD distributes a large route cost. If due to another time sequence, DeviceE distributes a Redistribute ID and detects a routing loop first, OSPFv3 process 1 on DeviceE distributes a large route cost.
   * Distributing a large route cost does not necessarily resolve routing loops. For example, if routes are imported between two routing protocols, a route with a larger cost may be preferentially selected.
   * If routes are imported within a protocol on a device and the device detects a routing loop, it increases the cost of the route to be distributed. After the remote device learns this route with a large cost, it does not preferentially select this route as the optimal route in the IP routing table. In this manner, the routing loop is resolved. In the case of inter-protocol route import, if a routing protocol with a higher priority detects a routing loop, although this protocol increases the cost of the corresponding route, the cost increase will not render the route inactive. As a result, the routing loop cannot be eliminated. If the routing protocol with a lower priority detects a routing loop and increases the cost of the corresponding route, the originally imported route is preferentially selected. In this case, the routing loop can be eliminated.

#### Cause (Mutual Route Import Between OSPFv3 and IS-IS)

On the network shown in [Figure 8](#EN-US_CONCEPT_0000001223706301__fig154351016135419), DeviceA, DeviceB, and DeviceC run OSPFv3 process 1, DeviceF and DeviceG run IS-IS process 2, and DeviceD and DeviceE run both processes. DeviceD imports routes from OSPFv3 process 1 to IS-IS process 2. DeviceE imports routes from IS-IS process 2 to OSPFv3 process 1. The routes imported by IS-IS process 2 on DeviceD are re-distributed back to OSPFv3 process 1 on DeviceE. As the costs of the routes newly distributed by DeviceE are smaller, they are preferentially selected by OSPFv3 process 1, resulting in routing loops.

**Figure 8** Traffic flow when a routing loop occurs during route import between OSPFv3 and IS-IS  
![](figure/en-us_image_0000001187583070.png "Click to enlarge")

#### Implementation (Mutual Route Import Between OSPFv3 and IS-IS)

Redistribute IDs of IS-IS routes are delivered to the IP routing table along with the routes. The IP routing table stores Redistribute IDs in a unified format. When OSPFv3 imports the IS-IS routes, the processing of Redistribute IDs is the same as that in a scenario where routes are mutually imported between OSPFv3 processes.

On the network shown in [Figure 9](#EN-US_CONCEPT_0000001223706301__fig11173182413446), assume that the system ID of IS-IS process 2 on DeviceD is 0000.0000.000d (the Redistribute ID is 0x00000000000d0000) and that the router ID of OSPFv3 process 1 on DeviceE is 5.5.5.1 (the Redistribute ID is 0x0505050100000001).

**Figure 9** Typical network diagram for routing loop detection when OSPFv3 and IS-IS import routes from each other  
![](figure/en-us_image_0000001784362146.png "Click to enlarge")

Routing loops are detected and resolved as follows:

1. Through OSPFv3 process 1, DeviceD learns the route distributed by DeviceB and imports the route from OSPFv3 process 1 to IS-IS process 2. When IS-IS process 2 on DeviceD distributes route information, it uses the extended prefix sub-TLV to distribute the Redistribute ID of IS-IS process 2 through an LSP.
2. IS-IS process 2 on DeviceE learns the route distributed by DeviceD and saves the Redistribute ID distributed by IS-IS process 2 on DeviceD in the routing table during route calculation. At this point, the next hop of the route 2001:DB8:1::1 in IS-IS process 2 on DeviceE is DeviceD.
3. DeviceE imports the route from IS-IS process 2 to OSPFv3 process 1 and uses an E-AS-External-LSA to distribute the Redistribute ID of OSPFv3 process 1 on DeviceE when distributing route information.
4. Similarly, after OSPFv3 process 1 on DeviceD learns the route from DeviceE, DeviceD saves the Redistribute ID distributed by OSPFv3 process 1 on DeviceE in the routing table during route calculation. At this point, the next hop of the route 2001:DB8:1::1 in OSPFv3 process 1 on DeviceD is DeviceE, indicating that a routing loop occurs.
5. When importing the route from OSPFv3 process 1 to IS-IS process 2, DeviceD finds that the Redistribute List of the route contains its own Redistribute ID, considers that a routing loop is detected, and reports an alarm. IS-IS process 2 on DeviceD distributes a large cost along with the imported route.
6. Because IS-IS has a higher priority than OSPFv3 ASE, the route selection result remains unchanged, and the routing loop persists.
7. DeviceE imports the route from IS-IS process 2 to OSPFv3 process 1, finds that the Redistribute List of the route contains its own Redistribute ID, considers that a routing loop is detected, and reports an alarm. OSPFv3 process 1 on DeviceE distributes a large route cost through an AS-External LSA along with the imported route.
8. After learning the LSA with a large cost from DeviceE, OSPFv3 process 1 on DeviceD preferentially selects the LSA distributed by DeviceB and updates the next hop of the route 2001:DB8:1::1 to DeviceB, indicating that the routing loop is resolved.![](../public_sys-resources/note_3.0-en-us.png) 
   
   In the preceding typical networking:
   
   If routes are imported within a protocol on a device and the device detects a routing loop, it increases the cost of the route to be distributed. After the remote device learns this route with a large cost, it does not preferentially select this route as the optimal route in the IP routing table. In this manner, the routing loop is resolved.
   
   In the case of inter-protocol route import, if a routing protocol with a higher priority detects a routing loop, although this protocol increases the cost of the corresponding route, the cost increase will not render the route inactive. As a result, the routing loop cannot be eliminated. If the routing protocol with a lower priority detects a routing loop and increases the cost of the corresponding route, the originally imported route is preferentially selected. In this case, the routing loop can be eliminated.

#### Cause (Mutual Route Import Between OSPFv3 and BGP)

On the network shown in [Figure 10](#EN-US_CONCEPT_0000001223706301__fig199452121070), DeviceA, DeviceB, and DeviceC run a BGP process, DeviceF and DeviceG run OSPFv3 process 2, and DeviceD and DeviceE run both processes. A BGP peer relationship is established between DeviceD and DeviceE. DeviceD imports routes from BGP to OSPFv3 process 2 for distribution. DeviceE imports routes from OSPFv3 process 2 to BGP, indicating that the routes are re-distributed back to BGP. Because no import route-policy is configured or the configured route-policy is improper, the route newly distributed by DeviceD may be selected as the optimal route by BGP, causing a routing loop.

**Figure 10** Traffic flow when a routing loop occurs during route import between OSPFv3 and BGP  
![](figure/en-us_image_0000001233181195.png "Click to enlarge")

#### Implementation (Mutual Route Import Between OSPFv3 and BGP)

Redistribute IDs of BGP routes are delivered to the IP routing table along with the routes. The IP routing table stores Redistribute IDs in a unified format. When OSPFv3 imports the BGP routes, the processing of Redistribute IDs is the same as that in a scenario where routes are mutually imported between OSPFv3 processes.

On the network shown in [Figure 11](#EN-US_CONCEPT_0000001223706301__fig167183331883), assume that the router ID of OSPFv3 process 2 on DeviceD is 4.4.4.2 (the Redistribute ID is 0x0404040200000002) and that BGP on DeviceE uses VrfID 0 and random number 7 (the Redistribute ID is 0x0000000000000007).

**Figure 11** Typical network diagram for routing loop detection when OSPFv3 and BGP import routes from each other  
![](figure/en-us_image_0000001831301901.png "Click to enlarge")

Routing loops are detected and resolved as follows:

1. Through BGP, DeviceD learns the route distributed by DeviceB and imports the BGP route to OSPFv3 process 2. When DeviceD distributes the imported route through OSPFv3 process 2, the extended prefix E-AS-External-LSA contains the Redistribute ID of OSPFv3 process 2 on DeviceD.
2. Through OSPFv3 process 2, DeviceE learns the route distributed by DeviceD and saves the Redistribute List distributed by OSPFv3 process 2 on DeviceD to the routing table when calculating routes. At this point, the next hop of the route 2001:DB8:1::1 in OSPFv3 process 2 on DeviceE is DeviceD.
3. After DeviceE imports routes from OSPFv3 process 2 to BGP, the Redistribute ID information of OSPFv3 process 2 is inherited by the generated BGP routes, and BGP routing loop attributes are generated and distributed.
4. After BGP on DeviceD learns the route distributed by DeviceE, DeviceD saves the Redistribute ID distributed by BGP on DeviceE to the routing table when calculating routes. At this point, the next hop of the BGP route 2001:DB8:1::1 on DeviceD is DeviceE, indicating that a routing loop occurs.
5. When importing the route from BGP to OSPFv3 process 2, DeviceD finds that the Redistribute List of the route contains its own Redistribute ID, considers that a routing loop is detected, and reports an alarm. OSPFv3 process 2 on DeviceD distributes a large cost along with the imported route.
6. Because OSPFv3 has a higher priority than BGP, the route selection result remains unchanged, and the routing loop persists.
7. OSPFv3 on DeviceE learns the route distributed by OSPFv3 on DeviceD. When importing the route from OSPFv3 process 2 to BGP, DeviceE finds that the Redistribute List of the route contains its own Redistribute ID, considers that a routing loop is detected, and reports an alarm. In addition, DeviceE reduces the priority of the imported route when distributing it through BGP.
8. After learning this route from DeviceE, BGP on DeviceD preferentially selects the route distributed by DeviceB. In this case, the next hop of the route 2001:DB8:1::1 in OSPFv3 process 2 on DeviceD is DeviceB, indicating that the routing loop is resolved.![](../public_sys-resources/note_3.0-en-us.png) 
   
   In the preceding typical networking:
   
   If routes are imported within a protocol on a device and the device detects a routing loop, it increases the cost of the route to be distributed. After the remote device learns this route with a large cost, it does not preferentially select this route as the optimal route in the IP routing table. In this manner, the routing loop is resolved.
   
   In the case of inter-protocol route import, if a routing protocol with a higher priority detects a routing loop, although this protocol increases the cost of the corresponding route, the cost increase will not render the route inactive. As a result, the routing loop cannot be eliminated. If the routing protocol with a lower priority detects a routing loop and increases the cost of the corresponding route, the originally imported route is preferentially selected. In this case, the routing loop can be eliminated.