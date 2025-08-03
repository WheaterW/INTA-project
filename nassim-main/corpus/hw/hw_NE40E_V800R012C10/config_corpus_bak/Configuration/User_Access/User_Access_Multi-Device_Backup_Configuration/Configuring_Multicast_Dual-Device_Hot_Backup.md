Configuring Multicast Dual-Device Hot Backup
============================================

Multicast hot backup can effectively meet the requirements for network reliability due to the wide application of multicast services. After the configuration is complete, multicast services are not interrupted and users are unaware of the fault when the BRAS is faulty.

#### Pre-configuration Tasks

Before configuring multicast dual-device hot backup, establish a multi-device backup platform.


[Enabling a Multicast RBS](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_rui_0031.html)

An RBS is enabled for multicast services.

[(Optional) Configuring IGMP Message Replication](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_rui_0032.html)

By default, the IGMP message replication function is enabled. When a DHCP STB is dual-homed to master and backup routers, IGMP message replication can be disabled to reduce resource consumption. 

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_rui_0033.html)

After configuring multicast dual-device hot backup, verify the configuration.