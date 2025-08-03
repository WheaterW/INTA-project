Understanding Data Plane Fast Recovery
======================================

Understanding Data Plane Fast Recovery

#### Overall Function Analysis

If any link between nodes on the network fails, traffic will be interrupted. To implement fast path switching, you need to perform local and remote fast fault convergence. As a sub-millisecond-level fault recovery technology, DPFR provides local or remote fast fault convergence based on the data plane. [Figure 1](#EN-US_CONCEPT_0000001539735320__fig205052035133516) shows the overall functions of DPFR.

* Fast fault detection: If an optical module on a port is faulty or a transmission optical cable is incorrectly connected, the data plane can quickly detect the port fault, trigger the troubleshooting mechanism, and generate the corresponding fault table.
* Local fast fault convergence: If the local device where a faulty port resides has a redundant path available, the data plane performs fast path switching for data packets before fault convergence on the control plane.
* Remote fault advertisement: If the local device where a faulty port resides has no redundant path available, the data plane generates an advertisement packet carrying the fault status based on the data packet information and sends the advertisement packet to the adjacent upstream device. The upstream device then learns the advertisement packet and generates a fault table for subsequent path switching.
* Remote fault relay: When a device performs remote advertisement and the upstream device cannot provide a redundant path, it performs advertisement packet relay, constructs a relay fault advertisement packet, and sends the packet to the adjacent upstream device.
* Remote fast fault convergence: When a device performs remote advertisement and the upstream device can provide redundant paths, the data packets mapping to entries in the fault table are quickly switched to normal links on the upstream device.
* Entry aging: Entries in the fault table are aged in a specified period to ensure that the behavior on the data plane is consistent with the route convergence result on the control plane.

**Figure 1** Overall function analysis  
![](figure/en-us_image_0000001647392578.png)

#### Local Fast Fault Convergence

In [Figure 2](#EN-US_CONCEPT_0000001539735320__fig14820102821813), data packets are forwarded from Spine1 to Server1. The normal packet forwarding path is Spine1 -> Leaf1 -> Server1. If the link between Spine1 and Leaf1 is faulty and Spine1 has a redundant path available to Server1, packets are quickly switched on Spine1 to implement local fast fault convergence. The process is as follows:

1. **Fast fault detection**:
   * If an optical module on a port is faulty or a transmission optical cable is incorrectly connected, Spine1 detects a fault on interface1.
   * Spine1 samples traffic whose outbound interface is interface1, determines information about the faulty flow, and generates the corresponding fault table, including the destination address of the faulty flow, faulty interface (interface1), and entry creation time.
2. **Local fast fault convergence**:
   * After receiving a new data packet, Spine1 matches it with the fault table based on the destination address and selects an available redundant path for the packet.
   * The data packet is forwarded along the path Spine1 -> Leaf2 -> Server1. Local fast fault convergence is performed on Spine1.
3. **Entry aging**: Entries in the fault table on Spine1 are aged in a specified period based on the entry creation time.

**Figure 2** Local fast fault convergence  
![](figure/en-us_image_0000001723918044.png)

#### Remote Fast Fault Convergence

In [Figure 3](#EN-US_CONCEPT_0000001539735320__fig148525497282), data packets are forwarded from Core1 to Server1. The normal packet forwarding path is Core1 -> Spine1 -> Leaf1 -> Server1. If the link between Leaf1 and Server1 is faulty but Leaf1 has no redundant path available for Server1, Leaf1 notifies its upstream device Spine1 of the fault. After receiving data packets, Spine1 still cannot provide redundant paths. In this case, Spine1 performs advertisement packet relay, constructs relay fault advertisement packets, and sends the packets to the adjacent upstream device Core1. Upon recipient, Core1 performs fast path switching to implement remote fast fault convergence. The process is as follows:

1. **Fast fault detection**:
   * If an optical module on a port is faulty or a transmission optical cable is incorrectly connected, Leaf1 detects a fault on interface1.
   * Leaf1 samples traffic whose outbound interface is interface1 (faulty interface), determines information about the faulty flow, and generates the corresponding fault table, including the destination address of the faulty flow, faulty interface, and entry creation time.
2. **Remote fault advertisement and receiving**:
   * After receiving a new data packet, Leaf1 matches it with the fault table based on the destination address, but has no redundant path available.
   * Leaf1 performs remote fault advertisement, generates an advertisement packet based on the sampled packet, and sends the advertisement packet to the adjacent upstream device Spine1.
   * Spine1 learns the fault advertisement packet and generates a fault table, including the destination address of the faulty flow, interface1 that receives the fault advertisement packet, and entry creation time.
3. **Remote fault relay and receiving**:
   * After receiving a new data packet, Spine1 matches it with the fault table based on the destination address, but has no redundant path available.
   * Spine1 performs advertisement packet relay, samples the data packet that matches the fault table on the interface where the advertisement packet is received, and generates the corresponding advertisement packet. It then sends the packet to the adjacent upstream device Core1.
   * Core1 learns the relay fault advertisement packet and generates a fault table, including the destination address of the faulty flow, interface1 that receives the fault advertisement packet, and entry creation time.
4. **Remote fast fault convergence**:
   * After receiving a new data packet, Core1 matches it with the fault table based on the destination address and selects an available redundant path for the packet.
   * The data packet is forwarded along the path Core1 -> Spine2 -> Leaf2 -> Server1, and remote fast fault convergence is performed on Core1.
5. **Entry aging**: Entries in the fault tables on Leaf1, Spine1, and Core1 are aged in a specified period based on the entry creation time.

**Figure 3** Remote fast fault convergence  
![](figure/en-us_image_0000001724109118.png)