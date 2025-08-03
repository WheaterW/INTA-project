Traffic Forwarding When an M-LAG Failure Occurs (Dual-Active Mode)
==================================================================

In an M-LAG, traffic is forwarded differently if an uplink, downlink, M-LAG device, DAD link, peer-link, or double-fault failure occurs. The following describes how traffic is forwarded when a fault occurs and when the fault is rectified.

#### Uplink Failure

**Figure 1** Traffic forwarding in case of an uplink failure  
![](figure/en-us_image_0000001564009313.png)

In [Figure 1](#EN-US_CONCEPT_0000001564128897__dc_cfg_m-lag_0047_fig_01), an M-LAG is connected to a common Ethernet network. If the uplink of the M-LAG master device fails, traffic passing through the M-LAG master device is forwarded by the M-LAG backup device through the peer-link. The M-LAG master device resumes forwarding traffic when its uplink recovers from the fault.

If the faulty link is the DAD link, the M-LAG continues to work properly without being affected. If the peer-link also fails, a dual-active conflict occurs and DAD cannot be performed. As a result, packet loss occurs.

When an M-LAG is connected to a Layer 3 network, a Layer 3 bypass link must be configured between the M-LAG master and backup devices. Otherwise, the uplink traffic that reaches the master device cannot reach the backup device.


#### Downlink Failure

**Figure 2** Traffic forwarding in case of a downlink failure  
![](figure/en-us_image_0000001564009301.png)

In [Figure 2](#EN-US_CONCEPT_0000001564128897__dc_cfg_m-lag_0047_fig_02), if the M-LAG master member interface fails, the link connected to this interface also goes down, and the M-LAG backup member interface becomes the new M-LAG master member interface. In this case, DeviceA is single-homed to the M-LAG. The M-LAG master device then changes the outbound interface to its peer-link interface in corresponding MAC address entries, instead of deleting MAC address entries with DeviceA's MAC address. In this way, the M-LAG master device quickly switches traffic to the M-LAG backup device for forwarding, preventing unknown unicast traffic flooding.

After the original M-LAG master member interface recovers, the M-LAG master device changes the outbound interface back to its M-LAG member interface in corresponding MAC address entries, implementing fast traffic switchover to itself and preventing unknown unicast traffic flooding. To prevent the protocol flapping that may be caused by M-LAG master/backup member interface switchovers, the new M-LAG master member interface retains its role and the original M-LAG master member interface acts as the M-LAG backup member interface after recovering from the fault.

In this situation, after enhanced M-LAG Layer 3 forwarding is enabled, the device with the faulty M-LAG member interface applies for backup FRR resources to generate backup ARP entries, ND entries, static routing entries, and dynamic routing entries where the outbound interface is the peer-link interface on the M-LAG backup member device, rather than the original M-LAG master member interface. As such, master and backup paths are established and traffic can be switched between them for normal forwarding.

![](../public_sys-resources/note_3.0-en-us.png) 

* When an M-LAG member interface fails and then recovers, the entry update duration is not affected by the numbers of MAC address entries, ARP entries, ND entries, static routing entries, and dynamic routing entries.
* The unidirectional isolation mechanism between the peer-link and M-LAG member interfaces is enabled when the M-LAG master member interface fails to prevent traffic interruption.
* FRR resources obtained for static ARP entries are not released when the M-LAG member interface is down and the corresponding VLANIF interface is still up, increasing FRR resource consumption.

Assume that a multicast source is at the network side and a multicast group member is at the access side. If the M-LAG member interface on the M-LAG master device fails, the master device instructs the peer device to update multicast entries through M-LAG synchronization packets. M-LAG master and backup devices no longer load balance traffic depending on whether the last digit of the multicast group address is an odd or even number, and all multicast traffic is forwarded by the M-LAG backup device on which the M-LAG member interface is Up. If the M-LAG member interface on the M-LAG backup device fails, multicast traffic is forwarded in a similar manner.


#### M-LAG Member Device Failure

**Figure 3** Traffic forwarding in case of an M-LAG master device failure  
![](figure/en-us_image_0000001564129149.png)
**Figure 4** Traffic forwarding in case of an M-LAG backup device failure  
![](figure/en-us_image_0000001513049046.png)

In [Figure 3](#EN-US_CONCEPT_0000001564128897__dc_cfg_m-lag_0047_fig_03), if the M-LAG master device fails, the M-LAG backup device becomes the new M-LAG master device. The Eth-Trunk on the original M-LAG master device goes down. In this case, DeviceA is single-homed to the M-LAG. In [Figure 4](#EN-US_CONCEPT_0000001564128897__fig53471453193), if the M-LAG backup device fails, the M-LAG master and backup device status remains unchanged, and the Eth-Trunk on the M-LAG backup device goes down. The Eth-Trunk on the M-LAG master device is still in the up state and continues to forward traffic. In this case, DeviceA is single-homed to the M-LAG.

When the faulty M-LAG device recovers, the peer-link goes up first, and the two M-LAG member devices negotiate their master and backup roles. After the negotiation succeeds, the M-LAG member interface on the faulty M-LAG member device goes up and traffic is load balanced on the M-LAG master and backup devices. The M-LAG master device retains its role after recovering from the fault, as does the M-LAG backup device.


#### DAD Link Failure

**Figure 5** Traffic forwarding in case of a DAD link failure  
![](figure/en-us_image_0000001513049062.png)

The DAD link between the M-LAG master and backup devices is used to detect whether two M-LAG master devices exist. If Layer 3 traffic is transmitted over the DAD link, traffic forwarding by the M-LAG will be affected. If the DAD link transmits Layer 2 traffic or does not transmit Layer 3 traffic, traffic forwarding will not be affected if the DAD link fails, as shown in [Figure 5](#EN-US_CONCEPT_0000001564128897__fig195788902610). A DAD link failure alarm will be generated in both cases. A DAD link failure clear alarm will be generated after the DAD link fault is rectified.


#### Peer-Link Failure

**Figure 6** Traffic forwarding in case of a peer-link failure  
![](figure/en-us_image_0000001563889017.png)

If the peer-link fails but the DAD status is normal, all interfaces excluding the Ethernet management interface, peer-link interface, and logical interfaces on one M-LAG device will enter the error-down state by default after the DAD delay (3s by default). In this case, only the other M-LAG device forwards traffic. The M-LAG system determines the M-LAG device on which interfaces enter the error-down state in the following sequence:

1. Whether there are uplink interfaces in the up state: If all uplink interfaces of one M-LAG device are down and the other M-LAG device has uplink interfaces in the up state, the interface error-down action is triggered on the M-LAG device whose uplink interfaces are all down.
2. Bandwidth throughput difference: If the bandwidth throughput difference calculated by one M-LAG device is greater than that calculated by the other M-LAG device, the interface error-down action is triggered on the M-LAG device with a greater bandwidth throughput difference.
   
   After DFS group pairing is successful, M-LAG devices calculate the bandwidth throughput every 10s by default. When DAD is triggered, M-LAG devices are triggered to calculate the bandwidth throughput at the same time.
   
   The formula for calculating the bandwidth throughput difference is as follows: Bandwidth throughput difference = Bandwidth throughput calculated last time â Bandwidth throughput calculated when DAD is triggered. In addition, each time the bandwidth throughput is calculated, the bandwidth throughput of the peer-link interface is not included.
   
   If the bandwidth throughput difference calculated by one M-LAG device is a negative value, the bandwidth throughput difference of the M-LAG device is considered to be 0.
3. In other scenarios, the interface error-down action is triggered on the M-LAG backup device, as shown in [Figure 6](#EN-US_CONCEPT_0000001564128897__dc_cfg_m-lag_0047_fig_04).

![](../public_sys-resources/note_3.0-en-us.png) 

You are advised to configure the interfaces that transmit uplink traffic as uplink interfaces. If no uplink interface is configured on a device, the system considers that uplink interfaces on the device are up.

If you need to isolate one M-LAG device, do not manually perform operations (for example, running the **shutdown** command on the peer-link interface) that cause the peer-link interface of the M-LAG device to go down. If such an operation is performed, the interface error-down action may be triggered on the other M-LAG device. As a result, both M-LAG devices cannot forward traffic, and traffic forwarding is interrupted.

When the peer-link recovers, the M-LAG member interface in the error-down state automatically goes up after 240s by default, while other interfaces in the error-down state go up immediately. Traffic is load balanced to the M-LAG master and backup devices.

In addition, you can run commands on an interface to configure whether the interface enters the error-down state if the peer-link fails but the DAD status is normal. [Table 1](#EN-US_CONCEPT_0000001564128897__table_0001) describes the interfaces that enter the error-down state if the peer-link fails but the DAD status is normal in different situations.

**Table 1** Interfaces that enter the error-down state if the peer-link fails but the DAD status is normal
| **Device Configuration** | **Interface Going Error-Down** |
| --- | --- |
| Default scenario | All interfaces excluding the Ethernet management interface, peer-link interface, and logical interfaces enter the error-down state. |
| Logical interfaces configured only | VLANIF interfaces, VBDIF interfaces, loopback interfaces, and the M-LAG member interface enter the error-down state. |
| Suspend function enabled only (function for configuring interfaces to enter the error-down state when the peer-link fails but the DAD status is normal) | Only the M-LAG member interface and the interfaces enabled with the suspend function enter the error-down state. |
| Reserved function enabled only (function for preventing interfaces from entering the error-down state when the peer-link fails but the DAD status is normal) | All interfaces excluding the Ethernet management interface, logical interfaces, peer-link interface, and interfaces enabled with the reserved function enter the error-down state. |
| Both suspend and reserved functions enabled | Only the M-LAG member interface and the interfaces enabled with the suspend function enter the error-down state. |



#### M-LAG Double-Fault Failure (Peer-Link Failure + M-LAG Device Failure)

**Figure 7** Traffic forwarding in case of an M-LAG double-fault failure (peer-link failure and M-LAG device failure)  
![](figure/en-us_image_0000001563889033.png)

In [Figure 7](#EN-US_CONCEPT_0000001564128897__dc_cfg_m-lag_0047_fig_05), when an M-LAG is working properly, if the peer-link fails but the DAD status is normal, some interfaces on one M-LAG device enter the error-down state and the other M-LAG device continues to work (see [Peer-Link Failure](#EN-US_CONCEPT_0000001564128897__peer-link_fault)). In this scenario, if the other M-LAG device then fails due to exceptions, such as unexpected power-off or an unexpected reboot, both the M-LAG master and backup devices will be unable to forward traffic (on the network in the figure, interfaces on the M-LAG backup device enter the error-down state).

In this fault scenario, enhanced DAD for double-fault failures can ensure non-stop forwarding, meeting service reliability requirements. (In the following example, interfaces on the M-LAG backup device enter the error-down state, and then the M-LAG master device fails.)

1. Enhanced DAD for double-fault failures: If the enhanced DAD for double-fault failures function has taken effect on M-LAG master and backup devices when the peer-link fails and then the M-LAG master device fails, the M-LAG backup device will detect the fault as it receives no DAD packets within a certain period. The M-LAG backup device then becomes the new M-LAG master device, restores the error-down interfaces to the up state, and forwards traffic.
   
   The enhanced DAD for double-fault failures function takes effect if the *peer-ip-address* parameter for DAD is configured, and does not take effect if the parameter is not configured.
2. M-LAG master device recovery: If the M-LAG master device recovers but the peer-link fault persists, the following applies:
   * If the M-LAG LACP system ID of the M-LAG master and backup devices is changed to their LACP system ID within a certain period, the access device selects only one of the uplinks as the active link during LACP negotiation. This ensures normal traffic forwarding.
   * If the default M-LAG LACP system ID is used (meaning it is not switched), the M-LAG master and backup devices use the same LACP system ID to negotiate with the access device, and links to both devices can be selected as active links. In this scenario, since the peer-link is still faulty, the M-LAG master and backup devices cannot synchronize information such as the DFS group priority and system MAC address of the peer device. As a result, two M-LAG master devices exist, and this can lead to abnormal traffic. In this case, as shown in [Figure 8](#EN-US_CONCEPT_0000001564128897__dc_cfg_m-lag_0047_fig_06), the HB DFS master/backup status is negotiated through DAD packets carrying necessary information for DFS group master/backup negotiation (such as the DFS group priority and system MAC address). Some interfaces (for details, see [Peer-Link Failure](#EN-US_CONCEPT_0000001564128897__peer-link_fault)) on the HB DFS backup device are triggered to enter the error-down state, and the HB DFS master device continues to work.**Figure 8** Traffic forwarding when a double-fault failure is rectified  
     ![](figure/en-us_image_0000001513049078.png)

If a peer-link failure occurs and is followed by the failure of the M-LAG device on which interfaces enter the error-down state, the other M-LAG device forwards traffic in the same manner as when only a peer-link failure occurs.

![](../public_sys-resources/note_3.0-en-us.png) 

If the function of making the downlink interface to go up after a delay upon failure recovery in a Monitor Link group is configured on a device, the function does not take effect in a double-fault failure scenario to reduce the service interruption time.