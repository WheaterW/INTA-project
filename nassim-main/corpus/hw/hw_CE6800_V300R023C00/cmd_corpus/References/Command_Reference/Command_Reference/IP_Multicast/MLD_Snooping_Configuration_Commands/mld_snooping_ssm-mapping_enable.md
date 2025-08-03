mld snooping ssm-mapping enable
===============================

mld snooping ssm-mapping enable

Function
--------



The **mld snooping ssm-mapping enable** command enables SSM mapping and specifies an SSM mapping policy.

The **undo mld snooping ssm-mapping enable** command disables SSM mapping.



By default, SSM mapping is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping ssm-mapping enable**

**mld snooping ssm-mapping enable policy** *policy-name*

**undo mld snooping ssm-mapping enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **policy** *policy-name* | Specifies the name of an SSM mapping policy. | The value is a string of 1 to 31 case-insensitive characters, spaces not supported. The string can contain spaces if it is enclosed in double quotation marks ("). |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To provide SSM services for multicast terminals that support only MLDv1, configure SSM mapping on the device. The SSM mapping mechanism is used to convert MLDv1 Report messages into messages with (S, G) information, allowing MLDv1-capable users to enjoy SSM services.To enable SSM mapping in a VLAN, run the **mld snooping ssm-mapping enable** command. If the policy parameter is specified, an SSM mapping policy is applied to the VLAN.


Example
-------

# Enable SSM mapping in VLAN 11 and apply the SSM mapping policy iptv to this VLAN.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping enable
[*HUAWEI] ssm-mapping ipv6 policy iptv
[*HUAWEI] vlan 11
[*HUAWEI-vlan11] mld snooping ssm-mapping enable policy iptv

```