Understanding Routing Loop Detection for Routes Imported to IS-IS
=================================================================

Routes of an IS-IS process can be imported to another IS-IS process or the process of another protocol (such as OSPF or BGP) for redistribution. However, if a device that performs such a route import is incorrectly configured, routing loops may occur. IS-IS can use the routing loop detection function to detect routing loops.

#### Related Concepts

**Redistribute ID**

IS-IS uses a system ID as a redistribution identifier, OSPF and OSPFv3 use a router ID + process ID as a redistribution identifier, and BGP uses a VrfID + random number as a redistribution identifier. For ease of understanding, the redistribution identifiers of different protocols are all called Redistribute IDs. When routes are distributed, the extended TLVs carried in the routes contain Redistribute IDs.

**Redistribute List**

A Redistribute list may consist of multiple Redistribute IDs. Each Redistribute list of BGP contains a maximum of four Redistribute IDs, and each Redistribute list of any other routing protocol contains a maximum of two Redistribute IDs. When the number of Redistribute IDs exceeds the corresponding limit, the old ones are discarded according to the sequence in which Redistribute IDs are added.


#### Cause (IS-IS Inter-Process Mutual Route Import)

On the network shown in [Figure 1](#EN-US_CONCEPT_0000001163338918__fig1948314117711), DeviceA, DeviceB, and DeviceC run IS-IS process 1, DeviceF and DeviceG run IS-IS process 2, and DeviceD and DeviceE run both processes. DeviceD and DeviceE are configured to import routes between IS-IS processes 1 and 2. The routes distributed by IS-IS process 1 are re-distributed back to IS-IS process 1 through IS-IS process 2. As the costs of the newly distributed routes are smaller, they are preferentially selected, resulting in routing loops.

**Figure 1** Typical network diagram of IS-IS inter-process mutual route import  
![](figure/en-us_image_0000001188021154.png)

Take DeviceA distributing route 10.0.0.1/32 as an example. A stable routing loop is formed through the following process:

**Phase 1**

On the network shown in [Figure 2](#EN-US_CONCEPT_0000001163338918__fig968472720326), IS-IS process 1 on DeviceA imports the static route 10.0.0.1, generates an LSP carrying the prefix of this route and floods the LSP in IS-IS process 1. After receiving the LSP, IS-IS process 1 on DeviceD and IS-IS process 1 on DeviceE each calculate a route to 10.0.0.1, with the outbound interface being interface1 on DeviceD and interface1 on DeviceE, respectively, and the cost being 110. At this point, the routes to 10.0.0.1 in IS-IS process 1 in the routing tables of DeviceD and DeviceE are active.

**Figure 2** Phase 1  
![](figure/en-us_image_0000001233342325.png)

**Phase 2**

In [Figure 3](#EN-US_CONCEPT_0000001163338918__fig42531247104216), DeviceD and DeviceE are configured to import routes from IS-IS process 1 to IS-IS process 2. Either no route-policy is configured for the import or the configured route-policy is improper. DeviceE is used as an example. In phase 1, the route to 10.0.0.1 in IS-IS process 1 in the routing table of DeviceE is active. In this case, IS-IS process 2 imports this route from IS-IS process 1, generates an LSP carrying the prefix of this route, and floods the LSP in IS-IS process 2. After receiving the LSP, IS-IS process 2 on DeviceD calculates a route to 10.0.0.1, with the cost being 10, which is smaller than that (110) of the route calculated by IS-IS process 1. As a result, the active route to 10.0.0.1 in the routing table of DeviceD is switched from the one calculated by IS-IS process 1 to the one calculated by IS-IS process 2, and the outbound interface is sub-interface 2.1.

**Figure 3** Phase 2  
![](figure/en-us_image_0000001233022273.png)

**Phase 3**

In [Figure 4](#EN-US_CONCEPT_0000001163338918__fig0407910517), after the route to 10.0.0.1 in IS-IS process 2 on DeviceD becomes active, IS-IS process 1 imports this route from IS-IS process 2, generates an LSP carrying the prefix of this route, and floods the LSP in IS-IS process 1. After receiving the LSP, IS-IS process 1 on DeviceE recalculates the route to 10.0.0.1, with the cost being 10, which is smaller than that (110) of the previously calculated route. As a result, the route to 10.0.0.1 in IS-IS process 1 in the routing table of DeviceE is switched to the route (with the smaller cost) advertised by DeviceD, and the outbound interface is interface 2.

**Figure 4** Phase 3  
![](figure/en-us_image_0000001187542714.png)

**Phase 4**

After the active route to 10.0.0.1 on DeviceE is updated, IS-IS process 2 still imports the route from IS-IS process 1 as the route remains active, and continues to advertise/update an LSP.

As a result, a stable routing loop is formed. Assuming that traffic is injected from DeviceF, [Figure 5](#EN-US_CONCEPT_0000001163338918__fig66391920185212) shows the traffic flow when the routing loop occurs.

**Figure 5** Traffic flow when a routing loop occurs  
![](figure/en-us_image_0000001187702686.png)

#### Implementation (IS-IS Inter-Process Mutual Route Import)

Routing loop detection for IS-IS inter-process mutual route import can resolve the routing loop in the preceding scenario.

When distributing a TLV (with the type value of 135 or 235) for an imported route, IS-IS also uses a sub-TLV (with the type value of 10) of the TLV (with the type value of 135 or 235) to distribute to other devices the Redistribute ID of the device that re-distributes the imported route. If the route is re-distributed by multiple devices, the Redistribute IDs of these devices are distributed through the sub-TLV (with the type value of 10) of the TLV (with the type value of 135 or 235). After receiving the sub-TLV, a route calculation device saves the Redistribute IDs of the re-distribution devices along with the route. When the route is imported by another process, the device checks whether the re-distribution information of the route contains the Redistribute ID of the local process. If the information contains the Redistribute ID of the local process, the device determines that a routing loop occurs and distributes a large route cost in the TLV (with the type value of 135 or 235) for the imported route. This ensures that other devices preferentially select other paths after learning the route, preventing routing loops.

**Figure 6** Typical networking of route import to IS-IS  
![](figure/en-us_image_0000001233300769.png)

The following uses the networking shown in [Figure 6](#EN-US_CONCEPT_0000001163338918__fig16542117181416) as an example to describe how a routing loop is detected and resolved.

1. DeviceD learns the route distributed by DeviceB through IS-IS process 1 and imports the route from IS-IS process 1 to IS-IS process 2. When distributing the imported route, IS-IS process 2 on DeviceD distributes the Redistribute ID of IS-IS process 2 through the sub-TLV (with the type value of 10) of the TLV (with the type value of 135 or 235). Similarly, IS-IS process 2 on DeviceE learns the route distributed by DeviceD and saves the Redistribute ID distributed by IS-IS process 2 on DeviceD to the routing table during route calculation.
2. When re-distributing the route imported from IS-IS process 2, IS-IS process 1 on DeviceE also distributes the Redistribute ID of IS-IS process 1 on DeviceE through the sub-TLV (with the type value of 10) of the TLV (with the type value of 135 or 235).
3. After learning the route from DeviceE, IS-IS process 1 on DeviceD saves the Redistribute ID distributed by IS-IS process 1 on DeviceE in the routing table during route calculation.
4. When importing the route from IS-IS process 1 to IS-IS process 2, DeviceD finds that the re-distribution information of the route contains its own Redistribute ID, considers that a routing loop is detected, and reports an alarm. IS-IS process 2 on DeviceD distributes a large cost when distributing the imported route so that other devices preferentially select other paths after learning the route. This prevents routing loops.![](public_sys-resources/note_3.0-en-us.png) 
   
   In the preceding typical networking:
   
   If routes are imported within a protocol on a device and the device detects a routing loop, it increases the cost of the route to be advertised. After the remote device learns this route with a large cost, it does not preferentially select this route as the optimal route in the IP routing table. In this manner, the routing loop is eliminated.
   
   In the case of inter-protocol route import, if a routing protocol with a higher priority detects a routing loop, although this protocol increases the cost of the corresponding route, the cost increase will not render the route inactive. As a result, the routing loop cannot be eliminated. If the routing protocol with a lower priority detects a routing loop and increases the cost of the corresponding route, the originally imported route is preferentially selected. In this case, the routing loop can be eliminated.

#### Cause (Mutual Route Import Between IS-IS and OSPF)

In [Figure 7](#EN-US_CONCEPT_0000001163338918__fig191726592490), DeviceA, DeviceB, and DeviceC run IS-IS process 1; DeviceD, DeviceE, DeviceF, and DeviceG run IS-IS process 2; in addition, DeviceB, DeviceC, DeviceD, and DeviceE run an OSPF process. DeviceB imports routes of IS-IS process 1 to OSPF, DeviceD imports OSPF routes to IS-IS process 2, and DeviceE imports routes of IS-IS process 2 to OSPF. Improper route import configurations may cause routing loops. For example, if DeviceD preferentially selects routes learned from DeviceE, a routing loop occurs between DeviceD and DeviceE. The following part describes how the routing loop is detected and resolved.

**Figure 7** Typical networking of route import from OSPF to IS-IS  
![](figure/en-us_image_0000001187861242.png)

#### Implementation (Mutual Route Import Between IS-IS and OSPF)

The following uses the networking shown in [Figure 7](#EN-US_CONCEPT_0000001163338918__fig191726592490) as an example to describe how a routing loop is detected and resolved.

1. DeviceA distributes its locally originated route 10.1.1.1/24 to DeviceB through IS-IS process 1. DeviceB imports the route from IS-IS process 1 to OSPF and adds the Redistribute ID of OSPF on DeviceB to the route when distributing the route through OSPF.
2. After learning the Redistribute list carried in the route advertised by DeviceB, OSPF on DeviceD saves the Redistribute ID of OSPF on DeviceB to the routing table during route calculation. After DeviceD imports this route from OSPF to IS-IS process 2, DeviceD redistributes the route through IS-IS process 2. In the redistributed route, the extended TLV contains the Redistribute ID of IS-IS process 2 on DeviceD and the Redistribute ID of OSPF on DeviceB. After learning the Redistribute list carried in the route advertised by DeviceD, IS-IS process 2 on DeviceE saves the Redistribute list in the routing table during route calculation.
3. After DeviceE imports this route from IS-IS process 2 to OSPF, DeviceE redistributes the route through OSPF. The redistributed route carries the Redistribute ID of OSPF on DeviceE and the Redistribute ID of IS-IS process 2 on DeviceD. The Redistribute ID of OSPF on DeviceB has been discarded from the route. DeviceD learns the Redistribute list carried in the route distributed by DeviceE and saves the Redistribute list in the routing table. When importing the OSPF route to IS-IS process 2, DeviceD finds that the Redistribute list of the route contains its own Redistribute ID, considers that a routing loop is detected, and reports an alarm. To eliminate the routing loop, IS-IS process 2 on DeviceD attaches a large cost to the route when redistributing it. However, because IS-IS has a higher preference than OSPF ASE, DeviceE still prefers the route learned from DeviceD through IS-IS process 2. As a result, the routing loop is not eliminated. The route received by DeviceE carries the Redistribute ID of OSPF on DeviceE and the Redistribute ID of IS-IS process 2 on DeviceD.
4. When importing the route from IS-IS process 2 to OSPF, DeviceE finds that the Redistribution information of the route contains its own Redistribute ID, considers that a routing loop is detected, and reports an alarm. To resolve the routing loop, OSPF on DeviceE distributes a large route cost when redistributing the route. In this case, DeviceD prefers the route distributed by DeviceB, which eliminates the routing loop.![](public_sys-resources/note_3.0-en-us.png) 
   
   In the preceding typical networking:
   
   If routes are imported within a protocol on a device and the device detects a routing loop, it increases the cost of the route to be advertised. After the remote device learns this route with a large cost, it does not preferentially select this route as the optimal route in the IP routing table. In this manner, the routing loop is eliminated.
   
   In the case of inter-protocol route import, if a routing protocol with a higher priority detects a routing loop, although this protocol increases the cost of the corresponding route, the cost increase will not render the route inactive. As a result, the routing loop cannot be eliminated. If the routing protocol with a lower priority detects a routing loop and increases the cost of the corresponding route, the originally imported route is preferentially selected. In this case, the routing loop can be eliminated.