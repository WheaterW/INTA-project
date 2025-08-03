Configuring a Device to Communicate with an NMS Using SNMPv3 USM User
=====================================================================

After SNMPv3 is configured, a managed device and an NMS can run SNMPv3 to communicate with each other. To ensure communication, you need to configure the agent and NMS. This section only describes the configuration on a managed device (the agent side). For details about configurations on an NMS, see the NMS operation guide.

#### Usage Scenario

The NMS manages a device by the following ways:

* Sends requests to the managed device to perform the GetRequest, GetNextRequest, GetResponse, GetBulk, or SetRequest operation, obtaining data or setting values.
* Receives alarms (traps or informs) from the managed device to locate and handle device faults based on the alarm information.


#### Pre-configuration Tasks

Before configuring a device to communicate with an NMS using SNMPv3 USM User, configure a routing protocol to ensure that at least one route exists between the Router and NMS.


#### Configuration Procedures

**Figure 1** Flowchart for configuring a device to communicate with an NMS using SNMPv3 USM User  
![](images/fig_dc_vrp_snmp_cfg_001502.png)


[Configuring Basic SNMPv3 Functions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_0016.html)

After basic SNMP functions are configured, the NMS can perform basic operations such as Get and Set operations on a managed device, and the managed device can send alarms to the NMS.

[(Optional) Controlling the NMS's Access to the Device](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_0017.html)

This section describes how to specify an NMS and manageable MIB objects for SNMPv3-based communication between the NMS and managed device to improve communication security.

[(Optional) Configuring the Trap Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_2007.html)

The device can be configured to send specified traps to the NMS, which facilitates fault locating. To enhance the trap transmission security, specify parameters for sending traps.

[(Optional) Configuring the Inform Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_1013.html)

A Router on which the SNMP agent function is enabled can generate two types of alarms: traps and informs. Traps are messages that notify the NMS of a condition on the network, and informs are alarms that require a reply from the NMS and are resent until a reply is received. Informs are more reliable than traps.

[(Optional) Configuring SNMPv3 Anti-Attack](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_0033.html)

To defense against a user's attack on other users' passwords, configuring the SNMPv3 blacklist function to improve security.

[Verifying the Configuration for a Device to Communicate with an NMS Using an SNMPv3 USM User](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_0021.html)

After configuring basic SNMPv3 functions, verify the configuration.