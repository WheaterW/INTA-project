Configuring a Device to Communicate with an NMS Using SNMPv1
============================================================

After SNMPv1 is configured, a managed device and an NMS can run SNMPv1 to communicate with each other. To ensure communication, you need to configure the agent and NMS. This section only describes the configuration on a managed device (the agent side). For details about configurations on an NMS, see the NMS operation guide.

#### Usage Scenario

To allow the NMS to manage network devices, configure SNMP.

If the network is secure and has few devices (for example, a campus network or a small enterprise network), SNMPv1 can be deployed to ensure communication between the NMS and managed devices.

SNMPv1 has a security risk. Using SNMPv3 is recommended.


#### Pre-configuration Tasks

Before configuring a device to communicate with an NMS using SNMPv1, configure a routing protocol to ensure that the Router and NMS are reachable.


#### Configuration Procedures

**Figure 1** Flowchart for configuring a device to communicate with an NMS using SNMPv1
  
![](images/fig_dc_vrp_snmp_cfg_000401.png)


[Configuring Basic SNMPv1 Functions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_0005.html)

After basic SNMP functions are configured, the NMS can perform basic operations such as Get and Set operations on a managed device, and the managed device can send alarms to the NMS.

[(Optional) Controlling the NMS's Access to the Device](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_0006.html)

This section describes how to specify an NMS and manageable MIB objects for SNMPv1-based communication between the NMS and managed device to improve communication security.

[(Optional) Configuring the Trap Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_0007.html)

The device can be configured to send specified traps to the NMS, which facilitates fault locating. To enhance the trap transmission security, specify parameters for sending traps.

[(Optional) Configuring SNMP Anti-Attack](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_0039.html)

To defense against a user's attack on other users' passwords, configuring the SNMP blacklist function to improve security.

[Verifying the Configuration for a Device to Communicate with an NMS Through SNMPv1](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_0008.html)

After configuring basic SNMPv1 functions, verify the configuration.