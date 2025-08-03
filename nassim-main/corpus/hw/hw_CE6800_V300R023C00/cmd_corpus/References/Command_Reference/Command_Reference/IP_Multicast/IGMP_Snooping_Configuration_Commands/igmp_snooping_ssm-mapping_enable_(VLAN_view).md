igmp snooping ssm-mapping enable (VLAN view)
============================================

igmp snooping ssm-mapping enable (VLAN view)

Function
--------



The **igmp snooping ssm-mapping enable** command enables SSM mapping and specifies an SSM mapping policy.

The **undo igmp snooping ssm-mapping enable** command disables SSM mapping.



By default, SSM mapping is disabled.


Format
------

**igmp snooping ssm-mapping enable**

**igmp snooping ssm-mapping enable policy** *SsmMappingAvlNameValue*

**undo igmp snooping ssm-mapping enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **policy** *SsmMappingAvlNameValue* | Specifies the name of an SSM mapping policy. | The value is a string of 1 to 31 case-insensitive characters. |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To provide SSM services for old-fashioned multicast terminals that support only IGMPv1 or IGMPv2, configure SSM mapping on the terminals. The SSM mapping mechanism is used to convert IGMPv1 and IGMPv2 Report messages into messages with (S, G) information. It allows hosts which do not support IGMPv3 to work with SSM-enabled devices.The **igmp snooping ssm-mapping enable** command enables SSM mapping in a VLAN. If policy is configured in the command, an SSM mapping policy can be specified for the VLAN.

**Prerequisites**

The SSM mapping policy specified by policy has been configured using the **ssm-mapping policy** command.

**Precautions**

* If policy is not configured in the command: The **igmp snooping ssm-mapping enable** command enables SSM mapping. An SSM mapping policy can be configured in the VLAN using the **igmp snooping ssm-mapping** command only after SSM mapping is enabled.
* If policy is configured in the command: The **igmp snooping ssm-mapping enable policy policy-name** command enables SSM mapping in a VLAN and specifies an SSM mapping policy for the VLAN.The igmp snooping ssm-mapping enable policy and **igmp snooping ssm-mapping** commands are mutually exclusive.

Example
-------

# Enable SSM mapping in VLAN 11 and set the SSM mapping policy to iptv.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] vlan 11
[*HUAWEI-vlan11] igmp snooping ssm-mapping enable policy iptv

```