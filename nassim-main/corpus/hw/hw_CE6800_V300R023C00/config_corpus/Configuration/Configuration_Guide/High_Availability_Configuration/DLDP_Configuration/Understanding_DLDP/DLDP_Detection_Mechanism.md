DLDP Detection Mechanism
========================

DLDP has two detection mechanisms: single-neighbor detection and multi-neighbor detection.

#### Single-Neighbor Detection

This section describes how DLDP detects unidirectional links when a single neighbor exists.

* **A link is unidirectional before DLDP is enabled**
  
  On the network shown in [Figure 1](#EN-US_CONCEPT_0000001415619110__fig692719811810), the optical fibers connecting two devices are cross-connected (the two lines connecting each interface represent the Tx and Rx optical fibers).
  
  **Figure 1** Cross-connected fibers  
  ![](figure/en-us_image_0000001465215857.png)
  
  After DLDP is enabled, the four interfaces in the Up state enter the Active state and send Advertisement packets with RSY tags to notify neighbors and request neighbor information. The following uses interface 1 as an example to describe the detection process:
  
  1. When receiving an Advertisement packet with RSY tags from interface 4, interface 1 determines that it has detected a neighbor. Interface 1 starts the Echo timer, sets up a neighbor entry, and starts the Entry Aging timer. Interface 1 then enters the Probe state and sends Probe packets to detect interface 4.
  2. Interface 4 cannot receive the Probe packets from interface 1, meaning that interface 1 will not receive Echo packets from interface 4. When the Echo timer on interface 1 times out, interface 1 enters the Disable state.
  
  The detection process on other interfaces is similar to that on interface 1. Finally, the four interfaces all enter the Disable state.

* **A link changes from bidirectional to unidirectional after DLDP is enabled**
  
  On the network shown in [Figure 2](#EN-US_CONCEPT_0000001415619110__fig1432414478223), optical fibers connect devices (the two lines connecting each interface represent the Tx and Rx optical fibers).
  
  **Figure 2** Optical fiber connections when a single neighbor exists  
  ![](figure/en-us_image_0000001415619118.png)
  
  When the Tx and Rx optical fibers are working properly, DeviceA and DeviceB establish a bidirectional relationship as follows:
  
  1. After DLDP is enabled, interface 1 in the Up state enters the Active state and sends Advertisement packets with RSY tags to notify the neighbor and request neighbor information.
  2. When receiving an Advertisement packet with RSY tags from interface 1, interface 2 determines that it has detected a neighbor. Interface 2 then starts the Echo timer, sets up a neighbor entry, and starts the Entry Aging timer. Interface 2 enters the Probe state and sends a Probe packet.
  3. Upon receiving the Probe packet, interface 1 sets up a neighbor entry, enters the Probe state, and returns an Echo packet to interface 2.
  4. When interface 2 receives the Echo packet, it finds that the neighbor entry exists and the neighbor information carried by the Echo packet is the same as that saved on the local device. Therefore, interface 2 marks this neighbor as a bidirectionally connected neighbor. Interface 2 transitions from the Probe state to the Advertisement state, and periodically sends Advertisement packets. Interface 2 in the Advertisement state resets the Entry Aging timer for a known neighbor each time a packet is received from the neighbor.
  5. After DLDP is enabled, the procedure for sending packets from interface 2 and setting up a neighbor on interface 1 is similar to steps 1 to 4.
  6. At last, interface 1 and interface 2 regard each other as bidirectionally connected neighbors and enter the Advertisement state.
  
  On the network shown in [Figure 3](#EN-US_CONCEPT_0000001415619110__fig18856396312), the Rx optical fiber of interface 2 has failed and cannot receive an optical signal. When this occurs, interface 2 enters the Inactive state and stops sending and receiving packets. However, the Tx optical fiber of interface 2 remains normal, meaning that interface 1 can receive signals and stay in the up state. Interface 1 cannot receive DLDPDUs from interface 2 before the Entry Aging timer times out. The procedure for detecting unidirectional links varies depending on the configured DLDP working mode.
  
  **Figure 3** A disconnected optical fiber when a single neighbor exists  
  ![](figure/en-us_image_0000001465455589.png)
  + Normal mode: After the Entry Aging timer times out, interface 1 deletes the neighbor entry, enters the Active state, and sends an Advertisement packet with RSY tags. Interface 1 enters the Advertisement state after being in the Active state for 5 seconds. It then remains in the Advertisement state and has no neighbor. Interface 2 remains in the Inactive state. In this case, DLDP cannot detect unidirectional links.
  + Enhanced mode: After the Entry Aging timer times out, interface 1 starts the Enhanced timer and Echo timer and sends a Probe packet to the neighbor. The Tx optical fiber of interface 1 is disconnected, preventing interface 1 from receiving the Echo packet from interface 2. When the Echo timer times out, interface 1 enters the Disable state and sends a Disable packet to the neighbor. In addition, interface 1 deletes the neighbor entry and starts the RecoverProbe timer to check whether the Tx optical fiber is restored. During the preceding process, interface 2 remains in the Inactive state.![](public_sys-resources/note_3.0-en-us.png) 
  + In enhanced mode, interface 2 is physically down, but interface 1 cannot detect the change. DLDP supports the fast Link Down notification mechanism that can rapidly detect a fault on the link connecting interface 1 and interface 2 without waiting for the Entry Aging timer to time out. Upon detecting that interface 2 is down, the physical layer sends a Link Down packet to interface 1. When receiving the Link Down packet, interface 1 enters the Disable state.
  + The fast Link Down notification mechanism applies only to the enhanced mode.

#### Multi-Neighbor Detection

DLDP can be configured on devices connected by hubs to detect unidirectional links. Each interface detects multiple neighbors.

On the network shown in [Figure 4](#EN-US_CONCEPT_0000001415619110__fig10200621952), a hub connects DeviceA to DeviceB, DeviceC, and DeviceD through copper twisted pairs or optical fibers. All devices support DLDP. To detect unidirectional links on this network, DLDP needs to be enabled on all interfaces connected to the hub.

**Figure 4** Network diagram of multiple neighbors  
![](figure/en-us_image_0000001415015966.png)

On a network with multiple neighbors, an interface immediately enters the Disable state when receiving a Disable packet from a neighbor or detecting that a neighbor is unidirectional. When DeviceA, DeviceB, and DeviceC detect a unidirectional link fault on DeviceD, they switch their involved interfaces to the Disable state. This prevents traffic forwarding errors when the topology changes in the multi-neighbor scenario. If the Rx optical fiber between DeviceB and the hub is disconnected when DeviceA is forwarding traffic to DeviceB, DeviceA shuts down its interface connected to the hub and stops sending packets to DeviceB, DeviceC, and DeviceD. If there is a backup link between DeviceA and DeviceB, STP immediately starts the backup link when DeviceA shuts down the interface.

If the devices on the preceding network are connected by a device that has DLDP disabled but supports DLDPDU forwarding, DLDP still detects unidirectional links as if multiple neighbors exist.