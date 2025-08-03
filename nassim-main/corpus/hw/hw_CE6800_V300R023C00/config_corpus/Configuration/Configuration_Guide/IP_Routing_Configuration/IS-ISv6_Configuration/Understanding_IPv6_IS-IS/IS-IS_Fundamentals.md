IS-IS Fundamentals
==================

IS-IS is a link-state routing protocol. Each routing device generates an LSP that contains link state information about all local IS-IS interfaces. Each routing device establishes IS-IS neighbor relationships with neighboring routing devices and updates its LSDB. The LSDBs of all routing devices on the IS-IS network are then synchronized. Based on the local LSDB, each routing device uses the SPF algorithm to calculate IS-IS routes. If a routing device determines that an IS-IS route to a destination is optimal, it adds the route to the local IP routing table to guide packet forwarding.

#### Establishment of IS-IS Neighbor Relationships

Two IS-IS routing devices must establish a neighbor relationship before exchanging packets to implement routing. The mode for establishing IS-IS neighbor relationships varies according to the network type.

**Establishment of a neighbor relationship on a broadcast network**

[Figure 1](#EN-US_CONCEPT_0000001130622642__en-us_concept_0000001130784120_fig_dc_feature_isis_000401) demonstrates the process of establishing an IS-IS neighbor relationship between Level-2 routing devices on a broadcast network. The process of establishing an IS-IS neighbor relationship between Level-1 routing devices on a broadcast network is similar to the process in this example.

**Figure 1** Process of establishing an IS-IS neighbor relationship on a broadcast network  
![](figure/en-us_image_0000001176663915.png)

1. DeviceA broadcasts a Level-2 LAN IIH with no neighbor specified.
2. After receiving the Level-2 LAN IIH, DeviceB sets its neighbor status with DeviceA to Initial. Then, DeviceB replies with a Level-2 LAN IIH with the neighbor set to DeviceA.
3. After receiving the Level-2 LAN IIH, DeviceA sets its neighbor status with DeviceB to up and replies with a Level-2 LAN IIH with the neighbor set to DeviceB.
4. After receiving the Level-2 LAN IIH, DeviceB sets its neighbor status with DeviceA to up, which concludes the establishment of an IS-IS neighbor relationship between the two routing devices.

As this is a broadcast network, a DIS must be elected. After the neighbor relationship is established, both devices wait for two IIH intervals and then exchange IIHs to elect a DIS. The IIHs contain the **Priority** field, and the device with the largest **Priority** value is elected as the DIS. If the two devices have the same priority, the device with the highest interface MAC address is elected as the DIS.

**Establishment of an IS-IS neighbor relationship on a P2P network**

An IS-IS neighbor relationship on a P2P network can be established in two-way or three-way handshake mode.

* Two-way handshake mode: When a routing device receives an IIH from the other end, it unilaterally declares its neighbor status with the other end as up. When both ends receive an IIH, an IS-IS neighbor relationship is established between the two ends.
* Three-way handshake mode: An IS-IS neighbor relationship is established after IIHs are sent three times between the two ends. This process is similar to that used for establishing an IS-IS neighbor relationship on a broadcast network.

The two-way handshake mode has distinct disadvantages. In a scenario where two or more links exist between two devices, an IS-IS neighbor relationship can still be established in two-way handshake mode even when one link is down unidirectionally and another link is up in the same direction. The parameters of the link that is up are used in SPF calculation. In this case, the other end, unaware of the local link fault, may still forward packets over the faulty link. The three-way handshake mode addresses this problem. In this mode, a routing device regards the remote end up and establishes a neighbor relationship with the remote end only after confirming that the remote end has received its IIH.

**Rules for establishing IS-IS neighbor relationships**

* Only adjacent routing devices of the same level can be neighbors.
* The Level-1 routing devices that will establish an IS-IS neighbor relationship with one another must have the same area ID.
* The IS-IS interfaces on both ends that will establish an IS-IS neighbor relationship with each other must have the same network type.
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  Ethernet interfaces can be emulated as P2P interfaces to establish a neighbor relationship on a P2P link.
* IP addresses of IS-IS interfaces on both ends of a link must be on the same network segment.
  
  As IS-IS runs on IP networks, each end needs to check the IP address of the other end before establishing an IS-IS neighbor relationship. If both primary and secondary IP addresses are configured for interfaces at both ends, the two ends can establish an IS-IS neighbor relationship as long as an IP address (either primary or secondary) on one end is on the same network segment as an IP address on the other end.
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  If IP addresses of IS-IS interfaces on both ends are on different network segments, a neighbor relationship can still be established between the two interfaces if they are configured to ignore the IP addresses in received IIHs. For P2P interfaces, you can directly configure them to ignore the IP addresses in received IIHs. For Ethernet interfaces, you must emulate them as P2P interfaces before configuring them to ignore the IP addresses in received IIHs.


#### Process of Exchanging IS-IS LSPs

**Causes of LSP generation**

All routing devices in an IS-IS routing domain generate LSPs. Any of the following events can trigger the generation of a new LSP:

* A neighbor goes up or down.
* An involved IS-IS interface goes up or down.
* An imported IP route changes.
* An inter-area IP route changes.
* An interface is assigned a new cost value.
* A new periodic update starts.

**Processing after a new LSP is received from a neighbor**

1. The local end installs the LSP to its LSDB and marks it for flooding.
2. The local end floods the LSP through all its interfaces except the one that received the LSP.
3. Neighbors flood the LSP to their neighbors.

**LSP flooding**

LSP flooding is a process in which a routing device advertises its LSP to its neighbors, which then send the same LSP to their neighbors, excluding the routing device from which the LSP was received. In this manner, the LSP is transmitted to all other routing devices of the same level as the routing device from which the LSP was received. LSP flooding allows all routing devices of the same level to have the same LSP information, helping implement LSDB synchronization.

Each LSP has a 4-byte sequence number. When a routing device is started, the sequence number of the first LSP that it sends is 1. When a new LSP is generated, its sequence number is that of the previous LSP plus 1. As such, newer LSPs have larger sequence numbers.

**Process of synchronizing LSDBs between the DIS on a broadcast network and a newly added routing device**

1. In the broadcast domain shown in [Figure 2](#EN-US_CONCEPT_0000001130622642__en-us_concept_0000001130784120_fig_dc_feature_isis_000402), after DeviceC is added to the domain, it sends IIHs to establish neighbor relationships with DeviceA and DeviceB. After the neighbor relationships are established, DeviceC sends its LSP to its neighbors once the LSP update timer has expired.
2. The DIS on the network adds the received LSP to its LSDB. When the CSNP timer expires, the DIS sends a CSNP for LSDB synchronization on the network.
3. After receiving the CSNP from the DIS, DeviceC checks its LSDB and responds with a PSNP to request the LSPs that it does not have.
4. Upon reception of the PSNP, the DIS sends the required LSPs to DeviceC for LSDB synchronization.

**Figure 2** LSDB synchronization in a broadcast domain  
![](figure/en-us_image_0000001176663919.png)
The LSDB of the DIS is updated as follows:

1. When the DIS receives an LSP, it searches its LSDB for related records. If the DIS finds no match, it adds the LSP to its LSDB and broadcasts the content of the updated LSDB.
2. If the sequence number of the received LSP is greater than that of the corresponding LSP in the LSDB, the DIS replaces the local LSP with the received LSP and broadcasts the content of the updated LSDB. If the sequence number of the received LSP is less than that of the corresponding LSP in the LSDB, the DIS responds with its LSP in the LSDB through the inbound interface of the received LSP.
3. If the sequence number of the received LSP is the same as that of the corresponding LSP in the LSDB, the DIS compares the Remaining Lifetime values of the two LSPs. If the Remaining Lifetime of the received LSP is less than that of the corresponding LSP in the LSDB, the DIS replaces the local LSP with the received LSP and broadcasts the content of the updated LSDB. If the Remaining Lifetime of the received LSP is greater than that of the corresponding LSP, the DIS responds with its LSP in the LSDB through the inbound interface of the received LSP.
4. If the sequence number and Remaining Lifetime of the received LSP are the same as those of the corresponding LSP in the LSDB, the DIS compares the Checksum values of the two LSPs. If the Checksum of the received LSP is greater than that of the corresponding LSP in the LSDB, the DIS replaces the local LSP with the received LSP and broadcasts the content of the updated LSDB. If the Checksum of the received LSP is less than that of the corresponding LSP in the LSDB, the DIS responds with its LSP in the LSDB through the inbound interface of the received LSP.
5. If the sequence number, Remaining Lifetime, and Checksum of the received LSP are the same as those of the corresponding LSP in the LSDB, the DIS does not forward the received LSP.

**LSDB update on a P2P link**

1. After establishing a P2P neighbor relationship, two devices send CSNPs to each other. If the LSDB of one end and the received CSNP are not synchronized, this end replies with a PSNP to request the LSPs that it does not have from the other end.
2. Assume that DeviceB requests an LSP from DeviceA on the network shown in [Figure 3](#EN-US_CONCEPT_0000001130622642__en-us_concept_0000001130784120_fig_dc_feature_isis_000403). DeviceA starts the LSP retransmission timer while sending the LSP requested by DeviceB, and then waits for a PSNP from DeviceB as an acknowledgment of the LSP.
3. If DeviceA has not received a PSNP from DeviceB when the LSP retransmission timer expires, DeviceA resends the LSP until it receives a PSNP from DeviceB.

![](public_sys-resources/note_3.0-en-us.png) 

On P2P links, PSNPs are used to request LSPs and acknowledge the reception of requested LSPs.


**Figure 3** LSDB update on a P2P link  
![](figure/en-us_image_0000001130624372.png)
The process of updating LSDBs on a P2P link is as follows:

1. If the sequence number of the received LSP is less than that of the local LSP, a routing device directly sends its LSP to the neighbor and waits for a PSNP as an acknowledgement from the neighbor. If the sequence number of the received LSP is greater than that of the local LSP, the routing device replaces the local LSP with the received one, replies with a PSNP to acknowledge the received LSP, and then sends the new LSP to all its neighbors except the one from which the new LSP was received.
2. If the sequence number of the received LSP is the same as that of the corresponding LSP in the LSDB, the routing device compares the Remaining Lifetime values of the two LSPs. If the Remaining Lifetime of the received LSP is less than that of the corresponding LSP in the LSDB, the routing device replaces the local LSP with the received LSP, replies with a PSNP to acknowledge the received LSP, and sends the new LSP to all its neighbors except the one from which the new LSP was received. If the Remaining Lifetime of the received LSP is greater than that of the corresponding LSP in the LSDB, the routing device directly sends its LSP to the neighbor and waits for a PSNP as an acknowledgement from the neighbor.
3. If the sequence number and Remaining Lifetime of the received LSP are the same as those of the corresponding LSP in the LSDB, the routing device compares the Checksum values of the two LSPs. If the Checksum of the received LSP is greater than that of the corresponding LSP in its LSDB, the routing device replaces the local LSP with the received LSP, replies with a PSNP to acknowledge the received LSP, and sends the new LSP to all its neighbors except the one from which the new LSP was received. If the Checksum of the received LSP is less than that of the corresponding LSP in its LSDB, the routing device directly sends its LSP to the neighbor and waits for a PSNP as an acknowledgement from the neighbor.
4. If the sequence number, Remaining Lifetime, and Checksum of the received LSP are the same as those of the corresponding LSP in the LSDB, the routing device does not forward the received LSP.


#### Route Calculation

After LSDB synchronization completes, IS-IS performs SPF calculation to obtain shortest path trees (SPTs), based on which IS-IS generates the routing table. In IS-IS, link costs are used to calculate SPTs. The default cost for an interface on a routing device is 10. The cost is configurable. The cost of a route is the sum of the costs of all outbound interfaces along the path of the route. As there may be multiple routes to a destination, that with the lowest cost is selected as the optimal route.

Each Level-1 routing device also calculates a path to the nearest Level-1-2 routing device for inter-area route selection. If Level-1-2 routing devices transmit Level-1 LSPs with the ATT bit set to 1 in the local area, each Level-1 routing device that receives the LSPs selects one Level-1-2 routing device to whom the path has the smallest cost for inter-area communication.