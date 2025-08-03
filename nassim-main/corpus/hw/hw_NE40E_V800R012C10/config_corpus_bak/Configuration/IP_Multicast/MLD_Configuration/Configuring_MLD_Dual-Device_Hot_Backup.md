Configuring MLD Dual-Device Hot Backup
======================================

MLD dual-device backup backs up multicast user join information between devices, improving multicast service continuity and reliability.

#### Usage Scenario

#### 

MLD dual-device hot backup uses a remote backup service (RBS) channel to back up MLD information between devices. Such implementation helps the system control and manage multicast services more flexibly, improving reliability of the services.

According to the master/backup protocol type, MLD dual-device hot backup can be classified as MLD dual-device hot backup in an E-Trunk scenario or MLD dual-device hot backup in a VRRP scenario.

MLD dual-device hot backup can also be classified as master/backup backup or master/backup active-active, depending on the backup mode used between the master and backup devices. In master/backup backup mode, only the master device receives MLD information and backs up the information to the backup device through the RBS channel. In master/backup active-active mode, both the master and backup devices receive MLD information and send multicast traffic to downstream devices in load balancing mode.


[Configuring MLD Dual-Device Hot Backup in an E-Trunk Master/Backup Backup Scenario](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mld_cfg_2245.html)

MLD dual-device backup backs up multicast user join information between devices, improving multicast service continuity and reliability.

[Configuring MLD Dual-Device Hot Backup in an E-Trunk Master/Backup Active-Active Scenario](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mld_cfg_2255.html)

MLD dual-device backup backs up multicast user join information between devices, improving multicast service continuity and reliability.

[Configuring MLD Dual-Device Hot Backup in a VRRP6 Master/Backup Backup Scenario](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mld_cfg_2246.html)

MLD dual-device backup backs up multicast user join information between devices, improving multicast service continuity and reliability.

[Configuring MLD Dual-Device Hot Backup in a VRRP6 Master/Backup Active-Active Scenario](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mld_cfg_2247.html)

MLD dual-device hot backup can trigger a rapid multicast service switchover if a node or link fails, improving service reliability.