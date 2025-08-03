M-LAG Setup Process
===================

During M-LAG setup, an M-LAG can work in dual-active or active/standby mode depending on the generation mode of M-LAG master and backup member interfaces.

#### Dual-Active Mode

In [Figure 1](#EN-US_CONCEPT_0000001512689650__fig356791610172), Eth-Trunks are established between DeviceA and DeviceC (a user-side device) and between DeviceB and DeviceC. DeviceA and DeviceB set up an M-LAG. In dual-active mode, DeviceA and DeviceB use the dynamic fabric service (DFS) group protocol for pairing between one another over the peer-link, negotiating the M-LAG master and backup device roles and member interfaces, and synchronizing required entries. The peer-link between DeviceA and DeviceB is an Eth-Trunk used to exchange negotiation packets and forward part of traffic. The interfaces at both ends of the peer-link are known as peer-link interfaces, which are added to all VLANs and bridge domains (BDs) by default. M-LAG member interfaces are Eth-Trunk interfaces on DeviceA and DeviceB that connect to DeviceC.

In dual-active mode, both Eth-Trunks can load balance traffic sent from the user-side device and provide backup for each other.

**Figure 1** Basic topology of an M-LAG in dual-active mode  
![](../images/en-us_image_0000001563888849.png)
The M-LAG setup process includes the following stages:

1. DFS group pairing
   
   A DFS group is used to pair DeviceA and DeviceB. After two M-LAG devices are configured, they send DFS group Hello packets to each other through the peer-link (an Eth-Trunk). Upon receiving Hello packets from the peer device, the local device checks whether the DFS group ID in the packets is the same as that of the local device. If the DFS group IDs are the same, DFS group pairing of the two devices is successful.
2. DFS master/backup device negotiation
   
   After DeviceA and DeviceB are paired successfully, they send DFS group device information packets to each other through the peer-link to determine the DFS master and backup devices based on the DFS group priorities and system MAC addresses carried in the packets. The DFS master and backup devices are also known as the M-LAG master device and M-LAG backup device, respectively.
   
   For example, after receiving packets from DeviceA, DeviceB checks and records DeviceA's information, and compares their DFS group priorities. If DeviceA has a higher DFS group priority than DeviceB, DeviceA acts as the M-LAG master device and DeviceB as the M-LAG backup device. If DeviceA and DeviceB have the same DFS group priority, the device with a smaller system MAC address acts as the M-LAG master device.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   Under normal circumstances, both the M-LAG master and backup devices forward service traffic and their forwarding behaviors are the same. These devices will only use different forwarding behaviors when a fault occurs in the M-LAG.
3. M-LAG master and backup member interface negotiation
   
   Once the M-LAG master and backup devices are determined, both devices send M-LAG device information packets carrying the configuration information of M-LAG member interfaces to one another through the peer-link. After member interface information is synchronized between the two devices, M-LAG master and backup member interfaces are determined.
   
   When the local and peer devices synchronize information about M-LAG member interfaces, the first M-LAG member interface that changes from down to up becomes the M-LAG master member interface, with the other becoming the M-LAG backup member interface. By default, the master and backup roles of M-LAG member interfaces remain unchanged after a fault is rectified. Specifically, if the device providing the M-LAG master member interface fails, the M-LAG member interface on the peer device changes from the backup state to the master state. After the faulty device recovers, the M-LAG member interface on it is in the backup state, and the M-LAG member interface on the peer device remains in the master state.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   The forwarding behaviors of M-LAG master and backup member interfaces are different only when the M-LAG forwards multicast traffic.
4. Dual-Active Detection (DAD)
   
   After M-LAG master and backup devices are determined, both devices send DAD packets at an interval of 1s through the DAD link (also known as the heartbeat link) at Layer 3. If both devices can successfully receive DAD packets from one another, the M-LAG starts to work. If an M-LAG member device detects that the peer-link fails, it sends three DAD packets separately at intervals of 200 ms to accelerate DAD after the DAD delay (3s by default). This prevents accelerated DAD from being incorrectly triggered and causing interfaces on the other M-LAG member device to enter the error-down state.
   
   Under normal circumstances, the DAD link does not participate in any traffic forwarding behaviors in the M-LAG, and the M-LAG continues to work even if DAD fails. Instead, it is only used to detect if two M-LAG master devices exist when the DFS group pairing or peer-link fails. [Table 1](#EN-US_CONCEPT_0000001512689650__table18480195010717) describes the DAD link deployment modes supported by the device.
   
   **Table 1** DAD link deployment modes
   | Mode | Description |
   | --- | --- |
   | An independent heartbeat link is used as the DAD link. | This mode is recommended.  When an independent heartbeat link is used as the DAD link, you are advised to use Layer 3 main interfaces to establish the DAD link. If a VLANIF interface is used, the corresponding VLAN cannot be allowed on the peer-link interface; otherwise, a loop or MAC address flapping occurs.  In addition, you need to configure interfaces at both ends of the DAD link not to enter the error-down state upon peer-link failure to prevent them from entering the error-down state if the peer-link fails. |
   | There is no independent heartbeat link, and a link between management interfaces is used as the DAD link. | This mode is recommended.  When a link between management interfaces is used as the DAD link, the management interface IP addresses bound to the DFS group must be reachable to each other, and VPN instances must be bound to the management interfaces to ensure that DAD packets and service packets are transmitted separately. |
   | There is no independent heartbeat link, and a link between service interfaces is used as the DAD link. | This mode is not recommended.  When a link between service interfaces is used as the DAD link, you need to disable the enhanced DAD for double-fault failures function (that is, do not configure the **peer** *ip-address* parameter for DAD). Otherwise, if the peer-link fails, service interfaces on one M-LAG member device are set to the error-down state, causing error-down flapping. |
   
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   A link cannot function as both the DAD link and peer-link. Otherwise, if the link is down, DAD packets cannot be forwarded over this link, resulting in a DAD failure. As a result, interfaces on one M-LAG member device will not enter the error-down state, leading to abnormal packet forwarding.
5. M-LAG information synchronization
   
   When working properly, the M-LAG master and backup devices send M-LAG synchronization packets through the peer-link to synchronize information with each other in real time. M-LAG synchronization packets contain MAC address entries, ARP entries, and ND entries. The devices also send the status of M-LAG member interfaces. As such, traffic forwarding is not affected if either device fails, ensuring that normal services are not interrupted.


#### Active/Standby Mode

In [Figure 2](#EN-US_CONCEPT_0000001512689650__fig47561245113319), Eth-Trunks are established between DeviceA and a user-side server and between DeviceB and the user-side server. DeviceA and DeviceB set up an M-LAG. In active/standby mode, DeviceA and DeviceB use the DFS group protocol for pairing between one another over the peer-link, negotiating the M-LAG master and backup device roles and member interfaces, and synchronizing required entries. The peer-link between DeviceA and DeviceB is an Eth-Trunk used to exchange negotiation packets and forward part of traffic. The interfaces at both ends of the peer-link are known as peer-link interfaces, which are added to all VLANs and BDs by default. M-LAG member interfaces are Eth-Trunk interfaces on DeviceA and DeviceB that connect to the active and standby network interface cards (NICs) on the user-side server.

The active/standby mode applies only to a scenario where the active and standby NICs of a server connect to an M-LAG. In active/standby mode, both links provide backup for each other but do not load balance traffic. Under normal circumstances, only the M-LAG device connected to the active NIC sends and receives traffic. After the M-LAG device connected to the standby NIC receives traffic, it forwards the traffic to the M-LAG device connected to the active NIC through the peer-link interface. When the M-LAG member interface connected to the active NIC of the server becomes down, traffic is diverted from the peer-link interface to the M-LAG device connected to the standby NIC, and is directly forwarded to the server through the M-LAG backup member interface, implementing fast switchover. This improves the switchover performance when a fault occurs in a scenario where the active and standby NICs of a server connect to an M-LAG.

**Figure 2** Basic topology of an M-LAG in active/standby mode  
![](../images/en-us_image_0000001513048890.png)

Similar to that in dual-active mode, the M-LAG setup process in active/standby mode includes the following stages:

1. DFS group pairing
2. DFS master/backup device negotiation
3. M-LAG master and backup member interface election
4. DAD
5. M-LAG information synchronization

The active/standby mode differs from the dual-active mode only in the generation mode of M-LAG master and backup member interfaces. In active/standby mode, the M-LAG master and backup devices negotiate the M-LAG master and backup member interfaces based on the protocol packets (for electing the M-LAG master member interface) sent by the active NIC of the server. The M-LAG member interface connected to the active NIC becomes the M-LAG master member interface, and the M-LAG member interface on the peer device becomes the M-LAG backup member interface. (That is, the M-LAG member interface connected to the standby NIC becomes the M-LAG backup member interface.)

When the active NIC of the server fails, the standby NIC becomes the active NIC. The new active NIC sends packets for electing the M-LAG master member interface. After the M-LAG device where the original M-LAG backup member interface resides receives the packets, the original M-LAG backup member interface becomes the M-LAG master member interface. After the active NIC of the server recovers, the master and backup roles of M-LAG member interfaces remain unchanged by default. Whether the master and backup roles are changed depends on whether the active NIC sends packets for electing the M-LAG master member interface after the fault is rectified. If the active NIC sends packets for electing the M-LAG master member interface again after the fault is rectified, the master/backup status of M-LAG member interfaces is switched back.

Currently, the CE6885-LL (low latency mode) supports M-LAG master and backup member interface election using only ARP, IGMP, and DHCP packets. Other models support M-LAG master and backup member interface election using ARP, ND, IGMP, DHCP, and MLD packets.

![](../public_sys-resources/note_3.0-en-us.png) 

In active/standby mode, M-LAG master and backup member interface election depends on the packets for electing the M-LAG master member interface sent to the CPU. To ensure that IGMP/DHCP/MLD packets can be sent to the CPU, you need to enable IGMP snooping in a VLAN or BD so that M-LAG master and backup member interface election can be performed through IGMP packets. Alternatively, you need to enable DHCP globally so that M-LAG master and backup member interface election can be performed through DHCP packets. You can also enable MLD snooping in a VLAN or BD so that M-LAG master and backup member interface election can be performed through MLD packets. In addition, when an M-LAG device functions as a Layer 2 transparent transmission device or Layer 2 gateway, ARP/ND packets are not sent to the CPU, and M-LAG master and backup member interface election cannot be performed through packets for electing the M-LAG master member interface. In this case, you need to enable Layer 2 proxy ARP in a VLAN and enable ARP broadcast suppression or NS multicast suppression in a BD so that ARP/ND packets can be used for M-LAG master and backup member interface election.