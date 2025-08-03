SNMP Configuration
==================

The Simple Network Management Protocol (SNMP) is a network management standard widely used on UDP networks. It uses a central computer (a network management station) that runs network management software to manage network elements. There are three SNMP versions: SNMPv1, SNMPv2c, and SNMPv3. One or more versions can be configured as required.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* After an NMS accesses a device from the admin-VS through SNMP, the NMS can access non-admin-VSs by carrying the VSID in the community (SNMPv1/v2c) or context (SNMPv3) field of packets. If the NMS accesses a non-admin-VS from the admin-VS, the NMS is authenticated only in the non-admin-VS. For example, if community is set to public123 for the admin-VS, the NMS can use public123@vs=1 (1 indicates the VSID) to access VS1.
* An NMS cannot access a non-admin-VS from another non-admin-VS.


[Overview of SNMP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_0002.html)

An NMS performs Get and Set operations on a managed device running the SNMP agent to manage objects, which are uniquely identified in the management information base (MIB).

[Configuration Precautions for SNMP](../../../../software/nev8r10_vrpv8r16/user/spec/SNMP_limitation.html)



[Configuring a Device to Communicate with an NMS Using SNMPv1](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_0004.html)

After SNMPv1 is configured, a managed device and an NMS can run SNMPv1 to communicate with each other. To ensure communication, you need to configure the agent and NMS. This section only describes the configuration on a managed device (the agent side). For details about configurations on an NMS, see the NMS operation guide.

[Configuring a Device to Communicate with an NMS Using SNMPv2c](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_0009.html)

After SNMPv2c is configured, a managed device and an NMS can run SNMPv2c to communicate with each other. To ensure communication, you need to configure the agent and NMS. This section only describes the configuration on a managed device (the agent side). For details about configurations on an NMS, see the pertaining NMS operation guide.

[Configuring a Device to Communicate with an NMS Using SNMPv3 USM User](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_0015.html)

After SNMPv3 is configured, a managed device and an NMS can run SNMPv3 to communicate with each other. To ensure communication, you need to configure the agent and NMS. This section only describes the configuration on a managed device (the agent side). For details about configurations on an NMS, see the NMS operation guide.

[Configuring a Device to Communicate with an NMS Through a Local SNMPv3 User](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_0034.html)

After SNMPv3 is configured, a managed device and an NMS can run SNMPv3 to communicate with each other. To ensure normal communication between them, you need to perform configuration on both the NMS and agent sides. This section describes only the configuration on the agent side. For details about the configuration on the NMS side, see the NMS operation guide.

[Configuring SNMP Proxy Using User-Defined Parameter Settings](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_0027.html)

This section describes how to configure Simple Network Management Protocol (SNMP) proxy using default parameter settings.

[Configuration Examples for SNMP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_0022.html)

This section provides configuration examples for SNMP.