Interface Basics Configuration
==============================

Learning about interface basics, including common interface types and configurable interface parameters, helps with interface management.

#### Usage Scenario

To ensure better communication between devices on the network, physical and logical interfaces must be used together. In addition, you need to set parameters for each interface as required, such as the description, MTU, alarm thresholds for the inbound and outbound bandwidth usage of each interface, interval for collecting traffic statistics, trap reporting to the NMS when the protocol status of an interface changes, and control-flap.


#### Pre-configuration Tasks

Before performing interface basics configurations, verify that the device has been powered on and started properly.


[Entering the Interface View](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ifm_cfg_0005.html)

The command for entering the view of an interface varies with the physical attribute of the interface.

[(Optional) Setting Interface Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ifm_cfg_0027.html)

This section describes how to set parameters for an interface based on the actual service requirements. The parameters include the description and maximum transmission unit (MTU).

[Enabling an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ifm_cfg_0008.html)

Physical interfaces on a device are initialized and started when the device is powered on.

[(Optional) Configuring a Device to Send a Trap Message to an NMS When an Interface Physical Status Changes](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ifm_cfg_5004.html)

You can enable a device to send a trap message to an NMS when the interface physical status changes. After this function is enabled, the NMS monitors the interface status in real time.

[(Optional) Configuring IPv4 and IPv6 Traffic Statistics Collection on a Main Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ifm_cfg_5003.html)

You can configure IPv4 and IPv6 traffic statistics collection for all main interfaces.

[(Optional) Configuring Power Locking and Gain Locking for an Optical Amplifier Module](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ifm_cfg_5001.html)

You can configure power locking and gain locking for an optical amplifier module to amplify the optical power.

[Setting Thresholds for Generating and Clearing Packet Loss Rate Alarms on an MP-group or Global MP-group Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ifm_cfg_6008.html)

To allow the device to generate and clear packet loss rate alarms on an MP-group or global MP-group interface, set packet loss alarm thresholds.

[(Optional) Configuring an Interface Splitting Mode](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ifm_cfg_7007_1.html)

By configuring an interface splitting mode, you can switch the bandwidth mode of the split interface.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ifm_cfg_0009.html)

After the configurations are complete, check the status of the interface, statistics on the interface, and the control-flap operation.