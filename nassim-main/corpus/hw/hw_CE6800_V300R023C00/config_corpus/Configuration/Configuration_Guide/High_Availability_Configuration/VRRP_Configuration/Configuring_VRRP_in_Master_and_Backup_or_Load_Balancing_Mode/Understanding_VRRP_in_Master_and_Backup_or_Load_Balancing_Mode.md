Understanding VRRP in Master/Backup or Load Balancing Mode
==========================================================

Understanding VRRP in Master/Backup or Load Balancing Mode

#### VRRP in Master/Backup Mode

VRRP usually works in master/backup mode, as shown in [Figure 1](#EN-US_CONCEPT_0000001176663823__fig_dc_vrp_vrrp_feature_012602). In this mode, a virtual router consists of one master device and multiple backup devices. Normally, DeviceA is the master device and forwards packets, whereas DeviceB and DeviceC are backup devices that monitor DeviceA's status. If DeviceA fails, either DeviceB or DeviceC is elected as the new master to take over the services from DeviceA.

**Figure 1** VRRP in master/backup mode  
![](figure/en-us_image_0000001176663849.png)

[Figure 1](#EN-US_CONCEPT_0000001176663823__fig_dc_vrp_vrrp_feature_012602) shows the implementation of VRRP in master/backup mode.

* DeviceA is the master with delayed preemption configured. Its priority is set to 120.
* DeviceB is a backup with immediate preemption configured. Its priority is set to 110.
* DeviceC is a backup with immediate preemption configured. The default priority 100 is used.

1. When DeviceA works properly, user-to-network traffic travels along the path DeviceE -> DeviceA -> DeviceD. DeviceA sends VRRP Advertisement packets periodically to notify DeviceB and DeviceC of its status.
2. If DeviceA fails, VRRP becomes unavailable on it. In this case, DeviceB assumes the master role because it has a higher priority than DeviceC, and DeviceC continues to remain as a backup device. User-to-network traffic then switches to the new path DeviceE -> DeviceB -> DeviceD.
3. After DeviceA recovers, it enters the Backup state, with a priority of 120. After receiving a VRRP Advertisement packet from DeviceB (the current master), DeviceA finds that its priority is higher than DeviceB's. Therefore, DeviceA preempts the master role after the configured preemption delay elapses, and sends VRRP Advertisement and gratuitous ARP packets.
   
   At this point, both DeviceA and DeviceB are in the Master state and send VRRP Advertisement packets. However, after receiving a VRRP Advertisement packet from DeviceA, DeviceB finds that the received priority is higher than the local priority. DeviceB then switches to the Backup state. User-to-network traffic then switches to the original path DeviceE -> DeviceA -> DeviceD.

#### VRRP in Load Balancing Mode

In load balancing mode, multiple VRRP groups work together to balance traffic, as shown in [Figure 2](#EN-US_CONCEPT_0000001176663823__fig_dc_vrp_vrrp_feature_012603). The implementation and packet negotiation mechanism of VRRP in load balancing mode are the same as those of VRRP in master/backup mode. Each VRRP group consists of one master device and multiple backup devices in either mode. The difference between the two modes is that in load balancing mode, two or more VRRP groups are configured, and the master device in each VRRP group may be different. In addition, the same VRRP device can be added to multiple VRRP groups and assigned different priorities in the groups.

VRRP load balancing is categorized into the following types:

**Multi-gateway load balancing**: Multiple VRRP groups with virtual IP addresses are created and specified as gateways for different users to implement load balancing.**Figure 2** Network diagram of multi-gateway load balancing  
![](figure/en-us_image_0000001130624302.png)

Two VRRP groups with the VRIDs of 1 and 2 are configured on the network shown in [Figure 2](#EN-US_CONCEPT_0000001176663823__fig_dc_vrp_vrrp_feature_012603).

* VRRP group 1: DeviceA is the master, and DeviceB is the backup.
* VRRP group 2: DeviceB is the master, and DeviceA is the backup.

VRRP group 1 is specified as the gateway for some users, and VRRP group 2 is specified as the gateway for others. In this way, the VRRP groups can balance service traffic while also backing up each other.

**Single-gateway load balancing**: A Load-Balance Redundancy Group (LBRG) with a virtual IP address is created, and VRRP groups (no virtual IP addresses need to be configured), are added to the LBRG. The LBRG is specified as the gateway for all users to implement load balancing.

Single-gateway load balancing is an enhancement to multi-gateway load balancing. It simplifies user-side configurations and facilitates network maintenance and management by allowing different users to share the same gateway.

**Figure 3** Single-gateway load balancing  
![](figure/en-us_image_0000001130624300.png)
Two VRRP groups with the VRIDs of 1 and 2 are configured on the network shown in [Figure 3](#EN-US_CONCEPT_0000001176663823__fig_dc_vrp_vrrp_feature_012604).

* VRRP group 1: an LBRG, in which DeviceA is the master, and DeviceB is the backup.
* VRRP group 2: an LBRG member group, in which DeviceB is the master, and DeviceA is the backup.

VRRP group 1 serves as the gateway for all users. After receiving an ARP request packet from a user, VRRP group 1 encapsulates its own virtual MAC address or VRRP group 2's virtual MAC address into an ARP reply packet to implement load balancing.