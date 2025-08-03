Configuring the LLDP Alarm Function
===================================

This section describes how to configure the LLDP alarm function on a network device, so that the device can send alarms to the NMS when information about neighbors changes.

#### Usage Scenario

After the LLDP alarm function is configured on a device, the device sends alarms to the NMS when information about neighbors changes.

To avoid network flapping caused by frequent LLDP alarms being sent to the NMS, configure a delay for the device to send alarms.


#### Pre-configuration Tasks

Before configuring the LLDP alarm function, complete the following task:

* Configure reachable routes between devices and the NMS, and SNMP parameters.


[Enabling the LLDP Alarm Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_lldp_cfg_0013.html)

This section describes how to enable the LLDP alarm function, so that a device can send alarms to the NMS when information about neighbors changes.

[(Optional) Configuring a Delay for Sending LLDP Alarms](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_lldp_cfg_0014.html)

This section describes how to configure a delay for sending LLDP alarms, so that flapping of network topology caused by frequent LLDP alarms can be prevented.

[Verifying the Configuration of the LLDP Alarm Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_lldp_cfg_0015.html)

After configuring the LLDP alarm function, verify the configuration.