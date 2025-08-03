Overview of STP and RSTP
========================

STP and RSTP are used to block redundant links on a Layer 2 network and trim a network into a loop-free tree topology.

#### Introduction

On a complex network, loops are inevitable. With the requirement for network redundancy backup, network designers tend to deploy multiple physical links between two devices, one of which is the master and the others are the backup. Loops are likely or bound to occur in such a situation.

Loops will cause broadcast storms, thereby exhausting network resources and paralyzing the network. Loops also cause flapping of MAC address tables and therefore damage MAC address entries.

The devices running STP discover loops on the network by exchanging information with each other and trim the ring topology into a loop-free tree topology by blocking a certain interface. In this manner, replication and circular propagation of packets are avoided on the network. In addition, this prevents performance deterioration when devices continuously process repeated packets.

STP, however, converges the network topology slowly. In 2001, the IEEE published document 802.1w to introduce an evolution of the Spanning Tree Protocol: Rapid Spanning Tree Protocol (RSTP). RSTP is developed based on STP but outperforms STP.


#### One Root Bridge

A tree topology must have a root. Therefore, the root bridge is introduced by STP.

There is only one root bridge on the entire STP-enabled network. The root bridge is the logical center, but not necessarily the physical center, of the entire network. The root bridge changes dynamically with the network topology.

After the network converges, the root bridge generates and sends out configuration BPDUs at specific intervals. Other devices forward the BPDUs, ensuring that the network topology is stable.


#### Two Types of Measurements

The spanning tree is calculated based on two types of measurements: ID and path cost.

* ID
  
  Two types of IDs are available: Bridge IDs (BIDs) and Port IDs (PIDs).
  
  + BID
    
    As defined in IEEE 802.1D, a BID is composed of a 16-bit bridge priority and a bridge MAC address. The bridge priority occupies the leftmost 16 bits, and the MAC address occupies the rightmost 48 bits.
    
    On an STP network, the device with the smallest BID is selected to be the root bridge.
  + PID
    
    The PID is composed of a 4-bit port priority and a 12-bit port number. The port priority occupies the leftmost 4 bits and the port number occupies the remaining rightmost bits.
    
    The PID is used to select the designated port.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The port priority affects the role of a port in a specified spanning tree instance. For details, see [STP Topology Calculation](feature_0003995761.html).
* Path cost
  
  The path cost is a port variable and is used by STP to select a link. STP calculates the path cost to select a robust link and blocks redundant links to trim the network into a loop-free tree topology.
  
  On an STP-enabled network, the total cost of the path from a certain port to the root bridge is the sum of the costs of all the segment paths into which the path is separated by the ports on the transit bridges.
  
  [Table 1](#EN-US_CONCEPT_0172363527__en-us_concept_0172352502_tab_dc_vrp_mstp_feature_000501) shows the path costs defined in IEEE 802.1t. Different device manufacturers use different path cost standards.
  
  **Table 1** List of path costs
  | Port Speed | Port Mode | STP Path Cost (Recommended Value) | | |
  | --- | --- | --- | --- | --- |
  | 802.1D-1998 | 802.1T | legacy |
  | 0 | - | 65535 | 200000000 | 200,000 |
  | 10 Mbps | Half-Duplex | 100 | 2000000 | 2,000 |
  | Full-Duplex | 99 | 1999999 | 1,999 |
  | Aggregated Link 2 Ports | 95 | 1000000 | 1800 |
  | Aggregated Link 3 Ports | 95 | 666666 | 1600 |
  | Aggregated Link 4 Ports | 95 | 500000 | 1400 |
  | 100 Mbps | Half-Duplex | 19 | 200000 | 200 |
  | Full-Duplex | 18 | 199999 | 199 |
  | Aggregated Link 2 Ports | 15 | 100000 | 180 |
  | Aggregated Link 3 Ports | 15 | 66666 | 160 |
  | Aggregated Link 4 Ports | 15 | 50000 | 140 |
  | 1000 Mbps | Full-Duplex | 4 | 20000 | 20 |
  | Aggregated Link 2 Ports | 3 | 10000 | 18 |
  | Aggregated Link 3 Ports | 3 | 6666 | 16 |
  | Aggregated Link 4 Ports | 3 | 5000 | 14 |
  | 10 Gbps | Full-Duplex | 2 | 2000 | 2 |
  | Aggregated Link 2 Ports | 1 | 1000 | 1 |
  | Aggregated Link 3 Ports | 1 | 666 | 1 |
  | Aggregated Link 4 Ports | 1 | 500 | 1 |
  | 100 Gbps | Full-Duplex | 2 | 200 | 2 |
  | Aggregated Link 2 Ports | 1 | 200 | 1 |
  | Aggregated Link 3 Ports | 1 | 200 | 1 |
  | Aggregated Link 4 Ports | 1 | 200 | 1 |
  
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The rate of an aggregated link is the sum of the rates of all Up member links in the aggregated group.

#### Three Elements

There are generally three elements involved when a ring topology is to be trimmed into a tree topology: root bridge, root port, and designated port. [Figure 1](#EN-US_CONCEPT_0172363527__en-us_concept_0172352502_fig_dc_vrp_mstp_feature_000501) shows the three elements.

**Figure 1** STP network architecture  
![](figure/en-us_image_0000001972751594.png)

* Root bridge
  
  The root bridge is the bridge with the smallest BID. The smallest BID is determined through the exchange of configuration BPDUs.
* Root port
  
  The root port is a port that has the smallest path cost to the root bridge. To be specific, the root port is determined based on the path cost. Among all STP-enabled ports on a network bridge, the port with the smallest root path cost is the root port. There is only one root port on an STP-enabled device, and no root port on the root bridge.
* Designated port
  
  For a description of the designated bridge and designated port, see [Table 2](#EN-US_CONCEPT_0172363527__en-us_concept_0172352502_tab_dc_vrp_mstp_feature_000503).
  
  **Table 2** Description of the designated bridge and designated port
  | Object | Designated Bridge | Designated Port |
  | --- | --- | --- |
  | Device | Device that forwards configuration BPDUs to a directly connected device | Designated bridge port that forwards configuration BPDUs to the device |
  | LAN | Device that forwards configuration BPDUs to a network segment | Designated bridge port that forwards configuration BPDUs to a network segment. |
  
  On the network shown in [Figure 2](#EN-US_CONCEPT_0172363527__en-us_concept_0172352502_fig_dc_vrp_mstp_feature_000502), AP1 and AP2 reside on DeviceA; BP1 and BP2 reside on DeviceB; CP1 and CP2 reside on DeviceC.
  
  + DeviceA sends configuration BPDUs to DeviceB through AP1. Device A is the designated bridge of DeviceB, and AP1 on DeviceA is the designated port.
  + Two devices, DeviceB and DeviceC, are connected to the LAN. If DeviceB is responsible for forwarding configuration BPDUs to the LAN, DeviceB is the designated bridge of the LAN and BP2 on DeviceB is the designated port.**Figure 2** Designated bridge and designated port  
  ![](images/fig_feature_image_0003994814.png)

After the root bridge, root port, and designated port are selected successfully, the entire tree topology is set up. When the topology is stable, only the root port and the designated port forward traffic. All the other ports are in the Blocking state and receive only STP protocol packets, without forwarding user traffic.


#### Four Comparison Principles

STP has four comparison principles that form a BPDU priority vector {root BID, total path costs, sender BID, PID}.

[Table 3](#EN-US_CONCEPT_0172363527__en-us_concept_0172352502_tab_dc_vrp_mstp_feature_000504) shows the information that is carried in the configuration BPDUs.

**Table 3** Four important fields
| Field | Brief Description |
| --- | --- |
| Root BID | Each STP-enabled network has only one root bridge. |
| Root path cost | Cost of the path from the port sending configuration BPDUs to the root bridge. |
| Sender BID | BID of the device sending configuration BPDUs. |
| Sender PID | PID of the port sending configuration BPDUs. |

After a device on the STP-enabled network receives configuration BPDUs, it compares the fields shown in [Table 3](#EN-US_CONCEPT_0172363527__en-us_concept_0172352502_tab_dc_vrp_mstp_feature_000504) with that of the configuration BPDUs. The four comparison principles are as follows:

![](../../../../public_sys-resources/note_3.0-en-us.png) 

During the STP calculation, the smaller the value, the higher the priority.

* Smallest BID: used to select the root bridge. Devices running STP select the smallest BID as the root BID shown in [Table 3](#EN-US_CONCEPT_0172363527__en-us_concept_0172352502_tab_dc_vrp_mstp_feature_000504).
* Smallest root path cost: used to select the root port on a non-root bridge. On the root bridge, the path cost of each port is 0.
* Smallest sender BID: used to select the root port when a device running STP has two ports with the same path cost. The port with a smaller BID is selected as the root port in STP calculation. Assuming that the BID of DeviceB is smaller than that of DeviceC in [Figure 1](feature_0003992595.html#EN-US_CONCEPT_0172352502__fig_dc_vrp_mstp_feature_000501), if the path costs in the BPDUs received by port A and port B on DeviceD are the same, port B becomes the root port.
* Smallest PID: used to determine which port should be blocked when multiple ports have the same root path cost. The port with the greatest PID is blocked. [Figure 3](#EN-US_CONCEPT_0172363527__en-us_concept_0172352502_fig_dc_vrp_mstp_feature_000503) shows a scenario where PIDs need to be used. The BPDUs received on ports A and B of DeviceA contain the same root path cost and same sender BID, but port A has a smaller PID than port B. Therefore, port B is blocked to prevent loops.**Figure 3** Topology to which PID comparison is applied  
  ![](figure/en-us_image_0000002009323629.png)