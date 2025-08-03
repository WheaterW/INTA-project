mld snooping ip-source-policy
=============================

mld snooping ip-source-policy

Function
--------



The **mld snooping ip-source-policy** command configures a filtering policy to permit or deny MLD Report messages of hosts in a VLAN, controlling the multicast groups that the hosts can join.

The **undo mld snooping ip-source-policy** command restores the default configuration.



By default, no filtering policy is configured, so that all hosts in a VLAN can join multicast groups.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping ip-source-policy** { *acl6-number* | **acl6-name** *acl6-name* }

**undo mld snooping ip-source-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl6-number* | Specifies an ACL6 number. | The value is an integer ranging from 2000 to 3999. The ACL6 is used to permit or deny services requests of hosts in a VLAN based on source or destination addresses carried in MLD Report messages. |
| **acl6-name** *acl6-name* | Specifies the name of a named ACL6. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To improve multicast service deployment security, run the mld snooping ip-source-policy command to configure a filtering policy to permit or deny MLD Report messages of hosts in a VLAN.If you specify a basic ACL6, the device filters the MLD Report messages based on the carried source IP addresses. If an advanced ACL6 is specified, the device filters MLD Report messages based on the carried source and destination addresses.


Example
-------

# Disable the user host with the source IP address 2001:db8:1::1 in VLAN 11 from enjoying multicast services.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 2000
[*HUAWEI-acl6-basic-2000] rule deny source 2001:db8:1::1 64
[*HUAWEI-acl6-basic-2000] rule permit source any
[*HUAWEI-acl6-basic-2000] quit
[*HUAWEI] mld snooping enable
[*HUAWEI] vlan 11
[*HUAWEI-vlan11] mld snooping ip-source-policy 2000

```