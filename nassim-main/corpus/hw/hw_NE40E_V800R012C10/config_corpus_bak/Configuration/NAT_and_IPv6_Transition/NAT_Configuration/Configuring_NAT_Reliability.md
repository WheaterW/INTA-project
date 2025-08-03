Configuring NAT Reliability
===========================

The NAT reliability function enables a device to properly transmit NAT services, which prevents service traffic interruptions.

#### Usage Scenario

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the NE40E-M2K and NE40E-M2K-B support this configuration.

If a fault occurs on a NAT device or NAT board during NAT operation, NAT cannot be performed. As a result, user services are interrupted.

Currently, the NE40E supports inter-chassis cold backup, inter-board hot backup, and inter-chassis hot backup. For details about inter-chassis hot backup configurations, see [CGN Reliability Configuration](dc_ne_cgn-reliability_cfg_0001.html).


#### Pre-configuration Tasks

Before configuring NAT reliability, complete the following tasks:

* Configure basic NAT functions.
* Configure NAT for traffic.


[Configuring Single-Chassis Inter-Board Hot Backup for NAT](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0036_1.html)

You can configure the single-chassis inter-board hot backup function to improve the reliability of a NAT device.

[Configuring Association of CGN Board Faults with Inter-chassis NAT Cold Backup](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0065_1.html)

You can associate CGN board faults with inter-chassis NAT cold backup to improve NAT device reliability.

[Configuring Centralized NAT Providing Backup for Distributed NAT](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0085_1.html)

Configuring centralized NAT providing backup for distributed NAT ensures the reliability of the NAT service on distributed NAT devices.

[Verifying the NAT Reliability Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0037_1.html)

After configuring NAT reliability, run the following **display** commands to check NAT reliability configurations.