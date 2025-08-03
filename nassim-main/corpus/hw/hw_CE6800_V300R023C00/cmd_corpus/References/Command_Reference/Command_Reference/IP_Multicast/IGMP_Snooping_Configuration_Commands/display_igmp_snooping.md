display igmp snooping
=====================

display igmp snooping

Function
--------



The **display igmp snooping** command displays all parameters of IGMP snooping running in a VLAN. These parameters include default and non-default parameters.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display igmp snooping vlan** *vlanid* [ **configuration** ]

**display igmp snooping vlan** [ **configuration** ]

**display igmp snooping** [ **configuration** ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display igmp snooping bridge-domain** *bdid* [ **configuration** ]

**display igmp snooping bridge-domain** [ **configuration** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **configuration** | Display non-default IGMP snooping configurations in a specified VLAN. | - |
| **vlan** *vlanid* | Displays IGMP snooping configurations in a specified VLAN. | The value is an integer that ranges from 1 to 4094. |
| **bridge-domain** *bdid* | Displays IGMP snooping configurations in a specified BD.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 1 to 1677215. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To locate a fault that occurs during multicast service transmission, run the display igmp-snooping command.This command is used to display IGMP snooping configurations of a VLAN in the Up state.When running the **display igmp snooping** command, note the following points:

* If the **display igmp snooping** command is run, IGMP snooping configurations of all VLANs will be displayed.
* If the display igmp snooping vlan command without the VLAN ID is run, IGMP snooping configurations of all VLANs will be displayed.

**Prerequisites**



IGMP snooping has been enabled both globally and in a specified VLAN.



**Precautions**

When both Layer 2 and Layer 3 services are configured, the VLAN inherits the multicast parameters configured on the VLANIF interface. The display igmp snooping vlan command displays the IGMP snooping configuration on the VLANIF interface.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all parameters of IGMP snooping on VLAN 10.
```
<HUAWEI> display igmp snooping vlan 10
IGMP Snooping Information for VLAN 10
     IGMP Snooping is Enabled
     IGMP Version is 3     
     IGMP Query Interval is Set to default 60     
     IGMP Max Response Interval is Set to default 10     
     IGMP Robustness is Set to default 2     
     IGMP Last Member Query Interval is Set to default 1     
     IGMP Router Port Aging Interval is Set to 180s or holdtime in hello 
     IGMP Filter Group-Policy is Set to default : Permit All 
     IGMP Filter IP-Source-Policy is Set to default : Permit All
     IGMP Filter Query IP-Source-Policy is Set to default : Permit All     
     IGMP Prompt Leave Disable     
     IGMP Router Alert is Not Required     
     IGMP Send Router Alert Enable     
     IGMP Router Port Learning Enable 
     IGMP Proxy Disable
     IGMP Proxy Router Protocol Action is Set to default: Terminate All
     IGMP Report Suppress Disable     
     IGMP Querier Disable
     IGMP Snooping Explicit-tracking Enable
     IGMP Snooping querier-election Disable
     IGMP ASM-SSM
     IGMP SSM-Mapping Disable     
     IGMP Suppress-dynamic-join Disable

```

# Display configurations of IGMP snooping on VLAN 10.
```
<HUAWEI> display igmp snooping vlan 10 configuration
IGMP Snooping Configuration for VLAN 10
     igmp snooping enable
     igmp snooping version 3
     igmp snooping explicit-tracking

```

**Table 1** Description of the **display igmp snooping** command output
| Item | Description |
| --- | --- |
| IGMP Snooping Information for VLAN 10 | IGMP Snooping information in the VLAN. |
| IGMP Snooping is Enabled | IGMP Snooping has been enabled in the VLAN. |
| IGMP Version is 3 | The version of IGMP messages supported by the VLAN is the default version. This means that only IGMPv3 messages can be processed. |
| IGMP Query Interval is Set to default 60 | IGMP general query messages are sent at a default interval (60s) in the VLAN. |
| IGMP Max Response Interval is Set to default 10 | The maximum time taken by a downstream host to respond to the querier is set to the default value (10s) in the VLAN. |
| IGMP Robustness is Set to default 2 | The number of times the querier sends group-specific query messages is set to the default value (2) in the VLAN. |
| IGMP Last Member Query Interval is Set to default 1 | Group-specific query messages are sent at a default interval (1s) in the VLAN. |
| IGMP Router Port Aging Interval is Set to 180s or holdtime in hello | The aging time of a router port is 180s or equals holdtime contained in a PIM Hello packet in the VLAN. |
| IGMP Filter Group-Policy is Set to default : Permit All | The default multicast group policy is used in the VLAN. This means hosts in the VLAN can join all multicast groups. |
| IGMP Filter IP-Source-Policy is Set to default : Permit All | The default IP policy is used in the VLAN. |
| IGMP Filter Query IP-Source-Policy is Set to default : Permit All | The default source IP policy for query packets is used in the VLAN. |
| IGMP Prompt Leave Disable | Prompt leave is disabled for interfaces in the VLAN. |
| IGMP Router Alert is Not Required | IGMP messages received by a device from the VLAN do not need to carry the Router Alert option in the IP header. |
| IGMP Send Router Alert Enable | IGMP messages sent by a device to the VLAN must carry the Router Alert option in the IP header. |
| IGMP Router Port Learning Enable | Router port learning has been enabled in the VLAN. |
| IGMP Proxy Disable | IGMP proxy is disabled in the VLAN. |
| IGMP Proxy Router Protocol Action is Set to default: Terminate All | IGMP proxy-enabled devices in the VLAN do not transparently transmit received IGMP messages. This means that these IGMP proxy-enabled devices terminate received Report, Leave, group-specific query, and source/group-specific query messages. |
| IGMP Report Suppress Disable | IGMP Report message suppression is disabled in the VLAN. |
| IGMP Querier Disable | The querier function is disabled in the VLAN. |
| IGMP Snooping Explicit-tracking Enable | The member tracking function is disabled in the VLAN. |
| IGMP Snooping querier-election Disable | The querier election function is disabled in the VLAN. |
| IGMP ASM-SSM | The multicast model is ASM-SSM in the VLAN. Both ASM and SSM packets are supported. |
| IGMP SSM-Mapping Disable | SSM mapping is disabled in the VLAN. |
| IGMP Suppress-dynamic-join Disable | The IGMP dynamic join suppress is disabled in the VLAN. |