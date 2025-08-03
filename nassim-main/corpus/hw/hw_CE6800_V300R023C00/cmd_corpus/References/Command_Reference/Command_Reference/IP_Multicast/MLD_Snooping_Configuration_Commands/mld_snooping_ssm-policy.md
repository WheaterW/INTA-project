mld snooping ssm-policy
=======================

mld snooping ssm-policy

Function
--------



The **mld snooping ssm-policy** command sets the source-specific multicast (SSM) group address range.

The **undo mld snooping ssm-policy** command restores the default configuration.



By default, the SSM group address range is FF3x::/32, where x cannot be 1 or 2.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping ssm-policy** { *basic-acl6-number* | **acl6-name** *acl6-name* }

**undo mld snooping ssm-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *basic-acl6-number* | Specifies the number of a basic IPv6 ACL. This ACL defines the range of IPv6 SSM group addresses. | The value is an integer ranging from 2000 to 2999. |
| **acl6-name** *acl6-name* | Specifies the name of a named basic IPv6 ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If a user joins a multicast group in the any-source multicast (ASM) range but wants to enjoy the SSM service of the multicast group, run the mld snooping ssm-policy command to add the multicast group address to an SSM policy.


Example
-------

# In VLAN10, add the multicast group address FF15::1 64 to the SSM group address range.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 2008
[~HUAWEI-acl6-basic-2008] rule permit source ff15::1 64
[*HUAWEI-acl6-basic-2008] quit
[*HUAWEI] vlan 10
[*HUAWEI-vlan10] mld snooping ssm-policy 2008

```