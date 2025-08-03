Configuring Basic CFM Functions
===============================

This section describes how to configure basic connectivity fault management (CFM) functions.

#### Usage Scenario

IP-layer mechanisms, such as IP ping and traceroute, are used to manage network-wide services, detect faults, and monitor performance on traditional Ethernet networks. These mechanisms are not effective for Ethernet operation and management.

CFM resolves this issue. On the network shown in [Figure 1](#EN-US_TASK_0172361932__fig_dc_vrp_cfm_cfg_00000401), CFM provides an end-to-end operation, administration and maintenance (OAM) mechanism based on VLAN, VPLS, or VLL for direct or Layer 2 Ethernet links. CFM applies to the following scenarios for monitoring link connectivity and locating faults:

* Both interfaces of the direct link between the CE and PE1 are Layer 2 interfaces.
* A Layer 2 network is deployed between the CE and PE2.
* A Layer 2 network is connected to a Layer 3 network through PE3.

[Figure 1](#EN-US_TASK_0172361932__fig_dc_vrp_cfm_cfg_00000401) shows an example networking scheme for basic CFM functions. 
**Figure 1** Example networking scheme for basic CFM functions  
![](images/fig_dc_vrp_cfm_cfg_00000401.png)

#### Pre-configuration Tasks

Before configuring basic CFM functions, complete the following tasks:

* Group the devices of each Internet service provider (ISP) into a maintenance domain (MD).
* Specify the name and level of the MD and configure the same MD name and level on the devices in the MD.
* Specify MAs for the MD based on service types, such as VLAN, VLL and VPLS. An MA generally corresponds to one type of service.
* Specify each MA's name and configure the same MA name on the devices in the MD.
* Specify maintenance association end points (MEPs) and maintenance association intermediate points (MIPs) for each MA in the MD.


[Enabling CFM Globally](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfm_cfg_000005.html)

This section describes how to globally enable connectivity fault management (CFM).

[(Optional) Switching CFM Versions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfm_cfg_000006.html)

This section describes how to switch connectivity fault management (CFM) versions.

[Creating an MD](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfm_cfg_000007.html)

This section describes how to create a maintenance domain (MD).

[(Optional) Creating a Default MD](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfm_cfg_000028.html)

This section describes how to create a default maintenance domain (MD).

[Creating an MA](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfm_cfg_000008.html)

An MD can include one or multiple MAs. The Ethernet CFM checks the connectivity for each MA.

[Creating MEPs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfm_cfg_000009.html)

This section describes how to create maintenance association end points (MEPs).

[(Optional) Creating a MIP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfm_cfg_000010.html)

A maintenance association intermediate point (MIP) is a node inside an MA. Each MEP periodically multicasts CCMs. MIPs are used to locate the fault.

[(Optional) Switching MAC Address Models for MPs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfm_cfg_000011.html)

This section describes how to switch Media Access Control (MAC) address models for maintenance points (MPs).

[Configuring CC](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfm_cfg_000012.html)

This section describes how to configure continuity check (CC).

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfm_cfg_000013.html)

After configuring basic Ethernet CFM functions, verify the configurations.