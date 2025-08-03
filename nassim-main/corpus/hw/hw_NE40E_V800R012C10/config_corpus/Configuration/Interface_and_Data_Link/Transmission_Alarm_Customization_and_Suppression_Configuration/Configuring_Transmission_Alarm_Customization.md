Configuring Transmission Alarm Customization
============================================

This section describes the usage scenario, pre-configuration tasks, and data preparation for transmission alarm customization.

#### Usage Scenario

In the scenario where transmission devices are connected to IP devices, if the network is unstable, a large number of burr alarms will be generated. As a result, the physical status of interfaces on the transmission devices will switch between Up and Down. To enable IP devices to ignore these burrs, configure transmission alarm customization on the IP devices.


#### Pre-configuration Tasks

Before configuring the transmission alarm customization function, power on the Router and ensure that it is working properly.


[Configuring the Types of Alarms that Affect the Physical Status of Interfaces](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_transalarm_cfg_0005.html)

In the scenario where a router is connected to a transmission device, if the network is unstable, a large number of burr alarms may be generated. As a result, the physical status of interfaces will frequently change between up and down. To specify the alarms that can trigger the physical status of an interface to go down, you can configure transmission alarm customization.

[(Optional) Configuring b1tca, b2tca, b3tca, sdbere, and sfbere Alarm Thresholds](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_transalarm_cfg_0006.html)

The b1tca, b2tca, b3tca, sdbere, and sfbere alarm thresholds can be configured. An alarm is reported only when the threshold is reached.

[Verifying the Transmission Alarm Customization Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_transalarm_cfg_0008.html)

After configuring transmission alarm customization, verify the configuration and check the alarm status and statistics on an interface.