Configuring IGMP Dual-Device Hot Backup in an E-Trunk Scenario
==============================================================

IGMP dual-device hot backup implements non-stop multicast service forwarding during a master/backup device switchover. This section describes how to configure IGMP dual-device hot backup in an E-Trunk scenario.

#### Pre-configuration Tasks

Before configuring IGMP dual-device hot backup in an E-Trunk scenario, complete the following tasks:

* Assign IP addresses to loopback interfaces on the master and backup devices, and configure a routing protocol.
* Configure an Eth-Trunk on each device, and add Ethernet interfaces to the Eth-Trunk interface.


[Configuring a Dual-Device Backup Platform](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0116.html)

This section describes how to configure a dual-device backup platform to back up IGMP entries. If a network node or link fails, a rapid multicast service switchover is triggered, improving service reliability.

[Enabling Remote Backup for IGMP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0117.html)

This section describes how to enable remote backup for IGMP to implement IGMP entry consistency between the master and backup devices.

[Verifying the Configuration of IGMP Dual-Device Hot Backup](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_0118.html)

After configuring IGMP dual-device hot backup, verify the configuration.