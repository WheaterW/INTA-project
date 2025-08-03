display mld snooping
====================

display mld snooping

Function
--------



The **display mld snooping** command displays MLD snooping parameter settings, including default and non-default parameter settings.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display mld snooping vlan** *vlan-id* [ **configuration** ]

**display mld snooping vlan** [ **configuration** ]

**display mld snooping** [ **configuration** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **configuration** | Displays non-default MLD snooping parameter settings. | - |
| **vlan** *vlan-id* | Displays MLD snooping parameter settings of a specified VLAN. | The value is an integer ranging from 1 to 4094. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To check MLD snooping parameter settings, run the **display mld snooping** command. The command output helps you locate multicast service faults.The command can display MLD snooping parameter settings of a VLAN only if the VLAN is in the Up state.When using the **display mld snooping** command, note the following points:

* The **display mld snooping** command can display MLD snooping parameter settings of all VLANs.
* If VLAN ID is not set, the command displays MLD snooping parameter settings of all VLANs.

**Precautions**

When both Layer 2 and Layer 3 services are configured, the VLAN inherits the multicast parameters configured on the VLANIF interface. The display mld snooping vlan command displays the MLD snooping configuration on the VLANIF interface.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all non-default MLD snooping settings.
```
<HUAWEI> display mld snooping configuration
  MLD Snooping Configuration for VLAN 1
     mld snooping enable

```

# Display all default and non-default MLD snooping parameter settings.
```
<HUAWEI> display mld snooping
  MLD Snooping Information for VLAN 1
     MLD Snooping is Enabled
     MLD Version is Set to default 2     
     MLD Query Interval is Set to default 125     
     MLD Max Response Interval is Set to default 10     
     MLD Robustness is Set to default 2     
     MLD Last Member Query Interval is Set to default 1     
     MLD Router Port Aging Interval is Set to 180s or holdtime in hello     
     MLD Filter Group-Policy is Set to default: Permit All 
     MLD Filter IP-Source-Policy is Set to default: Permit All
     MLD Filter Query IP-Source-Policy is Set to default: Permit All    
     MLD Prompt Leave Disable     
     MLD Router Alert is Not Required     
     MLD Send Router Alert Enable     
     MLD Router Port Learning Enable     
     MLD Proxy Disable
     MLD Proxy Router Protocol Action is Set to default: Terminate All   
     MLD Report Suppress Disable     
     MLD Querier Disable
     MLD Snooping querier-election Disable
     MLD ASM-SSM
     MLD SSM-Mapping Disable     
     MLD Suppress-dynamic-join Disable

```

**Table 1** Description of the **display mld snooping** command output
| Item | Description |
| --- | --- |
| MLD Snooping is Enabled | Indicates that MLD snooping is enabled in the VLAN. |
| MLD Version is Set to default 2 | Indicates that the default MLD version MLDv2 is used in the VLAN. With this default setting, the device can process both MLDv1 and MLDv2 messages. |
| MLD Query Interval is Set to default 125 | Indicates that the querier in the VLAN sends general Query messages at the default interval (125s). |
| MLD Max Response Interval is Set to default 10 | Indicates that the maximum time for the querier in the VLAN to wait for responses from downstream hosts is the default value (10s). |
| MLD Robustness is Set to default 2 | Indicates that the number of group-specific Query messages that the querier in the VLAN sends is the default value (2). |
| MLD Last Member Query Interval is Set to default 1 | Indicates that the querier in the VLAN sends group-specific Query messages at the default interval (1s). |
| MLD Router Port Aging Interval is Set to 180s or holdtime in hello | Indicates that the aging time of a router interface in the VLAN is the default value 180s or the Holdtime value contained in PIM Hello messages. |
| MLD Filter Group-Policy is Set to default: Permit All | Indicates that the default multicast group policy is used in the VLAN. With this default setting, the device allows hosts in the VLAN to join any multicast groups. |
| MLD Filter IP-Source-Policy is Set to default: Permit All | Indicates that the default source IP policy is used in the VLAN. |
| MLD Filter Query IP-Source-Policy is Set to default: Permit All | Indicates that the default filtering policy is used for MLD Query messages of this VLAN. With this default setting, the device allows all hosts in the VLAN to join multicast groups. |
| MLD Prompt Leave Disable | Indicates that prompt leave is disabled on the interfaces in the VLAN. |
| MLD Router Alert is Not Required | Indicates that the device permits MLD messages that do not carry the Router Alert option in IP headers received from interfaces in the VLAN. |
| MLD Send Router Alert Enable | Indicates that the device sends MLD messages carrying the Router-Alert option in IP headers to interfaces in the VLAN. |
| MLD Router Port Learning Enable | Indicates that router interface learning is enabled in the VLAN. |
| MLD Proxy Disable | Indicates that MLD proxy is disabled in the VLAN. |
| MLD Proxy Router Protocol Action is Set to default: Terminate All | Indicates that the MLD proxy-enabled device in the VLAN receives but does not transparently transmit MLD messages. With this setting, the MLD proxy-enabled router terminates received Report, Done, group-specific Query, and source-and group-specific Query messages. |
| MLD Report Suppress Disable | Indicates that MLD Report message suppression is disabled in the VLAN. |
| MLD Querier Disable | Indicates that the querier function is disabled in the VLAN. |
| MLD Snooping querier-election Disable | Indicates that the querier election function is disabled in the VLAN. |
| MLD ASM-SSM | Indicates that the ASM-SSM group module is used in the VLAN. With this setting, the device supports both ASM and SSM messages. |
| MLD SSM-Mapping Disable | Indicates that SSM mapping is disabled in the VLAN. |
| MLD Suppress-dynamic-join Disable | Disable interfaces in VLAN 1 from forwarding Report and Done messages to router interfaces with static groups configured. |