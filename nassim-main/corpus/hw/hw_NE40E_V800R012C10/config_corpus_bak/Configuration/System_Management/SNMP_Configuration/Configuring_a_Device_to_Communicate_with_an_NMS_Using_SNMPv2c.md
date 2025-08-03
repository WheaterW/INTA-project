Configuring a Device to Communicate with an NMS Using SNMPv2c
=============================================================

After SNMPv2c is configured, a managed device and an NMS can run SNMPv2c to communicate with each other. To ensure communication, you need to configure the agent and NMS. This section only describes the configuration on a managed device (the agent side). For details about configurations on an NMS, see the pertaining NMS operation guide.

#### Usage Scenario

SNMP has to be deployed in a network to allow the NMS to manage network devices.

If your network is of a large scale with many devices and its security requirements are not strict or the network is secure (for example, a VPN network) but services on the network are so busy that traffic congestion may occur, then the SNMPv2c can be deployed to ensure communication between the NMS and managed devices.

SNMPv2c has a security risk. Using SNMPv3 is recommended.


#### Pre-configuration Tasks

Before configuring a device to communicate with an NMS using SNMPv2c, configure a routing protocol to ensure that at least one route exists between Router and NMS.


#### Configuration Procedures

**Figure 1** Flowchart for configuring a device to communicate with an NMS using SNMPv2c
  
![](images/fig_dc_vrp_snmp_cfg_000901.png)


[Configuring Basic SNMPv2c Functions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_0010.html)

After basic SNMP functions are configured, the NMS can perform basic operations such as Get and Set operations on a managed device, and the managed device can send alarms to the NMS.

[(Optional) Controlling the NMS's Access to the Device](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_0011.html)

This section describes how to specify an NMS and manageable MIB objects for SNMP-based communication between the NMS and managed device to improve communication security.

[(Optional) Configuring the Trap Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_1007.html)

The device can be configured to send specified traps to the NMS, which facilitates fault locating. To enhance the trap transmission security, specify parameters for sending traps.

[(Optional) Configuring the Inform Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_0013.html)

A Router on which the SNMP agent function is enabled can generate two types of alarms: traps and informs. Traps are messages that notify the NMS of a condition on the network, and informs are alarms that require a reply from the NMS and are resent until a reply is received. Informs are more reliable than traps.

[(Optional) Configuring SNMP Anti-Attack](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_0040.html)

To defense against a user's attack on other users' passwords, configuring the SNMP blacklist function to improve security.

[Verifying the Configuration for a Device to Communicate with an NMS Through SNMPv2c](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_0014.html)

After configuring basic SNMPv2c functions, verify the configuration.