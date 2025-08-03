mld snooping query ip-source-policy
===================================

mld snooping query ip-source-policy

Function
--------



The **mld snooping query ip-source-policy** command configures an MLD Query message filtering policy for a VLAN.

The **undo mld snooping query ip-source-policy** command restores the default configuration.



By default, no MLD Query message filtering policy is configured in a VLAN. With this default setting, all hosts in the VLAN to join multicast groups.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping query ip-source-policy** { *acl6-number* | **acl6-name** *acl6-name* }

**undo mld snooping query ip-source-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl6-number* | Specifies the number of an ACL. The ACL specifies the source addresses of MLD Query messages allowed or denied by hosts in a VLAN. | The value is an integer ranging from 2000 to 3999. |
| **acl6-name** *acl6-name* | Specifies the name of a named ACL6. | The value is a string of 1 to 64 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To enable a device to filter out specific MLD Query messages, run the mld snooping query ip-source-policy command to configure an MLD Query message filtering policy, improving the multicast service security. This command takes effect only for MLD Query messages.


Example
-------

# Configure the device to deny the MLD Query messages with the source IP address 2001:db8:1::1 64 in VLAN 11 and to allow other MLD Query messages to pass through.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 2000
[*HUAWEI-acl6-basic-2000] rule deny source 2001:db8:1::1 64
[*HUAWEI-acl6-basic-2000] rule permit source any
[*HUAWEI-acl6-basic-2000] quit
[*HUAWEI] mld snooping enable
[*HUAWEI] vlan 11
[*HUAWEI-vlan11] mld snooping query ip-source-policy 2000

```