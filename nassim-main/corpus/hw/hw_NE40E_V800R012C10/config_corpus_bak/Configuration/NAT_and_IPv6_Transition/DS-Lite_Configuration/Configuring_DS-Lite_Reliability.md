Configuring DS-Lite Reliability
===============================

The DS-Lite reliability function enables a device to properly transmit DS-Lite services, which prevents service traffic interruptions.

#### Usage Scenario

If a fault occurs on a DS-Lite device or service board during the DS-Lite operation, DS-Lite cannot be performed. As a result, user services are interrupted. The NE40E supports inter-board hot backup and inter-chassis hot backup:

* Inter-board hot backup: Two service boards installed on a CGN device can be configured to work in master/backup mode to implement single-chassis inter-board backup. The single-chassis inter-board backup mechanism helps implement a data consistency between the master and backup DS-Lite boards. If a fault occurs, a master/backup DS-Lite board switchover is successfully performed. In this situation, services are properly transmitted, and users are unaware of the fault.
* Inter-chassis hot backup: This function enables the master device to back up its service board CPU's mapping table to the service board CPU on the backup device. If the service board on the master device or the master device fails, the backup device takes over traffic without service interruptions, improving DS-Lite reliability.

#### Pre-configuration Tasks

Before configuring DS-Lite reliability, complete the following tasks:

* Configure basic DS-Lite functions.
* Configure DS-Lite translation for user traffic.


[Configuring the Single-Chassis Inter-Board Hot Backup Function for a DS-Lite Device](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0035.html)

The single-chassis inter-board hot backup function improves the reliability of a DS-Lite device.

[Configuring Inter-Chassis DS-Lite Hot Backup](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0036.html)

You can configure the dual-device inter-chassis DS-Lite hot backup to improve the reliability of a DS-Lite device.

[Configuring Centralized DS-Lite Providing Backup for Centralized DS-Lite Backup](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0070.html)

Centralized DS-Lite providing backup for centralized DS-Lite improves DS-Lite device reliability.

[Verifying the DS-Lite Reliability Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ds-lite_cfg_0037.html)

After DS-Lite reliability is configured, you can run the following display commands to verify the DS-Lite reliability configuration.