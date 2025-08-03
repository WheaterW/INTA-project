OSPF Route Calculation
======================

OSPF route calculation involves the following processes:

1. Adjacency establishment. Local and remote devices establish an adjacency through the following process:
   
   1. Exchange Hello packets using OSPF interfaces to establish a neighbor relationship.
   2. Negotiate a master/slave relationship and exchange DD packets.
   3. Exchange LSAs to synchronize LSDBs.
2. Route calculation. OSPF uses the shortest path first (SPF) algorithm to calculate routes, implementing fast route convergence.

#### OSPF Neighbor States

To exchange routing information on an OSPF network, neighbor devices must establish adjacencies. The differences between neighbor relationships and adjacencies are described as follows:

* Neighbor relationship: After the local device starts, it uses an OSPF interface to send a Hello packet to the remote device. After the remote device receives the packet, it checks whether the parameters carried in the packet are consistent with its own. If they are consistent, the remote device establishes a neighbor relationship with the local device.
* Adjacency: After the local and remote devices establish a neighbor relationship, they exchange DD packets and LSAs to establish an adjacency.

OSPF has eight neighbor states: Down, Attempt, Init, 2-way, Exstart, Exchange, Loading, and Full, as shown in [Figure 1](#EN-US_CONCEPT_0000001130623482__fig_dc_vrp_ospf_feature_003101). Down, 2-way, and Full are stable states. Attempt, Init, Exstart, Exchange, and Loading are unstable states, each of which lasts only several minutes.

**Figure 1** OSPF neighbor states  
![](figure/en-us_image_0000001176663113.png)

**Table 1** OSPF neighbor states and their meanings
| OSPF Neighbor State | Description |
| --- | --- |
| Down | This is the initial state of a neighbor conversation, and indicates that a device has not received any Hello packets from its neighbors within a dead interval. |
| Attempt | In the Attempt state, a device periodically sends Hello packets to manually configured neighbors.  NOTE:  The Attempt state applies only to non-broadcast multiple access (NBMA) interfaces. |
| Init | This state indicates that a device has received Hello packets from its neighbors but the neighbors did not receive Hello packets from the device. |
| 2-way | This state indicates that the two ends have received Hello packets from each other and established a neighbor relationship.  If no adjacency needs to be established, the neighbors remain in the 2-way state. If adjacencies need to be established, the neighbors enter the Exstart state. |
| Exstart | In the Exstart state, devices establish a master/slave relationship to ensure that DD packets are sequentially exchanged. |
| Exchange | In the Exchange state, devices exchange DD packets. A device uses a DD packet to describe its own LSDB and sends the packet to its neighbors. |
| Loading | In the Loading state, a device sends LSR packets to its neighbors in order to request their LSAs for LSDB synchronization. |
| Full | In the Full state, the local LSDB is synchronized with the other LSDBs, and adjacencies are established between the local device and neighbors. |


![](../public_sys-resources/note_3.0-en-us.png) 

The neighbor state of the local device may be different from that of a remote device. For example, the neighbor state of the local device is Full, but the neighbor state of the remote device is Loading.



#### DR and BDR

On a broadcast or NBMA network, routing information is transmitted between any two devices. As shown in [Figure 2](#EN-US_CONCEPT_0000001130623482__fig_dc_vrp_ospf_feature_003006), *n* devices are deployed on the network, and *n* x (*n* â 1)/2 adjacencies are established in normal cases. Any route change on a device is transmitted to the other devices, which wastes bandwidth resources. OSPF resolves this problem by defining a DR and a BDR. After a DR is elected, all other devices send routing information only to the DR, which then broadcasts LSAs. Devices other than the DR and BDR are called DR others. The DR others establish adjacencies only with the DR and BDR and not with each other. The DR and BDR mechanism reduces the number of adjacencies on a broadcast or NBMA network.

**Figure 2** Network topologies before and after a DR election  
![](figure/en-us_image_0000001176663111.png)

If the original DR fails, devices must reelect a DR and all devices (except the new DR) must synchronize routing information with the new DR. This is a lengthy process, during which route calculations may be incorrect. A BDR, which is a backup for a DR, is used to shorten the process. A BDR is elected together with a DR, establishes adjacencies with all devices on the network segment where the BDR resides, and exchanges routing information with them. If the DR fails, the BDR immediately becomes a new DR. Although it still takes a long time for the devices to reelect a new BDR, this process does not affect route calculation.

The DR and BDR on a network segment are automatically elected, not manually assigned, and the DR priority of a device interface determines its qualification for DR and BDR elections. The device interfaces with DR priorities greater than 0 are eligible. Hello packets are used in the election, with each device adding information about the elected DR to a Hello packet and sending it to the other devices on the same network segment. When two device interfaces on the same network segment declare that they are DRs, the device interface with a higher DR priority is elected as the DR. If the two device interfaces have the same DR priority, the device interface with a larger router ID is elected as the DR. If the DR priority of a device interface is 0, the device cannot be elected as a DR or BDR.


#### Adjacency Establishment

Adjacencies can be established in either of the following situations:

* Two devices have established a neighbor relationship and communicate for the first time.
* The DR or BDR on a network segment changes.

The OSPF adjacency establishment process varies according to the network type (broadcast, NBMA, P2P, or P2MP).

**OSPF adjacency establishment on a broadcast network**

[Figure 3](#EN-US_CONCEPT_0000001130623482__fig_dc_vrp_ospf_feature_003102) shows the adjacency establishment process on a broadcast network.

On a broadcast network, the DR and BDR establish adjacencies with each device on the same network segment, but DR others establish only neighbor relationships with each other.

**Figure 3** OSPF adjacency establishment on a broadcast network  
![](figure/en-us_image_0000001205491889.png)

In [Figure 3](#EN-US_CONCEPT_0000001130623482__fig_dc_vrp_ospf_feature_003102), the process of OSPF adjacency establishment on a broadcast network is as follows:

1. Neighbor relationship establishment
   
   1. DeviceA uses the multicast address 224.0.0.5 to send a Hello packet through the OSPF interface connected to a broadcast network. In this case, DeviceA does not know which router is the DR or which device is a neighbor. Therefore, the DR field is 0.0.0.0, and the Neighbors Seen field is 0.
   2. After DeviceB receives the packet, it returns a Hello packet to DeviceA. The returned packet carries a DR field of 2.2.2.2 (ID of DeviceB) and a Neighbors Seen field of 1.1.1.1 (DeviceA's router ID). DeviceA has been discovered but its router ID is smaller than that of DeviceB. As a result, DeviceB regards itself as a DR and its state then changes to Init.
   3. After DeviceA receives the Hello packet from DeviceB, DeviceA sets the neighbor state to 2-way. The two ends will start to exchange information about their LSDBs.![](../public_sys-resources/note_3.0-en-us.png) 
   
   The following procedures are not performed for DR others on a broadcast network.
2. Master/Slave negotiation and DD packet exchange
   
   1. DeviceA sends a DD packet to DeviceB, declaring itself a master by setting the MS field in the packet to 1 and the Seq field to *x*, indicating the sequence number. The I field is set to 1, indicating that the packet is the first DD packet, which is used to negotiate a master/slave relationship and does not carry LSA summaries. The M field is set to 1, indicating that the packet is not the last one.
      
      To improve transmission efficiency, DeviceA and DeviceB determine which LSAs in each other's LSDB need to be updated. If one party determines that an LSA of the other party is already in its own LSDB, it does not send an LSR packet for updating the LSA to the other party. Instead, DeviceA and DeviceB first send DD packets, which carry summaries of LSAs in their own LSDBs, with each summary uniquely identifying an LSA. To ensure packet transmission reliability, a master/slave relationship must be determined during DD packet exchange. One party serving as a master uses the Seq field to define a sequence number. The master increases the sequence number by one each time it sends a DD packet. When the other party serving as a slave sends a DD packet, it uses the sequence number carried in the last DD packet received from the master.
   2. After DeviceB receives the DD packet from DeviceA, DeviceB sets the state of the neighbor relationship with DeviceA to Exstart and replies with a DD packet, which does not contain LSA summaries either. Because DeviceB's router ID is larger, DeviceB declares itself a master and sets the Seq field to *y*.
   3. After DeviceA receives the packet, it agrees that DeviceB is the master and sets the state of the neighbor relationship with DeviceB to Exchange. DeviceA sends a new DD packet carrying the sequence number (Seq=y) set by DeviceB to transmit LSA summaries. In the packet, the MS field set by DeviceA is 0, indicating that DeviceA is the slave.
   4. After DeviceB receives the packet, it sets the state of the neighbor relationship with DeviceA to Exchange and responds with a new DD packet containing its own LSA summaries. The value of the Seq field carried in the new DD packet is *y* plus 1.
   
   The preceding process continues. DeviceA uses the sequence number of the previous packet sent by DeviceB to acknowledge the reception of the packet from DeviceB. DeviceB uses the sequence number plus one to confirm that it has received DD packets from DeviceA. When DeviceB sends the last DD packet, it sets the M field of the packet to 0.
3. LSDB synchronization (through LSA requests, transmission, and response)
   
   1. After DeviceA receives the last DD packet, it finds that many LSAs in DeviceB's LSDB do not exist in its LSDB. Therefore, DeviceA sets the state of the neighbor relationship with DeviceB to Loading. DeviceB also receives the last DD packet from DeviceA. Because DeviceB already has all the LSAs of DeviceA and needs no requests, DeviceB directly changes the state of the neighbor relationship with DeviceA to Full.
   2. DeviceA sends an LSR packet for updating LSAs to DeviceB, which then returns an LSU packet to DeviceA. After DeviceA receives the packet, it sends an LSAck packet for acknowledgment.
   
   The preceding procedures continue until the LSAs of DeviceA are the same as those of DeviceB. Then DeviceA sets the state of the neighbor relationship with DeviceB to Full. An adjacency is established after DeviceA and DeviceB exchange DD packets and update all LSAs.

**OSPF adjacency establishment on an NBMA network**

The adjacency establishment process on an NBMA network is different from that on a broadcast network only before DD packets are exchanged, as marked in blue in [Figure 4](#EN-US_CONCEPT_0000001130623482__fig_dc_vrp_ospf_feature_003103).

On an NBMA network, all devices establish adjacencies only with the DR and BDR.

**Figure 4** OSPF adjacency establishment process on an NBMA network  
![](figure/en-us_image_0000001130783352.png)

[Figure 4](#EN-US_CONCEPT_0000001130623482__fig_dc_vrp_ospf_feature_003103) shows the process of OSPF adjacency establishment on an NBMA network.

1. Neighbor relationship establishment
   
   1. After DeviceB sends a Hello packet to a down interface of DeviceA, DeviceB's state changes to Attempt. The packet carries a DR field of 2.2.2.2 (router ID of DeviceB) and a Neighbors Seen field of 0. A neighbor device has not been discovered, and DeviceB regards itself as a DR.
   2. After DeviceA receives the packet, DeviceA's state changes to Init, and DeviceA returns a Hello packet. The returned packet carries a DR and Neighbors Seen fields of 2.2.2.2. DeviceB has been discovered but its router ID is greater than that of DeviceA, and therefore DeviceA agrees that DeviceB is a DR.![](../public_sys-resources/note_3.0-en-us.png) 
   
   The following procedures are not performed for DR others on an NBMA network.
2. The procedures for negotiating a master/slave relationship and for exchanging DD packets on an NBMA network are the same as those on a broadcast network.
3. The procedure for synchronizing LSDBs (through LSA requests, transmission, and response) on this type of network is the same as that on a broadcast network.

**OSPF adjacency establishment on a point-to-point (P2P)/Point-to-multipoint (P2MP) network**

The adjacency establishment process on a P2P/P2MP network is similar to that on a broadcast network. On a P2P/P2MP network, however, no DR or BDR needs to be elected and DD packets are transmitted in multicast mode.


#### Route Calculation

OSPF uses the SPF algorithm to calculate routes, implementing fast route convergence.

OSPF uses LSAs to describe the network topology. A router LSA describes the attributes of a link between devices. A device transforms its LSDB into a weighted, directed graph, which reflects the topology of the entire AS. All devices have the same directed graph, as shown in [Figure 5](#EN-US_CONCEPT_0000001130623482__fig_dc_vrp_ospf_feature_003104).

**Figure 5** Weighted, directed graph generated based on the LSDB  
![](figure/en-us_image_0000001176743011.png)

Based on the graph, each device uses the SPF algorithm to calculate an SPT with itself as the root. The SPT shows routes to nodes in the AS. [Figure 6](#EN-US_CONCEPT_0000001130623482__fig_dc_vrp_ospf_feature_003105) shows SPTs with different roots.

**Figure 6** SPTs  
![](figure/en-us_image_0000001130623564.png "Click to enlarge")

If a device's LSDB changes, the device recalculates the shortest path. However, frequent SPF calculations consume a large number of resources and this can affect the overall efficiency of the device. Changing the interval between SPF calculations can prevent the resource consumption caused by frequent LSDB changes. The default interval between SPF calculations is 5 seconds.

The route calculation process is as follows:

1. A device calculates intra-area routes.
   
   The device uses the SPF algorithm to calculate shortest paths to the other devices in the same area. Router-LSAs and network-LSAs accurately describe the network topology in an area. Based on the network topology described by a Router LSA, the device calculates paths to the other devices in the area.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   If multiple equal-cost routes are produced during route calculation, the SPF algorithm retains all these routes in the LSDB.
2. The device calculates inter-area routes.
   
   For devices in the same area, the network segment of the routes in an adjacent area is directly connected to the ABR. As the shortest path to the ABR has already been calculated in the previous step, the devices can directly check a network-summary-LSA to obtain the shortest path to the network segment. The ASBR can also be considered connected to the ABR. As a result, the shortest path to the ASBR can also be calculated in this phase.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   * If the device performing SPF calculation is an ABR, the device only needs to check Network Summary LSAs in the backbone area.
   * If there are multiple paths to an ASBR, check whether the rules for selecting a path to the ASBR among intra-area and inter-area paths on different types of devices are the same. If the rules are different, routing loops may occur.
     
     The RFC 1583 compatibility mode and RFC 1583 non-compatibility mode may affect path selection rules. Even in the same mode, the path selection rules on devices from different vendors may be slightly different. In this case, the rules used in RFC 1583 compatibility mode or RFC 1583 non-compatibility mode for selecting a path to an ASBR can be adjusted, preventing loops to some extent.
3. The device calculates AS external routes.
   
   AS external routes can be considered to be directly connected to the ASBR. As the shortest path to the ASBR has already been calculated in the previous phase, the device can check each AS external LSA to obtain the shortest paths to other ASs.

#### PRC

Partial route calculation (PRC) only calculates routes that have been altered due to network topology changes.

When a node changes on the network, the SPF algorithm is used to recalculate all routes on the network. This calculation takes a long time and consumes a large number of CPU resources, which affects the convergence speed. Incremental SPF (I-SPF) improves the algorithm. While the algorithm still calculates routes using all nodes on the network the first time it is run, only nodes that have changed are used in subsequent calculations. The SPT generated using I-SPF is the same as that generated using the SPF algorithm. This significantly decreases CPU usage and speeds up network convergence.

Similar to I-SPF, PRC calculates only routes that have changed. PRC, however, does not calculate the shortest path. Instead, it updates routes based on the SPT calculated by I-SPF. In route calculation, a leaf represents a route, and a node represents a device. Either an SPT change or a leaf change causes a routing information change. The SPT change is irrelevant to the leaf change. PRC processes routing information as follows:

* If the SPT changes, PRC processes the routing information of all leaves on a changed node.
* If the SPT remains unchanged, PRC does not process the routing information on any node.
* If a leaf changes, PRC processes the routing information for that leaf only.
* If a leaf remains unchanged, PRC does not process the routing information for any leaf.

For example, if OSPF is newly enabled on an interface of a node, the SPT calculated on the entire network remains unchanged. In this case, PRC updates only the routes of this interface, consuming less CPU resources.

PRC working with I-SPF further improves the network convergence performance. As a result of these improvements, PRC and I-SPF have replaced the SPF algorithm.