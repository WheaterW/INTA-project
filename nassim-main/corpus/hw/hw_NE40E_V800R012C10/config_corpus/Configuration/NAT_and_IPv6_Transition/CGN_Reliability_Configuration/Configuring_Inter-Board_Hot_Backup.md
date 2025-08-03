Configuring Inter-Board Hot Backup
==================================

Before configuring inter-board hot backup, familiarize yourself with the applicable environment, complete the pre-configuration tasks, and obtain the data required for the configuration.

#### Usage Scenario

If multiple CGN devices equipped with service boards are deployed on a network, the service boards on a CGN device can be configured to work in active/standby mode to implement inter-board backup for the active and standby CGN boards.

* If a CGN device has slots for two or more dedicated boards and provides access services for a small number of users, inter-board 1:1 backup can be configured. In inter-board 1:1 backup, when the service board on the master device processes services, the service board on the backup device does not work. The service board on the master device backs up the user tables, session tables, and address pool entries to the service board on the backup device. Once the active service board fails, the standby service board takes over services.
* If a CGN device has slots for two or more dedicated boards and provides access services for a large number of users, inter-board 1+1 backup is recommended. In inter-board 1+1 backup, both the active and standby service boards process services and back up their user tables, session tables, and address pool entries to each other. Once a service board fails, the other service board processes all services.


#### Pre-configuration Tasks

Before configuring inter-board hot backup, complete the following tasks:

* Set the dedicated board working mode.
* Load the license to the device, and ensure that the service board is working properly.


[Configuring Single-Chassis Inter-Board Hot Backup for NAT](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0036_copy.html)

You can configure the single-chassis inter-board hot backup function to improve the reliability of a NAT device.

[Configuring the Single-Chassis Inter-Board Hot Backup Function for a DS-Lite Device](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0035_copy.html)

The single-chassis inter-board hot backup function improves the reliability of a DS-Lite device.

[Verifying the Inter-Board Hot Backup Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cgn-reliability_cfg_0011.html)