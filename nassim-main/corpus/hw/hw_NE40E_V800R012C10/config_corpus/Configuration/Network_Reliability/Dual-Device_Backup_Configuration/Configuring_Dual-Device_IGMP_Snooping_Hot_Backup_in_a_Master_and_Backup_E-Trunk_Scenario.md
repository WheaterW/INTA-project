Configuring Dual-Device IGMP Snooping Hot Backup in a Master/Backup E-Trunk Scenario
====================================================================================

To enable the master device to back up IGMP snooping entries to the backup device in a master/backup E-Trunk scenario, configure dual-device IGMP snooping hot backup. After dual-device IGMP snooping hot backup is configured, multicast services are not interrupted during a master/backup E-Trunk switchover.

#### Pre-configuration Tasks

Before configuring dual-device IGMP snooping hot backup in a master/backup E-Trunk scenario, complete the following tasks:

* Assign IP addresses to loopback interfaces on the master and backup devices, and configure a routing protocol.
* Configure an Eth-Trunk on each device, and add an Ethernet interface to the Eth-Trunk.


[Establishing a Dual-Device Backup Platform](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rbs_cfg_0016.html)

This section describes how to establish a dual-device backup platform to back up IGMP snooping entries. If a network node or link fails, a rapid Layer 2 multicast service switchover is triggered, improving service reliability.

[Enabling Remote Backup for IGMP Snooping Services](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rbs_cfg_0017.html)

This section describes how to enable remote backup for IGMP snooping services to implement IGMP snooping entry consistency on the master and backup devices.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rbs_cfg_0018.html)

After configuring dual-device IGMP snooping hot backup, verify the configurations.