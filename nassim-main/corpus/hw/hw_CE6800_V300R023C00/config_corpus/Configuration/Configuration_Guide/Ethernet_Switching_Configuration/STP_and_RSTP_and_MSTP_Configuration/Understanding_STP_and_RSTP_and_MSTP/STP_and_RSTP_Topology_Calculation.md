STP/RSTP Topology Calculation
=============================

After STP or RSTP is enabled on all devices on a network, all devices consider themselves as the root bridge. At this time, they only send and receive configuration BPDUs or RST BPDUs and do not forward user traffic. The devices select the root bridge, root port, and designated ports by exchanging configuration BPDUs or RST BPDUs.

#### STP/RSTP Algorithm Implementation

1. Initialization
   
   Since each device considers itself to be the root bridge, in BPDUs sent by each port: the root ID is the BID of the local bridge, the root path cost is the accumulative path cost from the port to the local bridge (0 in this situation), the sender BID is the BID of the local bridge, and the PID is the ID of the port which sends the BPDU.
2. Root bridge election
   
   During network initialization, every device considers itself the root bridge and so sets the root ID to its own BID. By exchanging configuration BPDUs, devices compare their root IDs and select the device with the smallest BID as the root bridge.
3. Root port and designated port election, as shown in [Table 1](#EN-US_CONCEPT_0000001291918944__tab_dc_fd_stp_000701).
   
   **Table 1** Selecting the root port and designated ports
   | Step | Process |
   | --- | --- |
   | 1 | A non-root bridge device selects the port that receives the optimal configuration BPDU as the root port. [Table 2](#EN-US_CONCEPT_0000001291918944__tab_dc_fd_stp_000702) describes the process of selecting the optimal configuration BPDU. |
   | 2 | The device generates a configuration BPDU for each port and modifies the following fields based on the configuration BPDU on the root port and path cost of the root port:  * Replaces the root ID with that in the configuration BPDU on the root port. * Replaces the root path cost with the sum of the root path cost in the configuration BPDU on the root port and the path cost of the root port. * Replaces the sender BID with the local BID. * Replaces the PID with the local port ID. |
   | 3 | Each port compares the calculated configuration BPDU with its own configuration BPDU:  * If the calculated configuration BPDU is superior, then the port is selected as the designated port and periodically sends the calculated configuration BPDU. * If the port's own configuration BPDU is superior, then the configuration BPDU on the port is not updated and the port is blocked. In this case, the port only receives BPDUs, and does not send them or forward data. |
   
   
   **Table 2** Selecting the optimal configuration BPDU
   | Step | Process |
   | --- | --- |
   | 1 | Each port compares the received configuration BPDU with its own configuration BPDU:  * If the received configuration BPDU is inferior, the port discards it and retains its own configuration BPDU. * If the received configuration BPDU is superior, the port replaces its own configuration BPDU with the received one. * If the received configuration BPDU is the same as its own, the port discards the received configuration BPDU. |
   | 2 | The device compares configuration BPDUs on all the ports and selects the optimal one. |

#### Example of STP Topology Calculation

After the root bridge, root ports, and designated ports are selected successfully, a tree topology is set up on the entire network. The following example illustrates how STP calculation is implemented.

**Figure 1** Networking and STP-calculated topology  
![](figure/en-us_image_0000001291919000.png)

In [Figure 1](#EN-US_CONCEPT_0000001291918944__fig390113581200), DeviceA, DeviceB, and DeviceC are deployed on the network, with bridge priorities 0, 1, and 2, respectively. The path costs between DeviceA and DeviceB, DeviceA and DeviceC, and DeviceB and DeviceC are 5, 10, and 4, respectively.

1. Initial state of each device, as shown in [Table 3](#EN-US_CONCEPT_0000001291918944__tab_dc_fd_stp_000703).
   
   **Table 3** Initial state of each device
   | Device | Port | Configuration BPDU  {root ID, root path cost, sender BID, sender PID} |
   | --- | --- | --- |
   | DeviceA | Port A1 | {0, 0, 0, Port A1} |
   | Port A2 | {0, 0, 0, Port A2} |
   | DeviceB | Port B1 | {1, 0, 1, Port B1} |
   | Port B2 | {1, 0, 1, Port B2} |
   | DeviceC | Port C1 | {2, 0, 2, Port C1} |
   | Port C2 | {2, 0, 2, Port C2} |
2. Configuration BPDU comparison and result, as shown in [Table 4](#EN-US_CONCEPT_0000001291918944__tab_dc_fd_stp_000704).
   
   **Table 4** STP topology calculation process and result
   | Device | Comparison | Configuration BPDU After Comparison |
   | --- | --- | --- |
   | DeviceA | * Port A1 receives the configuration BPDU {1, 0, 1, Port B1} from port B1 and finds it inferior to its own configuration BPDU {0, 0, 0, Port A1}, so port A1 discards the received configuration BPDU. * Port A2 receives the configuration BPDU {2, 0, 2, Port C1} from port C1 and finds it inferior to its own configuration BPDU {0, 0, 0, Port A2}, so port A2 discards the received configuration BPDU. * DeviceA finds that the root bridge and designated bridge specified in the configuration BPDUs on its ports are on itself. Therefore, DeviceA considers itself as the root bridge and periodically sends configuration BPDUs from each port without modifying the BPDUs. | * Port A1: {0, 0, 0, Port A1} * Port A2: {0, 0, 0, Port A2} |
   | DeviceB | * Port B1 receives the configuration BPDU {0, 0, 0, Port A1} from port A1 and finds it superior to its own {0, 0, 0, Port B1}, so port B1 updates its configuration BPDU. * Port B2 receives the configuration BPDU {2, 0, 2, Port C2} from port C2 and finds it inferior to its own {1, 0, 1, Port B2}, so port B2 discards the received configuration BPDU. | * Port B1: {0, 0, 0, Port A1} * Port B2: {1, 0, 1, Port B2} |
   | * DeviceB compares the configuration BPDU on each port and finds that port B1 has an optimal configuration BPDU. DeviceB selects port B1 as the root port and retains the configuration BPDU on port B1. * DeviceB calculates the configuration BPDU {0, 5, 1, Port B2} for port B2 based on the configuration BPDU and path cost of the root port, and compares the calculated configuration BPDU with the original configuration BPDU {1, 0, 1, Port B2} on port B2. The calculated configuration BPDU is superior to the original, so DeviceB selects port B2 as the designated port, replaces port B2's configuration BPDU with the calculated one, and periodically sends configuration BPDUs from port B2. | * Root port (port B1): {0, 0, 0, Port A1} * Designated port (port B2): {0, 5, 1, Port B2} |
   | DeviceC | * Port C1 receives the configuration BPDU {0, 0, 0, Port A2} from Port A2 and finds it superior to its own configuration BPDU {2, 0, 2, Port C1}, so Port C1 updates its configuration BPDU. * Port C2 receives the configuration BPDU {1, 0, 1, Port B2} from Port B2 and finds it superior to its own configuration BPDU {2, 0, 2, Port C2}, so Port C2 updates its configuration BPDU. | * Port C1: {0, 0, 0, Port A2} * Port C2: {1, 0, 1, Port B2} |
   | * DeviceC compares the configuration BPDU on each port and finds that the configuration BPDU on port C1 is optimal. DeviceC selects port C1 as the root port and retains the configuration BPDU on port C1. * DeviceC calculates the configuration BPDU {0, 10, 2, Port C2} for port C2 based on the configuration BPDU and path cost of the root port, and compares the calculated configuration BPDU with the original configuration BPDU {1, 0, 1, Port B2} on port C2. The calculated configuration BPDU is superior to the original one, so DeviceC selects port C2 as the designated port and replaces port C2's configuration BPDU with the calculated one. | * Root port (port C1): {0, 0, 0, Port A2} * Designated port (port C2): {0, 10, 2, Port C2} |
   | * Port C2 receives the configuration BPDU {0, 5, 1, Port B2} from port B2 and finds it superior to its own {0, 10, 2, Port C2}, so port C2 updates its configuration BPDU. * Port C1 receives the configuration BPDU {0, 0, 0, Port A2} from port A2 and finds it to be the same as its own, so port C1 discards the received configuration BPDU. | * Port C1: {0, 0, 0, Port A2} * Port C2: {0, 5, 1, Port B2} |
   | * The root path cost of port C1 is 10 (root path cost 0 in the received configuration BPDU plus the link path cost 10), and the root path cost of port C2 is 9 (root path cost 5 in the received configuration BPDU plus the link path cost 4). DeviceC finds that port C2 has a smaller root path cost and therefore considers the configuration BPDU of port C2 superior to that of port C1. DeviceC then selects port C2 as the root port and retains its configuration BPDU. * DeviceC calculates the configuration BPDU {0, 9, 2, Port C1} for port C1 based on the configuration BPDU and path cost of the root port, and finds the calculated configuration BPDU inferior to the original one {0, 0, 0, Port A2} on port C1. DeviceC blocks port C1 and does not update port C1's configuration BPDU. Port C1 no longer forwards data until spanning tree recalculation is triggered, for example, when the link between DeviceB and DeviceC is down. | * Blocked port (port C1): {0, 0, 0, Port A2} * Root port (port C2): {0, 5, 1, Port B2} |
   
   After the topology becomes stable, the root bridge still sends configuration BPDUs at specific intervals. If the received configuration BPDU is superior to its own, a non-root bridge replaces the configuration BPDU on the corresponding port with the received one. However, if the received configuration BPDU is either inferior or the same, then a non-root bridge discards the received configuration BPDU.