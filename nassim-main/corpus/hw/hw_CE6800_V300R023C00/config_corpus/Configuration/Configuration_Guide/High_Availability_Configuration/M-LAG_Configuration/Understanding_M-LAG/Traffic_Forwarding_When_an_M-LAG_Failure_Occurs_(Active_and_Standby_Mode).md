Traffic Forwarding When an M-LAG Failure Occurs (Active/Standby Mode)
=====================================================================

In an M-LAG, traffic is forwarded differently if an uplink, downlink, M-LAG device, DAD link, peer-link, or double-fault failure occurs. The following describes how traffic is forwarded when a fault occurs and when the fault is rectified.

#### Uplink Failure

**Figure 1** Traffic forwarding in case of an uplink failure  
![](../images/en-us_image_0000001512689698.png)

In [Figure 1](#EN-US_CONCEPT_0000001564009053__fig475816351287), the active and standby NICs of ServerA are connected to DeviceA and DeviceB in an M-LAG, respectively. The M-LAG is connected to a common Ethernet network. If the uplink of DeviceA fails, traffic passing through DeviceA is forwarded to DeviceB through the peer-link for forwarding. DeviceA resumes forwarding traffic when its uplink recovers from the fault.

If the uplink of DeviceB fails, the M-LAG continues to work properly without being affected because the M-LAG backup member interface of DeviceB is connected to the standby NIC of ServerA and does not forward traffic.

If the faulty link is the DAD link, the M-LAG continues to work properly without being affected. If the peer-link also fails, a dual-active conflict occurs and DAD cannot be performed. As a result, packet loss occurs.

In a Layer 3 scenario, a bypass link must be configured between the two M-LAG devices. Otherwise, the uplink traffic that reaches DeviceA cannot reach DeviceB.


#### Downlink Failure

**Figure 2** Traffic forwarding in case of a downlink failure  
![](../images/en-us_image_0000001512849302.png)

In [Figure 2](#EN-US_CONCEPT_0000001564009053__fig6882134610617), the active and standby NICs of ServerA are connected to DeviceA and DeviceB in an M-LAG, respectively.

If the M-LAG master member interface fails, the link where the interface resides goes down. DeviceA detects the interface fault, switches the M-LAG master member interface to the M-LAG backup member interface, and notifies DeviceB of the fault. After receiving the notification, DeviceB switches the M-LAG backup member interface to the M-LAG master member interface. In addition, when the active NIC of the server detects a link fault, the standby NIC becomes the active NIC and sends packets for electing the M-LAG master member interface. After receiving the packets from the server, the M-LAG backup member interface on DeviceB also becomes the M-LAG master member interface. If the M-LAG master member interface fails, DeviceA changes the outbound interface to its peer-link interface in MAC address entries learned from the server side instead of clearing the MAC address entries. After DeviceB switches the M-LAG backup member interface to the M-LAG master member interface, DeviceB directly changes the outbound interface in MAC address entries from the peer-link interface to the M-LAG member interface. This implements fast traffic switchover and prevents unknown unicast flooding.

After the faulty M-LAG member interface recovers, to prevent protocol flapping caused by M-LAG master/backup member interface switchover, the master/backup status of M-LAG member interfaces is not proactively switched back by default. Whether the master/backup status of M-LAG member interfaces is switched back depends on whether the original active NIC becomes the active NIC after detecting that the link fault is rectified. If the original active NIC becomes the active NIC and sends packets for electing the M-LAG master and backup member interfaces again, the master/backup status of M-LAG member interfaces is switched back.

If the M-LAG backup member interface fails, the M-LAG continues to work properly without being affected because the M-LAG backup member interface is connected to the standby NIC of ServerA and does not forward traffic.

In this situation, after enhanced M-LAG Layer 3 forwarding is enabled, the device with the faulty M-LAG member interface applies for backup FRR resources to generate backup ARP entries, ND entries, static routing entries, and dynamic routing entries where the outbound interface is the peer-link interface on the M-LAG backup member device, rather than the original M-LAG master member interface. As such, master and backup paths are established and traffic can be switched between them for normal forwarding.

![](../public_sys-resources/note_3.0-en-us.png) 

* When an M-LAG member interface fails and then recovers, the entry update duration is not affected by the numbers of MAC address entries, ARP entries, ND entries, static routing entries, and dynamic routing entries.
* FRR resources obtained for static ARP entries are not released when the M-LAG member interface is down and the corresponding VLANIF interface is still up, increasing FRR resource consumption.
* During switchback upon an M-LAG member interface failure, if the original active NIC of the server becomes the active NIC immediately, traffic switching depends on ARP/ND entry resynchronization. Therefore, you are advised to configure delayed switchback for the server.

Assume that a multicast source is at the network side and a multicast group member is at the access side. If the M-LAG master member interface on the local M-LAG device fails, the local device instructs the peer device (the device whose M-LAG member interface is in the backup state) to update multicast entries through M-LAG synchronization packets. In this way, multicast traffic can be quickly switched to the peer M-LAG device for forwarding.


#### M-LAG Member Device Failure

**Figure 3** Traffic forwarding when the device whose M-LAG member interface is in the master state fails  
![](../images/en-us_image_0000001563769193.png)
**Figure 4** Traffic forwarding when the device whose M-LAG member interface is in the backup state fails  
![](../images/en-us_image_0000001563769185.png)

In [Figure 3](#EN-US_CONCEPT_0000001564009053__fig18736558302), if DeviceA whose M-LAG member interface is in the master state fails, the link status of the M-LAG member interface on DeviceA becomes down, and DeviceB becomes the M-LAG master device (if DeviceB is the M-LAG master device before the fault occurs, the master/backup status of M-LAG devices does not change). After DeviceB detects the peer-link fault, the M-LAG backup member interface on DeviceB becomes the M-LAG master member interface. In addition, when the active NIC of the server detects a link fault, the standby NIC becomes the active NIC and sends packets for electing the M-LAG master member interface. After receiving the packets from the server, the M-LAG backup member interface on DeviceB also becomes the M-LAG master member interface.

In [Figure 4](#EN-US_CONCEPT_0000001564009053__fig8675720382), if DeviceB whose M-LAG member interface is in the backup state fails, the link status of the M-LAG member interface on DeviceB becomes down, DeviceA becomes the M-LAG master device (if DeviceA is the M-LAG master device before the fault occurs, the master/backup status of M-LAG devices does not change), and the master/backup status of M-LAG member interfaces does not change. The M-LAG master member interface on DeviceA is still up, and the traffic forwarding status remains unchanged.

When the faulty M-LAG device recovers, the peer-link goes up first, and the two M-LAG member devices negotiate their master and backup roles. After the negotiation succeeds, the M-LAG member interface on the faulty M-LAG member device goes up. The M-LAG master device retains its role after recovering from the fault, as does the M-LAG backup device. When DeviceA whose M-LAG member interface is in the master state recovers from a fault, the master/backup status of M-LAG member interfaces is not proactively switched back by default. Whether the master/backup status of M-LAG member interfaces is switched back depends on whether the original active NIC becomes the active NIC after detecting that the link fault is rectified. If the original active NIC becomes the active NIC and sends packets for electing the M-LAG master and backup member interfaces again, the master/backup status of M-LAG member interfaces is switched back.


#### DAD Link Failure

**Figure 5** Traffic forwarding in case of a DAD link failure  
![](../images/en-us_image_0000001564128933.png)

The DAD link between the M-LAG master and backup devices is used to detect whether two M-LAG master devices exist. If Layer 3 traffic is transmitted over the DAD link, traffic forwarding by the M-LAG will be affected. If the DAD link transmits Layer 2 traffic or does not transmit Layer 3 traffic, traffic forwarding will not be affected upon a DAD link failure. In [Figure 5](#EN-US_CONCEPT_0000001564009053__fig1144512421125), the active and standby NICs of ServerA are connected to DeviceA and DeviceB in an M-LAG, respectively. A DAD link failure alarm will be generated in both cases. A DAD link failure clear alarm will be generated after the DAD link fault is rectified.


#### Peer-Link Failure

**Figure 6** Traffic forwarding in case of a peer-link failure (the device where the M-LAG master member interface resides is the M-LAG backup device)  
![](../images/en-us_image_0000001513168810.png)
**Figure 7** Traffic forwarding in case of a peer-link failure (the device where the M-LAG master member interface resides is the M-LAG master device)  
![](../images/en-us_image_0000001512849294.png)

If the peer-link fails but the DAD status is normal, all interfaces excluding the Ethernet management interface, peer-link interface, and logical interfaces on one M-LAG device will enter the error-down state by default after the DAD delay (3s by default). In this case, only the other M-LAG device forwards traffic. The M-LAG system determines the M-LAG device on which interfaces enter the error-down state in the following sequence:

1. Whether there are uplink interfaces in the up state: If all uplink interfaces of one M-LAG device are down and the other M-LAG device has uplink interfaces in the up state, the interface error-down action is triggered on the M-LAG device whose uplink interfaces are all down.
2. Bandwidth throughput difference: If the bandwidth throughput difference calculated by one M-LAG device is greater than that calculated by the other M-LAG device, the interface error-down action is triggered on the M-LAG device with a greater bandwidth throughput difference.
   
   After DFS group pairing is successful, M-LAG devices calculate the bandwidth throughput every 10s by default. When DAD is triggered, M-LAG devices are triggered to calculate the bandwidth throughput at the same time.
   
   The formula for calculating the bandwidth throughput difference is as follows: Bandwidth throughput difference = Bandwidth throughput calculated last time â Bandwidth throughput calculated when DAD is triggered. In addition, each time the bandwidth throughput is calculated, the bandwidth throughput of the peer-link interface is not included.
   
   If the bandwidth throughput difference calculated by one M-LAG device is a negative value, the bandwidth throughput difference of the M-LAG device is considered to be 0.
3. In other scenarios, the interface error-down action is triggered on the M-LAG backup device.
   * In [Figure 6](#EN-US_CONCEPT_0000001564009053__fig1258112579384), the active and standby NICs of ServerA are connected to DeviceA and DeviceB in an M-LAG respectively, and DeviceA is the M-LAG backup device. If the peer-link fails, the master/backup status of M-LAG devices does not change. However, after DeviceB detects the peer-link fault, the M-LAG backup member interface on DeviceB becomes the M-LAG master member interface. In addition, when the active NIC of the server detects a link fault, the standby NIC becomes the active NIC and sends packets for electing the M-LAG master member interface. After receiving the packets from the server, the M-LAG backup member interface on DeviceB also becomes the M-LAG master member interface.
   * In [Figure 7](#EN-US_CONCEPT_0000001564009053__fig2484112874815), the active and standby NICs of ServerA are connected to DeviceA and DeviceB in an M-LAG respectively, and DeviceB is the M-LAG backup device. When the peer-link fails, the master/backup status of M-LAG devices does not change, so does the master/backup status of M-LAG member interfaces. The M-LAG master member interface on DeviceA is still up, and the traffic forwarding status remains unchanged.

![](../public_sys-resources/note_3.0-en-us.png) 

You are advised to configure the interfaces that transmit uplink traffic as uplink interfaces. If no uplink interface is configured on a device, the system considers that uplink interfaces on the device are up.

If you need to isolate one M-LAG device, do not manually perform operations (for example, running the **shutdown** command on the peer-link interface) that cause the peer-link interface of the M-LAG device to go down. If such an operation is performed, the interface error-down action may be triggered on the other M-LAG device. As a result, both M-LAG devices cannot forward traffic, and traffic forwarding is interrupted.

When the peer-link recovers, the M-LAG member interface in the error-down state automatically goes up after 240s by default, while other interfaces in the error-down state go up immediately. After the M-LAG member interface in the error-down state goes up, the master/backup status of M-LAG member interfaces is not proactively switched back by default. Whether the master/backup status of M-LAG member interfaces is switched back depends on whether the original active NIC becomes the active NIC after detecting that the link fault is rectified. If the original active NIC becomes the active NIC and sends packets for electing the M-LAG master and backup member interfaces again, the master/backup status of M-LAG member interfaces is switched back.

In addition, you can run commands on an interface to configure whether the interface enters the error-down state if the peer-link fails but the DAD status is normal. [Table 1](#EN-US_CONCEPT_0000001564009053__table2835172284814) describes the interfaces that enter the error-down state if the peer-link fails but the DAD status is normal in different situations.

**Table 1** Interfaces that enter the error-down state if the peer-link fails but the DAD status is normal
| **Device Configuration** | **Interface Going Error-Down** |
| --- | --- |
| Default scenario | All interfaces excluding the Ethernet management interface, peer-link interface, and logical interfaces enter the error-down state. |
| Logical interfaces configured only | VLANIF interfaces, VBDIF interfaces, loopback interfaces, and the M-LAG member interface enter the error-down state. |
| Suspend function enabled only (function for configuring interfaces to enter the error-down state when the peer-link fails but the DAD status is normal) | Only the M-LAG member interface and the interfaces enabled with the suspend function enter the error-down state. |
| Reserved function enabled only (function for preventing interfaces from entering the error-down state when the peer-link fails but the DAD status is normal) | All interfaces excluding the Ethernet management interface, logical interfaces, peer-link interface, and interfaces enabled with the reserved function enter the error-down state. |
| Both suspend and reserved functions enabled | Only the M-LAG member interface and the interfaces enabled with the suspend function enter the error-down state. |



#### M-LAG Double-Fault Failure (Peer-Link Failure + M-LAG Device Failure)

**Figure 8** Traffic forwarding in case of an M-LAG double-fault failure (peer-link failure and M-LAG device failure)  
![](../images/en-us_image_0000001513168826.png)

In [Figure 8](#EN-US_CONCEPT_0000001564009053__fig9180240195015), when an M-LAG is working properly, if the peer-link fails but the DAD status is normal, some interfaces on one M-LAG device enter the error-down state and the other M-LAG device continues to work (see [Peer-Link Failure](#EN-US_CONCEPT_0000001564009053__section2034618158483)). In this scenario, if the other M-LAG device then fails due to exceptions, such as unexpected power-off or an unexpected reboot, both the M-LAG master and backup devices will be unable to forward traffic (on the network in the figure, interfaces on the M-LAG backup device enter the error-down state).

In this fault scenario, enhanced DAD for double-fault failures can ensure non-stop forwarding, meeting service reliability requirements. (In the following example, interfaces on the M-LAG backup device enter the error-down state, and then the M-LAG master device fails.)

1. Enhanced DAD for double-fault failures: If the enhanced DAD for double-fault failures function has taken effect on M-LAG master and backup devices when the peer-link fails and then the M-LAG master device fails, the M-LAG backup device will detect the fault as it receives no DAD packets within a certain period. The M-LAG backup device then becomes the new M-LAG master device, and restores the error-down interfaces to the up state. After the M-LAG member interface on the new M-LAG master device goes up and the device detects the peer-link fault, the M-LAG member interface becomes the M-LAG master member interface. In addition, when the active NIC of the server detects a link fault, the standby NIC becomes the active NIC and sends packets for electing the M-LAG master member interface. After receiving the packets from the server, the M-LAG backup member interface also becomes the M-LAG master member interface.
   
   The enhanced DAD for double-fault failures function takes effect if the *peer-ip-address* parameter for DAD is configured, and does not take effect if the parameter is not configured.
2. M-LAG master device recovery: If the M-LAG master device recovers but the peer-link fault persists, the following applies:
   
   When the original M-LAG master device recovers, since the peer-link is still faulty, the M-LAG master and backup devices cannot synchronize information such as the DFS group priority and system MAC address of the peer device. As a result, two M-LAG master devices exist, and this can lead to abnormal traffic. In this case, as shown in [Figure 9](#EN-US_CONCEPT_0000001564009053__fig2871625454), the M-LAG uplink interface has recovered to the up state and the DAD link has recovered. The HB DFS master/backup status is negotiated through DAD packets carrying information for DFS group master/backup negotiation (such as the DFS group priority and system MAC address). Some interfaces (for details, see [Table 1](#EN-US_CONCEPT_0000001564009053__table2835172284814)) on the HB DFS backup device are triggered to enter the error-down state, and the HB DFS master device continues to work.

**Figure 9** Traffic forwarding when a double-fault failure is rectified  
![](../images/en-us_image_0000001513168846.png)

If a peer-link failure occurs and is followed by the failure of the M-LAG device on which interfaces enter the error-down state, the other M-LAG device forwards traffic in the same manner as when only a peer-link failure occurs.

![](../public_sys-resources/note_3.0-en-us.png) 

If the function of making the downlink interface to go up after a delay upon failure recovery in a Monitor Link group is configured on a device, the function does not take effect in a double-fault failure scenario to reduce the service interruption time.