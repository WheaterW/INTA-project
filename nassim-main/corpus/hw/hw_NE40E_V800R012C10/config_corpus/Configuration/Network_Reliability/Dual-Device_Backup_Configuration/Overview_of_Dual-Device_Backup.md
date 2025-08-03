Overview of Dual-Device Backup
==============================

Dual-device backup provides a unified platform for backing up service control data from the master device to the backup device.

#### Definition

Dual-device backup enables the master device to back up service control data to the backup device in real time in scenarios where a master/backup status negotiation protocol (for example, VRRP or E-Trunk) is deployed. When the master device or the link directly connected to the master device fails, service traffic is quickly switched to the backup device. When the master device or the link directly connected to the master device recovers, service traffic is switched back to the master device. This ensures service continuity.


#### Purpose

In traditional service scenarios, all users use a single device to access a network. Once the device or the link directly connected to the device fails, all user services are interrupted, and the service recovery time is uncertain. To resolve this issue, deploy dual-device backup to enable the master device to back up service control data to the backup device. When a fault occurs on the network, the backup device can quickly take over user services without waiting for service control data to be relearned. In doing so, users are unaware of the fault, hence improving network reliability by improving service reliability.


#### Benefits

* Benefits to users:
  
  Improved user service reliability and user experience.
* Benefits to carriers:
  
  + Improved network reliability from the perspective of service reliability. If a network fault occurs, the backup device immediately takes over user services without re-learning service control data.
  + Improved network reliability. If a network fault occurs, the backup device can quickly take over user services. In this way, users can use network resources continuously without being aware of the network failure.