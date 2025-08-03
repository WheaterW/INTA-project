Configuring Automatic ZTP Deployment Through DHCP
=================================================

Automatic deployment of ZTP can be implemented through DHCP. Configuring automatic deployment through DHCP can lower labor costs and improve deployment efficiency.

#### Usage Scenario

In conventional network device deployment, network administrators are required to perform onsite software commissioning after hardware installation is complete. Therefore, deploying a large number of geographically scattered devices is inefficient and incurs high labor costs.

To address these issues, configure DHCP-based ZTP to implement automatic deployment, without requiring onsite manual intervention in device deployment and configuration.


#### Pre-configuration Tasks

Before configuring ZTP, complete the following tasks:

* Configure routes for the target device's gateway to communicate with DHCP servers and file servers.
* Check that no configuration file is loaded to the target device.


[Editing an Intermediate File](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ztp_cfg_0004.html)



[Configuring a DHCPv4 Server and Relay Agent](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ztp_cfg_0005.html)



[Configuring a DHCPv6 Server and Relay Agent](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ztp_cfg_0012.html)



[Configuring a File Server](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ztp_cfg_0006.html)



[Powering on the Device](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ztp_cfg_0007.html)



[(Optional) Uploading a Pre-Configuration Script](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ztp_cfg_0011_01.html)



[(Optional) Configuring Automatic Patch Repair](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ztp_cfg_0013.html)

You can configure ZTP-based automatic patch repair to resolve a non-environment problem that occurs during automatic ZTP deployment.

[Enabling ZTP](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ztp_cfg_0003.html)



[Verifying the ZTP Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ztp_cfg_0008.html)