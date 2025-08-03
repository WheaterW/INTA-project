Configuring 802.1X Port-based Authentication
============================================

Before configuring 802.1X Port-based Authentication services, familiarize yourself with the usage scenario, complete the pre-configuration tasks, and obtain the data required for the configuration. This helps you complete the configuration task quickly and accurately.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, this feature is supported only by the admin VS.


#### Usage Scenario

A traditional network does not take internal devices into consideration as potential attack sources, and existing network devices are not immune to attacks from internal devices. On a mobile bearer network, base stations of different carriers may share an equipment room. If the NE40E that serves as an aggregation device cannot distinguish between authorized and unauthorized base stations, the network is at risk. Therefore, the NE40E must be configured with security functions to control base station access to the network.

802.1X Port-based Authentication can be configured on the interfaces of the NE40E to authenticate and control access devices. This authentication implements port-based network access control.


#### Pre-configuration Tasks

IEEE 802.1X provides only a user identity authentication mechanism. Therefore, RADIUS authentication is required to complete user identity authentication. Before configuring 802.1X authentication, complete the following tasks:

* Configure an authentication scheme (RADIUS authentication).
* Configure a RADIUS server group.
* Configure user names and passwords on the RADIUS server.


[Overview of 802.1X Port-based Authentication](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_8021x_00022.html)

802.1X authentication allows only authorized users or devices to access a network, which improves network security.

[Configuration Precautions for 802.1X Port-based Authentication](../../../../software/nev8r10_vrpv8r16/user/spec/802.1X_Port-based_Authentication_limitation.html)



[Configuring 802.1X Port-based Authentication on the NE40E Functioning as an Authenticator](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_8021x_0012.html)



[Configuring 802.1X Port-based Authentication on the NE40E Functioning as a Supplicant](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_8021x_0011.html)

Before configuring 802.1X port-based authentication on a supplicant, familiarize yourself with the usage scenario, pre-configuration tasks, and configuration flowchart, which helps you quickly and accurately complete the configuration.

[Configuration Examples for 802.1X Port-based Authentication](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_8021x_0009.html)

This section provides configuration examples for 802.1X port-based authentication, including networking requirements, configuration roadmap, data preparation, configuration procedure, and configuration files.