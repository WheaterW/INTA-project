mld snooping group-policy
=========================

mld snooping group-policy

Function
--------



The **mld snooping group-policy** command sets the range of multicast groups that hosts can join.

The **undo mld snooping group-policy** command cancels the configuration.



By default, hosts can join any multicast groups.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping group-policy** { *acl6-number* | **acl6-name** *acl6-name* } [ **version** *number* ]

**undo mld snooping group-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl6-number* | Specifies an ACL6 number. | The value is an integer ranging from 2000 to 3999. |
| **acl6-name** *acl6-name* | Specifies the name of a named ACL6. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |
| **version** *number* | Specifies an MLD version. | The value can be 1 or 2. |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To limit the range of multicast groups that hosts can join, run the mld snooping group-policy command.


Example
-------

# Allow users in VLAN 2 to join only the multicast group FF15::1.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 2008
[*HUAWEI-acl6-basic-2008] rule permit source ff15::1 128
[*HUAWEI-acl6-basic-2008] quit
[*HUAWEI] vlan 2
[*HUAWEI-vlan2] mld snooping group-policy 2008

```