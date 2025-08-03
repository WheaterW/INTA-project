Configuring a Device to Communicate with an NMS Through a Local SNMPv3 User
===========================================================================

After SNMPv3 is configured, a managed device and an NMS can run SNMPv3 to communicate with each other. To ensure normal communication between them, you need to perform configuration on both the NMS and agent sides. This section describes only the configuration on the agent side. For details about the configuration on the NMS side, see the NMS operation guide.

#### Usage Scenario

AAA is an authentication, authorization, and accounting technique. Local AAA users can be configured to log in to a device in multiple modes, such as SSH, FTP, or TELNET. However, SNMPv3 supports only SNMP user login, which can be inconvenient for network administrators in unified network device management scenarios.

To resolve this issue, you can configure SNMP to support AAA users. This allows AAA users to access the NMS, facilitates network administrators to manage devices in a unified manner, and achieves task-based authentication on different MIB nodes. The NMS does not distinguish between AAA user login and SNMP user login.

[Figure 1](#EN-US_TASK_0172361018__fig_dc_vrp_snmp_cfg_003401) shows the process of an AAA user logging in to the NMS through SNMP.

**Figure 1** Process of an AAA user logging in to the NMS through SNMP  
![](images/fig_dc_vrp_snmp_cfg_000302.png)

The NMS can communicate with the devices to be managed once basic functions are configured. To perform refined management, you can refer to the follow-up configuration procedure.


#### Pre-configuration Tasks

Before configuring a device to communicate with an NMS through a local SNMPv3 user, configure a routing protocol to ensure that at least one route exists between the Router and NMS.


#### Configuration Procedure

**Figure 2** Flowchart for configuring a device to communicate with an NMS through a local SNMPv3 user  
![](images/fig_dc_vrp_snmp_cfg_003402.png)


[Configuring Basic SNMPv3 Functions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_0036.html)

Basic SNMPv3 functions can be configured to allow an NMS to monitor and operate a managed device.

[(Optional) Configuring SNMP Anti-Attack](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_0035.html)

To defense against a user's attack on other users' passwords, configuring the SNMPv3 blacklist function to improve security.

[Verifying the Configuration for a Local SNMPv3 User on a Device to Communicate with an NMS](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_0037.html)

After configuring basic SNMPv3 functions, verify the configuration.