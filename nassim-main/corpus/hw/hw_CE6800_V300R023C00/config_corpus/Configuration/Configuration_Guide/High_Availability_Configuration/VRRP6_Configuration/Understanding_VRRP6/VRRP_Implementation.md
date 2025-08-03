VRRP Implementation
===================

VRRP Implementation

#### Transition Process of the VRRP States

Three states are defined in a VRRP state machine: Initialize, Master, and Backup. Only the device that is in the Master state can forward packets destined for the virtual IP address.

[Figure 1](#EN-US_CONCEPT_0000001176741667__en-us_concept_0000001130624270_fig_dc_vrp_vrrp_feature_013001) shows the VRRP state transition.

**Figure 1** Transition process of the VRRP states  
![](figure/en-us_image_0000001130624290.png)

**Table 1** VRRP states
| State | Description | Transition |
| --- | --- | --- |
| Initialize | VRRP is unavailable. A device in the Initialize state does not process VRRP Advertisement packets.  A device usually enters the Initialize state when it starts or detects a fault. | After receiving an interface up event, a device changes its state as follows:  * It changes from Initialize to Master if it is an IP address owner with a priority of 255. * It changes from Initialize to Backup if it has a priority less than 255. |
| Master | A VRRP device in the Master state performs the following operations:  * It sends a VRRP Advertisement packet each time the Adver\_Interval timer expires. * It responds to an ARP request destined for a virtual IP address with an ARP reply carrying the virtual MAC address. * It forwards IP packets destined for the virtual MAC address. * It allows a virtual IP address to be pinged by default. | The device changes its state as follows:  * It changes from Master to Backup if the VRRP priority in a received VRRP packet is higher than the local VRRP priority. * It remains in the Master state if the VRRP priority in a received VRRP packet is the same as the local VRRP priority. * It changes from Backup to Initialize after it receives a Shutdown event, indicating that the VRRP-enabled interface has been shut down.   NOTE:  If a device in the Master state receives a VRRP packet carrying a VRRP priority that is the same as the local VRRP priority, it compares the interface IP address carried in the packet with the local interface IP address. If the received interface IP address is larger, the device switches to the Backup state. Otherwise, the device remains in the Master state. |
| Backup | A VRRP device in the Backup state performs the following operations:  * It checks whether the master device is working properly based on the information in the VRRP Advertisement packets received from the master device. * It does not respond to ARP requests destined for a virtual IP address. * It discards the IP packets destined for a virtual MAC address. * It processes IP packets with the destination IP address being a virtual IP address according to the normal Layer 2 forwarding process. * When receiving a packet carrying a VRRP priority lower than the local priority:   + If the device is in preemption mode, it becomes the master after a specified preemption delay expires.   + If the device is in non-preemption mode, it remains in the Backup state. * It resets the Master\_Down timer, but does not compare interface IP addresses if it receives a VRRP packet carrying a VRRP priority higher than or equal to the local one. | The device changes its state as follows:   * It changes from Backup to Master after it receives a Master\_Down timer timeout event. * It changes from Backup to Initialize after it receives a Shutdown event, indicating that the VRRP-enabled interface has been shut down. |



#### VRRP Working Process

The VRRP working process is as follows:

1. VRRP selects the master based on the priorities of devices in a VRRP group. The master device sends gratuitous ARP packets to notify devices or hosts that are connected to it of the virtual MAC address, and then starts forwarding packets.
2. The master device periodically sends VRRP Advertisement packets to all backup devices in the VRRP group to advertise its configurations (such as the priority) and operating status.
3. If the master device fails, the backup device with the highest priority is elected as the new master.
4. After a master/backup switchover, the new master device immediately sends gratuitous ARP packets carrying the virtual MAC and virtual IP addresses to allow devices or hosts that are connected to it to update corresponding MAC entries. After the update is complete, user traffic is switched to the new master device. The switching process is transparent to users.
5. If the original master device recovers and it is the IP address owner (its priority is 255), it immediately switches to the Master state. If the original master device recovers and its priority is lower than 255, it switches to the Backup state, and its original priority is restored.
6. If the priority of a backup device is higher than that of a master device, VRRP determines whether to reelect a new master, depending on the backup device's working mode (preemption or non-preemption).

To ensure the master and backup devices work properly, VRRP must implement the following functions: electing the master and advertising the master status. The detailed VRRP working process is as follows:

**Electing the master**

VRRP determines the master or backup role of each device in a VRRP group based on priorities. A device with a higher priority is more likely to be elected as the master.

If devices in the Initialize state receive an interface up event and their priorities are lower than 255, they switch to the Backup state and then to the Master state after the Master\_Down timer expires. The VRRP device that first switches to the Master state sends VRRP Advertisement packets to the other backup devices in the VRRP group.

* If a device in the Backup state receives a VRRP Advertisement packet carrying a priority higher than or equal to its own priority, it remains in the Backup state.
* However, if the priority carried in the VRRP Advertisement packet is lower than its priority, the device switches to the Master state if it works in preemption mode, and it remains in the Backup state if it works in non-preemption mode.

![](public_sys-resources/note_3.0-en-us.png) 

If a VRRP device is the IP address owner, it will immediately switch to the Master state after receiving an interface up event.

If multiple devices in a VRRP group switch to the Master state simultaneously, they will negotiate the master and backup roles through VRRP Advertisement packets.

* VRRP devices with lower priorities will switch to the Backup state.
* VRRP device with the highest priority will become the master.
* If multiple devices have the same priority, the device whose interface where the VRRP group resides has the largest primary IP address will be elected as the master device.

**Advertising the master status**

The master device periodically sends VRRP Advertisement packets to all backup devices in the VRRP group to advertise its configurations (such as the priority) and operating status. The backup devices determine whether the master device is working properly based on the received VRRP Advertisement packets.

* If the master device proactively gives up the master role (by leaving the VRRP group for example), it sends VRRP Advertisement packets carrying a priority of 0 to the backup devices. Instead of waiting for the Master\_Down timer to expire, the backup device with the highest priority switches to the Master state after a specified switching time expires. This switching time (in seconds) is referred to as Skew\_Time, and it is calculated using the following formula: Skew\_Time = (256 - Backup device's priority)/256
* If the master device fails and cannot send VRRP Advertisement packets, the backup devices will not be able to immediately detect the master device's operating status. In this case, the backup device with the highest priority will switch to the master state only after the Master\_Down timer expires. The Master\_Down timer value (in seconds) is calculated using the following formula: Master\_Down timer value = (3 x Adver\_Interval timer value) + Skew\_Time

![](public_sys-resources/note_3.0-en-us.png) 

If network congestion occurs on an unstable network, a backup device may not receive VRRP Advertisement packets from the master device before the Master\_Down timer expires. In this case, the backup device proactively switches to the Master state. If the new master device receives a VRRP Advertisement packet from the original master device, it will switch back to the Backup state. On a network with unstable performance, the status of a VRRP group member may be frequently switched. To prevent this problem, run the **[**vrrp vrid**](cmdqueryname=vrrp+vrid)** **virtual-router-id** ****preempt-mode timer delay******delay-time** command to set a preemption delay so that the backup device waits for the time specified by *delay-time* after the Master\_Down event. If no VRRP Advertisement packets are received during this period, the backup device becomes the master device.